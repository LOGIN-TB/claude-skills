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

Die `description` ist der Auslöser: Claude liest nur sie, um zu entscheiden, ob der Skill geladen wird. Sie sollte beides nennen — die Aufgabe und die Situation, in der der Skill greift. Der Text darunter wird erst dann geladen und kann entsprechend ausführlich sein.

Ergänzende Dateien (Referenzen, Skripte, Vorlagen) liegen im selben Ordner und werden aus der `SKILL.md` heraus mit relativem Pfad angesprochen.

Trag den neuen Skill anschließend in `.claude-plugin/marketplace.json` und in die Skill-Liste der `README.md` ein.

## Vor dem Pull Request

Prüfe, ob der Skill in einer echten Sitzung von selbst greift. Wenn nicht, liegt es fast immer an der `description`. Nimm den Skill nur auf, wenn er ohne Zugangsdaten, interne Systeme oder personenbezogene Daten funktioniert.

Mit dem Pull Request stellst du deinen Beitrag unter die [MIT-Lizenz](LICENSE) dieses Repos.
