---
name: ai-seo
description: "Sichtbarkeit, Zitierung und Empfehlung in KI-Antwortsystemen für Deutschland und den DACH-Raum evidenzbasiert prüfen und verbessern. Nutze diesen Skill, wenn eine Marke oder Seite in KI-Overviews, ChatGPT, Perplexity, Gemini oder Copilot auftauchen soll, wenn Crawler-Freigaben für KI-Bots, llms.txt, strukturierte Daten oder die Extrahierbarkeit von Inhalten zu bewerten sind, oder wenn jemand nach AEO, GEO oder LLMO fragt. Trennt Abruf, Zitierung, Erwähnung und Empfehlung, prüft Behauptungen über KI-Rankingfaktoren gegen Primärquellen und verspricht keine Sichtbarkeit. Für klassisches technisches SEO ist seo-audit zuständig."
license: MIT
metadata:
  version: "2.2.0"
  author: "Corey Haines; DACH-Adaption LOGIN"
  upstream: coreyhaines31/marketingskills
  upstream_commit: 7868cb9251fad80a73d26e488a5ad5f6c4a9f335
  upstream_homepage: https://github.com/coreyhaines31/marketingskills/tree/7868cb9251fad80a73d26e488a5ad5f6c4a9f335/skills/ai-seo
  tags: [ai-seo, aeo, geo, llmo, ai-overviews, citations]
---

# KI-SEO

Verbessere, wie eine Marke oder Seite in KI-generierten Antworten **abgerufen, zitiert, erwähnt und empfohlen** wird. Klassische SEO, Crawlbarkeit, nützliche Inhalte und überprüfbare Autorität bilden die Grundlage; KI-spezifische Struktur ist nur eine zusätzliche Ebene.

## Evidenzregeln

KI-Suchverhalten ändert sich schnell, viele Studien sind beobachtend. Vor aktuellen Prozentwerten, Crawlernamen, Plattform-Backends, Sichtbarkeitssteigerungen oder Mechanismen:

1. aktuelle Primärdokumentation oder Originalstudie prüfen;
2. Quelle, Datum, Plattform/Modell, Region und Methode nennen;
3. Korrelation nicht als Rankingfaktor oder Kausalität ausgeben;
4. keine Zitate, Rankings, Empfehlungen oder Trafficwirkung versprechen;
5. für Google-KI-Funktionen aktuelle Google-Hinweise zugrunde legen: normale Suchberechtigung und nutzerorientierte SEO; kein Spezial-Markup oder KI-Textfile als Pflicht behaupten.

**Keine erfundenen Rankingfaktoren.** Weder Strukturmuster, `llms.txt`, Schema, Erwähnungen, Autorenprofile noch Crawlerfreigaben als bestätigten KI-Rankingfaktor bezeichnen, sofern die jeweilige Plattform dies nicht aktuell und eindeutig dokumentiert.

## Kontext und Sichtbarkeitsstufen

Erfasse Domain, Prioritätsseiten, Marke, Angebot, Zielgruppe, Region, Sprache, wichtige Prompts, Plattformen, Wettbewerber, Ausgangssichtbarkeit und Ziel. Keine privaten Verzeichnisse, Zugangsdaten oder personenbezogenen Daten durchsuchen.

Trenne:

1. **Abgerufen:** System liest die Seite während der Antwortbildung.
2. **Zitiert:** Seite erscheint als Quelle.
3. **Erwähnt:** Marke steht im Antworttext.
4. **Empfohlen:** Marke gelangt in eine Auswahlliste.

Ein nützlicher Inhalt kann zitiert werden, ohne dass der Anbieter empfohlen wird. Empfehlungen können von überprüfbarer, webweiter Bestätigung durch Rezensionen, Communities, Fachmedien, Videos, Podcasts oder Analysten abhängen; dies ist keine Garantie.

## Audit-Ablauf

### 1. Reproduzierbare Baseline

| Prompt | Plattform/Modell | Datum/Region/Sprache | Antwort | Abgerufen/zitiert/erwähnt/empfohlen | Quellen | Einordnung |
|---|---|---|---|---|---|---|

Wiederholte Prüfungen nutzen, um Volatilität sichtbar zu machen. Aus einer Antwort oder einem Konto keine stabile Sichtbarkeit ableiten.

### 2. Technische Eignung

Erreichbarkeit, Statuscode, Canonical, Robots, Sitemap, Indexierbarkeit, gerendertes HTML, semantische Struktur, Login-/Consent-Barrieren, Titel, Überschriften, Autorenschaft, Datum, interne Links und strukturierte Daten prüfen. Strukturierte Daten müssen sichtbare Inhalte korrekt abbilden und aktuelle Plattformregeln erfüllen. Visuelle, DOM- und Accessibility-Tree-Nutzbarkeit berücksichtigen.

### 3. Crawler-Richtlinien präzise prüfen

Keine pauschale Empfehlung „alle KI-Bots erlauben“. Aktuelle Tokens und Zwecke aus Primärquellen unterscheiden:

- Such-/Indexcrawler beeinflussen möglicherweise Auffindbarkeit;
- nutzerausgelöste Fetcher rufen auf konkrete Anfrage ab;
- Trainingscrawler regeln Modelltraining und steuern nicht zwingend Suchzitate.

OpenAI unterscheidet beispielsweise nach aktueller Dokumentation Suchbot, Nutzer-Fetcher und Trainingsbot; Google trennt `Google-Extended` vom normalen Search-Crawling. Anthropic, Perplexity und andere live prüfen. Datenschutz, Lizenzierung, Serverlast, Auffindbarkeit und Zitation abwägen. `robots.txt` nie ohne Freigabe und Validierung ändern.

### 4. Extrahierbarkeit und Nutzwert

Direkte, korrekte Antworten dort voranstellen, wo es natürlich ist; beschreibende H2/H3, fokussierte Absätze, echte Vergleichstabellen, Prozesslisten, selbstständige Aussagen, Definitionen, Grenzen, Daten, Einheiten und Beispiele verwenden. Landmarken, Überschriften und Alt-Texte korrekt setzen. Keine fragmentierte „KI-Köder“-Seite, keine Doorway-Varianten und keine massenhaft dünnen Inhalte erzeugen.

### 5. Autorität und Evidenz

Primärquellen bevorzugen, Statistik mit Datum/Methodik versehen, praktische Erfahrung zeigen, echte Autorenschaft und relevante Qualifikation nennen, Fakt/Schätzung/Meinung/Anbieteraussage trennen und übertriebene oder veraltete Aussagen entfernen. Keine Statistiken, Zitate, Kunden, Rezensionen, Auszeichnungen, Qualifikationen oder Quellen erfinden.

### 6. Externer Konsens

Für Empfehlungsziele seriöse Bewertungsplattformen, Fachgemeinschaften, Branchenberichterstattung, redaktionell verdiente Reichweite, YouTube, Podcasts, Transkripte und konsistente Organisationsdaten prüfen. Nur authentische Beteiligung empfehlen; keine falschen Bewertungen, verdeckten Platzierungen, Wikipedia-Manipulation, Forenspam oder erfundenen Belege.

### 7. Maschinenlesbare Ergänzungen

`llms.txt`, öffentliche Markdown-Dokumentation, transparente Preis-/Spezifikationsdateien oder Feeds höchstens als messbare Zugänglichkeits-/Discovery-Experimente behandeln. Mit sichtbarem kanonischem Inhalt konsistent halten, nur wartbar einführen, keine vertraulichen Daten oder geschütztes Material offenlegen und nie als Google-Pflicht oder bestätigten Rankingfaktor bezeichnen. Aufkommende Protokolle bleiben experimentell, bis Erstanbieteradoption belegt ist.

## Inhaltsmuster

- **Definition:** direkte Definition, Geltungsbereich, Abgrenzung und Nutzen.
- **Prozess:** nummerierte, konkrete Handlungen mit Abschlusskriterien.
- **Vergleich:** überprüfbare Kriterien, Eignung, Grenzen, Datum, Methodik und Quellen; Eigenangebot nicht automatisch zuerst.
- **Evidenzblock:** Aussage, Primärquelle, Ergebnis mit Datum/Umfang, Einschränkung und praktische Folgerung.
- **FAQ:** echte Nutzerfragen; FAQ-Markup nur bei sichtbarem Inhalt und aktuell zulässiger Verwendung.

## Priorisierung und Messung

Bewerte Geschäftsnutzen, Evidenzstärke, Aufwand, Täuschungs-/Richtlinienrisiko und Messbarkeit. Reihenfolge: Crawl-/Index-/Renderingfehler; falsche Aussagen; fehlende Kerninformation; schwache Struktur/Barrierefreiheit; fehlende Evidenz/Autorenschaft; externer Konsens; experimentelle Dateien.

Messdreiklang:

1. Prompt-Tracking mit Prompt, Datum, Modell, Region, Sprache, Quellen und Einordnung;
2. freiwillige Selbstauskunft zur Herkunft;
3. Vertriebs-/Gesprächsevidenz nur rechtmäßig und mit nötiger Einwilligung.

Zusätzlich markenbezogene Suche, qualifizierte Besuche, Conversions, Bot-Logs und zitierte Zielseiten beobachten. Direkter Traffic oder Markensuche kann Einfluss verschleiern; daraus nicht automatisch Kausalität ableiten.

## Deutscher/DACH-Kontext

**Standardannahme ist Deutschland**, falls kein Zielmarkt genannt ist. Prompts, Quellen, Modelle, Sprachvarianten und Antwortregion müssen für Deutschland reproduzierbar dokumentiert werden. DSGVO/TDDDG, Urheber-, Marken- und Persönlichkeitsrechte sind konkrete Reviewpunkte bei Logs, Tracking, Trainings-/Crawlerentscheidungen, Quellenübernahme und personenbezogenen Inhalten. Keine Rechtsberatung und keine Rechtsgarantie.

- **Deutschland:** deutsche Fachsprache, Suchintention, Anbieter-/Autorenvertrauen und Primärquellen berücksichtigen, ohne daraus Rankingfaktoren zu erfinden.
- **Österreich:** österreichische Terminologie, Quellenlandschaft, Markt- und Rechtskontext separat testen.
- **Schweiz:** deutsche, französische und italienische Prompts sowie Schweizer Quellen, Markt- und revDSG-Kontext getrennt untersuchen.

Ein Ergebnis für Deutschland ist nicht automatisch auf AT/CH übertragbar. Plattformantworten können je Konto, Modell, Zeitpunkt, Sprache und Standort variieren.

## Ausgabeformat

1. Umfang, Zielmarkt und Methodik
2. Evidenzaufnahme mit Quellenständen
3. Baseline-Tabelle je Prompt/Plattform/Region
4. Befunde je Sichtbarkeitsstufe
5. Befunde zu Struktur, Autorität und Präsenz
6. Plattformspezifische Einschränkungen
7. Priorisierte Maßnahmen mit Verantwortlichem, Aufwand, Wirkungshypothese und Validierung
8. 30-/60-/90-Tage-Plan
9. Messtabelle
10. Unsicherheiten, experimentelle Annahmen und neu zu prüfende Aussagen

## Prüfliste

- [ ] Aktuelle Primärquellen und Datumsstände genannt
- [ ] Abgerufen, zitiert, erwähnt und empfohlen getrennt
- [ ] Mehrfachmessung und regionale/sprachliche Parameter dokumentiert
- [ ] Keine erfundenen Rankingfaktoren oder Kausalitäten
- [ ] Crawler nach Zweck statt pauschal bewertet
- [ ] Technische Eignung und gerenderter Inhalt geprüft
- [ ] Aussagen, Autoren, Statistik und Quellen verifiziert
- [ ] Keine Doorways, Fake-Reviews oder Spam-Maßnahmen
- [ ] Experimentelle Dateien klar als Experiment markiert
- [ ] DE-Standardannahme sowie AT/CH separat ausgewiesen
- [ ] Keine Website-, Crawler- oder Analyseänderung ohne Freigabe

## Herkunft und Abweichungen

Deutsche/DACH-Adaption des MIT-lizenzierten Ausgangs-Skills von Corey Haines; Homepage und Commit bleiben unverändert in den Metadaten. Gegenüber Commit `7868cb9251fad80a73d26e488a5ad5f6c4a9f335` wurden Haupttext und Beschreibung vollständig deutsch gefasst, Deutschland als Standardannahme sowie Österreich und Schweiz getrennt ergänzt. Nicht belegte Rankingfaktoren wurden ausdrücklich ausgeschlossen; Crawlerzwecke, volatile Promptmessung, experimentelle maschinenlesbare Dateien, Rechte und DACH-Lokalisierung wurden präzisiert. Der externe Werkzeugregister-Verweis der Ausgangsfassung bleibt entfernt und die Trennung von Trainingscrawlern, Suchcrawlern und Nutzer-Fetchern erhalten. Zentraler Nachweis: `docs/UPSTREAM-AENDERUNGEN.md`.
