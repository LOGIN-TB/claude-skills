---
name: image
description: "Marketingbilder rechtebewusst planen, erzeugen, bearbeiten, optimieren und prüfen. Nutze diesen Skill für Bildbriefings, Produktscreenshots und Mock-ups, generative Bilder, Stock- und Lizenzrouten, Bildbearbeitung, Formate und Komprimierung sowie deutsche Alt-Texte. Klärt Herkunft und Nutzungsrechte vor der Produktion, beachtet Persönlichkeits-, Marken- und Urheberrecht, verlangt Kennzeichnung wo nötig und schließt erfundene Produktansichten und unbelegte Bildaussagen aus. Nicht gedacht für Logos, Design-Systeme und Layoutarbeit."
license: MIT
metadata:
  version: "2.0.1"
  author: "Corey Haines; DACH-Adaption LOGIN"
  upstream: coreyhaines31/marketingskills
  upstream_commit: 7868cb9251fad80a73d26e488a5ad5f6c4a9f335
  upstream_homepage: https://github.com/coreyhaines31/marketingskills/tree/7868cb9251fad80a73d26e488a5ad5f6c4a9f335/skills/image
  tags: [image, marketing-visuals, image-generation, image-editing, optimization]
  related_skills: [product-marketing]
---

# Bildproduktion

Plane, erzeuge, bearbeite, komponiere, optimiere und prüfe Marketingbilder unter Wahrung von Herkunft, Rechten, Markenintegrität, Privatsphäre und wahrheitsgemäßer Produktdarstellung. Eine Bildanfrage erlaubt das angefragte Artefakt, nicht ungefragte Dateisuche, bezahlte Dienste, Kontoaktionen, Veröffentlichung oder destruktive Stapelbearbeitung. Das gelieferte Ergebnis muss tatsächlich geöffnet und geprüft werden.

## Sicherheit, Rechte und Herkunft

1. **Projektlokaler Umfang.** Nur bereitgestellte Assets und relevante Dateien im benannten Projekt verwenden; keine privaten Fotobibliotheken, Cloudspeicher, Browserprofile oder Zugangsdaten durchsuchen.
2. **Keine Geheimnisse.** Keine API-Schlüssel im Chat, Prompt, URL, Metadatum oder Ergebnis. Kostenpflichtige/externe Verarbeitung und Uploads vorab mit Anbieter, Material und Umfang freigeben lassen.
3. **Rechteinventar.** Eigentum, Lizenz, Einwilligung, Attribution und Einschränkungen für Logos, Schriften, Fotos, Screenshots, Illustrationen, Stockmaterial, Produktdesigns, Marken und Stilreferenzen dokumentieren.
4. **Personen und Bildnisse.** Reale Personen oder private Fotos nur mit angemessener Autorisierung verwenden. Keine falschen Empfehlungen, Identitätstäuschung, intime Darstellung oder irreführende Darstellung folgenreicher Handlungen.
5. **Minderjährige und Schutzbedürftige.** Identifizierbare Darstellungen im Marketing nur bei klarem legitimen Zweck, geeigneter Einwilligung, Schutzkonzept und erforderlicher Prüfung.
6. **Marken und Zugehörigkeit.** Kundenlogos, Gütesiegel, Preise, Pressezeichen, Ratings und Partnermarken nur mit aktueller Berechtigung; keine unbelegte Kooperation suggerieren.
7. **Wahrheitsgemäße Produkte.** Für Produktversprechen echte aktuelle Screenshots verwenden. Konzept-UIs klar kennzeichnen; keine nicht verfügbaren Funktionen, Kundendaten, Sicherheitszustände oder Leistungswerte erfinden.
8. **Keine irreführende Dokumentation.** Wesentliche Bearbeitungen offenlegen, wenn sonst Täuschung droht. Keine Beweisfotos, Belege, Dashboards, Testimonials, Gesundheits- oder Finanzergebnisse erfinden.
9. **Stilanfragen.** Keinen exakten Stil lebender Kreativer versprechen oder Urheberschaft suggerieren; in allgemeine visuelle Merkmale übersetzen, sofern keine zulässigen autorisierten Assets vorliegen.
10. **Privatsphäre und Metadaten.** Standort-, Geräte-, Autoren- und Vorschaudaten prüfen. Nur an Kopien und nach Freigabe entfernen; notwendige Rechte-/Herkunftsdaten erhalten und Entfernung verifizieren.
11. **Originale erhalten.** Separates Ausgabeverzeichnis und eindeutige Namen verwenden; keine In-place-Konverter, rekursiven Änderungen oder breiten Globs ohne Vorschau, Sicherung und Freigabe.
12. **Keine automatische Veröffentlichung.** Export erlaubt weder Website-/CMS-/Profiländerung noch Anzeigenstart.

## Briefing

Kläre Zweck, Zielgruppe, Botschaft, Platzierung, Maße, Seitenverhältnis, Format, Byte-Limit, Safe Areas, sichtbaren Text und Sprache, Markenfarben/-schriften/-logo, Quellen und Nutzungsrechte, Personen-/Produkt-/Markenbezug, Tool/Anbieter/Kosten, Ausgabepfad, Varianten, Barrierefreiheit, Lokalisierung, Hell/Dunkel und Druck. Aktuelle Plattformmaße aus Primärquellen prüfen.

## Produktionsweg

### Deterministisches Design

HTML/CSS/SVG, freigegebene Templates oder präzise Layoutmethoden bevorzugen, wenn Text, Logos, Geometrie, Barrierefreiheit oder Varianten exakt sein müssen. Generierung gegebenenfalls nur für Hintergründe/Konzepte einsetzen.

### Produktscreenshot und Mock-up

Echtes Produkt in autorisierter Demo-/Testumgebung erfassen. Personen-, Kunden-, Token-, Konto- und Produktionsdaten vorher entfernen. UI, Funktion, Datum und Umgebung prüfen und deterministisch annotieren. Kein generiertes Fake-UI als tatsächliche Produktansicht ausgeben.

### Generatives Bild

Modell nach freigegebenem Workflow wählen. Anbieterfähigkeiten, Preise, Bedingungen, Eigentum, Aufbewahrung und Referenzbildverarbeitung bei Relevanz aktuell prüfen. Prompt enthält Motiv/Handlung, Umgebung, Medium/Eigenschaften, Licht/Palette, Ausschnitt/Perspektive/Negativraum, Verhältnis/Komposition, gegebenenfalls exakten Text sowie Ausschlüsse wie Logos, Wasserzeichen, private Daten, zusätzliche Personen oder Fake-UI. „4K“ und Kamerajargon nicht verwenden, wenn sie keine reale Steuerwirkung haben.

### Browser-, Stock- und Lizenzroute

Bei angemeldetem Webgenerator `browser-generative-media-workflows` nutzen, nur genehmigte Referenzen hochladen, Abschluss prüfen und echte Datei herunterladen; nicht still einen anderen Generator ersetzen. Bei Stockmaterial aktuelle Lizenz, Attribution, kommerzielle Nutzung, Model-/Property-Releases, Gebiets- und Bearbeitungsgrenzen sowie Quelle, Urheber, Abrufdatum und Beleg dokumentieren.

### Bearbeitung und Optimierung

Immer mit Kopie arbeiten. Format und Qualität nach Motiv, Transparenz, Zielsystem, visueller QA und Byte-Budget wählen. Fotos können AVIF/WebP/JPEG nutzen; Screenshots/Liniengrafik brauchen Lesbarkeit; Logos/Illustrationen nur als vertrauenswürdiges, bereinigtes SVG. Nicht blind Metadaten entfernen. Unbekannte SVGs auf Skripte, externe Referenzen, Handler, HTML und Remote-Assets prüfen.

## Produktionsablauf

1. Briefing, Rechte, Quellen, Anbieter, Kosten und Ziel bestätigen.
2. Nur autorisierte Inputs prüfen und Herkunft erfassen.
3. Günstigen Konzeptentwurf oder deterministischen Draft erstellen.
4. Komposition, Marke, Text, Produkttreue, Identität, Hände/Gesichter, Reflexionen und Artefakte prüfen.
5. Im freigegebenen Weg iterieren; keine neuen Uploads oder Mehrkosten ohne Freigabe.
6. Exakte Texte, Logos, Labels und UI deterministisch ergänzen.
7. Neue Datei mit expliziten Maßen und Format exportieren.
8. Export dekodieren und visuell prüfen, nicht nur Dateiexistenz melden.
9. Maße, Verhältnis, Farbe, Transparenz, Typ, Bytes, Metadaten und Varianten verifizieren.
10. In tatsächlicher Anzeigegröße erneut öffnen und Lesbarkeit/Safe Areas prüfen.
11. Werkzeug/Anbieter, Bearbeitung, Quellen/Lizenzen, Pfad und Einschränkungen berichten.

## Marketing, Barrierefreiheit und Aussagen

Hero-/Previewbilder auf echtes Template und Crop-Verhalten testen; `1200×630` ist kein Universalformat. Social-Varianten je Verhältnis neu komponieren, wenn Zuschnitt Bedeutung, Hierarchie, Gesicht, UI oder Text verändert. Produktbilder nur mit echten Screenshots, Demo-Konten und synthetischen nicht sensiblen Daten.

Logos/Icons aus Generierung sind nicht automatisch originär, registrierbar, konfliktfrei, barrierefrei oder vektortauglich. Vor Nutzung Ähnlichkeit, Markenlage, Schriftlizenz, Vektorqualität, Kleingröße, Monochrom und Kontrast prüfen.

Alt-Text beschreibt Funktion und Kontext statt Keywords. Dekorative Bilder erhalten, wo passend, leeren Alt-Text. Benachbarten Text nicht unnötig wiederholen; wesentliche Information nie ausschließlich als Bild kodieren; Diagramme und textlastige Grafiken brauchen ein gleichwertiges Textäquivalent. Deutsche Alt-Texte natürlich, knapp und kontextgerecht formulieren; sichtbaren Text nicht als Keywordliste abschreiben.

Vor öffentlicher Nutzung Produkt-/Leistungs-, Kunden-, Partner-, Zertifizierungs-, Umwelt-, Gesundheits-, Finanz-, Sicherheits-, Rechts- und Vergleichaussagen sowie synthetische oder wesentlich bearbeitete Darstellungen prüfen. Wasserzeichen, Eigentumszeichen, Offenlegungen oder Authentizitätsnachweise nicht zur Verschleierung entfernen.

## Deutscher/DACH-Kontext

**Standardannahme ist Deutschland**, sofern kein Zielmarkt benannt ist. Das ist keine Rechtsberatung und keine Rechtsgarantie. Für produktive Kampagnen sind konkrete Nutzung, Medium, Lizenz, Einwilligung, Branche und Plattform fachkundig zu prüfen.

- **Deutschland:** Urheber-, Nutzungs-, **Bild-/Persönlichkeits- und Markenrechte** sowie Recht am eigenen Bild, Datenschutz, Wettbewerbsrecht und gegebenenfalls Kennzeichnung synthetischer oder werblicher Inhalte als Prüfpunkte behandeln. Ein öffentlich auffindbares Bild ist nicht automatisch frei nutzbar. Für Mitarbeitende, Kunden, Models und nutzergenerierte Inhalte Einwilligung, Nutzungsrechte oder eine andere einschlägige Grundlage zweck- und kanalspezifisch dokumentieren. Bei Gebäuden und Grundstücken Aufnahmeort, Hausrecht, Panoramafreiheit sowie Marken- und Designbezug getrennt prüfen; eine Freigabe ist nicht pauschal immer erforderlich.
- **Österreich:** österreichisches Urheber-, Bildnis-, Marken-, Datenschutz- und Lauterkeitsrecht separat prüfen; deutsche Freigaben nicht automatisch übertragen.
- **Schweiz:** schweizerisches Urheber-, Persönlichkeits-, Marken-, Datenschutz- und Lauterkeitsrecht sowie vereinbarte Gebietsrechte getrennt prüfen.

Bei grenzüberschreitenden Kampagnen Lizenzgebiet, Laufzeit, Medien, Bearbeitungsrecht sowie vertragliche Beendigungs-, Widerrufs- und Entfernungsprozesse für DE, AT und CH explizit erfassen. Nicht jede Lizenz oder Einwilligung ist jederzeit frei widerruflich; Grundlage und Vereinbarung getrennt bewerten.

## Ausgabeformat

- Lieferpfad oder Medienanhang
- Maße, Seitenverhältnis, Format und Byte-Größe
- Generator/Werkzeug und wesentliche Nachbearbeitung
- Quellen-/Referenzherkunft, Rechte- und Lizenzhinweise
- deutscher Alt-Text und gegebenenfalls Textäquivalent
- visuelle, technische und rechtliche Reviewpunkte
- QA-Ergebnis und verbleibende Einschränkungen
- klare Kennzeichnung, falls Konzept statt realer Produktdarstellung

## Prüfliste

- [ ] Jede Quelle hat bekannte Herkunft und zulässige Nutzung
- [ ] Bild-/Persönlichkeits- und Markenrechte sowie Freigaben geprüft
- [ ] Keine falsche Empfehlung, Funktion oder Dokumentarwirkung
- [ ] Datei dekodiert; Maße, Format, Farbe, Transparenz und Bytes korrekt
- [ ] Sichtbarer deutscher Text korrekt und lesbar
- [ ] Produkt-UI wahrheitsgemäß und frei von sensiblen Daten
- [ ] Gesichter, Hände, Logos, Schatten und Reflexionen visuell geprüft
- [ ] Crops, Safe Areas und Hierarchie in Zielgröße geprüft
- [ ] Originale unverändert; Metadatenpolitik verifiziert
- [ ] Deutscher Alt-Text/Textäquivalent geliefert
- [ ] Finale Datei geöffnet und visuell kontrolliert
- [ ] Keine Publikation oder Produktionsänderung ohne Freigabe

## Herkunft und Abweichungen

Deutsche/DACH-Adaption des MIT-lizenzierten Ausgangs-Skills von Corey Haines; Homepage und Commit bleiben unverändert in den Metadaten. Gegenüber Commit `7868cb9251fad80a73d26e488a5ad5f6c4a9f335` wurden Haupttext und Beschreibung vollständig deutsch gefasst, Deutschland als Standardannahme und Österreich/Schweiz separat ergänzt. Bild-/Persönlichkeits-/Markenrechte, Freigabegebiete und deutsche Alt-Texte wurden konkretisiert; Herkunft, Wahrheitstreue, Metadaten, sichere Bearbeitung sowie visuelle und technische Qualitätssicherung blieben fachlich vertieft. Zentraler Nachweis: `docs/UPSTREAM-AENDERUNGEN.md`.
