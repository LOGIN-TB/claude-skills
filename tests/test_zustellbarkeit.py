from __future__ import annotations

import importlib.util
import json
from email.message import EmailMessage
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
PRUEFER = ROOT / "skills" / "zustellbarkeit" / "scripts" / "zustellbarkeit.py"


def lade_modul():
    spec = importlib.util.spec_from_file_location("zustellbarkeit", PRUEFER)
    modul = importlib.util.module_from_spec(spec)
    assert spec.loader
    sys.modules[spec.name] = modul
    spec.loader.exec_module(modul)
    return modul


zustellbarkeit = lade_modul()


def baue(betreff: str = "Rueckfrage zur Wartung", text: str = "Guten Tag Frau Meier,\n\nkurze Rueckfrage.\n\nHolger Reins",
         html: str | None = None, **kopfzeilen: str) -> EmailMessage:
    nachricht = EmailMessage()
    nachricht["Subject"] = betreff
    nachricht["From"] = kopfzeilen.pop("From", "Holger Reins <holger@example.de>")
    nachricht["To"] = kopfzeilen.pop("To", "frau.meier@kunde.example")
    for name, wert in kopfzeilen.items():
        nachricht[name.replace("_", "-")] = wert
    nachricht.set_content(text)
    if html is not None:
        nachricht.add_alternative(html, subtype="html")
    return nachricht


def auswerten(nachricht: EmailMessage) -> dict:
    with tempfile.TemporaryDirectory(prefix="zustellbarkeit-test-") as ordner:
        pfad = Path(ordner) / "nachricht.eml"
        pfad.write_bytes(bytes(nachricht))
        betreff, text, html, kopfzeilen = zustellbarkeit.lade_eml(pfad)
    return zustellbarkeit.analysiere(betreff, text, html, kopfzeilen)


def regeln(ergebnis: dict) -> set[str]:
    return {eintrag["regel"] for eintrag in ergebnis["befunde"]}


def schwere_von(ergebnis: dict, regel: str) -> str:
    for eintrag in ergebnis["befunde"]:
        if eintrag["regel"] == regel:
            return eintrag["schwere"]
    raise AssertionError(f"Regel {regel} wurde nicht gemeldet")


class HilfsfunktionenTest(unittest.TestCase):
    def test_registrierbare_domain_kuerzt_auf_zwei_label(self):
        self.assertEqual(zustellbarkeit.registrierbare_domain("u4.ct.sendgrid.net"), "sendgrid.net")
        self.assertEqual(zustellbarkeit.registrierbare_domain("www.example.de"), "example.de")

    def test_registrierbare_domain_kennt_mehrteilige_suffixe(self):
        self.assertEqual(zustellbarkeit.registrierbare_domain("shop.example.co.uk"), "example.co.uk")

    def test_gleiche_domain_vergleicht_registrierbar(self):
        self.assertTrue(zustellbarkeit.gleiche_domain("www.example.de", "mail.example.de"))
        self.assertFalse(zustellbarkeit.gleiche_domain("calendly.com", "ct.sendgrid.net"))

    def test_entfaltet_erhaelt_mehrfach_leerzeichen(self):
        self.assertEqual(zustellbarkeit.entfaltet("LOGIN\r\n SystemHaus  und Neukunden"),
                         "LOGIN SystemHaus  und Neukunden")

    def test_domains_im_text_findet_url_und_blanke_domain(self):
        gefunden = zustellbarkeit.domains_im_text("Mehr auf https://www.example.de/preise und bei partner.example.org")
        self.assertIn("www.example.de", gefunden)
        self.assertIn("partner.example.org", gefunden)


class KlasseATest(unittest.TestCase):
    def test_linkziel_weicht_ab(self):
        html = '<p>Termin: <a href="https://ct.sendgrid.net/ls/click?x=1">https://calendly.com/holger/15min</a></p>'
        ergebnis = auswerten(baue(html=html))
        self.assertIn("linkziel-weicht-ab", regeln(ergebnis))
        self.assertEqual(schwere_von(ergebnis, "linkziel-weicht-ab"), "hart")

    def test_linkziel_ohne_abweichung_meldet_nichts(self):
        html = '<p>Termin: <a href="https://www.example.de/termin">https://example.de/termin</a></p>'
        self.assertNotIn("linkziel-weicht-ab", regeln(auswerten(baue(html=html))))

    def test_linktext_ohne_domain_meldet_nichts(self):
        html = '<p><a href="https://ct.sendgrid.net/ls/click?x=1">hier klicken</a></p>'
        self.assertNotIn("linkziel-weicht-ab", regeln(auswerten(baue(html=html))))

    def test_abmeldung_unvollstaendig(self):
        ergebnis = auswerten(baue(**{"List-Unsubscribe-Post": "List-Unsubscribe=One-Click"}))
        self.assertEqual(schwere_von(ergebnis, "abmeldung-unvollstaendig"), "hart")

    def test_abmeldung_vollstaendig_meldet_nichts(self):
        ergebnis = auswerten(baue(**{
            "List-Unsubscribe": "<https://example.de/ab>",
            "List-Unsubscribe-Post": "List-Unsubscribe=One-Click",
        }))
        self.assertNotIn("abmeldung-unvollstaendig", regeln(ergebnis))

    def test_abmeldung_nur_im_text(self):
        ergebnis = auswerten(baue(text="Angebot.\n\nUm diese E-Mails abzubestellen, bitte hier klicken."))
        self.assertEqual(schwere_von(ergebnis, "abmeldung-nur-im-text"), "stark")

    def test_thread_selbstbezug(self):
        eigene = "<abc123@example.de>"
        ergebnis = auswerten(baue(**{"Message-ID": eigene, "References": eigene}))
        self.assertEqual(schwere_von(ergebnis, "thread-selbstbezug"), "hart")

    def test_echter_thread_meldet_keinen_selbstbezug(self):
        ergebnis = auswerten(baue(**{"Message-ID": "<neu@example.de>", "References": "<alt@example.de>"}))
        self.assertNotIn("thread-selbstbezug", regeln(ergebnis))

    def test_zitat_ohne_vorgaenger(self):
        html = '<div>Neue Nachricht</div><blockquote class="gmail_quote">Alte Nachricht</blockquote>'
        ergebnis = auswerten(baue(html=html))
        self.assertEqual(schwere_von(ergebnis, "zitat-ohne-vorgaenger"), "hart")

    def test_zitat_mit_vorgaenger_meldet_nichts(self):
        html = '<div>Neue Nachricht</div><blockquote class="gmail_quote">Alte Nachricht</blockquote>'
        ergebnis = auswerten(baue(html=html, **{"In-Reply-To": "<alt@example.de>"}))
        self.assertNotIn("zitat-ohne-vorgaenger", regeln(ergebnis))

    def test_merge_artefakt_im_betreff(self):
        ergebnis = auswerten(baue(betreff="LOGIN SystemHaus  und Neukunden"))
        self.assertEqual(schwere_von(ergebnis, "merge-artefakt"), "hart")
        beleg = next(e["beleg"] for e in ergebnis["befunde"] if e["regel"] == "merge-artefakt")
        self.assertIn("··", beleg)

    def test_merge_artefakt_platzhalter(self):
        ergebnis = auswerten(baue(text="Hallo {{vorname}},\n\nkurze Frage."))
        self.assertIn("merge-artefakt", regeln(ergebnis))

    def test_merge_artefakt_anrede_ohne_namen(self):
        ergebnis = auswerten(baue(text="Hallo ,\n\nkurze Frage."))
        self.assertIn("merge-artefakt", regeln(ergebnis))

    def test_normale_anrede_ist_kein_artefakt(self):
        self.assertNotIn("merge-artefakt", regeln(auswerten(baue(text="Hallo Frau Meier,\n\nkurze Frage."))))

    def test_zaehlpixel_versteckt(self):
        html = '<p>Text</p><img src="https://track.example.org/o/1" style="display:none" width="1" height="1">'
        ergebnis = auswerten(baue(html=html))
        self.assertEqual(schwere_von(ergebnis, "zaehlpixel-versteckt"), "hart")

    def test_zaehlpixel_falsches_alt(self):
        html = '<p>Text</p><img src="https://track.example.org/o/1" width="1" height="1" alt="logo">'
        ergebnis = auswerten(baue(html=html))
        self.assertEqual(schwere_von(ergebnis, "zaehlpixel-falsches-alt"), "hart")

    def test_offenes_zaehlpixel_ist_hinweis(self):
        html = '<p>Text</p><img src="https://track.example.org/o/1" width="1" height="1">'
        ergebnis = auswerten(baue(html=html))
        self.assertEqual(schwere_von(ergebnis, "zaehlpixel-vorhanden"), "hinweis")

    def test_normales_bild_meldet_nichts(self):
        html = '<p>Text</p><img src="https://example.de/logo.png" width="180" height="40" alt="Logo">'
        gemeldet = regeln(auswerten(baue(html=html)))
        self.assertFalse({"zaehlpixel-versteckt", "zaehlpixel-falsches-alt", "zaehlpixel-vorhanden"} & gemeldet)

    def test_domainstreuung(self):
        html = ('<p><a href="https://ct.sendgrid.net/x">Termin</a></p>'
                '<img src="https://cdn.folk.app/bild.png" width="100" height="20" alt="Logo">')
        ergebnis = auswerten(baue(html=html))
        self.assertEqual(schwere_von(ergebnis, "domainstreuung"), "stark")

    def test_eigene_domain_streut_nicht(self):
        html = ('<p><a href="https://www.example.de/termin">Termin</a></p>'
                '<img src="https://example.de/logo.png" width="100" height="20" alt="Logo">')
        ergebnis = auswerten(baue(html=html, **{"Message-ID": "<x@example.de>"}))
        self.assertNotIn("domainstreuung", regeln(ergebnis))

    def test_domain_im_text_weicht_ab(self):
        ergebnis = auswerten(baue(text="Mehr dazu auf example.com.\n\nHolger"))
        self.assertEqual(schwere_von(ergebnis, "domain-im-text-weicht-ab"), "stark")

    def test_text_html_verhaeltnis(self):
        html = "<div>" + '<span style="margin:0;padding:0;border:0">' * 200 + "kurz" + "</span>" * 200 + "</div>"
        ergebnis = auswerten(baue(html=html))
        self.assertEqual(schwere_von(ergebnis, "text-html-verhaeltnis"), "stark")
        self.assertLess(ergebnis["kennzahlen"]["text_html_verhaeltnis"], 0.25)


class KlasseBTest(unittest.TestCase):
    def test_kennzahl_ohne_beleg(self):
        ergebnis = auswerten(baue(text="Kunden schliessen 40% mehr ab."))
        self.assertEqual(schwere_von(ergebnis, "kennzahl-ohne-beleg"), "stark")

    def test_kennzahl_mit_quelle_meldet_nichts(self):
        ergebnis = auswerten(baue(text="Kunden schliessen 40% mehr ab (Quelle: eigene Auswertung, Stand 08.2026)."))
        self.assertNotIn("kennzahl-ohne-beleg", regeln(ergebnis))

    def test_grosse_zahl_ohne_beleg(self):
        self.assertIn("kennzahl-ohne-beleg", regeln(auswerten(baue(text="Ueber 10.000 Anfragen pro Monat."))))

    def test_rechtfertigungsabsatz(self):
        text = "Wir erlauben uns, Dich einmalig zu kontaktieren, da wir ein berechtigtes Interesse sehen."
        self.assertEqual(schwere_von(auswerten(baue(text=text)), "rechtfertigungsabsatz"), "stark")

    def test_nachfass_ohne_vorgeschichte(self):
        text = "Ich wollte nachfragen, ob meine letzte Nachricht dich erreicht hat."
        self.assertEqual(schwere_von(auswerten(baue(text=text)), "nachfass-ohne-vorgeschichte"), "stark")

    def test_hinweise_der_klasse_b(self):
        text = ("Fragst du dich auch, wie es weitergeht? \U0001F914 "
                "Wir sind die groesste Plattform im DACH-Raum und ich bin auf dich aufmerksam geworden. "
                "Lass uns unverbindlich 15 Minuten sprechen.")
        gemeldet = regeln(auswerten(baue(text=text)))
        for regel in ("rhetorische-frage-einstieg", "emoji-im-einstieg", "superlativ-ohne-beleg",
                      "behauptete-relevanz", "terminlink-koeder"):
            self.assertIn(regel, gemeldet)

    def test_angstrahmen(self):
        text = "2026 war das haerteste Jahr seit langem, Budgets gekuerzt, Projekte verschoben."
        self.assertIn("angstrahmen", regeln(auswerten(baue(text=text))))


class KlasseCTest(unittest.TestCase):
    def test_rollenpostfach_absender(self):
        ergebnis = auswerten(baue(text="Hallo Frau Meier,\n\nkurze Frage.", From="Kate Chen <member@example.de>"))
        self.assertEqual(schwere_von(ergebnis, "rollenpostfach-absender"), "hinweis")

    def test_rollenpostfach_ohne_persoenliche_anrede_meldet_nichts(self):
        ergebnis = auswerten(baue(text="Rechnung 4711 im Anhang.", From="Buchhaltung <info@example.de>"))
        self.assertNotIn("rollenpostfach-absender", regeln(ergebnis))

    def test_empfaenger_rollenadresse(self):
        ergebnis = auswerten(baue(To="info@kunde.example"))
        self.assertEqual(schwere_von(ergebnis, "empfaenger-rollenadresse"), "hinweis")

    def test_handschrift_imitat(self):
        html = '<div class="gmail_extra"><div class="gmail_signature">Holger</div></div>'
        ergebnis = auswerten(baue(html=html))
        self.assertEqual(schwere_von(ergebnis, "handschrift-imitat"), "stark")


class FilterurteilTest(unittest.TestCase):
    def test_liest_microsoft_gateway_und_authentifizierung(self):
        ergebnis = auswerten(baue(**{
            "X-Forefront-Antispam-Report": "CIP:198.51.100.7;CTRY:US;LANG:de;SCL:5;SFV:SPM;CAT:SPM;DIR:INB;",
            "X-Microsoft-Antispam": "BCL:0;ARA:13230040;",
            "X-Microsoft-Antispam-Mailbox-Delivery": "ucf:0;dest:J;RF:JunkEmail;",
            "X-Spam-Status": "No, score=2.13 tagged_above=-999 required=5 tests=[KAM_SENDGRID=1.5, HTML_MESSAGE=0.001]",
            "Authentication-Results": "spf=pass; dkim=pass; dmarc=bestguesspass; compauth=pass",
        }))
        urteil = ergebnis["filterurteil"]
        self.assertEqual(urteil["microsoft"]["SCL"], "5")
        self.assertEqual(urteil["microsoft"]["CAT"], "SPM")
        self.assertEqual(urteil["microsoft"]["DIR"], "INB")
        self.assertEqual(urteil["microsoft"]["BCL"], "0")
        self.assertEqual(urteil["microsoft"]["RF"], "JunkEmail")
        self.assertEqual(urteil["gateway"]["urteil"], "No")
        self.assertEqual(urteil["gateway"]["punkte"], "2.13")
        self.assertIn("KAM_SENDGRID=1.5", urteil["gateway"]["regeln"])
        self.assertEqual(urteil["authentifizierung"]["dmarc"], "bestguesspass")

    def test_ohne_filterkopfzeilen_kein_urteil(self):
        self.assertNotIn("filterurteil", auswerten(baue()))


class ErgebnisTest(unittest.TestCase):
    def test_saubere_nachricht_ohne_befund(self):
        text = ("Guten Tag Frau Meier,\n\n"
                "Sie haben am 12.08.2026 die Wartung Ihrer beiden Hosts ausgeschrieben.\n\n"
                "Falls die Ausschreibung offen ist, schicke ich das Leistungsverzeichnis.\n\n"
                "Holger Reins")
        ergebnis = auswerten(baue(text=text))
        self.assertEqual(ergebnis["befunde"], [])
        self.assertEqual(ergebnis["zusammenfassung"], {"hart": 0, "stark": 0, "hinweis": 0})

    def test_struktur_des_ergebnisses(self):
        ergebnis = auswerten(baue(betreff="Hallo {{vorname}}"))
        self.assertEqual(ergebnis["schema_version"], 1)
        self.assertEqual(
            set(ergebnis),
            {"schema_version", "betreff", "kennzahlen", "befunde", "zusammenfassung", "hinweis", "filterurteil"}
            - {"filterurteil"},
        )
        for eintrag in ergebnis["befunde"]:
            self.assertEqual(set(eintrag), {"regel", "klasse", "schwere", "fundstelle", "beleg", "korrektur"})
            self.assertIn(eintrag["klasse"], {"A", "B", "C"})
            self.assertIn(eintrag["schwere"], {"hart", "stark", "hinweis"})
            self.assertLessEqual(len(eintrag["beleg"]), 160)

    def test_befunde_sind_nach_schwere_sortiert(self):
        html = ('<p>Hallo {{vorname}}, <a href="https://ct.sendgrid.net/x">https://calendly.com/x</a></p>'
                '<img src="https://track.example.org/o" width="1" height="1">')
        ergebnis = auswerten(baue(betreff="Angebot", html=html))
        reihenfolge = [zustellbarkeit.SCHWERE_ORDNUNG[e["schwere"]] for e in ergebnis["befunde"]]
        self.assertEqual(reihenfolge, sorted(reihenfolge))

    def test_hinweis_verspricht_keine_zustellung(self):
        self.assertIn("keine Zustellprognose", auswerten(baue())["hinweis"])


class SkriptTest(unittest.TestCase):
    def lauf(self, *argumente: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(PRUEFER), *argumente],
            text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )

    def test_entwurf_als_json(self):
        ergebnis = self.lauf("--json", "pruefe-entwurf", "--betreff", "Test", "--text", "Hallo {{vorname}}")
        self.assertEqual(ergebnis.returncode, 0)
        daten = json.loads(ergebnis.stdout)
        self.assertEqual(daten["quelle"], "entwurf")
        self.assertIn("merge-artefakt", {eintrag["regel"] for eintrag in daten["befunde"]})

    def test_strict_meldet_harten_befund(self):
        ergebnis = self.lauf("--strict", "pruefe-entwurf", "--text", "Hallo {{vorname}}")
        self.assertEqual(ergebnis.returncode, 1)

    def test_strict_ohne_harten_befund(self):
        ergebnis = self.lauf("--strict", "pruefe-entwurf", "--text", "Guten Tag Frau Meier, kurze Rueckfrage.")
        self.assertEqual(ergebnis.returncode, 0)

    def test_eml_wird_ausgewertet(self):
        with tempfile.TemporaryDirectory(prefix="zustellbarkeit-cli-") as ordner:
            pfad = Path(ordner) / "nachricht.eml"
            pfad.write_bytes(bytes(baue(betreff="Angebot", **{"List-Unsubscribe-Post": "List-Unsubscribe=One-Click"})))
            ergebnis = self.lauf("--json", "pruefe-eml", str(pfad))
        self.assertEqual(ergebnis.returncode, 0)
        daten = json.loads(ergebnis.stdout)
        self.assertEqual(daten["quelle"], "nachricht.eml")
        self.assertIn("abmeldung-unvollstaendig", {eintrag["regel"] for eintrag in daten["befunde"]})

    def test_fehlende_datei(self):
        ergebnis = self.lauf("pruefe-eml", "/nicht/vorhanden.eml")
        self.assertEqual(ergebnis.returncode, 2)

    def test_leerer_entwurf(self):
        self.assertEqual(self.lauf("pruefe-entwurf", "--betreff", "Nur Betreff").returncode, 2)

    def test_text_und_datei_schliessen_sich_aus(self):
        with tempfile.TemporaryDirectory(prefix="zustellbarkeit-cli-") as ordner:
            pfad = Path(ordner) / "entwurf.txt"
            pfad.write_text("Text", encoding="utf-8")
            ergebnis = self.lauf("pruefe-entwurf", "--text", "Text", "--text-datei", str(pfad))
        self.assertNotEqual(ergebnis.returncode, 0)

    def test_skript_kann_nicht_ins_netz(self):
        quelltext = PRUEFER.read_text(encoding="utf-8")
        for verboten in ("urllib", "http.client", "socket", "requests", "subprocess"):
            self.assertNotIn(verboten, quelltext)


if __name__ == "__main__":
    unittest.main()
