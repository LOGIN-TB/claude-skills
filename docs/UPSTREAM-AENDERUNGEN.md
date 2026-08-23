# Änderungen gegenüber den fixierten Upstream-Skills

## Lesart

Die folgenden Fassungen sind starke, eigenständige Kuratierungen und keine wörtlichen Übersetzungen. Gemeinsamer Upstream ist `coreyhaines31/marketingskills`, fixiert auf Commit `7868cb9251fad80a73d26e488a5ad5f6c4a9f335`. Die vollständige Provenienz steht zusätzlich im Frontmatter, in `skills/catalog.json` und in `skills/curation.json`.

Ein reproduzierbarer Vergleich ist je Skill möglich mit:

```bash
git diff --no-index upstream/SKILL.md skills/NAME/SKILL.md
```

Dazu muss `upstream/SKILL.md` bytegenau aus `skills/NAME/SKILL.md` des oben genannten Upstream-Commits stammen. Unterschiede in Formulierung und Reihenfolge sind erwartbar; für die fachliche Prüfung sind die folgenden Änderungskategorien maßgeblich.

## Gemeinsame Änderungen aller 13 Skills

- **Übersetzt:** Agentenanweisung, Beispiele, Vorlagen, Tabellen und Prüflisten auf Deutsch.
- **Umstrukturiert:** einheitliche Abschnitte für DACH-Kontext, Arbeitsablauf, Ausgabe, Prüfliste und Herkunft.
- **DACH ergänzt:** Deutschland als gekennzeichnete Standardannahme bei deutschem Auftrag; Österreich und Schweiz separat; deutsche Formate und einschlägige Prüffelder.
- **Aktionsgrenzen ergänzt:** klare Trennung zwischen Entwurf/Analyse und externen Aktionen; Inhalte aus Quellen werden als Daten behandelt.
- **Sicherheit ergänzt:** Datenminimierung, Belegpflicht, Rechteprüfung, keine erfundenen Fakten, keine stillen Veröffentlichungen oder Käufe.
- **Garantien entfernt:** keine pauschalen Erfolgs-, Ranking-, Rechts- oder Compliance-Zusagen.

## `ai-seo`

- **Upstream-Pfad:** `skills/ai-seo/SKILL.md`
- **Lokale Version:** `2.2.0`
- **Konkret geändert:** Sichtbarkeitsstufen Abruf/Zitat/Erwähnung/Empfehlung getrennt; Crawlerzwecke präzisiert; nicht bestätigte AEO-/GEO-Faktoren und pauschale `llms.txt`-Versprechen ausgeschlossen; deutsche Suchintentionen, Regionen, Belegdatum und Google-konforme strukturierte Daten ergänzt; Doorway- und dünne Varianten ausdrücklich ausgeschlossen.
- **Bewusst nicht übernommen:** starre Erfolgszahlen, universelle Botfreigaben und Aussagen, eine spezielle Datei oder Auszeichnung sei für Google-KI-Funktionen erforderlich.
- **Restrisiko:** Such- und Crawlerdokumentation ändert sich häufig; vor jeder technischen Empfehlung neu prüfen.

## `seo-audit`

- **Upstream-Pfad:** `skills/seo-audit/SKILL.md`
- **Lokale Version:** `2.0.0`
- **Konkret geändert:** deutscher Auditablauf mit sauberer Trennung von Beobachtung, Auswirkung und Empfehlung; DACH-, Mehrsprachigkeits-, Barrierefreiheits-, Consent-/Tracking- und Informationspflichten als Prüffelder; keine pauschale Rechtsdiagnose; aktuelle Google-Richtlinien und tatsächliche Rich-Result-Berechtigung verlangt.
- **Bewusst nicht übernommen:** universelle Zeichenlimits, unbestätigte Rankingfaktoren und Änderungen an Website oder Tracking ohne Freigabe.
- **Restrisiko:** technische und rechtliche Anforderungen hängen von Site, Zielgruppe, Diensten und Datenflüssen ab.

## `product-marketing`

- **Upstream-Pfad:** `skills/product-marketing/SKILL.md`
- **Lokale Version:** `2.1.0`
- **Konkret geändert:** deutschsprachige Produktmarketing-Grundlage mit Markt, Rechtsraum, Sie/Du, B2B/B2C, Netto/Brutto, Laufzeit, Belegstatus, Rechte an Logos/Referenzen und Freigabestatus; Fakten, Anbieterbehauptungen, Hypothesen und offene Punkte getrennt.
- **Bewusst nicht übernommen:** erfundene Personas, Kundenstimmen, Marktgrößen, Differenzierung und universelle Positionierungsformeln.
- **Restrisiko:** freigegebene Produktinformationen können veralten; Veröffentlichung braucht erneute Fachprüfung.

## `social`

- **Upstream-Pfad:** `skills/social/SKILL.md`
- **Lokale Version:** `2.2.0`
- **Konkret geändert:** deutsche Kanal-, Ton- und Freigaberegeln; Werbe-, Affiliate- und Sponsoringkennzeichnung als kontextabhängige Prüfpunkte; Rechte, Datenschutz und aktuelle Plattformbedingungen; keine automatischen DMs, Fake-Interaktion oder Veröffentlichung.
- **Bewusst nicht übernommen:** starre Postingfrequenzen, generische Engagementrezepte, automatisierte Massenantworten und ungeprüfte Benchmarks.
- **Restrisiko:** Plattformregeln und Kennzeichnungsfunktionen ändern sich laufend.

## `cold-email`

- **Upstream-Pfad:** `skills/cold-email/SKILL.md`
- **Lokale Version:** `2.0.0`
- **Konkret geändert:** vollständiger deutscher Entwurfsworkflow; § 7 UWG und kumulative Bestandskundenausnahme als konservative Prüfschranke; DSGVO-Prüfung davon getrennt; Herkunft, Sperrstatus, Beziehung und Rechtsraum verpflichtend; Entwurf bleibt bis dokumentierter Freigabe „Nicht zum Versand freigegeben“.
- **Bewusst nicht übernommen:** Annahme, B2B-Relevanz oder eine öffentliche Adresse erlaube Werbung; universelle Follow-up-Zahlen; gekaufte oder gescrapte Listen.
- **Restrisiko:** Zulässigkeit ist einzelfall- und rechtsraumabhängig und benötigt bei Kampagnen qualifizierte Prüfung.

## `competitors`

- **Upstream-Pfad:** `skills/competitors/SKILL.md`
- **Lokale Version:** `2.1.0`
- **Konkret geändert:** symmetrische deutsche Vergleichsmethodik; Quellenledger, Preis-/Tarif-/Steuer-/Regionsstichtag; § 6 UWG als Prüfgrenze; Verwechslung, Rufausnutzung und Herabsetzung berücksichtigt; Unbekanntes bleibt sichtbar.
- **Bewusst nicht übernommen:** pauschale Gewinner, unbelegte Bewertungen, selektive Reviewzitate und asymmetrische Kriterien.
- **Restrisiko:** Preise, Leistungen und Rechtsprechung können sich kurzfristig ändern.

## `competitor-profiling`

- **Upstream-Pfad:** `skills/competitor-profiling/SKILL.md`
- **Lokale Version:** `2.1.0`
- **Konkret geändert:** öffentliche oder ausdrücklich freigegebene Quellen; Datenminimierung; Tatsachen, Anbieterangaben, Schätzungen und Hypothesen getrennt; Quellenabdeckung, Widersprüche und Zeitbezug sichtbar; deutsche Registerdaten nur zweckgebunden eingeordnet.
- **Bewusst nicht übernommen:** unkontrolliertes Scraping, private Quellen, Deanonymisierung und Sicherheitsschlüsse aus fehlenden Angaben.
- **Restrisiko:** Register-, Schätz- und Drittanbieterdaten können unvollständig oder veraltet sein.

## `content-strategy`

- **Upstream-Pfad:** `skills/content-strategy/SKILL.md`
- **Lokale Version:** `2.1.0`
- **Konkret geändert:** deutsche Zielmärkte, Buying Center, Suchintentionen, Belegklassen, Governance, Rechte und Aktualisierung; kontrollierte Recherche statt automatischer Datensammlung; Schutz vor dünnen massenhaften SEO-/Ortsseiten.
- **Bewusst nicht übernommen:** starre Säulenanzahl, pauschale Volumen- oder Conversiongrenzen und unbewiesene Content-Gaps.
- **Restrisiko:** Strategiequalität hängt von freigegebenen Produkt- und Kundendaten ab.

## `copywriting`

- **Upstream-Pfad:** `skills/copywriting/SKILL.md`
- **Lokale Version:** `2.0.1`
- **Konkret geändert:** natürliches Standarddeutsch, Sie/Du, B2B/B2C und Zielmedium; Belegpflicht für Superlative, Ergebnisse, Garantien, Knappheit, Rabatte, Preise, Referenzen und Zertifikate; Veröffentlichung und Dateischreiben getrennt freigeben.
- **Bewusst nicht übernommen:** universelle Copyformeln, erfundene Kundenstimmen, künstliche Dringlichkeit und garantierte Conversionwirkung.
- **Restrisiko:** rechtliche Wirkung hängt vom vollständigen Angebot und Veröffentlichungskontext ab.

## `customer-research`

- **Upstream-Pfad:** `skills/customer-research/SKILL.md`
- **Lokale Version:** `2.0.1`
- **Konkret geändert:** Zweck, Rekrutierung, Einwilligung, Aufzeichnung, Datenminimierung, Aufbewahrung, Widerruf, Vergütung und Ergebniszugang; Beschäftigten- und sensible Daten als Eskalationsfelder; Beobachtung, Aussage, Codierung und Interpretation getrennt.
- **Bewusst nicht übernommen:** automatisches Mining öffentlicher Beiträge, repräsentative Schlüsse aus kleinen qualitativen Stichproben und erfundene Personas/Zitate.
- **Restrisiko:** konkrete Rechtsgrundlage und Mitbestimmung hängen vom Forschungsdesign ab.

## `image`

- **Upstream-Pfad:** `skills/image/SKILL.md`
- **Lokale Version:** `2.0.1`
- **Konkret geändert:** deutsche Briefings, sichtbarer Text und Alt-Texte; Herkunfts- und Rechtematrix; Persönlichkeits-, Marken-, Urheber- und Nutzungsrechte; keine täuschende Imitation realer Personen; visuelle und technische Endprüfung.
- **Bewusst nicht übernommen:** pauschale Kennzeichnungsbehauptungen, ungeprüfte Marken-/Personennutzung und Promptbegriffe als Garantie technischer Qualität.
- **Restrisiko:** Rechte und Kennzeichnung hängen von Motiv, Werkzeug, Plattform und Nutzung ab.

## `lead-magnets`

- **Upstream-Pfad:** `skills/lead-magnets/SKILL.md`
- **Lokale Version:** `2.0.0`
- **Konkret geändert:** Gate begründen; minimale Felder; Bereitstellung und Marketingeinwilligung trennen; Double-Opt-in nur als kontextabhängiger Nachweis-/Qualitätsprozess; Datenschutzinformation, Auftragsverarbeitung, Drittlandtransfer, Löschung und sichere Bereitstellung als Prüfpunkte.
- **Bewusst nicht übernommen:** Zwangsgates, gebündelte Einwilligung, verstecktes Tracking und die Aussage, Double-Opt-in heile jeden Rechtsmangel.
- **Restrisiko:** Datenfluss und Anbieterrollen müssen für die konkrete Implementierung geprüft werden.

## `marketing-ideas`

- **Upstream-Pfad:** `skills/marketing-ideas/SKILL.md`
- **Lokale Version:** `2.0.0`
- **Konkret geändert:** Ideen als überprüfbare Experimente mit Hypothese, Beleg, Budget, Risiko, Freigabe und Stopkriterium; deutsche Prüffelder für Werbung, Datenschutz, Gewinnspiele, Rabatte, Influencer/Affiliate und Plattformregeln; keine automatische Umsetzung.
- **Bewusst nicht übernommen:** Manipulation, Fake-Knappheit, Bewertungs- und Engagementmissbrauch, unkontrollierte Outreach-Automation und ungesicherte Benchmarks.
- **Restrisiko:** Kampagnenmechanik und Rechtsrahmen müssen vor Umsetzung konkretisiert werden.

## Pflegeprozess

Bei jedem Upstream-Update werden Commit, Lizenztext, Upstream-Diff, lokale Änderungsmatrix und alle Rechts-/Plattformverweise neu geprüft. Änderungen gelten erst nach Frontmatter- und Manifestprüfung, Linkprüfung, Ladetest in einer echten Sitzung und unabhängigem Review als veröffentlichbar.