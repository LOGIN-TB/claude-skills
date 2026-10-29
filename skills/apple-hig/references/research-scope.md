# Rechercheumfang und Pflege

## Stand und Methode

Recherche: 29. Oktober 2026. Ausgangspunkt war die vom Nutzer angegebene Apple-HIG-Startseite. Die Apple-DocC-Daten wurden über den offiziellen JSON-Endpunkt abgerufen. Alle über `topicSections` rekursiv erreichbaren HIG-Themenseiten wurden dedupliziert erfasst: **173 Seiten einschließlich Startseite, Kategorien und Übersichten**, ohne Abruffehler. Das ist die definierte Abdeckungsmenge, nicht eine Behauptung über sämtliche Apple-Developer-Inhalte.

Die sechs Themenfamilien wurden in drei Fachreferenzen ausgewertet. Das Themeninventar in `source-map.md` bildet die Abdeckung nachvollziehbar ab. Plattformunterschiede, Empfehlungen, Aktivierungskriterien und eigene Engineering-Tests bleiben getrennt. Quellen-IDs stammen aus einem maschinell erzeugten Ledger.

Die Website wurde zusätzlich im Browser geöffnet; die Materials-Seite wurde visuell stichprobenartig geprüft. Nicht sämtliche Bilder, interaktiven Beispiele oder Videos wurden einzeln visuell analysiert. Die Referenzen sind deshalb ein textbasiertes Implementierungs-Handbuch mit visueller Stichprobe, keine vollständige audiovisuelle Transkription.

Nicht vollständig ausgewertet: ausgehende Framework-API-Dokumentationen, WWDC-Videos, herunterladbare Designressourcen, sämtliche Change-log-Einträge und externe regulatorische/App-Review-Anforderungen. Bei Anwendung relevante Detailseiten und aktuelle API-Verfügbarkeit nachprüfen.

## Aktualisierung

1. Öffne Apples HIG-Startseite und prüfe die aktuelle Navigation.
2. Wenn der HTML-Text wegen JavaScript fehlt, nutze den Browser oder die offizielle DocC-Datenquelle. Für diese Recherche funktionierte das Muster `https://developer.apple.com/tutorials/data/design/human-interface-guidelines.json`; Unterseiten folgen demselben Muster mit `/slug.json`. Das ist ein beobachteter Abrufweg, keine garantierte öffentliche API.
3. Folge den tatsächlichen `topicSections[].identifiers`, löse sie über `references` auf und bleibe innerhalb des HIG-Pfades. Dedupliziere URLs, protokolliere HTTP-/Parsefehler, speichere Zwischenstände und vergleiche das Inventar.
4. Prüfe `primaryContentSections`, `abstract`, Plattformmetadaten, Tabellen (`rows`/Zellen), Bildbeschreibungen und weiterführende Referenzen. Ein reiner Absatz-Extraktor kann Tabellen und Größenangaben verlieren. Bei maßgeblichen Werten Original-JSON und gerenderte Seite prüfen.
5. Aktualisiere zuerst Quellenregister, dann Referenzen und Agentenanweisungen. Keine neu entdeckte Regel ausschließlich aus einem Such-Snippet übernehmen.
6. Halte bestehende Quellen-IDs stabil; neue Quellen am Ende ergänzen. Passe anschließend auch den Quellen-ID-Bereich des Auditvalidators und seine Tests an.
7. Dokumentiere Abrufdatum, neue/entfernte Themen und verbleibende Lücken. Teste Frontmatter, lokale Verweise, Quellenauflösung, Auditvalidator und Exportpaket erneut.

## Aussagekraft des Skills

Der Skill ist eine redaktionelle, eigenständige Umsetzungshilfe. „Alle Aspekte“ bedeutet: alle erfassten Themenfamilien auf Relevanz prüfen und ausgewählte Features durch passende Detailregeln absichern. Es bedeutet nicht, jede Plattformfunktion in jede App einzubauen. Ein erfolgreiches Audit bestätigt nur die dokumentierte Prüfung im angegebenen Scope. Es ist weder Apple-Zertifizierung noch automatischer Nachweis einer App-Store-Freigabe.
