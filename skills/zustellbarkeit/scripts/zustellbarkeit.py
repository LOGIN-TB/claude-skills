#!/usr/bin/env python3
"""Prueft E-Mail-Entwuerfe und empfangene Nachrichten auf bekannte Junk-Ausloeser.

Das Skript wertet ausschliesslich lokal vorliegendes Material aus. Es versendet
nichts, laedt keine externen Ressourcen nach und loest insbesondere keine
Zaehlpixel aus. Es sagt keine Zustellung voraus und vergibt keinen Gesamtscore.
"""
from __future__ import annotations

import argparse
import email
import json
import re
import sys
from email import policy
from html.parser import HTMLParser
from pathlib import Path

SCHEMA_VERSION = 1
SCHWERE_ORDNUNG = {"hart": 0, "stark": 1, "hinweis": 2}

# Suffixe, bei denen die registrierbare Domain aus drei Labeln besteht.
MEHRTEILIGE_SUFFIXE = {
    "co.uk", "org.uk", "ac.uk", "gov.uk", "co.jp", "or.jp", "ne.jp",
    "com.au", "net.au", "org.au", "co.nz", "com.br", "co.za", "com.tr",
}

ROLLEN_LOKALTEILE = {
    "info", "kontakt", "contact", "office", "mail", "team", "sales", "vertrieb",
    "marketing", "news", "newsletter", "member", "members", "noreply", "no-reply",
    "donotreply", "hi", "hello", "hallo", "service", "support", "presse", "press",
}

ABMELDE_MUSTER = re.compile(
    r"(?:ab(?:zu)?(?:bestell|meld)|austrag|unsubscribe|opt[\s-]?out)", re.I
)

HANDSCHRIFT_MARKER = (
    "gmail_quote", "gmail_signature", "gmail_extra", "ispasted", "isselectedend",
)

ZITAT_MARKER = re.compile(
    r"(?:^\s*>\s?\S)|(?:\b(?:wrote|schrieb|schrieben)\s*:\s*$)",
    re.MULTILINE,
)

EMOJI = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F2FF←-⇿⬀-⯿]"
)

URL_IM_TEXT = re.compile(r"https?://[^\s<>\"'\)\]]+", re.I)
BLANKE_DOMAIN = re.compile(
    r"(?<![\w@.-])((?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z]{2,24})(?![\w-])", re.I
)
PROZENTWERT = re.compile(r"\b\d{1,3}(?:[.,]\d+)?\s?(?:%|\bProzent\b)", re.I)
GROSSE_ZAHL = re.compile(r"(?<![\d.,])\d{1,3}(?:\.\d{3})+(?![\d.,])")
BELEG_NAHE = re.compile(r"(?:https?://|\bQuelle\b|\bStand\b|\bgemessen\b|\bStudie\b)", re.I)

# Klasse B: inhaltliche Ausloeser. Jeder Eintrag nennt Regel, Schwere und Korrektur.
PHRASEN = (
    (
        "superlativ-ohne-beleg", "hinweis",
        (r"\b(?:gr(?:ö|oe)(?:ß|ss)te[rnms]?|f(?:ü|ue)hrende[rnms]?|Marktf(?:ü|ue)hrer"
         r"|Nummer\s?1|einzigartig|weltweit\s+f(?:ü|ue)hrend|beste[rnms]?\s+(?:L(?:ö|oe)sung|Plattform|Anbieter))\b"),
        "Superlativ belegen oder streichen. Ohne pruefbare Quelle wirkt er als Werbebehauptung.",
    ),
    (
        "kennzahl-ohne-beleg", "stark", None,
        "Zahl mit Quelle, Erhebungszeitraum und Bezugsgroesse versehen oder streichen.",
    ),
    (
        "angstrahmen", "hinweis",
        (r"(?:h(?:ä|ae)rteste[sn]?\s+Jahr|Budgets?\s+(?:gek(?:ü|ue)rzt|knapp)"
         r"|Projekte\s+verschoben|wird\s+nicht\s+einfacher|bevor\s+es\s+zu\s+sp(?:ä|ae)t\s+ist"
         r"|verlieren\s+Sie\s+keine|Entscheidungen\s+vertagt)"),
        "Einstieg auf einen nachpruefbaren Anlass umstellen statt auf eine Bedrohungslage.",
    ),
    (
        "behauptete-relevanz", "hinweis",
        (r"(?:aufmerksam\s+geworden|auf\s+(?:Sie|dich|euch)\s+gesto(?:ß|ss)en"
         r"|ich\s+habe\s+gesehen,\s+dass|beim\s+St(?:ö|oe)bern)"),
        "Konkreten, nachpruefbaren Anlass nennen oder den Satz streichen.",
    ),
    (
        "nachfass-ohne-vorgeschichte", "stark",
        (r"(?:meine\s+letzte\s+(?:Nachricht|E-?Mail)|ob\s+(?:meine|die)\s+Nachricht"
         r"|wollte\s+(?:kurz\s+)?nachfassen|falls\s+(?:Sie|du)\s+(?:es\s+)?(?:ü|ue)bersehen)"),
        "Nur verwenden, wenn eine erste Nachricht wirklich verschickt wurde und im Thread referenziert ist.",
    ),
    (
        "rechtfertigungsabsatz", "stark",
        (r"(?:berechtigte[sn]?\s+Interesse|(?:ö|oe)ffentlich\s+zug(?:ä|ae)nglichen?\s+Quellen"
         r"|einmalig\s+zu\s+kontaktieren|kein\s+zweites\s+Mal\s+kontaktieren)"),
        "Standardbaustein aus Outreach-Vorlagen. Herkunft der Adresse konkret benennen oder Absatz streichen.",
    ),
    (
        "terminlink-koeder", "hinweis",
        (r"(?:15[\s-]?Minuten|kurzes?\s+(?:Gespr(?:ä|ae)ch|Call)|unverbindlich"
         r"|kostenlos\s+(?:testen|ausprobieren)|Kennenlerngespr(?:ä|ae)ch)"),
        "Formel aus Kaltakquise-Vorlagen. Konkreten Zweck und Dauer nennen statt der Standardfloskel.",
    ),
)


class Sammler(HTMLParser):
    """Liest Anker, Bilder, sichtbaren Text und Vorlagenmarker aus HTML."""

    UEBERSPRINGEN = {"style", "script", "head", "title"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.anker: list[dict] = []
        self.bilder: list[dict] = []
        self.textteile: list[str] = []
        self._ankerstapel: list[dict] = []
        self._stumm = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        werte = {name.lower(): (wert or "") for name, wert in attrs}
        if tag in self.UEBERSPRINGEN:
            self._stumm += 1
            return
        if tag == "a":
            eintrag = {"ziel": werte.get("href", "").strip(), "text": ""}
            self.anker.append(eintrag)
            self._ankerstapel.append(eintrag)
        elif tag == "img":
            self.bilder.append(
                {
                    "quelle": werte.get("src", "").strip(),
                    "breite": werte.get("width", "").strip(),
                    "hoehe": werte.get("height", "").strip(),
                    "alt": werte.get("alt", "").strip(),
                    "stil": werte.get("style", "").strip(),
                }
            )
        elif tag == "br":
            self.textteile.append(" ")

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"img", "br"}:
            self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        if tag in self.UEBERSPRINGEN:
            self._stumm = max(0, self._stumm - 1)
            return
        if tag == "a" and self._ankerstapel:
            self._ankerstapel.pop()
        if tag in {"p", "div", "tr", "li", "table"}:
            self.textteile.append(" ")

    def handle_data(self, daten: str) -> None:
        if self._stumm:
            return
        self.textteile.append(daten)
        for eintrag in self._ankerstapel:
            eintrag["text"] += daten

    @property
    def sichtbarer_text(self) -> str:
        return normiert("".join(self.textteile))


def normiert(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def entfaltet(text: str) -> str:
    """Loest Kopfzeilenfaltung auf, erhaelt aber Mehrfach-Leerzeichen als Befund.

    Nach RFC 5322 besteht eine Faltung aus CRLF und mindestens einem folgenden
    Leerzeichen; beides zusammen wird zu genau einem Leerzeichen. Sonst wuerde
    jede gefaltete Kopfzeile ein doppeltes Leerzeichen vortaeuschen.
    """
    entfaltet_text = re.sub(r"\r?\n[ \t]+", " ", text or "")
    return re.sub(r"[\r\n\t]+", " ", entfaltet_text).strip()


def gekuerzt(text: str, laenge: int = 160) -> str:
    knapp = normiert(text)
    return knapp if len(knapp) <= laenge else knapp[: laenge - 1] + "…"


def host_aus_url(url: str) -> str:
    treffer = re.match(r"^\s*(?:https?:)?//([^/?#\s]+)", url or "", re.I)
    if not treffer:
        return ""
    host = treffer.group(1).split("@")[-1].split(":")[0]
    return host.strip(".").lower()


def registrierbare_domain(host: str) -> str:
    label = [teil for teil in (host or "").lower().split(".") if teil]
    if len(label) < 2:
        return ".".join(label)
    if ".".join(label[-2:]) in MEHRTEILIGE_SUFFIXE and len(label) >= 3:
        return ".".join(label[-3:])
    return ".".join(label[-2:])


def gleiche_domain(links: str, rechts: str) -> bool:
    if not links or not rechts:
        return True
    return registrierbare_domain(links) == registrierbare_domain(rechts)


def domains_im_text(text: str) -> list[str]:
    gefunden: list[str] = []
    rest = text or ""
    for treffer in URL_IM_TEXT.finditer(rest):
        host = host_aus_url(treffer.group(0))
        if host:
            gefunden.append(host)
    ohne_urls = URL_IM_TEXT.sub(" ", rest)
    for treffer in BLANKE_DOMAIN.finditer(ohne_urls):
        kandidat = treffer.group(1).lower().rstrip(".")
        if "." in kandidat and not kandidat.endswith((".jpg", ".png", ".gif", ".pdf")):
            gefunden.append(kandidat)
    return gefunden


def befund(regel: str, klasse: str, schwere: str, fundstelle: str, beleg: str, korrektur: str) -> dict:
    return {
        "regel": regel,
        "klasse": klasse,
        "schwere": schwere,
        "fundstelle": fundstelle,
        "beleg": gekuerzt(beleg),
        "korrektur": korrektur,
    }


def umfeld(text: str, start: int, ende: int, rand: int = 60) -> str:
    return text[max(0, start - rand) : min(len(text), ende + rand)]


def pruefe_linkziele(anker: list[dict]) -> list[dict]:
    treffer: list[dict] = []
    for eintrag in anker:
        ziel = eintrag["ziel"]
        if not ziel.lower().startswith(("http://", "https://", "//")):
            continue
        zielhost = host_aus_url(ziel)
        if not zielhost:
            continue
        for genannt in domains_im_text(eintrag["text"]):
            if not gleiche_domain(genannt, zielhost):
                treffer.append(
                    befund(
                        "linkziel-weicht-ab", "A", "hart", "HTML-Link",
                        f"sichtbar {genannt} → Ziel {zielhost}",
                        "Sichtbaren Text und Linkziel auf dieselbe Domain bringen. "
                        "Sonst liest der Filter das Muster als Verschleierung.",
                    )
                )
                break
    return treffer


def pruefe_abmeldung(kopfzeilen: dict, sichtbar: str, hat_kopfzeilen: bool) -> list[dict]:
    treffer: list[dict] = []
    hat_header = "list-unsubscribe" in kopfzeilen
    hat_post = "list-unsubscribe-post" in kopfzeilen
    if hat_post and not hat_header:
        treffer.append(
            befund(
                "abmeldung-unvollstaendig", "A", "hart", "Kopfzeilen",
                "List-Unsubscribe-Post ohne List-Unsubscribe",
                "Beide Kopfzeilen setzen. Ein One-Click-Post ohne Ziel ist ein defekter Abmeldeweg (RFC 8058).",
            )
        )
    if hat_kopfzeilen and not hat_header:
        if ABMELDE_MUSTER.search(sichtbar):
            treffer.append(
                befund(
                    "abmeldung-nur-im-text", "A", "stark", "Kopfzeilen",
                    "Abmeldehinweis im Text, kein List-Unsubscribe im Kopf",
                    "List-Unsubscribe ergaenzen. Wer im Text abmelden laesst, versendet Werbung "
                    "und sollte sie auch im Kopf kennzeichnen.",
                )
            )
    return treffer


def pruefe_thread(kopfzeilen: dict, sichtbar: str, roh_text: str, html: str, hat_kopfzeilen: bool) -> list[dict]:
    treffer: list[dict] = []
    eigene_id = (kopfzeilen.get("message-id", [""])[0] or "").strip()
    bezug = " ".join(kopfzeilen.get("references", []) + kopfzeilen.get("in-reply-to", []))
    if eigene_id and eigene_id in bezug:
        treffer.append(
            befund(
                "thread-selbstbezug", "A", "hart", "Kopfzeilen",
                f"References verweist auf die eigene Message-ID {eigene_id}",
                "References und In-Reply-To nur mit der Message-ID einer tatsaechlich vorhandenen "
                "Vorgaengernachricht fuellen, sonst weglassen.",
            )
        )
    zitat_html = any(marker in html.lower() for marker in ("gmail_quote", "<blockquote"))
    zitat_text = bool(ZITAT_MARKER.search(roh_text))
    if zitat_html or zitat_text:
        if hat_kopfzeilen and not bezug.strip():
            treffer.append(
                befund(
                    "zitat-ohne-vorgaenger", "A", "hart", "Nachrichtenkoerper",
                    "Zitatblock vorhanden, In-Reply-To und References fehlen",
                    "Zitat nur verwenden, wenn die zitierte Nachricht existiert und im Kopf referenziert ist.",
                )
            )
        elif not hat_kopfzeilen:
            treffer.append(
                befund(
                    "zitat-ohne-vorgaenger", "A", "hinweis", "Nachrichtenkoerper",
                    "Zitatblock im Entwurf",
                    "Beim Versand muessen In-Reply-To und References auf die zitierte Nachricht zeigen.",
                )
            )
    return treffer


MERGE_MUSTER = (
    (r"\{\{|\}\}|\[\[|\]\]|%%|\*\|", "Platzhalter der Versandvorlage"),
    (r"\$\{[^}]*\}", "nicht ersetzte Variable"),
    (r"\bundefined\b|\bNaN\b|\[object Object\]", "leerer Feldwert"),
    (r"(?:Hallo|Hi|Moin|Guten Tag|Liebe[rs]?)\s+[,!]", "Anrede ohne Namen"),
    (r"\S {2,}\S", "doppeltes Leerzeichen"),
)


def pruefe_merge(betreff: str, sichtbar: str) -> list[dict]:
    treffer: list[dict] = []
    for stelle, inhalt in (("Betreff", betreff), ("Nachrichtenkoerper", sichtbar)):
        if not inhalt:
            continue
        for muster, erklaerung in MERGE_MUSTER:
            fund = re.search(muster, inhalt)
            if not fund:
                continue
            ausschnitt = umfeld(inhalt, fund.start(), fund.end(), 25)
            ausschnitt = re.sub(r" {2,}", lambda stelle_: "·" * len(stelle_.group(0)), ausschnitt)
            treffer.append(
                befund(
                    "merge-artefakt", "A", "hart", stelle,
                    f"{erklaerung}: {ausschnitt}",
                    "Seriendruckfeld fuellen oder den Satz ohne das Feld formulieren. "
                    "Sichtbare Vorlagenreste weisen die Nachricht als Massenversand aus.",
                )
            )
    return treffer


def pruefe_zaehlpixel(bilder: list[dict]) -> list[dict]:
    treffer: list[dict] = []
    for bild in bilder:
        stil = bild["stil"].lower().replace(" ", "")
        winzig = bild["breite"] in {"1", "1px"} or bild["hoehe"] in {"1", "1px"}
        winzig = winzig or "width:1px" in stil or "height:1px" in stil
        versteckt = "display:none" in stil or "visibility:hidden" in stil or "opacity:0" in stil
        if not (winzig or versteckt):
            continue
        if versteckt:
            treffer.append(
                befund(
                    "zaehlpixel-versteckt", "A", "hart", "HTML-Bild",
                    f"{bild['quelle']} mit {bild['stil']}",
                    "Verstecktes Zaehlpixel entfernen. Wenn Oeffnungsmessung noetig ist, "
                    "sie offenlegen statt sie zu verbergen.",
                )
            )
        if winzig and bild["alt"]:
            treffer.append(
                befund(
                    "zaehlpixel-falsches-alt", "A", "hart", "HTML-Bild",
                    f"1x1-Pixel mit alt=\"{bild['alt']}\"",
                    "Einem Zaehlpixel keinen inhaltlichen Alternativtext geben. "
                    "Ein als Logo deklariertes Ein-Pixel-Bild ist ein Verschleierungsmerkmal.",
                )
            )
        elif winzig and not versteckt:
            treffer.append(
                befund(
                    "zaehlpixel-vorhanden", "A", "hinweis", "HTML-Bild",
                    f"1x1-Pixel {bild['quelle']}",
                    "Oeffnungsmessung ist ein Werbemerkmal. Nutzen gegen den Zustellnachteil abwaegen.",
                )
            )
    return treffer


def pruefe_domainstreuung(rollen: dict, hat_kopfzeilen: bool) -> list[dict]:
    verwendet = {rolle: sorted(werte) for rolle, werte in rollen.items() if werte}
    alle = {wert for werte in verwendet.values() for wert in werte}
    if len(alle) < 2:
        return []
    absender = set(rollen.get("Absender", set()))
    fremd = sorted(alle - absender)
    if hat_kopfzeilen and absender and not fremd:
        return []
    beschreibung = "; ".join(f"{rolle}: {', '.join(werte)}" for rolle, werte in sorted(verwendet.items()))
    return [
        befund(
            "domainstreuung", "A", "stark", "Nachricht",
            beschreibung,
            "Links und Bilder von der eigenen Absenderdomain ausliefern. Je mehr fremde Domains "
            "eine Nachricht verteilt, desto eher wird sie als Versandplattform-Werbung erkannt.",
        )
    ]


def pruefe_verhaeltnis(sichtbar: str, html: str) -> tuple[list[dict], float | None]:
    if not html:
        return [], None
    verhaeltnis = round(len(sichtbar) / len(html), 3)
    if verhaeltnis >= 0.35:
        return [], verhaeltnis
    schwere = "stark" if verhaeltnis < 0.25 else "hinweis"
    return (
        [
            befund(
                "text-html-verhaeltnis", "A", schwere, "HTML-Teil",
                f"{len(sichtbar)} Zeichen Text auf {len(html)} Zeichen HTML, Verhaeltnis {verhaeltnis}",
                "Markup reduzieren oder Inhalt ergaenzen. Viel Geruest bei wenig Text ist ein Werbemerkmal.",
            )
        ],
        verhaeltnis,
    )


def pruefe_domain_im_text(sichtbar: str, absenderdomain: str) -> list[dict]:
    if not absenderdomain:
        return []
    eigenes_label = absenderdomain.split(".")[0]
    gemeldet: set[str] = set()
    treffer: list[dict] = []
    for genannt in domains_im_text(sichtbar):
        registriert = registrierbare_domain(genannt)
        if registriert in gemeldet or registriert == absenderdomain:
            continue
        if registriert.split(".")[0] == eigenes_label:
            gemeldet.add(registriert)
            treffer.append(
                befund(
                    "domain-im-text-weicht-ab", "A", "stark", "Nachrichtenkoerper",
                    f"im Text {registriert}, versendet von {absenderdomain}",
                    "Von derselben Domain versenden, die im Text genannt wird, oder den Unterschied erklaeren.",
                )
            )
    return treffer


def pruefe_inhalt(sichtbar: str) -> list[dict]:
    treffer: list[dict] = []
    for regel, schwere, muster, korrektur in PHRASEN:
        if muster is None:
            continue
        fund = re.search(muster, sichtbar, re.I)
        if fund:
            treffer.append(
                befund(regel, "B", schwere, "Nachrichtenkoerper",
                       umfeld(sichtbar, fund.start(), fund.end()), korrektur)
            )
    korrektur_zahl = next(eintrag[3] for eintrag in PHRASEN if eintrag[0] == "kennzahl-ohne-beleg")
    for muster in (PROZENTWERT, GROSSE_ZAHL):
        for fund in muster.finditer(sichtbar):
            if BELEG_NAHE.search(umfeld(sichtbar, fund.start(), fund.end(), 120)):
                continue
            treffer.append(
                befund("kennzahl-ohne-beleg", "B", "stark", "Nachrichtenkoerper",
                       umfeld(sichtbar, fund.start(), fund.end()), korrektur_zahl)
            )
            break
    einstieg = sichtbar[:200]
    erster_satz = re.split(r"(?<=[.!?])\s", sichtbar.strip(), maxsplit=1)[0] if sichtbar.strip() else ""
    if erster_satz.endswith("?"):
        treffer.append(
            befund("rhetorische-frage-einstieg", "B", "hinweis", "Einstieg", erster_satz,
                   "Mit dem Anlass beginnen statt mit einer Frage, die der Empfaenger nicht gestellt hat.")
        )
    if EMOJI.search(einstieg):
        treffer.append(
            befund("emoji-im-einstieg", "B", "hinweis", "Einstieg", einstieg,
                   "Emoji im ersten Satz weglassen. In geschaeftlicher Erstansprache ist es ein Werbemerkmal.")
        )
    return treffer


def pruefe_kontext(kopfzeilen: dict, sichtbar: str, html: str) -> list[dict]:
    treffer: list[dict] = []
    persoenlich = re.search(r"\b(?:Hallo|Hi|Moin|Guten Tag|Liebe[rs]?)\s+\w", sichtbar)
    for kopf, regel, hinweistext in (
        ("from", "rollenpostfach-absender",
         "Persoenliche Anrede aus einem Rollenpostfach. Von einer benannten Person senden."),
        ("to", "empfaenger-rollenadresse",
         "Rollenadresse ohne Versandhistorie. Ein Filter hat hier keinen Vertrauensanker."),
    ):
        wert = (kopfzeilen.get(kopf, [""])[0] or "")
        adresse = re.search(r"([\w.+-]+)@([\w.-]+)", wert)
        if not adresse:
            continue
        if adresse.group(1).lower() not in ROLLEN_LOKALTEILE:
            continue
        if regel == "rollenpostfach-absender" and not persoenlich:
            continue
        treffer.append(befund(regel, "C", "hinweis", f"Kopfzeile {kopf.title()}",
                              adresse.group(0), hinweistext))
    niedrig = html.lower()
    marker = [name for name in HANDSCHRIFT_MARKER if name in niedrig]
    if marker:
        treffer.append(
            befund("handschrift-imitat", "C", "stark", "HTML-Teil", ", ".join(marker),
                   "Vorlagenreste entfernen, die eine handgeschriebene Nachricht vortaeuschen. "
                   "Filter erkennen diese Marker zusammen mit dem Plattformversand.")
        )
    return treffer


def filterurteil(kopfzeilen: dict) -> dict:
    def erst(name: str) -> str:
        return normiert(kopfzeilen.get(name, [""])[0])

    forefront = erst("x-forefront-antispam-report")
    microsoft = {}
    for schluessel in ("CAT", "DIR", "SFV", "SRV", "SCL", "CIP", "CTRY", "LANG", "H", "PTR"):
        fund = re.search(rf"(?:^|;)\s*{schluessel}:([^;]*)", forefront)
        if fund and fund.group(1).strip():
            microsoft[schluessel] = fund.group(1).strip()
    scl_kopf = erst("x-ms-exchange-organization-scl")
    if scl_kopf:
        microsoft["SCL"] = scl_kopf
    bulk = re.search(r"BCL:(\d+)", erst("x-microsoft-antispam"))
    if bulk:
        microsoft["BCL"] = bulk.group(1)
    zustellung = erst("x-microsoft-antispam-mailbox-delivery")
    ablage = re.search(r"RF:([^;]*)", zustellung)
    if ablage:
        microsoft["RF"] = ablage.group(1).strip()

    spam_status = erst("x-spam-status")
    gateway = {}
    if spam_status:
        gateway["urteil"] = spam_status.split(",")[0].strip()
        punkte = re.search(r"score=(-?[\d.]+)", spam_status)
        schwelle = re.search(r"required=(-?[\d.]+)", spam_status)
        tests = re.search(r"tests=\[([^\]]*)\]", spam_status)
        if punkte:
            gateway["punkte"] = punkte.group(1)
        if schwelle:
            gateway["schwelle"] = schwelle.group(1)
        if tests:
            gateway["regeln"] = [teil.strip() for teil in tests.group(1).split(",") if teil.strip()]

    authentifizierung = {}
    quelle = erst("authentication-results") or erst("arc-authentication-results")
    for name in ("spf", "dkim", "dmarc", "compauth"):
        fund = re.search(rf"\b{name}=(\w+)", quelle)
        if fund:
            authentifizierung[name] = fund.group(1)

    urteil = {}
    if microsoft:
        urteil["microsoft"] = microsoft
    if gateway:
        urteil["gateway"] = gateway
    if authentifizierung:
        urteil["authentifizierung"] = authentifizierung
    return urteil


def analysiere(betreff: str, text: str, html: str, kopfzeilen: dict | None = None) -> dict:
    kopfzeilen = kopfzeilen or {}
    hat_kopfzeilen = bool(kopfzeilen)
    sammler = Sammler()
    if html:
        sammler.feed(html)
        sammler.close()
    html_sichtbar = sammler.sichtbarer_text
    sichtbar = html_sichtbar or normiert(text)

    absender = re.search(r"@([\w.-]+)", (kopfzeilen.get("from", [""])[0] or ""))
    absenderdomain = registrierbare_domain(absender.group(1)) if absender else ""
    link_hosts = {host_aus_url(eintrag["ziel"]) for eintrag in sammler.anker}
    link_hosts |= {host_aus_url(treffer.group(0)) for treffer in URL_IM_TEXT.finditer(text or "")}
    bild_hosts = {host_aus_url(bild["quelle"]) for bild in sammler.bilder}
    nachrichten_id = re.search(r"@([\w.-]+)>?\s*$", (kopfzeilen.get("message-id", [""])[0] or "").strip())
    rollen = {
        "Absender": {absenderdomain} if absenderdomain else set(),
        "Links": {registrierbare_domain(host) for host in link_hosts if host},
        "Bilder": {registrierbare_domain(host) for host in bild_hosts if host},
        "Message-ID": {registrierbare_domain(nachrichten_id.group(1))} if nachrichten_id else set(),
    }

    befunde: list[dict] = []
    befunde += pruefe_linkziele(sammler.anker)
    befunde += pruefe_abmeldung(kopfzeilen, sichtbar, hat_kopfzeilen)
    befunde += pruefe_thread(kopfzeilen, sichtbar, text or "", html or "", hat_kopfzeilen)
    befunde += pruefe_merge(entfaltet(betreff), sichtbar)
    befunde += pruefe_zaehlpixel(sammler.bilder)
    befunde += pruefe_domainstreuung(rollen, hat_kopfzeilen)
    verhaeltnis_befunde, verhaeltnis = pruefe_verhaeltnis(html_sichtbar, html or "")
    befunde += verhaeltnis_befunde
    befunde += pruefe_domain_im_text(sichtbar, absenderdomain)
    befunde += pruefe_inhalt(sichtbar)
    befunde += pruefe_kontext(kopfzeilen, sichtbar, html or "")
    befunde.sort(key=lambda eintrag: (SCHWERE_ORDNUNG[eintrag["schwere"]], eintrag["klasse"], eintrag["regel"]))

    ergebnis = {
        "schema_version": SCHEMA_VERSION,
        "betreff": normiert(betreff),
        "kennzahlen": {
            "sichtbare_textlaenge": len(sichtbar),
            "html_laenge": len(html or ""),
            "text_html_verhaeltnis": verhaeltnis,
            "anzahl_links": len(sammler.anker),
            "anzahl_bilder": len(sammler.bilder),
            "domains": {rolle: sorted(werte) for rolle, werte in rollen.items() if werte},
        },
        "befunde": befunde,
        "zusammenfassung": {
            schwere: sum(1 for eintrag in befunde if eintrag["schwere"] == schwere)
            for schwere in SCHWERE_ORDNUNG
        },
        "hinweis": (
            "Befundliste, keine Zustellprognose. Domainalter, Versandhistorie, Volumen und "
            "Empfaengerbeziehung wirken zusaetzlich und stehen nicht im Text."
        ),
    }
    if hat_kopfzeilen:
        urteil = filterurteil(kopfzeilen)
        if urteil:
            ergebnis["filterurteil"] = urteil
    return ergebnis


def teiltext(teil) -> str:
    try:
        inhalt = teil.get_content()
        return inhalt if isinstance(inhalt, str) else ""
    except (LookupError, ValueError, TypeError):
        roh = teil.get_payload(decode=True)
        return roh.decode("utf-8", errors="replace") if roh else ""


def lade_eml(pfad: Path) -> tuple[str, str, str, dict]:
    with pfad.open("rb") as datei:
        nachricht = email.message_from_binary_file(datei, policy=policy.default)
    kopfzeilen: dict[str, list[str]] = {}
    for name, wert in nachricht.items():
        kopfzeilen.setdefault(name.lower(), []).append(str(wert))
    text = ""
    html = ""
    for teil in nachricht.walk():
        if teil.get_content_maintype() == "multipart":
            continue
        if teil.get_content_disposition() == "attachment":
            continue
        art = teil.get_content_type()
        if art == "text/plain" and not text:
            text = teiltext(teil)
        elif art == "text/html" and not html:
            html = teiltext(teil)
    betreff = str(nachricht.get("Subject", "") or "")
    return betreff, text, html, kopfzeilen


UEBERSCHRIFT = {
    "hart": "Harte Defekte",
    "stark": "Starke Auffaelligkeiten",
    "hinweis": "Hinweise",
}


def als_text(ergebnis: dict) -> str:
    zeilen: list[str] = []
    if ergebnis["betreff"]:
        zeilen.append(f"Betreff: {ergebnis['betreff']}")
    urteil = ergebnis.get("filterurteil", {})
    if urteil:
        zeilen.append("")
        zeilen.append("Filterurteil der empfangenden Seite")
        for bereich, werte in urteil.items():
            teile = ", ".join(
                f"{name}={wert if not isinstance(wert, list) else ' '.join(wert)}"
                for name, wert in werte.items()
            )
            zeilen.append(f"  {bereich}: {teile}")
    kennzahlen = ergebnis["kennzahlen"]
    zeilen.append("")
    zeilen.append(
        "Kennzahlen: {} Zeichen Text, {} Zeichen HTML, Verhaeltnis {}, {} Links, {} Bilder".format(
            kennzahlen["sichtbare_textlaenge"], kennzahlen["html_laenge"],
            kennzahlen["text_html_verhaeltnis"], kennzahlen["anzahl_links"],
            kennzahlen["anzahl_bilder"],
        )
    )
    for rolle, werte in kennzahlen["domains"].items():
        zeilen.append(f"  {rolle}: {', '.join(werte)}")
    for schwere in ("hart", "stark", "hinweis"):
        gruppe = [eintrag for eintrag in ergebnis["befunde"] if eintrag["schwere"] == schwere]
        if not gruppe:
            continue
        zeilen.append("")
        zeilen.append(f"{UEBERSCHRIFT[schwere]} ({len(gruppe)})")
        for eintrag in gruppe:
            zeilen.append(f"  [{eintrag['klasse']}] {eintrag['regel']} — {eintrag['fundstelle']}")
            zeilen.append(f"      Beleg: {eintrag['beleg']}")
            zeilen.append(f"      Korrektur: {eintrag['korrektur']}")
    if not ergebnis["befunde"]:
        zeilen.append("")
        zeilen.append("Kein Befund aus dem geprueften Regelwerk.")
    zeilen.append("")
    zeilen.append(ergebnis["hinweis"])
    return "\n".join(zeilen)


def lies_vorgabe(wert: str | None, pfad: str | None, bezeichnung: str) -> str:
    if wert is not None and pfad is not None:
        raise SystemExit(f"--{bezeichnung} und --{bezeichnung}-datei schliessen einander aus")
    if pfad is not None:
        return Path(pfad).read_text(encoding="utf-8", errors="replace")
    return wert or ""


def main(argv: list[str] | None = None) -> int:
    zerleger = argparse.ArgumentParser(
        description="Prueft E-Mail-Entwuerfe und empfangene Nachrichten auf bekannte Junk-Ausloeser.",
    )
    zerleger.add_argument("--json", action="store_true", help="Ergebnis als JSON ausgeben")
    zerleger.add_argument(
        "--strict", action="store_true",
        help="Rueckgabewert 1, wenn ein Befund der Schwere hart vorliegt",
    )
    unterbefehle = zerleger.add_subparsers(dest="befehl", required=True)

    eml = unterbefehle.add_parser("pruefe-eml", help="empfangene Nachricht als .eml auswerten")
    eml.add_argument("pfad", help="Pfad zur .eml-Datei")

    entwurf = unterbefehle.add_parser("pruefe-entwurf", help="eigenen Entwurf auswerten")
    entwurf.add_argument("--betreff", default="")
    entwurf.add_argument("--text")
    entwurf.add_argument("--text-datei", dest="text_datei")
    entwurf.add_argument("--html")
    entwurf.add_argument("--html-datei", dest="html_datei")

    argumente = zerleger.parse_args(argv)

    if argumente.befehl == "pruefe-eml":
        pfad = Path(argumente.pfad)
        if not pfad.is_file():
            print(f"Datei nicht gefunden: {pfad}", file=sys.stderr)
            return 2
        betreff, text, html, kopfzeilen = lade_eml(pfad)
        ergebnis = analysiere(betreff, text, html, kopfzeilen)
        ergebnis["quelle"] = pfad.name
    else:
        text = lies_vorgabe(argumente.text, argumente.text_datei, "text")
        html = lies_vorgabe(argumente.html, argumente.html_datei, "html")
        if not text.strip() and not html.strip():
            print("Weder Text noch HTML uebergeben", file=sys.stderr)
            return 2
        ergebnis = analysiere(argumente.betreff, text, html, None)
        ergebnis["quelle"] = "entwurf"

    if argumente.json:
        print(json.dumps(ergebnis, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(als_text(ergebnis))

    if argumente.strict and ergebnis["zusammenfassung"]["hart"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
