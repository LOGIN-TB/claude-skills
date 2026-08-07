# LOGIN Claude Skills

Agent Skills zur freien Nutzung. Ein Skill ist eine Markdown-Datei mit Anweisungen, die Claude lädt, sobald sie zum jeweiligen Auftrag passt. Das Format folgt dem SKILL.md-Standard und funktioniert in Claude Code, in der Claude-App (claude.ai, Desktop, Cowork) und über die API.

## Enthaltene Skills

### deutscher-schreibstil-ohne-ki-muster

Schreibregeln für deutsche Texte, die nicht nach KI klingen. Der Skill greift bei allem, was auf Deutsch geschrieben wird: Chat-Antworten, Berichte, Artikel, E-Mails, Zusammenfassungen, Social-Media-Posts.

Er unterbindet die Muster, an denen sich maschinell erzeugte Texte erkennen lassen: aufgeblähte Bedeutungszuschreibung, Werbesprache, vage Autoritäten („Studien zeigen"), gehäufte Gedankenstriche, mechanische Verbindungswörter, das Schema „nicht nur …, sondern auch", ausweichende Verben statt „ist/hat", erzwungene Synonym-Rotation, Fazit- und Herausforderungen-Bausteine, Inline-Header-Listen mit fetten Schlagwörtern, Chatbot-Zitierreste und Meta-Sätze über den eigenen Entwurf. Am Ende steht ein Selbstcheck, den Claude vor der Ausgabe durchgeht.

Grundlage ist die Wikipedia-Seite [Anzeichen für KI-generierte Inhalte](https://de.wikipedia.org/wiki/Wikipedia:WikiProjekt_KI_und_Wikipedia/Anzeichen_f%C3%BCr_KI-generierte_Inhalte).

→ [`skills/deutscher-schreibstil-ohne-ki-muster/SKILL.md`](skills/deutscher-schreibstil-ohne-ki-muster/SKILL.md)

## Installation

### Claude Code

Das Repo als Plugin-Marketplace registrieren und das Plugin installieren:

```
/plugin marketplace add LOGIN-TB/claude-skills
/plugin install deutscher-schreibstil@login-skills
```

Updates holst du dir mit `/plugin marketplace update login-skills`.

### Claude Code, manuell

Skill-Ordner direkt kopieren, wahlweise persönlich oder pro Projekt:

```bash
git clone https://github.com/LOGIN-TB/claude-skills.git
cp -r claude-skills/skills/deutscher-schreibstil-ohne-ki-muster ~/.claude/skills/
```

`~/.claude/skills/` gilt für alle Projekte, `.claude/skills/` im Projektordner nur dort und lässt sich mit dem Team versionieren.

### Claude-App (claude.ai, Desktop, Cowork)

Custom Skills werden als ZIP hochgeladen. Der Ordnername im Archiv muss dem Skill-Namen entsprechen, sonst schlägt der Upload fehl.

```bash
cd skills
zip -r deutscher-schreibstil-ohne-ki-muster.zip deutscher-schreibstil-ohne-ki-muster
```

Danach unter [claude.ai/customize/skills](https://claude.ai/customize/skills) auf „+" → „Create skill" → „Upload a skill" und die ZIP-Datei auswählen. Hochgeladene Skills sind privat für den eigenen Account. Team- und Enterprise-Organisationen verteilen sie über die Organisationseinstellungen.

### API

Über die [Skills API](https://docs.claude.com/en/api/skills-guide) lässt sich der Skill als Ressource anlegen und an Anfragen hängen.

### Andere Agenten

SKILL.md ist ein offenes Format aus Markdown mit YAML-Frontmatter. Agenten ohne eigene Skill-Unterstützung nehmen den Text unterhalb des Frontmatters als System-Prompt oder Custom Instruction.

## Aufbau des Repos

```
.claude-plugin/marketplace.json   Marketplace-Definition für Claude Code
skills/<skill-name>/SKILL.md      ein Ordner je Skill, Ordnername = Feld "name"
```

Jede SKILL.md beginnt mit einem Frontmatter-Block aus `name` und `description`. Die Beschreibung entscheidet darüber, ob Claude den Skill im richtigen Moment lädt, und sollte deshalb benennen, was der Skill tut und wann er greifen soll.

```yaml
---
name: skill-name
description: Was der Skill tut und wann er verwendet werden soll.
---
```

## Beiträge

Fehler, Ergänzungen und neue Skills gern als Issue oder Pull Request. Details in [CONTRIBUTING.md](CONTRIBUTING.md).

## Lizenz

[MIT](LICENSE)
