# Apple HIG

**Apple-Interfaces entwickeln und prüfen – nicht nur Apple-Optik nachbauen.**

Apple HIG unterstützt Coding-Agenten dabei, Anwendungen nach Apples Human Interface Guidelines zu erstellen oder bestehende Oberflächen daran zu prüfen. Der Skill führt von der Plattformwahl über konkrete Komponenten und Zustände bis zur realen Prüfung der Anwendung.

## Was der Skill macht

- Klärt Nutzeraufgabe, Zielplattform, Framework und unterstützte OS-Versionen.
- Übersetzt relevante HIG-Empfehlungen in konkrete Implementierungs- und Abnahmekriterien.
- Unterstützt Navigation, Layout, Typografie, Farben, Materialien/Liquid Glass, Eingaben und Accessibility.
- Berücksichtigt Loading, Empty, Error, Offline, Berechtigungsverweigerung sowie Abbruch und Undo, soweit relevant.
- Verlangt Build, funktionierende Hauptabläufe, UI-Prüfung und ehrliche Testbelege.
- Trennt Apple-Empfehlungen, eigene Engineering-Ableitungen und Produktentscheidungen.

**Beispiele:** Eine SwiftUI-App entwickeln, ein iPad-Layout adaptiv machen, eine Mac-App auf Tastaturbedienung prüfen oder eine bestehende PWA ausdrücklich an HIG-Prinzipien orientieren. Web/PWA bleibt eine Webanwendung; native APIs und Apple-Zertifizierung werden nicht suggeriert.

## Schnellstart mit Claude Code

In Claude Code:

```text
/plugin marketplace add LOGIN-TB/claude-skills
/plugin install apple-hig@login-skills
```

Ist der Marketplace bereits registriert, vor der Installation aktualisieren:

```text
/plugin marketplace update login-skills
```

Nach der Installation gegebenenfalls eine neue Sitzung öffnen. Der Plugin-Aufruf ist namensräumlich:

```text
/apple-hig:apple-hig Prüfe die vorhandene App anhand der HIG. Implementiere anschließend die priorisierten Verbesserungen und liefere ein Audit mit Belegen.
```

Bei manueller Installation unter `.claude/skills/apple-hig/` oder `~/.claude/skills/apple-hig/` lautet der Aufruf `/apple-hig`. Alternativ im Auftrag ausdrücklich „Nutze Apple HIG“ nennen. Die vollständige [Anleitung](../../docs/apple-hig-anleitung.md) enthält Installation, Beispiele, Testverfahren und Fehlerbehebung.

## Erwartetes Ergebnis

1. Ein projektspezifischer HIG-Umsetzungsplan.
2. Funktionierende Implementierung – oder bei einem reinen Prüfauftrag ein Audit ohne ungefragte Änderungen.
3. Eine vollständige Liste relevanter Kriterien mit Quellen, Ergebnissen und Belegen.
4. Klar benannte Ausnahmen, offene Tests und Infrastrukturblocker.

Der Agent muss nicht jede Apple-Technologie hinzufügen: HealthKit, Apple Pay, CarPlay, KI oder Spatial Computing werden nur bei tatsächlichem Produktbedarf relevant.

## Inhalt

- [SKILL.md](SKILL.md): Arbeitsablauf und Qualitätsgates.
- [Grundlagen, Plattformen, Eingaben](references/foundations-platforms-inputs.md): 43 Seiten einschließlich Übersichten.
- [Patterns und Technologien](references/patterns-technologies.md): 56 Seiten einschließlich Kategorien.
- [Komponenten](references/components.md): 64 Komponenten aus 73 Navigationsseiten.
- [Quelleninventar](references/source-map.md): 173 eindeutige HIG-Seiten inklusive Startseite und Kategorien.
- [Rechercheumfang und Pflege](references/research-scope.md): Methode, Aktualisierung und Grenzen.
- [Agentenauftrag](templates/agent-prompt.md), [Planvorlage](templates/hig-plan.md), [Auditvorlage](templates/hig-audit.json).
- [Auditvalidator](scripts/validate_audit.py) und [dessen Tests](scripts/test_validate_audit.py).

## Lokale Prüfwerkzeuge

Python 3, nur Standardbibliothek; keine Zugangsdaten und kein Netzwerkzugriff durch die Scripts. Aus diesem Skill-Ordner:

```bash
python3 scripts/test_validate_audit.py -v
python3 scripts/validate_audit.py /pfad/zum/projekt/hig-audit.json
```

Die unveränderte Auditvorlage schlägt absichtlich fehl: Sie enthält Platzhalter und ungetestete Kriterien. `PASS` bedeutet ausschließlich, dass die deklarierten Kriterien vollständig und formal korrekt als bestanden oder nicht anwendbar dokumentiert wurden. Das Script prüft **nicht** die Anwendung, die tatsächliche Existenz oder Qualität der Belege oder die fachliche Vollständigkeit der vom Agenten ausgewählten Kriterien.

## Grenzen und Rechte

Recherchestand: **29. Oktober 2026**. Alle über die sechs Themenbereiche rekursiv navigationsverlinkten Seiten wurden textlich ausgewertet. Die Referenzen sind verdichtete Umsetzungshilfen, keine vollständige Übersetzung. Nicht jedes Bild, Video, Designasset oder externe API-Dokument wurde geprüft. Kritische Details und API-Verfügbarkeit vor Implementierung erneut gegen offizielle Quellen prüfen.

Kein Apple-Zertifikat, keine App-Store-Freigabezusage und keine pauschale Accessibility-Konformitätsgarantie. Bei fehlendem Simulator, SDK oder Zielgerät bleiben die entsprechenden Tests offen. Die Installation autorisiert weder Veröffentlichung noch Deployment oder andere externe Aktionen.

Eigenständige Anweisungen, Paraphrasen und Scripts unter [MIT](LICENSE). Apple-Originaltexte, Marken, Schriften, Symbole und Designressourcen sind davon nicht erfasst; keine Apple-Assets enthalten. Nicht von Apple herausgegeben oder zertifiziert.
