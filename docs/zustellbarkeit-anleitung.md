# Anleitung: der Skill `zustellbarkeit`

Diese Anleitung richtet sich an alle, die den Skill benutzen wollen, ohne sich vorher mit
Mail-Kopfzeilen beschäftigt zu haben.

## Wofür der Skill gut ist

Spamfilter sortieren geschäftliche E-Mails oft nicht wegen der Technik aus, sondern wegen
Aufbau und Inhalt. Der Skill kennt die Merkmale, an denen Filter Werbepost erkennen, und
kann zwei Dinge:

**Eine Mail prüfen, bevor du sie verschickst.** Du gibst Betreff und Text, wahlweise auch
die HTML-Fassung. Zurück kommt eine Liste dessen, was ein Filter negativ bewerten dürfte,
mit jeweils einem konkreten Vorschlag, wie du es änderst.

**Verstehen, warum eine empfangene Mail im Junk gelandet ist.** Du gibst die Mail als
`.eml`-Datei. Der Skill liest aus den Kopfzeilen, wer die Entscheidung getroffen hat und
mit welchen Werten, und benennt anschließend die Merkmale in der Nachricht selbst.

Zwei Sätze, die genauso wichtig sind: Der Skill verspricht nicht, dass deine Mail im
Posteingang landet. Und er ist kein Werkzeug, um Filter auszutricksen — er behebt echte
Mängel, statt sie zu verstecken. Wenn eine Mail nur deshalb als Spam gilt, weil sie
unerwünschte Werbung ist, sagt er das und verweist auf `cold-email`.

## Was du brauchst

Claude Code, die Claude-App oder einen anderen Agenten, der SKILL.md-Dateien liest. Für
die maschinelle Prüfung zusätzlich Python 3.11 oder neuer. Ob du es hast:

```bash
python3 --version
```

Auf macOS und den meisten Linux-Systemen ist Python vorinstalliert. Der Skill braucht
keine Zusatzpakete und geht nie ins Internet.

## Installation

### Claude Code, als Plugin

Einmalig den Marketplace registrieren:

```
/plugin marketplace add LOGIN-TB/claude-skills
```

Dann den Skill installieren:

```
/plugin install zustellbarkeit@login-skills
```

Später aktualisieren mit `/plugin marketplace update login-skills`.

### Claude Code, von Hand

```bash
git clone https://github.com/LOGIN-TB/claude-skills.git
cp -r claude-skills/skills/zustellbarkeit ~/.claude/skills/
```

`~/.claude/skills/` gilt für alle deine Projekte. Willst du den Skill nur in einem
Projekt und im Team versioniert, kopiere ihn stattdessen nach `.claude/skills/` im
Projektordner. Ein neu kopierter Skill erscheint erst in einer neuen Sitzung.

### Claude-App

Die App nimmt Skills als ZIP-Datei entgegen. Der Ordner im Archiv muss `zustellbarkeit`
heißen:

```bash
cd claude-skills/skills
zip -r zustellbarkeit.zip zustellbarkeit
```

Danach unter [claude.ai/customize/skills](https://claude.ai/customize/skills) auf „+" →
„Create skill" → „Upload a skill".

## Benutzen

Meistens musst du gar nichts aufrufen. Claude lädt den Skill von selbst, sobald du etwas
in dieser Richtung fragst:

> Warum ist diese Mail im Junk gelandet?

> Schau dir den Entwurf an, bevor ich ihn rausschicke.

Direkt aufrufen kannst du ihn mit `/zustellbarkeit`.

### Eine empfangene Mail prüfen

Speichere die Nachricht in deinem Mailprogramm als `.eml`-Datei. In Outlook geht das über
„Datei" → „Speichern unter", in Apple Mail über „Ablage" → „Sichern" mit dem Format
„Rohformat". Dann fragst du zum Beispiel:

> Hier ist eine Mail, die im Junk gelandet ist: ~/Downloads/nachricht.eml — woran liegt das?

### Einen Entwurf prüfen

> Prüfe diesen Entwurf, bevor ich ihn verschicke:
> Betreff: Rückfrage zu Ihrer Ausschreibung
> [dein Text]

Hast du auch eine HTML-Fassung, gib sie mit dazu. Viele Befunde stecken im HTML und nicht
im sichtbaren Text.

### Ohne Claude, direkt auf der Kommandozeile

Das Prüfskript läuft auch allein:

```bash
python3 ~/.claude/skills/zustellbarkeit/scripts/zustellbarkeit.py pruefe-eml nachricht.eml
```

```bash
python3 ~/.claude/skills/zustellbarkeit/scripts/zustellbarkeit.py pruefe-entwurf --betreff "Rückfrage" --text-datei entwurf.txt
```

Mit `--json` bekommst du das Ergebnis maschinenlesbar, mit `--strict` endet der Aufruf mit
Rückgabewert 1, sobald ein harter Defekt gefunden wurde. Das eignet sich für automatische
Prüfungen vor dem Versand.

## Die Ausgabe lesen

Jeder Befund hat eine von drei Stufen:

**hart** — ein mechanischer Defekt. Dafür gibt es keine gute Begründung, das gehört
behoben. Beispiel: Im Text steht `calendly.com`, der Link führt aber woanders hin.

**stark** — ein deutliches Werbemerkmal. Entscheide bewusst und begründe, wenn du es
stehen lässt. Beispiel: eine Prozentzahl ohne Quelle.

**hinweis** — ein Redaktionsvorschlag. Beispiel: Emoji im ersten Satz.

Dazu kommen Kennzahlen: wie viel sichtbarer Text auf wie viel HTML kommt, wie viele Links
und Bilder in der Mail stecken und welche Domains beteiligt sind. Bei empfangenen Mails
außerdem das Urteil der Gegenseite.

Es gibt bewusst keine Gesamtnote. Eine Zahl würde eine Vorhersage suggerieren, die niemand
treffen kann.

## Ein Beispiel

Eine Mail, die tatsächlich im Junk lag, ergab:

```
Harte Defekte (3)
  [A] abmeldung-unvollstaendig — Kopfzeilen
      Beleg: List-Unsubscribe-Post ohne List-Unsubscribe
  [A] linkziel-weicht-ab — HTML-Link
      Beleg: sichtbar calendly.com → Ziel u44935817.ct.sendgrid.net
  [A] thread-selbstbezug — Kopfzeilen
      Beleg: References verweist auf die eigene Message-ID
```

Der Absender wollte niemanden täuschen; das ist alles Standardverhalten eines
Versandwerkzeugs. Für den Filter sieht es trotzdem aus wie Verschleierung.

Ein anderer Fall war ein doppeltes Leerzeichen im Betreff — dort, wo ein Seriendruckfeld
leer geblieben war:

```
  [A] merge-artefakt — Betreff
      Beleg: doppeltes Leerzeichen: LOGIN SystemHaus··und Neukunden
```

## Was der Skill nicht prüft

Er sagt nichts darüber, ob du eine Mail verschicken **darfst**. Kaltakquise an
Geschäftskontakte ist in Deutschland an § 7 UWG gebunden; dafür ist `cold-email` da.

Er bewertet auch nicht die Reputation deiner Absenderdomain, dein Versandvolumen oder
deine Beschwerdequote. Das sind starke Faktoren, die nicht im Text stehen.

Und er ersetzt kein Korrekturlesen. Für die sprachliche Überarbeitung gibt Claude den Text
an `vermenschlichen` weiter: `zustellbarkeit` entscheidet, was raus muss, `vermenschlichen`
sorgt dafür, dass die neue Fassung natürlich klingt.

## Häufige Fragen

**Ruft das Skript meine Mail-Links auf?** Nein. Es liest die Datei und sonst nichts. Ein
Abruf würde Zählpixel auslösen und dem Absender melden, dass du die Mail geöffnet hast.

**Gehen meine Mails irgendwohin?** Nein. Alles läuft lokal auf deinem Rechner.

**Woher stammen die Regeln?** Aus der Auswertung tatsächlich einsortierter Nachrichten und
aus den Formatvorgaben RFC 5322 und RFC 8058. Die Bedeutung der Microsoft-Kopfzeilen steht
in deren Dokumentation. Die Quellen mit Prüfdatum stehen im
[Quellenregister](QUELLENREGISTER.md).

**Meine Mail hat keinen einzigen Befund und landet trotzdem im Junk.** Dann liegt es an
etwas, das nicht im Text steht: Domainreputation, Versandhistorie, Volumen, oder daran,
dass der Empfänger dich bereits als unerwünscht markiert hat. Ein leerer Befundbericht
heißt nur, dass die geprüften Merkmale fehlen.

**Kann ich damit Spamfilter umgehen?** Nein, und das ist Absicht. Der Skill behebt Mängel,
statt sie zu tarnen.
