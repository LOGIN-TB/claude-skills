# Beiträge

## Neuen Skill hinzufügen

Lege unter `skills/` einen Ordner an, dessen Name dem `name`-Feld im Frontmatter entspricht (Kleinbuchstaben, Bindestriche statt Leerzeichen). Darin liegt die `SKILL.md`:

```
skills/mein-skill/SKILL.md
```

Das Frontmatter braucht zwei Felder:

```yaml
---
name: mein-skill
description: Was der Skill tut und wann er verwendet werden soll.
---
```

Der `name` ist zugleich der Slash-Befehl (`/mein-skill`). Die `description` ist der Auslöser für den automatischen Aufruf: Claude liest nur sie, um zu entscheiden, ob der Skill geladen wird. Sie sollte beides nennen — die Aufgabe und die Situation, in der der Skill greift. Der Text darunter wird erst dann geladen und kann entsprechend ausführlich sein.

Ergänzende Dateien (Referenzen, Skripte, Vorlagen) liegen im selben Ordner und werden aus der `SKILL.md` heraus mit relativem Pfad angesprochen.

Optional, aber im Repo üblich: weitere Angaben unter `metadata` statt als eigene Frontmatter-Felder. Claude liest sie nicht, sie dienen der Nachvollziehbarkeit.

```yaml
license: MIT
metadata:
  version: "1.0.0"
  author: "Name"
  tags: [stichwort, stichwort]
  related_skills: [anderer-skill]
```

`related_skills` verweist nur auf Skills, die es in diesem Repo tatsächlich gibt.

Trag den neuen Skill anschließend in `.claude-plugin/marketplace.json` und in die Skill-Liste der `README.md` ein.

## Abgeleitete Skills

Beruht ein Skill auf fremdem Material, gehört die Herkunft dokumentiert, bevor er aufgenommen wird:

- Upstream-Repository, Datei und vollständiger Commit unter `metadata` (`upstream`, `upstream_commit`, `upstream_homepage`)
- vollständiger Lizenztext des Ausgangsprojekts unter `licenses/`
- Eintrag in [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) mit Copyright, Lizenz und Commit
- Eintrag in `skills/catalog.json` und `skills/curation.json`
- die konkreten Abweichungen in [`docs/UPSTREAM-AENDERUNGEN.md`](docs/UPSTREAM-AENDERUNGEN.md)

Der Maßstab für solche Bearbeitungen steht in [`docs/KURATIERUNGSRICHTLINIE.md`](docs/KURATIERUNGSRICHTLINIE.md). Eine Bearbeitung wird nicht als offizielle Ausgabe des Ausgangsprojekts dargestellt.

## Vor dem Pull Request

Prüfe, ob der Skill in einer echten Sitzung von selbst greift. Wenn nicht, liegt es fast immer an der `description`. Nimm den Skill nur auf, wenn er ohne Zugangsdaten, interne Systeme oder personenbezogene Daten funktioniert.

Mit dem Pull Request stellst du deinen Beitrag unter die [MIT-Lizenz](LICENSE) dieses Repos.
