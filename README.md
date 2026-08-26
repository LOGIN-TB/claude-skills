# LOGIN Claude Skills

Agent Skills zur freien Nutzung. Ein Skill ist eine Markdown-Datei mit Anweisungen, die Claude lädt, sobald sie zum jeweiligen Auftrag passt. Das Format folgt dem SKILL.md-Standard und funktioniert in Claude Code, in der Claude-App (claude.ai, Desktop, Cowork) und über die API.

## Enthaltene Skills

### vermenschlichen

Schreibregeln für deutsche Texte, die nicht nach KI klingen. Der Skill greift bei allem, was auf Deutsch geschrieben wird: Chat-Antworten, Berichte, Artikel, E-Mails, Zusammenfassungen, Social-Media-Posts. Direkt aufrufen kannst du ihn mit `/vermenschlichen`, etwa um einen vorhandenen Text zu überarbeiten.

Er unterbindet die Muster, an denen sich maschinell erzeugte Texte erkennen lassen: aufgeblähte Bedeutungszuschreibung, Werbesprache, vage Autoritäten („Studien zeigen"), gehäufte Gedankenstriche, mechanische Verbindungswörter, das Schema „nicht nur …, sondern auch", ausweichende Verben statt „ist/hat", erzwungene Synonym-Rotation, Fazit- und Herausforderungen-Bausteine, Inline-Header-Listen mit fetten Schlagwörtern, Chatbot-Zitierreste und Meta-Sätze über den eigenen Entwurf. Am Ende steht ein Selbstcheck, den Claude vor der Ausgabe durchgeht.

Dazu kommt, was oft übersehen wird: ein Abschnitt darüber, welche Merkmale gerade *kein* Hinweis auf KI sind (fehlerfreie Grammatik, förmlicher Ton, ein einzelnes Verbindungswort). Er verhindert, dass Texte beim Überarbeiten künstlich verschlechtert werden.

Grundlage sind die Sammlungen der Wikipedia-Communitys: [Anzeichen für KI-generierte Inhalte](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte) (deutsch) und [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (englisch).

→ [`skills/vermenschlichen/SKILL.md`](skills/vermenschlichen/SKILL.md)

### DACH-Marketing-Suite

Dreizehn deutschsprachige Skills für Marketing, Recherche und Redaktion, zugeschnitten auf Deutschland, Österreich und die Schweiz. Was sie von generischen Marketing-Skills unterscheidet, ist die Arbeitshaltung: Aussagen brauchen Belege mit Quelle und Datum, Schätzungen bleiben als Schätzungen kenntlich, personenbezogene Daten werden minimiert, Deutschland gilt bei deutschem Auftrag als sichtbar gekennzeichnete Annahme (Österreich und Schweiz separat), und externe Aktionen wie Versand, Veröffentlichung, Tracking oder Käufe brauchen eine gesonderte Freigabe. Rechtsverweise sind Prüfpunkte, keine Rechtsberatung.

Jeder Skill lässt sich mit seinem Namen direkt aufrufen, etwa `/seo-audit`.

| Skill | Aufgabe |
|---|---|
| [`ai-seo`](skills/ai-seo/SKILL.md) | Sichtbarkeit, Zitierung und Empfehlung in KI-Antwortsystemen prüfen und verbessern. Trennt Abruf, Zitierung, Erwähnung und Empfehlung und weist unbelegte KI-Rankingfaktoren zurück. |
| [`seo-audit`](skills/seo-audit/SKILL.md) | Crawling, Indexierung, Rendering, Leistung, Onpage, hreflang und Migrationen mit reproduzierbarer Evidenz prüfen und priorisieren. Bleibt lesend. |
| [`product-marketing`](skills/product-marketing/SKILL.md) | Produktmarketing-Kontext als `.agents/product-marketing.md` pflegen: ICP, Jobs-to-be-Done, Nutzenversprechen, Einwände, Belegklassen. Grundlage für die übrigen Skills. |
| [`social`](skills/social/SKILL.md) | Organische Social-Media-Inhalte planen, verfassen und wiederverwenden, mit Werbekennzeichnung, Rechteprüfung, Alt-Texten und aktuellen Plattformregeln. |
| [`cold-email`](skills/cold-email/SKILL.md) | B2B-Outreach entwerfen und prüfen: § 7 UWG, die kumulative Bestandskundenausnahme, Datenherkunft, Sperrlisten. Liefert nur Entwürfe mit sichtbarem Versandblocker. |
| [`competitors`](skills/competitors/SKILL.md) | Vergleichs- und Alternativseiten mit Aussagenverzeichnis, Preisstichtag und symmetrischer Bewertung. Prüft § 6 UWG und Markenrecht konservativ. |
| [`competitor-profiling`](skills/competitor-profiling/SKILL.md) | Profile einzelner Anbieter aus öffentlichen Quellen, mit Claim-Ledger, der Tatsache, Anbieterangabe, Schätzung und Hypothese auseinanderhält. |
| [`content-strategy`](skills/content-strategy/SKILL.md) | Themenfelder, Redaktionsplan und Backlog aus Nachfrage, Evidenz und tatsächlicher Produktionskapazität. Schützt vor dünnen Massenseiten. |
| [`copywriting`](skills/copywriting/SKILL.md) | Website-Texte, die Fähigkeit, Wirkung und Beleg verbinden. Erhält Einschränkungen statt sie zu glätten und verzichtet auf manipulative Muster. |
| [`customer-research`](skills/customer-research/SKILL.md) | Interviews, Umfragen und Auswertungen mit Zweckbindung, Einwilligung, Pseudonymisierung und Auswertung im Stichprobenrahmen. Trennt Befund von Entscheidung. |
| [`image`](skills/image/SKILL.md) | Bildbriefings, Screenshots, generative Bilder, Stockrouten, Optimierung und deutsche Alt-Texte. Klärt Herkunft und Rechte vor der Produktion. |
| [`lead-magnets`](skills/lead-magnets/SKILL.md) | Gated Content mit minimalen Formularen, von der Auslieferung getrennter Marketingeinwilligung und Einordnung von Double-Opt-in und TDDDG. |
| [`marketing-ideas`](skills/marketing-ideas/SKILL.md) | Hypothesen zu Experimentsteckbriefen mit Metrik, Laufzeit, Budget und Stopkriterium. Sortiert Untragbares vor der Bewertung aus. |

Die dreizehn Skills sind kuratierte Bearbeitungen der MIT-lizenzierten [`coreyhaines31/marketingskills`](https://github.com/coreyhaines31/marketingskills). Herkunft, geprüfter Upstream-Commit und die konkreten Abweichungen stehen in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) und [docs/UPSTREAM-AENDERUNGEN.md](docs/UPSTREAM-AENDERUNGEN.md).

## Installation

### Claude Code

Das Repo einmalig als Plugin-Marketplace registrieren:

```
/plugin marketplace add LOGIN-TB/claude-skills
```

Danach einzelne Skills installieren:

```
/plugin install vermenschlichen@login-skills
/plugin install seo-audit@login-skills
```

Oder die komplette Marketing-Suite als Bündel:

```
/plugin install marketing-dach@login-skills
```

**Entweder das Bündel oder einzelne Marketing-Skills, nicht beides.** Das Bündel enthält alle dreizehn Skills; wer zusätzlich einen davon einzeln installiert, lädt ihn doppelt.

Updates holst du dir mit `/plugin marketplace update login-skills`.

### Claude Code, manuell

Skill-Ordner direkt kopieren, wahlweise persönlich oder pro Projekt:

```bash
git clone https://github.com/LOGIN-TB/claude-skills.git
cp -r claude-skills/skills/vermenschlichen ~/.claude/skills/
```

Alle dreizehn Marketing-Skills auf einmal, ohne `catalog.json` und `curation.json`:

```bash
for s in ai-seo seo-audit product-marketing social cold-email competitors \
         competitor-profiling content-strategy copywriting customer-research \
         image lead-magnets marketing-ideas; do
  cp -r "claude-skills/skills/$s" ~/.claude/skills/
done
```

`~/.claude/skills/` gilt für alle Projekte, `.claude/skills/` im Projektordner nur dort und lässt sich mit dem Team versionieren. Neu kopierte Skills erscheinen erst in einer neuen Sitzung.

### Claude-App (claude.ai, Desktop, Cowork)

Custom Skills werden als ZIP hochgeladen. Der Ordnername im Archiv muss dem Skill-Namen entsprechen, sonst schlägt der Upload fehl.

```bash
cd skills
zip -r vermenschlichen.zip vermenschlichen
zip -r seo-audit.zip seo-audit
```

Jeder Skill braucht ein eigenes Archiv; ein Sammelarchiv über mehrere Ordner nimmt die App nicht an.

Danach unter [claude.ai/customize/skills](https://claude.ai/customize/skills) auf „+" → „Create skill" → „Upload a skill" und die ZIP-Datei auswählen. Hochgeladene Skills sind privat für den eigenen Account. Team- und Enterprise-Organisationen verteilen sie über die Organisationseinstellungen.

### API

Über die [Skills API](https://docs.claude.com/en/api/skills-guide) lässt sich der Skill als Ressource anlegen und an Anfragen hängen.

### Andere Agenten

SKILL.md ist ein offenes Format aus Markdown mit YAML-Frontmatter. Agenten ohne eigene Skill-Unterstützung nehmen den Text unterhalb des Frontmatters als System-Prompt oder Custom Instruction.

## Aufbau des Repos

```
.claude-plugin/marketplace.json   Marketplace-Definition für Claude Code
skills/<skill-name>/SKILL.md      ein Ordner je Skill, Ordnername = Feld "name"
skills/catalog.json               Herkunft und Art jedes kuratierten Skills
skills/curation.json              Version, Änderungskategorien und Prüffelder je Skill
docs/                             Kuratierungsrichtlinie, Terminologie, Quellenregister,
                                  Abweichungen gegenüber Upstream
licenses/                         geprüfte Lizenztexte der Ausgangsprojekte
THIRD_PARTY_NOTICES.md            Herkunft und Lizenzen abgeleiteter Skills
```

Jede SKILL.md beginnt mit einem Frontmatter-Block aus `name` und `description`. Der Name ist zugleich der Slash-Befehl, unter dem sich der Skill direkt aufrufen lässt. Die Beschreibung entscheidet darüber, ob Claude den Skill von sich aus im richtigen Moment lädt, und sollte deshalb benennen, was der Skill tut und wann er greifen soll.

```yaml
---
name: skill-name
description: Was der Skill tut und wann er verwendet werden soll.
---
```

## Herkunft und Kuratierung

`vermenschlichen` ist eine Eigenentwicklung. Die dreizehn Marketing-Skills sind kuratierte deutsche Fassungen eines MIT-lizenzierten Ausgangsprojekts; sie sind weder wörtliche Übersetzungen noch offizielle Ausgaben davon.

- [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) — Herkunft, geprüfter Commit, Lizenztexte
- [docs/KURATIERUNGSRICHTLINIE.md](docs/KURATIERUNGSRICHTLINIE.md) — Maßstab für die Bearbeitungen
- [docs/UPSTREAM-AENDERUNGEN.md](docs/UPSTREAM-AENDERUNGEN.md) — Abweichungen je Skill
- [docs/TERMINOLOGIE.md](docs/TERMINOLOGIE.md) — Schreibstandard und Begriffe
- [docs/QUELLENREGISTER.md](docs/QUELLENREGISTER.md) — autoritative Quellen und Prüfeinstiege

Die Installation eines Skills autorisiert keine darin beschriebene externe Aktion. Vor Versand, Veröffentlichung, Tracking, Käufen oder Kontoänderungen bleibt eine konkrete Freigabe erforderlich. Rechtsverweise in den Skills sind Prüfpunkte, keine Rechtsberatung.

## Beiträge

Fehler, Ergänzungen und neue Skills gern als Issue oder Pull Request. Details in [CONTRIBUTING.md](CONTRIBUTING.md).

## Lizenz

[MIT](LICENSE)
