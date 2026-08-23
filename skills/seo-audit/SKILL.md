---
name: seo-audit
description: "Technische, inhaltliche und internationale SEO-Probleme für Deutschland und den DACH-Raum prüfen und priorisieren. Nutze diesen Skill bei Ranking- oder Trafficeinbrüchen, bei Problemen mit Crawling, Indexierung, Rendering, Canonicals, Weiterleitungen, Ladezeit, interner Verlinkung, hreflang oder lokaler Sichtbarkeit, vor und nach Migrationen und Relaunches, und wenn Befunde aus der Search Console eingeordnet werden sollen. Liefert reproduzierbare Evidenz statt Vermutungen, trennt Beobachtung von Hypothese und bleibt lesend: produktive Änderungen brauchen eine gesonderte Freigabe."
license: MIT
metadata:
  version: "2.0.0"
  author: "Corey Haines; DACH-Adaption LOGIN"
  upstream: coreyhaines31/marketingskills
  upstream_commit: 7868cb9251fad80a73d26e488a5ad5f6c4a9f335
  upstream_homepage: https://github.com/coreyhaines31/marketingskills/tree/7868cb9251fad80a73d26e488a5ad5f6c4a9f335/skills/seo-audit
  tags: [seo, technical-seo, on-page, indexing, migrations]
---

# SEO-Audit

Diagnostiziere Crawling, Indexierung, Rendering, Leistung, Inhalte, interne Verlinkung, Internationalisierung, lokale Suche und Migrationen mit reproduzierbarer Evidenz.

## Audit-Grundsätze

1. Bei einer URL zuerst die aktuelle Website untersuchen.
2. Beobachtung, Plattformbericht und Hypothese klar trennen.
3. Keine Rankings, Sichtbarkeit, Trafficwerte oder Erholungsfristen versprechen.
4. Suchmaschinenrichtlinien und Rich-Result-Voraussetzungen vor Empfehlungen in Primärquellen prüfen.
5. Zeichenzahl, H1-Anzahl, Klicktiefe, Keywordplatzierung und Wortzahl als Heuristiken, nicht als universelle Rankingregeln behandeln.
6. Zugangsdaten, private Daten, Analytics oder Search Console nur mit ausdrücklicher Berechtigung nutzen.
7. Audit bleibt lesend; produktive Änderungen brauchen gesonderte Freigabe.
8. Keine Doorway Pages, skalierten minderwertigen Orts-/Keywordvarianten, manipulativen Links oder fingierten Bewertungen empfehlen.

## Kontext und Evidenz

Erfasse Website, Land, Sprache, Geschäftsmodell, Conversionziel, Umfang, wichtige Suchanfragen/Seiten, Wettbewerber, Baseline, Änderungen und verfügbare Erstanbieterdaten. Bei Einbrüchen Zeitpunkt gegen Releases, Migration, Tracking, Saisonalität, Nachfrage, manuelle Maßnahmen, Sicherheitsereignisse und dokumentierte Suchänderungen prüfen.

Evidenzreihenfolge: Search Console; Server/CDN-Logs und reproduzierbare HTTP-/Rendering-Prüfungen; validierte Analytics; Versions-/Deploymenthistorie; Crawl-Exporte; aktuelle Suchmaschinen-Dokumentation; Drittwerkzeuge ergänzend. `site:`-Abfragen sind kein Indexzähler.

## Audit-Ablauf

### 1. Umfang und Baseline

Hostname-, Protokoll-, Subdomain- und Sprachvarianten bestätigen. Vorher-/Nachher-Zeiträume definieren. Nach Suchanfrage, Land, Gerät, Seitentyp, Verzeichnis und Darstellung segmentieren. Datenintegrität prüfen und je wichtigem Template repräsentative URLs wählen.

### 2. Crawlbarkeit und Indexierbarkeit

HTTP-Status, Redirectketten/-schleifen, Soft-404, `robots.txt`, Meta Robots, `X-Robots-Tag`, Canonicals, XML-Sitemaps, interne Auffindbarkeit, Orphans, Pagination, Facetten, Parameter und Infinite-Scroll-Fallback prüfen. Search-Console-Gründe und URL-Prüfungen stichprobenartig heranziehen. Canonicals sind Hinweise, keine Befehle; fehlende Self-Canonicals nur bei tatsächlichem Duplikationsrisiko beanstanden.

### 3. Rendering und Parität

Initiales HTML, gerenderten DOM und Accessibility Tree vergleichen. Hauptinhalt und Links, Mobil/Desktop-Parität, Hydration, Lazy Loading, Ressourcenfehler, Consent-Walls, Logins, Geo-/Sprachweiterleitungen sowie per JavaScript erzeugte Canonicals, Robots, Links und strukturierte Daten prüfen. `curl` erkennt clientseitig injiziertes JSON-LD nicht zuverlässig; gerenderten DOM und aktuelle Validatoren verwenden.

### 4. Architektur und interne Links

Kontextuelle Links, Navigation, Breadcrumbs, Hubs, Pagination, Orphans, tote Enden, defekte oder unnötig doppelte Links prüfen. Ankertexte natürlich und beschreibend halten. Klicktiefe priorisiert, ist aber keine universelle Drei-Klick-Regel. URLs stabil und konsistent gestalten, Keywords nicht erzwingen.

### 5. Leistung und technische Qualität

Felddaten aus CrUX/Search Console von Labordaten aus Lighthouse, DevTools oder WebPageTest trennen. Aktuelle Core-Web-Vitals-Schwellen vor Verwendung prüfen; zusätzlich TTFB, Cache/CDN, Bilder, Schriften, Hauptthread, CSS, Drittanbieter, Viewport, Tap-Ziele, Overflow, HTTPS, Mixed Content und relevante Sicherheitsheader untersuchen. CWV ersetzen weder Relevanz noch Inhaltsqualität.

### 6. Onpage und Suchdarstellung

Suchintention, Seitennutzen, unterscheidbaren Titel und Hauptüberschrift, Snippet-Kandidat, semantische Hierarchie, Canonical, Robots, Sprache, Datum, Autorenschaft, Klarheit, Originalität, Evidenz, Alt-Texte, interne Links und beobachtete Suchdarstellung bewerten. Nicht erzwingen: exakt eine H1, feste Zeichenlimits, Keyword in den ersten 100 Wörtern, Mindestwortzahl oder Exact Match in jedem Feld.

### 7. Inhalt und Vertrauen

Prüfen, ob Inhalte Bedarf erfüllen, Erfahrung/Fachkunde zeigen, Primärquellen und Methodik nennen, Fakt/Schätzung/Meinung/Anbieteraussage trennen, Verantwortlichkeit offenlegen und gepflegt werden. Doorways, kopierte Beschreibungen, irreführende Aussagen und skalierten Minderwert vermeiden. Absprungrate oder Verweildauer nicht als bestätigte direkte Rankingfaktoren darstellen. Qualität nicht an oberflächlichen „KI-Schreibmerkmalen“ festmachen.

### 8. Externe Signale

Erworbene Links, verweisende Domains, verlorene Links, Entitätskonsistenz, echte Bewertungen und seriöse Berichterstattung untersuchen. Keine Linkkäufe, PBNs, Review-Fälschung, Outreach-Spam oder manipulative Anker empfehlen.

### 9. International und lokal

Eindeutige Sprach-/Regions-URLs, `hreflang`-Codes, Selbst-/Rückverweise, erreichbare indexierbare Ziele, Canonical-Ausrichtung, konsistente Implementierung, echtes `x-default`, vollständige Lokalisierung und erreichbare Varianten prüfen. Nicht behaupten, jedes Dokument brauche `x-default`; betroffene URL-Paare konkret ausweisen. Lokal NAP, Unternehmensprofil, Bewertungen, Orts-/Servicegebietsseiten und doppelte Doorway-Ortsseiten prüfen.

### 10. Migration und Vorfälle

Bei Migration alte-zu-neue URL-Zuordnung, Statuscodes, Canonicals, Robots, Sitemaps, Links, Inhalts-/Metadatenparität, Analytics, Backlinks, Hostvarianten und Properties prüfen. Bei Verlust: Realität/Tracking bestätigen, Startdatum/Segmente bestimmen, Änderungen und manuelle Maßnahmen prüfen, verlorene Queries/Seiten vergleichen, Hypothesen priorisieren, kontrollierte Fixgruppen umsetzen und definierte Signale beobachten.

## Befundstandard und Priorisierung

Jeder Befund enthält Problem, betroffene URLs/Templates, Evidenz und Methode, Konfidenz (bestätigt/wahrscheinlich/Hypothese), Auswirkung, empfohlene Korrektur, Validierung danach sowie gegebenenfalls Aufwand und Verantwortliche. „Kritisch“ nur bei blockiertem Crawling/Indexieren, schwerem Canonical-/Duplikationsfehler, kaputtem Rendering, großflächigen Fehlern oder vergleichbarem Geschäftsrisiko.

Priorisiere nach Auswirkung, Evidenzstärke, Reichweite, Aufwand, Abhängigkeiten und Umkehrrisiko. Trenne schnelle Korrekturen von strukturellen Maßnahmen und Experimenten.

## Deutscher/DACH-Kontext

**Standardannahme ist Deutschland**, sofern kein Zielmarkt genannt ist. Für Deutschland sind DSGVO und TDDDG bei Consent-Walls, Tracking, Logfiles, Drittanbieterskripten, eingebetteten Diensten und Personalisierung **nur Reviewpunkte**. Aus dem Vorhandensein oder Fehlen eines Banners folgt kein pauschales Rechtsurteil. Dieser Skill erteilt keine Rechtsberatung und keine Rechtsgarantie; konkrete Datenflüsse und Implementierungen brauchen bei Bedarf fachkundige Prüfung.

- **Deutschland:** deutsche Suchintention, Terminologie, Umlaute/Schreibvarianten, Impressums-/Vertrauensinformationen und lokale Unternehmensdaten im Kontext prüfen, ohne sie pauschal zu Rankingfaktoren zu erklären.
- **Österreich:** Suchnachfrage, österreichische Sprache/Begriffe, lokale Entitäten und rechtliche Rahmenbedingungen separat prüfen.
- **Schweiz:** Deutsch, Französisch, Italienisch und regionale Suchintention, `.ch`-/Verzeichnisstrategie, lokale Entitäten und revDSG-Kontext separat bewerten; keine deutsche Bewertung übertragen.

Für DACH-Sprachvarianten echte Nutzerbedürfnisse und ausreichende Lokalisierung verlangen. Keine massenhaft erzeugten Stadt-, Kanton-, Bundesland- oder Keywordseiten ohne eigenständigen Nutzen; solche Doorways sind ausgeschlossen.

## Ausgabeformat

1. Management-Zusammenfassung
2. Umfang, Datum, Werkzeuge und Zugriffsgrenzen
3. Baseline, Segmente und Evidenzquellen
4. Kritische Blocker
5. Crawling-, Indexierungs-, Rendering- und Technikbefunde
6. Onpage-, Inhalts-, Architektur- und Linkbefunde
7. Internationale und lokale DACH-Befunde
8. Priorisierter Maßnahmenplan mit Aufwand, Verantwortlichen und Abhängigkeiten
9. Validierungs- und Monitoringplan
10. Offene Fragen, Hypothesen und Rechts-/Datenschutz-Reviewpunkte

## Prüfliste

- [ ] Live-Quelle und repräsentative URLs geprüft
- [ ] Beobachtung, Bericht und Hypothese getrennt
- [ ] Datenintegrität und Zeiträume validiert
- [ ] HTTP, Robots, Canonicals, Sitemaps und interne Links geprüft
- [ ] Initiales und gerendertes Ergebnis verglichen
- [ ] Feld- und Labordaten getrennt
- [ ] Keine starren SEO-Heuristiken als Rankingregeln ausgegeben
- [ ] Keine Doorways oder manipulative Linkmethoden empfohlen
- [ ] DSGVO/TDDDG nur als konkreter Reviewpunkt, kein Pauschalurteil
- [ ] DE als Annahme, AT und CH separat behandelt
- [ ] Jeder Befund hat Evidenz, Konfidenz, Fix und Validierung
- [ ] Keine produktive Änderung ohne Freigabe

## Herkunft und Abweichungen

Deutsche/DACH-Adaption des MIT-lizenzierten Ausgangs-Skills von Corey Haines; Homepage und Commit bleiben unverändert in den Metadaten. Gegenüber Commit `7868cb9251fad80a73d26e488a5ad5f6c4a9f335` wurden Haupttext und Beschreibung vollständig ins Deutsche übertragen, Deutschland als Standardannahme und Österreich/Schweiz als getrennte Märkte ergänzt. DSGVO und TDDDG wurden ausdrücklich auf konkrete Prüfpunkte ohne pauschales Rechtsurteil begrenzt; Doorway-Seiten und skalierte lokale Minderwertvarianten explizit ausgeschlossen. Auditsequenz, Evidenzhierarchie, Befundstandard, Migration und internationale SEO bleiben fachlich erhalten. Zentraler Nachweis: `docs/UPSTREAM-AENDERUNGEN.md`.
