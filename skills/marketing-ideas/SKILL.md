---
name: marketing-ideas
description: "Kontextspezifische Marketinghypothesen entwickeln, vorprüfen und als messbare Experimente priorisieren. Nutze diesen Skill, wenn Ideen für Kanäle, Kampagnen, Angebote oder Wachstum gesucht werden, wenn eine Ideenliste auf Risiko und Machbarkeit geprüft werden soll, oder wenn aus Vorschlägen Experimentsteckbriefe mit Metrik, Laufzeit, Budget und Stopkriterium werden sollen. Sortiert vor der Bewertung aus, was rechtlich, plattformseitig oder finanziell nicht tragbar ist, und trennt Evidenz von Vermutung. Führt keine Kampagne aus und schaltet keine Anzeigen."
license: MIT
metadata:
  version: "2.0.0"
  author: "Corey Haines; DACH-Adaption LOGIN"
  upstream: coreyhaines31/marketingskills
  upstream_commit: 7868cb9251fad80a73d26e488a5ad5f6c4a9f335
  upstream_homepage: https://github.com/coreyhaines31/marketingskills/tree/7868cb9251fad80a73d26e488a5ad5f6c4a9f335/skills/marketing-ideas
  tags: [marketing-ideas, ideation, growth, experiments, prioritization]
  related_skills: [product-marketing, content-strategy, customer-research]
---

# Marketingideen und Experimente

Erzeuge und priorisiere kontextspezifische Marketinghypothesen statt einer Liste angeblich allgemein bewährter Taktiken. Standard ist eine Auswahlliste mit Testskizze im Chat. Ideenfindung erlaubt Analyse, aber keine Umsetzung.

## Sicherheits- und Evidenzregeln

1. **Begrenzte Quellen.** Nutze nur gelieferte Informationen und freigegebene Projektdateien. CRM, Analytics, E-Mail, Support, Kontaktlisten, Browserprofile, Communities und Zugangsdaten nicht ohne konkrete Freigabe verwenden.
2. **Ideen sind Hypothesen.** „Bewährt“, „Quick Win“, „günstig“, „beste“ oder „hohe Absicht“ nur mit vergleichbarer Evidenz. Trenne Beobachtung, interne Aussage, Drittschätzung, Hypothese und Unbekanntes.
3. **Keine Ausführung durch Andeutung.** Keine Recherche, Kontaktsammlung, Nachricht, Veröffentlichung, Kontoaktion, Anzeige, Ausgabe, Installation, Produkt-/Websiteänderung, Rabattaktion, Partnerschaft oder Vertrag ohne ausdrückliche Freigabe.
4. **Keine erfundenen Nachweise.** Keine Nachfrage, Conversion, Rendite, Rankings, Kundengeschichten, Empfehlungen, Dringlichkeit oder Wettbewerberschwächen erfinden.
5. **Datenschutz und Einwilligung.** Keine versteckte Verfolgung, Fingerprinting, Datenbroker-Anreicherung, Kontakt-Scraping, unerlaubte Profilbildung, private Community-Auswertung oder Audience-/Pixel-Weitergabe empfehlen.
6. **Plattformintegrität.** Keine Fake-Bewertungen, Review-Gating, Engagement-Pods, gekauften Follower, Cloaking, Identitätsverwechslung, Regelumgehung oder verdeckte Automatisierung.
7. **Suchintegrität.** Keine Doorway-Seiten, parasitäre Reputationsnutzung, Linkmanipulation, kopierte Vergleiche oder massenhafte dünne Inhalte.
8. **Faire Vergleiche.** Aktuelle Quellen, neutrale Abwägungen und Marken-/Rechtsprüfung; keine Verleumdung, Nachahmung oder vertrauliche Wettbewerbsdaten.
9. **Kommunikation.** E-Mail, DM, Presse-, Podcast-, Influencer- oder Partneransprache braucht legitime Zielauswahl, Identität, Einwilligungs-/Rechtsprüfung, Sperrlisten, einfachen Widerspruch und separate Sendefreigabe. Kein massenhafter unaufgeforderter Versand.
10. **Partnerschaften und Vorteile.** Affiliate-, Referral-, Sponsoring-, Influencer-, Zertifizierungs- und Integrationsprogramme benötigen Bedingungen, Offenlegung, Markenrechte, Datenrollen, Betrugsschutz, Steuer-/Buchhaltungsprüfung und Einwilligungsgrenzen.
11. **Aktionen und Knappheit.** Gewinnspiele, Rabatte, Testphasen, Early Access und Giveaways benötigen echte Bedingungen, Eignung, Regionen, Steuer-, Plattform-, Datenschutz-, Verbraucher- und Budgetprüfung. Keine erfundene Knappheit.
12. **Rechte.** Quellen und Nutzungsrechte für Zitate, Bilder, Logos, Musik, Daten, Vorlagen, Open Source, Kundenstories und Forschung prüfen.
13. **Produktideen sind Produktprojekte.** Tools, Erweiterungen, APIs, OAuth, Importe, Viral Loops und Open-Source-Komponenten benötigen Spezifikation, Security/Privacy, Barrierefreiheit, Missbrauchsschutz, Wartung, Support, Tests und Rollback.
14. **Sensible Bereiche.** Gesundheit, Finanzen, Recht, Arbeit, Wohnen, Bildung, Versicherung, Minderjährige, Politik und vulnerable Gruppen erfordern Fachprüfung; keine sensiblen Merkmale für diskriminierende Auswahl oder Preise.
15. **Physische und Reputationsrisiken.** Events, Stunts, Außenwerbung und kontroverse Kampagnen benötigen Rechte, Genehmigungen, Sicherheit, Barrierefreiheit, Einwilligung Unbeteiligter, Versicherung und Krisenplan.

## Kontextbrief

Erfrage nur shortlist-relevante Angaben:

- Produkt, Land, Sprache, Markt und Geschäftsmodell;
- Zielorganisationen, Buying Group, Job, Auslöser und Ausschlüsse;
- Phase, Ziel, Zeithorizont und belastbarer Ausgangswert;
- freigegebene Aussagen und Nachweise;
- bestehende Kanäle, eigene Reichweite und Distributionsvorteile;
- frühere Tests, Methodik, Resultate und Learnings;
- Team, Fähigkeiten, Budgetobergrenze, Prüf- und Wartungskapazität;
- Vertriebszyklus, Wert, Marge und Umsetzungs-/Supportlast;
- Datenschutz-, Sicherheits-, Rechts-, Marken- und Barrierefreiheitsgrenzen;
- Risikobereitschaft und ausdrücklich ausgeschlossene Handlungen.

Ein freigegebener `.agents/product-marketing.md` kann projektlokal dienen. Keine privaten Systeme automatisch lesen.

## Ideenfindungsablauf

### 1. Problem als Entscheidung formulieren

„Wachsen“, „Leads gewinnen“ oder „Autorität aufbauen“ übersetzen in Zielgruppe und Verhalten, Funnel-/Kundenphase, Ausgangswert/Quelle, Ergebnis/Zeitraum, praktische Grenze, Früh-/Spätkennzahl, Schutzkennzahlen und Folgeentscheidung. Schnelle Akquise ist nicht automatisch Paid oder Outbound; Geschwindigkeit hängt von Zugang, Angebot, Vertriebszyklus, Nachweis, Kreativmaterial, Messung, Budget und Kapazität ab.

### 2. Evidenzverzeichnis aufbauen

| ID | Signal/Aussage | Klasse | Quelle/Datum | Relevanz | Konfidenz | Unbekanntes |
|---|---|---|---|---|---|---|
| E-01 | | Beobachtung / Intern / Schätzung / Hypothese / Unbekannt | | | Hoch/Mittel/Niedrig | |

Eine Wettbewerbstaktik belegt Aktivität, nicht Leistung, Profitabilität, Inkrementalität, Rechtskonformität oder Passung.

### 3. Über Mechanismen hinweg entwickeln

Kandidaten aus Produktnutzen/Kundenerfolg, Bildung/Entscheidungshilfe, Suche mit eigenständigem Wert, Experten-/Gründerdistribution, erlaubter Kundenempfehlung, Partnerschaften, respektvoller Community-Teilnahme, Veranstaltungen/Demos, kontrollierten Empfehlungsprogrammen, bezahlten Medien, echter PR, einwilligungsbasierter Bestandskundenkommunikation und nur bei Betriebsreife Lokalisierung erzeugen.

### 4. Vor Bewertung aussortieren

Ablehnen oder eskalieren bei unklarer Datennutzung, Manipulation, irreführender Nutzerführung, unbelegten Aussagen, falscher Empfehlung, unerlaubten Rechten, Konten oder Kundendaten, Massenansprache, nicht vorhandenen Funktionen, versteckten Folgekosten, Diskriminierung sowie unvertretbarem physischem, rechtlichem, Sicherheits- oder Reputationsrisiko.

### 5. Transparent bewerten

Situativ Kriterien und Gewichte vereinbaren: Zielgruppenevidenz, Ziel-/Phasenpassung, Angebotsreife, Distributionszugang, Lernwert, Nachweis-/Kreativreife, Zeit bis Signal, Aufwand/Wartung, Budgetrisiko, Datenschutz/Recht/Plattform/Security/Barrierefreiheit/Reputation, Messbarkeit, Umkehrbarkeit und Konfidenz. Annahmen und Sensitivität zeigen; fehlende Daten senken Konfidenz.

### 6. Portfolio empfehlen

Drei bis fünf Ideen nur, wenn dies die Entscheidung erleichtert: gegebenenfalls ein günstiger Lerntest, ein wiederverwendbares Asset, ein Distributions-/Beziehungstest und optional ein klar markierter höherer Einsatz. Bei gewünschter Langliste nach Mechanismus gruppieren und Voraussetzungen sowie geringe Konfidenz sichtbar machen.

## Experimentsteckbrief

Für jede engere Idee:

1. **Idee und Mechanismus:** erwartetes Verhalten und Begründung.
2. **Passung:** Zielgruppe, Phase, Ziel und Evidenz.
3. **Hypothese:** widerlegbare Aussage statt Versprechen.
4. **Minimaltest:** kleinste ethische Umsetzung, die die Frage beantwortet.
5. **Mittel:** Verantwortung, Kompetenzen, Zeitspanne, Budgetdeckel, Abhängigkeiten, Werkzeuge.
6. **Benötigte Evidenz:** Fakten, Rechte, Kreativmaterial, Produktreife.
7. **Risiken/Prüftore:** Datenschutz, Recht, Plattform, Rechte, Security, Barrierefreiheit, Reputation.
8. **Messung:** Zähler, Nenner, Kohorte, Quelle, Zeitraum, Qualitäts- und Schadensgrenzen.
9. **Entscheidungsregel:** fortsetzen, ändern, stoppen oder untersuchen.
10. **Freigabegrenze:** genaue externe Aktion, die noch nicht autorisiert ist.

Spannen nur bei Grundlage verwenden. Erwartetes Ergebnis als beobachtbares Signal, nie als garantierten Geschäftserfolg beschreiben.

## Kanalspezifische Leitplanken

- **Content/Suche/Social/Community:** eigenständiger Wert, Quellen, Moderationsnormen, Rechte, Barrierefreiheit und Privatsphäre; keine privaten Gruppen auslesen oder automatisch posten.
- **Bezahlte Werbung/Retargeting:** aktuelle Plattformregeln, Zielgruppenbeschränkung, Einwilligung, Aussagen, Landingpage, Budget, Abrechnung, Attribution, Kontakthäufigkeit und Abbruchkriterien vor Start prüfen.
- **E-Mail/Lifecycle:** Zweck und Empfänger passend; Transaktion und Marketing trennen; Abmeldung, Sperrung und Einwilligungswiderruf respektieren.
- **Referral/Affiliate/Promotion:** Nutzen, Anreiz, Offenlegung, Missbrauchsschutz, Bedingungen, Steuern, Eignung, Obergrenzen und Support planen.
- **Daten/Reports:** autorisiert, minimiert und hinreichend aggregiert; Stichprobe, Methode, Unsicherheit, Zweck, Aufbewahrung und Re-Identifikationsrisiko dokumentieren.
- **Produkt/Developer:** Spezifikation, Berechtigungen, Testumgebung, Rollback, Monitoring, Support und echte QA.
- **Events/PR:** Einwilligung, Aufnahme-/Ortsrechte, Genehmigung, Barrierefreiheit, Offenlegung, Moderation und Krisenplan.

## Messprinzipien

Kennzahlen vor Zielsetzung definieren. Qualität, Kosten, Beschwerden, Abmeldungen, Supportlast, Barrierefreiheitsfehler, Betrug und negatives Feedback als Schutzkennzahlen einbeziehen. Korrelation von Inkrementalität und Beitrag von Attribution unterscheiden. Impressionen, Klicks, Follower, Registrierungen, Rankings oder Erwähnungen allein sind kein Erfolg. Wenn möglich Vergleichsbasis, Holdout, Geo-Split oder belastbares Zeitreihendesign nutzen. Bei schlechter Datenqualität, fehlender Rechtsgrundlage, Überlastung oder Nutzerschaden stoppen.

## Deutscher/DACH-Kontext

Bei deutschsprachigem Auftrag ist **Deutschland die gekennzeichnete Standardannahme**. Österreich und Schweiz separat bewerten; Zulässigkeit, Kanäle, Erwartungen, Sprache, Steuern und Kosten nicht pauschal übertragen.

- Nutzer-/Zielsprache und `Sie`/`Du` je Publikum und Kanal konsistent festlegen.
- Budget und Preise in passender Währung; EUR sowie Netto/Brutto/Umsatzsteuer sachgerecht kennzeichnen, CH getrennt behandeln.
- Datums- und Fristangaben eindeutig lokalisieren; technische ISO-Daten beibehalten.
- UWG, DSGVO und TDDDG, Einwilligung, Direktmarketing, Gewinnspiele, Preisangaben, Plattformregeln, Markenrecht und Barrierefreiheit als aktuelle Prüffelder markieren.
- Keine Rechtsberatung oder Rechtsgarantie geben; vor Umsetzung zuständige Fachprüfung vorsehen.
- DACH-Lokalisierung ist eine Hypothese, solange lokale Zielgruppen- und Kanalevidenz fehlt.

## Ausgabeformat

### Auswahlliste

| Rang | Idee | Mechanismus | Evidenz | Minimaltest | Zeit-/Kostenrahmen | Hauptrisiko | Kennzahl/Schutzgrenze | Konfidenz |
|---:|---|---|---|---|---|---|---|---|

Danach für den Spitzenkandidaten den Experimentsteckbrief und alle nötigen Freigaben liefern. Bei großer Ideensammlung nach Mechanismus gruppieren und je Idee Konzept, Passung, Voraussetzung, Evidenzklasse, Aufwand, Budgetrisiko, Prüfung und nächsten Validierungsschritt zeigen. Keine Scheinpräzision.

## Prüfliste

- [ ] Ziel, Zielgruppe, Ausgangswert, Grenze und Folgeentscheidung sind klar.
- [ ] Beobachtung, Schätzung, Hypothese und Unbekanntes sind getrennt.
- [ ] Ideen wurden vor dem Scoring sicherheitlich geprüft.
- [ ] Keine Idee beruht auf Tracking, Spam, Manipulation, falschem Nachweis oder unerlaubten Daten/Rechten.
- [ ] Kosten umfassen Umsetzung, Medienbudget, Werkzeuge, Arbeit, Support, Wartung und Compliance.
- [ ] Aussagen, Rechte, Plattform, Datenschutz, Sicherheit, Barrierefreiheit und Reputation sind sichtbar.
- [ ] Messung enthält Qualitäts- und Schadensgrenzen.
- [ ] Experiment hat Verantwortung, Budgetdeckel, Stopregel und Freigabegrenze.
- [ ] Deutschland/AT/CH, Sprache, Anrede, Währung, Steuer und Datum sind geklärt.
- [ ] Keine Rechtsgarantie und keine externe Aktion ohne Freigabe.

## Abgrenzung

`product-marketing` liefert Positionierung und Nachweise, Kundenforschung validiert Bedürfnisse, `content-strategy` plant Content-Portfolios und Angebotsstrategie strukturiert Leistungen. Kanal-, Rechts-, Produkt-, Forschungs- und Betriebsworkflows regeln die Umsetzung. Dieser Skill entwickelt Hypothesen und setzt sie nicht stillschweigend um.

## Herkunft und Abweichungen

Deutsche/DACH-Adaption des MIT-lizenzierten Ausgangs-Skills `marketing-ideas` von Corey Haines auf Basis des Upstream-Commits `7868cb9251fad80a73d26e488a5ad5f6c4a9f335` (Homepage im Frontmatter). Abweichungskategorien: **Übersetzung**, **Umstrukturierung**, **DACH**-Lokalisierung und **Sicherheitsanpassung** durch Evidenztrennung, Risikoprüfung und Freigabe externer Aktionen. Details stehen im Repositorypfad `docs/UPSTREAM-AENDERUNGEN.md`.
