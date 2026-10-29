# Apple HIG – Anleitung

## Wofür ist dieser Skill gedacht?

Apple HIG hilft einem Coding-Agenten, Apples Human Interface Guidelines in konkrete Software umzusetzen. Es geht nicht um eine Sammlung optischer Effekte, sondern um verständliche Aufgabenwege, passende Navigation, adaptive Oberflächen, Accessibility und überprüfbare Ergebnisse.

Der Skill ist für neue Anwendungen, Änderungen an einzelnen Screens, UI-Redesigns und Audits geeignet. Er unterstützt native Apple-Plattformen sowie ausdrücklich HIG-inspirierte Cross-Platform- und Web/PWA-Oberflächen. Bestehende Produktentscheidungen und der Nutzerauftrag bestimmen den Umfang: Ein Auditauftrag bleibt lesend; ein Implementierungsauftrag führt zu Codeänderungen und Tests.

## Installation

### Claude Code über den Marketplace

In Claude Code ausführen:

```text
/plugin marketplace add LOGIN-TB/claude-skills
/plugin install apple-hig@login-skills
```

Wenn `login-skills` bereits bekannt ist, nicht erneut hinzufügen, sondern zuerst aktualisieren:

```text
/plugin marketplace update login-skills
/plugin install apple-hig@login-skills
```

Bei bereits installiertem Skill aktualisieren:

```text
/plugin update apple-hig@login-skills
```

Eine neue Sitzung öffnen, falls die Änderung in der laufenden Sitzung noch nicht sichtbar ist. Für die Plugin-Variante ist der explizite Aufruf:

```text
/apple-hig:apple-hig
```

Die Namen vor und nach dem Doppelpunkt bezeichnen Plugin und Skill. Bei abweichender Anzeige die angebotene Slash-Autovervollständigung verwenden.

### Claude Code, manuell

Im Terminal:

```bash
git clone https://github.com/LOGIN-TB/claude-skills.git
mkdir -p ~/.claude/skills
cp -R claude-skills/skills/apple-hig ~/.claude/skills/
```

Vor dem Kopieren prüfen, ob bereits ein eigener Ordner dieses Namens existiert. Keine eigene Fassung ungeprüft überschreiben. Statt persönlicher Installation kann der vollständige Skill-Ordner im Projekt unter `.claude/skills/apple-hig/` liegen. **Alle Referenzen, Vorlagen und Scripts mitkopieren**, nicht nur `SKILL.md`.

Manueller Aufruf:

```text
/apple-hig
```

Nicht gleichzeitig manuell und als Plugin installieren; sonst entstehen doppelte oder auseinanderlaufende Fassungen.

### Claude-App oder anderer Agent

Für einen Skill-Upload den Ordner `apple-hig` als einzelnes Archiv verpacken:

```bash
cd claude-skills/skills
zip -r apple-hig.zip apple-hig -x '*/__pycache__/*' '*.pyc'
```

Das ZIP enthält `apple-hig/SKILL.md` und die Unterordner. Den jeweiligen Custom-Skill-Upload des verwendeten Clients nutzen. Ein Agent ohne Skill-Loader kann das Verzeichnis lesen, wenn der Auftrag ausdrücklich auf `SKILL.md` verweist. Ob Scripts, Browser, SDK oder Simulator verfügbar sind, hängt von der Umgebung ab; ein Upload allein stellt diese Werkzeuge nicht bereit.

## Gute Aufträge

### Neue App

> Nutze Apple HIG. Entwickle eine iPhone- und iPad-App zur Verwaltung privater Leselisten im vorhandenen SwiftUI-Projekt. Hauptaufgabe: Buch erfassen, Status ändern und wiederfinden. Beachte die im Projekt festgelegten Deployment Targets. Erstelle einen HIG-Plan, implementiere die relevanten Kriterien und liefere ein Audit mit Build-, Funktions- und UI-Prüfbelegen. Keine Veröffentlichung.

### Bestehende Oberfläche verbessern

> Nutze Apple HIG für unsere macOS-Einstellungsansicht. Prüfe zuerst den vorhandenen Code. Verbessere Navigation, Tastaturbedienung, Fokus und lange Beschriftungen, ohne die Geschäftslogik zu verändern. Baue und teste anschließend; dokumentiere verbleibende Probleme.

### Nur Audit, keine Codeänderungen

> Prüfe die vorhandene App mit Apple HIG ausschließlich lesend. Priorisiere Befunde nach Nutzerwirkung. Nenne pro Befund Screen, reproduzierbare Schritte, relevante HIG-Quelle und konkrete Korrektur. Kennzeichne nicht ausführbare Tests. Keine Dateien ändern und nichts veröffentlichen.

### Web/PWA

> Überarbeite die bestehende PWA nach den übertragbaren HIG-Prinzipien. Behalte Browsernavigation, semantisches HTML und Web-Accessibility bei. Baue keine nativen APIs nach und kopiere keine Apple-Schriften oder Symbole ohne passende Rechte. Prüfe Smartphone-Layout, Tastatur, Screenreader, größere Schrift und relevante Offlinezustände.

Eine ausführlichere [Auftragsvorlage](../skills/apple-hig/templates/agent-prompt.md) liegt beim Skill.

## So arbeitet der Agent

1. **Bestand und Scope:** Projektanweisungen, Nutzeraufgabe, Plattformen, Mindestversionen, Framework und Eingaben bestimmen.
2. **Anwendbarkeit:** Alle sechs HIG-Themenfamilien sichten; relevante Themen auswählen und Ausschlüsse begründen.
3. **Plan:** Stabile Kriterien-IDs, Quellen, Screens, Umsetzung und Tests vor dem Bauen festlegen.
4. **Implementierung:** Systemmuster bevorzugen, Zustände und Accessibility mitbauen, API-Verfügbarkeit prüfen.
5. **Prüfung:** Reale Build-/Testbefehle ausführen, Hauptaufgabe und gerenderte UI prüfen; Defekte nachbessern.
6. **Übergabe:** Code beziehungsweise Audit, Belege, Ausnahmen und offene Tests liefern.

Die Referenzen sind nach Bedarf zu laden, nicht ungefragt vollständig in jeden Prompt zu kopieren. Spezialtechnologien werden nicht allein deshalb eingebaut, weil sie in der HIG vorkommen.

## Plan und Audit

Die [Planvorlage](../skills/apple-hig/templates/hig-plan.md) und [JSON-Auditvorlage](../skills/apple-hig/templates/hig-audit.json) in das Anwendungsprojekt kopieren. Platzhalter ersetzen, die Kriterien auf das Projekt zuschneiden und deren IDs vor Implementierung festhalten.

### Felder des Audits

- `project`: tatsächlicher Projektname.
- `scope`: Plattformen, Versionen, Framework und geprüfte Hauptaufgabe.
- `expected_ids`: vollständige, eindeutige Kriterien-ID-Liste aus dem Plan.
- `criteria`: genau ein Eintrag pro erwarteter ID; keine fehlenden oder zusätzlichen IDs.
- `requirement`: konkret prüfbare Anforderung.
- `origin`: `hig`, `engineering` oder `product`.
- `source_ids`: numerische IDs aus dem [Quelleninventar](../skills/apple-hig/references/source-map.md). HIG-Kriterien brauchen mindestens eine Quelle; eigene Regeln dürfen eine leere Liste verwenden.
- `status`: `pass`, `fail`, `not_tested`, `blocked` oder `not_applicable`.
- `evidence`: Liste konkreter Belegreferenzen, etwa Testbericht plus Testname, Screenshot plus Prüfschritte oder manuelles VoiceOver-Protokoll. Ein bestandener Test braucht mindestens eine Referenz.
- `reason`: Begründung für jeden Status außer `pass`; besonders bei Ausschlüssen und Blockern.

**Wichtig:** `pass` nur nach tatsächlich ausgeführter Prüfung. Bei fehlendem Zielgerät bleibt der Hardwaretest offen. Ein Screenshot belegt keine vollständige Tastatur- oder VoiceOver-Bedienbarkeit. Eine nicht implementierte, aber erforderliche Funktion ist kein `not_applicable`.

### Validator ausführen

Aus dem Repository:

```bash
python3 skills/apple-hig/scripts/validate_audit.py /pfad/zum/projekt/hig-audit.json
```

- **Exit 0:** Die angegebenen Kriterien sind formal vollständig und als `pass` oder begründet `not_applicable` dokumentiert.
- **Exit 1:** Strukturfehler, Platzhalter, fehlende/doppelte Kriterien, fehlende Belegreferenz, fehlende Begründung oder offener/fehlgeschlagener Test.

Die unveränderte Vorlage muss mit Exit 1 abgewiesen werden. Die Tests des Validators verwenden synthetische Daten; sie sind kein Nachweis einer geprüften App.

**Was der Validator nicht prüft:** Wahrheit, Existenz und Qualität der Belege; vollständige Auswahl relevanter Kriterien; tatsächliche UI, Datenschutz oder API-Korrektheit. Ein formal gültiges Audit kann inhaltlich schlecht sein. Plan und Nachweise zusätzlich fachlich und mit Werkzeugen prüfen.

## Quellen und Abdeckung

Stand: **29. Oktober 2026**. Die Recherche erfasste 173 eindeutige, über die HIG-Navigation rekursiv erreichbare Seiten einschließlich Kategorien und Startseite:

- 43 Seiten zu Einstieg, Grundlagen und Eingaben.
- 56 Seiten zu Patterns und Technologien.
- 73 Seiten im Komponentenbaum: 64 Komponenten und neun Navigationseinstiege/-gruppen.
- Eine übergeordnete HIG-Startseite.

Die Referenzen sind eigenständige, komprimierte Paraphrasen. „Alle Aspekte“ bedeutet Themenabdeckung und Relevanzprüfung, nicht eine vollständige Kopie jedes Absatzes. Visuelle Beispiele wurden nur stichprobenartig geprüft; nicht alle Videos, Assets oder externen Framework-Dokumentationen sind ausgewertet. Die [Recherchemethodik](../skills/apple-hig/references/research-scope.md) erklärt Details und Aktualisierung.

Apple-Empfehlungen, eigene Engineering-Ableitungen und Produktentscheidungen sind getrennt. Plattformbezogene Zahlen werden nicht auf andere Geräte übertragen. Quellenkonflikte sind gekennzeichnet. Neue OS-Funktionen, konkrete APIs, Hardware- und Entitlement-Verfügbarkeit müssen vor Implementierung aktuell nachgeprüft werden.

## Grenzen und Sicherheit

- Keine Apple-Zertifizierung, App-Store-Zulassung oder pauschale WCAG-/Rechtskonformitätsgarantie.
- Keine eigenmächtige Veröffentlichung, Kontoänderung, Zahlung oder Übertragung privater Projektdaten.
- Kein Ersatz für Security-Review, Datenschutzprüfung oder fachliche Anforderungen regulierter Anwendungen.
- Kein Zugriff auf interne LOGIN-Systeme, keine Zugangsdaten und keine externen Pakete für die mitgelieferten Python-Scripts nötig.
- Keine Apple-Assets im Paket; Quellenlinks verleihen keine Nutzungsrechte an Apple-Schriften, Symbolen oder Marken.

## Tests und Fehlerbehebung

```bash
python3 -m unittest discover -s tests -v
python3 skills/apple-hig/scripts/test_validate_audit.py -v
claude plugin validate .claude-plugin/marketplace.json --strict
```

- **Skill erscheint nicht:** Marketplace aktualisieren, Installation prüfen und neue Sitzung öffnen; Plugin-Aufruf und manuellen Aufruf nicht verwechseln.
- **Referenz fehlt:** Den ganzen Ordner kopieren; relative Pfade beginnen am Skill-Verzeichnis, nicht am Projekt.
- **Validator lehnt Vorlage ab:** Erwartetes Verhalten; echte Projektwerte und Prüfergebnisse fehlen noch.
- **Keine native Testumgebung:** Teilprüfungen durchführen, fehlende Tests als `blocked` dokumentieren; keine grünen Ergebnisse erfinden.
- **Apple-Seite liefert nur JavaScript:** Browser beziehungsweise den in der Recherchemethodik beschriebenen beobachteten DocC-Abrufweg verwenden; Abruflücken sichtbar dokumentieren.

Die Ergebnisse der Erstprüfung einschließlich echter Claude-Code-Skill-Aktivierung stehen im [Prüfbericht](apple-hig-pruefbericht.md).

## Lizenz und Herkunft

Eigenständiger LOGIN-Skill, aus einer HIG-Recherche und einem Agenten-Arbeitsablauf entwickelt, kein übernommenes Apple-Skill-Repository. Die eigenen Texte und Scripts stehen unter MIT; Apple-Originalmaterial bleibt davon ausgenommen. Siehe [Drittanbieterhinweise](../THIRD_PARTY_NOTICES.md). Es besteht keine Verbindung, Zertifizierung oder Herausgeberschaft durch Apple.
