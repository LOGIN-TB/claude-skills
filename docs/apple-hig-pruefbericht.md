# Apple HIG – Prüfbericht zur Erstveröffentlichung

Datum: 29. Oktober 2026. Geprüfte Fassung: Apple HIG 1.0.0, Marketplace 2.2.0.

## Tatsächlich ausgeführte Prüfungen

### Repository-Tests

```bash
python3 -m unittest discover -s tests -v
```

Ergebnis: **71 Tests bestanden**. Darin enthalten sind acht neue Paket-/Integrationstests, elf Tests des Auditvalidators und die bestehenden Tests für Zustellbarkeit. Die Tests arbeiten mit synthetischen Daten, nicht mit einer behaupteten HIG-geprüften Anwendung.

Geprüft werden insbesondere Skill-Name und Frontmatter, eindeutige Marketplace-Einbindung, lokale Referenzpfade, Quellen-IDs, Dokumentationslinks, Ausschluss alter Skill-Namen und privater Pfade, Ablehnung der unausgefüllten Auditvorlage sowie die CLI mit einem ausdrücklich synthetischen positiven Testfall.

### Claude-Code-Marketplace

```bash
claude plugin validate .claude-plugin/marketplace.json --strict
```

Ergebnis: **Validation passed**, ausgeführt mit Claude Code 2.1.310. Der Validator bestätigt das Marketplace-Manifest, nicht die fachliche Richtigkeit sämtlicher Skill-Inhalte. Ein einzelner Skill-Ordner ohne Plugin-Manifest ist bei dieser Version kein gültiges Ziel dieses Befehls; die Dokumentation empfiehlt deshalb nur den geprüften Marketplace-Befehl.

### Echte Claude-Code-Sitzung

Der unveränderte Skill wurde in einer nur für diesen Test geladenen lokalen Plugin-Hülle bereitgestellt, ohne dauerhafte Installation oder Änderung von Nutzerkonfigurationen. Erlaubte Werkzeuge: `Skill` und `Read`; keine Shell, keine Schreibwerkzeuge und keine zusätzlichen MCP-Server.

Testauftrag: Eine bestehende SwiftUI-Oberfläche für iPhone/iPad ausschließlich lesend anhand der HIG prüfen; kein Anwendungsprojekt vorhanden. Der Auftrag nannte keinen konkreten Skill-Befehl und verlangte die Auswahl eines passenden verfügbaren Skills sowie die Erklärung fehlender Unterlagen und der Aussagekraft des Auditvalidators.

Beobachtet:

- Claude Code meldete `apple-hig:apple-hig` als verfügbaren Skill.
- Der Agent rief selbstständig `Skill` mit `skill: apple-hig:apple-hig` auf.
- Anschließend las er `scripts/validate_audit.py` über `Read`.
- Die Antwort unterschied Prüfplan und tatsächlich ausgeführte Tests, benannte fehlende Projektunterlagen und erklärte die Grenzen eines formal grünen Audits.
- Keine App-Prüfung, kein Build und keine HIG-Konformität wurden als ausgeführt beziehungsweise bewiesen ausgegeben.
- Die Sitzung endete erfolgreich mit Exit 0.

Dies bestätigt Laden und Aktivierung in dieser konkreten Sitzung, nicht garantiertes automatisches Routing jedes künftigen Prompts. Das explizite Aufrufen bleibt möglich.

## Nicht behauptete Prüfungen

Keine echte App, kein iOS-/macOS-Build, keine VoiceOver-Hardwareprüfung und keine vollständige visuelle HIG-Prüfung waren Gegenstand der Skill-Veröffentlichung. Quellen-IDs und interne Verweise wurden geprüft; dies ersetzt keine erneute fachliche Prüfung aller Apple-Aussagen. CI-Ergebnisse für den jeweiligen Commit sind separat im GitHub-Actions-Lauf sichtbar.

## Reproduzierbarkeit

Die automatischen Tests liegen im Repository und laufen über `.github/workflows/tests.yml` bei Pull Requests und Änderungen an `main`. Die Workflow-Berechtigung ist auf lesenden Repositoryzugriff begrenzt; die Checkout-Action ist an einen vollständigen Commit gebunden. Die Claude-Code-Sitzung war ein manueller Smoke-Test, kein Bestandteil der CI und kein Test mit eingebauten Zugangsdaten.
