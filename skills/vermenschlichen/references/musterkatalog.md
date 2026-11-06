# Musterkatalog zu vermenschlichen

Geprüft am 6. November 2026. Grundlage sind die Wikipedia-Seiten [Anzeichen für KI-generierte Inhalte](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte) (Stand 29. Oktober 2026) und [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) mit den Unterseiten `/Style` und `/Markup` (Stand 4. November 2026) sowie die Studien im Quellenverzeichnis unten.

Der Katalog ist beschreibend. Er sammelt, was in KI-Texten gehäuft auftritt, und ist keine Verbotsliste. Ein Treffer ist ein Anlass, den Satz zu prüfen, kein Beweis. Die Merkmale ändern sich mit jeder Modellgeneration; den Katalog daher etwa vierteljährlich mit den Quellen abgleichen und das Prüfdatum anpassen.

## Deutsche Wendungen nach Funktion

Die Beispiele zeigen die Funktion. Wer nur das Wort tauscht und die Funktion behält, hat nichts gewonnen.

| Funktion | Beispiele | Besser |
|---|---|---|
| Bedeutung aufblähen | „spielt eine bedeutende Rolle“, „steht als Zeugnis für“, „markiert einen Wendepunkt“, „fasziniert weiterhin“, „Schlüsselmoment“, „festigt seinen Ruf“ | sagen, was geschah |
| Relevanz ankündigen | „Das ist wichtig, weil …“, „Warum X zählt“, „X ist mehr als nur ein …“, „Mit Blick nach vorn …“, „fügt eine weitere Ebene hinzu“, „statt einfach nur …“ | Grund ohne Ankündigung nennen |
| Werben | „reiches kulturelles Erbe“, „reicher kultureller Teppich“, „eingebettet in“, „im Herzen von“, „atemberaubend“, „unbedingt besuchen“ | neutral beschreiben |
| Helferton | „hilft Ihnen dabei“, „macht es leichter“, „ermöglicht es Ihnen“ | sagen, was passiert |
| Vage Verbindung | „im Zusammenhang mit“, „wird mit … in Verbindung gebracht“, „ist mit … verbunden“ | Beziehung benennen |
| Debattenrahmung | „löste eine breite Debatte aus“, „beteiligte sich an öffentlichen Diskussionen über“, „Diese Unterscheidung ist wichtig, weil“ | Inhalt der Debatte oder weglassen |
| Identifikation über Eigenangaben | „Laut seiner Website ist er …“, „wird im Register als … geführt“, „sein Profil weist ihn als … aus“ | Aussage machen, Quelle als Beleg |
| Bekanntheit behaupten | „fand Beachtung in der Fachpresse“, „unterhält eine aktive Präsenz in sozialen Medien“ | Ereignis nennen, Beleg setzen |
| Selbstkommentar | „Es ist wichtig zu beachten“, „Erwähnenswert ist“, „Keine Diskussion wäre vollständig ohne“, „Dieser Artikel würde nicht ohne … existieren“ | streichen |
| Schluss-Zusammenfassung | „Insgesamt zeigt sich“, „Zusammenfassend lässt sich sagen“, „Abschließend“ | streichen oder an den Anfang |

## Absicherungsformeln nach Zeitraum

Laut englischer Wikipedia lösen sich die Formen ab. Die jüngste ist für Claude-Ausgaben besonders relevant.

| Zeitraum | Englisch | Deutsche Entsprechung |
|---|---|---|
| 2023 bis 2024 | „as of my last knowledge update“ | „Stand meines letzten Updates“, „bis zu meinem Wissensstand“ |
| 2024 bis 2025 | „not widely documented“, „limited in the provided search results“, dann Spekulation mit „likely“; „maintains a low profile“ | „nicht umfassend dokumentiert“, „obwohl spezifische Details rar sind“, „basierend auf verfügbaren Informationen“, dann „dürfte wahrscheinlich“; „hält sich bedeckt“ |
| seit Mitte 2026 | „should be treated as … rather than …“, „does not (by itself) establish …“, „should not be confused with …“ | „ist als … zu verstehen, nicht als …“, „belegt für sich genommen nicht, dass …“, „ist nicht zu verwechseln mit …“ |

## Dialog-, Brief- und Meta-Reste

- Chatbot-Floskeln: „Gerne!“, „Natürlich!“, „Sicherlich!“, „Gute Frage!“, „Du hast völlig recht!“, „Ich hoffe, das hilft“, „Lassen Sie mich wissen, wenn …“, „Gibt es noch etwas …“, „Hier ist eine detailliertere Aufschlüsselung“.
- Briefreste: „Betreff:“ über einem Artikel, „Liebe Redaktion“, „Ich schreibe, um …“, „Ich hoffe, diese Nachricht erreicht Sie wohlauf“, „Vielen Dank für Ihre Zeit“, Beteuerungen guter Absicht.
- Ratschläge im Ergebnistext: „Bitte vor der Veröffentlichung prüfen“, „Vor dem Anlegen der Seite sollten Sie …“, angehängte Checklisten für den Nutzer.
- Versteckte Arbeitsanweisungen in Kommentaren, etwa `<!-- EINLEITUNG: auf zwei Absätze erweitern -->`.
- Notizen an Prüfer: „Hinweis für Prüfer: Dieser Entwurf ist neutral und gut belegt.“
- KI-typische Änderungsnotizen: „Neutralität sichergestellt“, „alle Fakten beibehalten“, „Werbesprache vermieden“, „mit unabhängigen Quellen belegt“, Aufzählung jedes geänderten Feldes, lange Notizen in der Ich-Form ohne Abkürzungen.

## Platzhalter

- Eckige Klammern: „[Name einfügen]“, „[Jahr]“, „[Gründernamen]“, „hier Details ergänzen“.
- Datumsplatzhalter: „2025-XX-XX“, „TT.MM.JJJJ“.
- Quellenplatzhalter: `INSERT_SOURCE_URL_30`, `SOURCE_PUBLISHER`, „Beispiel-Quellentitel“.
- URL-Platzhalter: `example.com/source1`, `example.com/article`. Das bloße `example.com` ist in Vorlagen und Dokumentation legitim.

## Zitier- und Formatierungsartefakte nach Anbieter

| Anbieter | Artefakte |
|---|---|
| ChatGPT | `utm_source=chatgpt.com`, `utm_source=openai`, `oaicite`, `oai_citation`, `:contentReference[oaicite:…]`, `attributableIndex`, `turn0search0`, „Gehe zu Suche Nr. …“ (seit Februar 2025, oft mit Unicode-Punkten und aufsteigender Nummer), Marker wie „Beispiel+1“ |
| Copilot | `utm_source=copilot.com` |
| Gemini | `[cite: 1]`, `[span_1]`, nackte `[1, 2]`, Reste von `<mark>` aus der Funktion „Antwort überprüfen“ |
| Grok | `grok_render_citation_card`, `referrer=grok.com` |
| DeepSeek | Linsenklammern mit Dolch, etwa `【85†L261-269】` |
| Perplexity | `[web:1]`, `[attached_file:1]` |
| allgemein | Rücksprungzeichen `↩` aus Fußnoten, Umhüllungen wie `:::writing{variant="document" id=…}`, auffällig niedrige Datenbank-IDs wie `pubmed.ncbi.nlm.nih.gov/3` |

Ein utm- oder referrer-Anhang zeigt, dass ein Chatbot die Quelle gefunden hat. Er sagt nichts darüber, wer den Text geschrieben hat.

Markdown-Reste in Umgebungen ohne Markdown: `**fett**`, `###`, `[Text](URL)`, Codeblöcke um Fließtext (oft als „wikitext“ beschriftet), `---` oder `----` als Trenner. Ein starkes Zeichen ist Markdown gemischt mit fehlerhafter Zielsyntax. Markdown allein beweist nichts.

Anführungszeichen: ChatGPT und DeepSeek mischen gelegentlich typografische und gerade Zeichen. Im Deutschen ist nur die Mischung auffällig; typografische Zeichen allein entstehen auch durch Word oder macOS.

Unsichtbare Zeichen: Variationsselektoren (U+FE00 bis U+FE0F, U+E0100 bis U+E01EF) nach einem U+FEFF können ein C2PA-Herkunftsnachweis im Text sein (C2PA-Spezifikation 2.3 und 2.4, Anhang A.8). Nicht pauschal entfernen.

## Belegprüfung

- Existiert die Quelle? ISBN-Prüfziffer nachrechnen, DOI über doi.org auflösen, Links öffnen.
- Tote Links im Webarchiv suchen. Mehrere tote Links, die auch im Archiv fehlen, sind ein Warnsignal. Manche Links scheitern nur für dich (Bezahlschranke, Bot-Sperre).
- Sagt die Quelle genau das, was ihr zugeschrieben wird? Stimmen Verlag, Herausgeber, Jahr und Seitenzahl?
- Hängt jeder Eintrag im Quellenverzeichnis an einer Aussage?
- Passt der Zitierstil zur Sprache? Englische Zitierweise in deutschen Texten fällt auf.
- Von KI erzeugte Webseiten sind keine tragfähige Quelle.
- Ein einzelner Fehler ist ein Versehen. Mehrere fehlerhafte Belege verlangen eine vollständige Nachprüfung.

## Englische Wortlisten nach Modellgeneration

Diese Listen stammen aus der englischen Wikipedia und gelten für englische Texte. Wörtlich nehmen: Die Häufung eines Wortes bedeutet nicht, dass seine Synonyme oder deutschen Entsprechungen ebenfalls gehäuft vorkommen. Für deutsche Texte gibt es keine vergleichbar belegte Liste.

| Generation | Wörter | Belegstärke |
|---|---|---|
| GPT-4 (2023 bis Mitte 2024) | delve, tapestry, testament, intricate | gut belegt |
| GPT-4o (Mitte 2024 bis Mitte 2025) | align with, fostering, showcasing | gut belegt |
| GPT-5 (Mitte 2025 bis Mitte 2026) | emphasizing, enhance, highlighting, showcasing | belegt |
| GPT-6 (seit Mitte 2026) | challenge, clearer, dependable, echoed, foster, leverage, matters, multifaceted, practical, prioritize, quietly, steady, universally; sehr kurze Sätze | schwach, eine Blogquelle |

„Delve“ ist seit 2025 stark zurückgegangen.

Phrasen in Claude Opus 5.5, als Vielfaches der menschlichen Häufigkeit (Graphite, Oktober 2026, Agenturstudie ohne Begutachtung): „this matters“ (116-fach), „is more than a … it“ (98-fach), „why … matters“ (92-fach), „looking ahead the“ (40-fach), „rather than simply“ (32-fach), „adds another layer“ (27-fach). Die deutschen Entsprechungen stehen oben unter „Relevanz ankündigen“.

Gedankenstriche je 1.000 Wörter (Graphite, September und Oktober 2026): menschliche Vergleichstexte 3,14; GPT-5 6,92; Claude Opus 5 2,92; Claude Opus 5.5 0,015; Gemini 3.1 Pro 0,014. Die Werte zeigen, wie schnell sich ein Merkmal umkehrt. Sie sind kein Zielwert.

## Ältere Erkennungsmerkmale

Diese Muster führt die englische Wikipedia inzwischen unter „Historical indicators“. Als Stilregeln bleiben sie sinnvoll.

| Muster | Zeitraum laut Wikipedia | Hinweis |
|---|---|---|
| Gehäufte Gedankenstriche | 2022 bis September 2026 | Neueste Modelle meiden sie fast ganz; Claude lag laut Economist-Studie (Juli 2026) noch über professionellen Autoren |
| Werbesprache | 2023 bis 2025 | Werbende Wirkung entsteht heute eher durch Auswahl der Inhalte |
| Synonym-Rotation | ältere Modelle | Wird in Schulen gelehrt, daher im Deutschen ein schwaches Signal |
| Abschnitts-Zusammenfassungen und Fazit | ältere Modelle | „Herausforderungen und Ausblick“ ist weiter aktuell |
| Hinweise auf den Wissensstand | ältere Modelle | Abgelöst durch die Absicherungsformeln oben |
| Abrupte Abbrüche | ältere Modelle | Auch Kopierfehler kommen als Ursache in Frage |
| „Als großes Sprachmodell …“, Verweigerungen | ältere Modelle | |
| Emojis | möglicherweise historisch | Heute vor allem in Diskussionsbeiträgen und Änderungsnotizen |

## Unterschiede zwischen Modellen

Gemini und Claude schreiben laut englischer Wikipedia knapper, ChatGPT und Grok holen weiter aus. Die Häufigkeit von Merkmalen wie Kurzformen schwankt zwischen aktuellen Modellen um mehr als das Zwanzigfache (Rudnicka und Juzek, 2026). Aussagen über „die KI“ sind deshalb fast immer zu grob.

## Quellenverzeichnis

Belegstärke: B = begutachtet, P = Preprint oder Arbeitspapier, A = Anbieterangabe, C = Community-Richtlinie, R = Rechtstext.

Stil und Sprache

- Reinhart u. a.: Do LLMs write like humans? Variation in grammatical and rhetorical styles. PNAS 122(8), 2025. https://doi.org/10.1073/pnas.2422455122 (B)
- Terčon und Dobrovoljc: Linguistic Characteristics of AI-Generated Text: A Survey. 2025. https://arxiv.org/abs/2510.05136 (P)
- Kendro, Maloney und Jarvis: Do LLMs produce texts with „human-like“ lexical diversity? 2025. https://arxiv.org/abs/2508.00086 (P)
- Valentinelli: Tracing English interference in AI-generated German. AI-Linguistica 5(1), 2026. https://doi.org/10.62408/ai-ling.v5i1.36 (B)
- Rudnicka und Juzek: Beyond „AI Language“: The case for the idiolectal nature of LLM output. 2026. https://arxiv.org/abs/2608.06589 (P)
- Jiang u. a.: Artificial Hivemind: The Open-Ended Homogeneity of Language Models. NeurIPS 2025. https://arxiv.org/abs/2510.22954 (B)
- Agarwal, Naaman und Vashistha: AI Suggestions Homogenize Writing Toward Western Styles. CHI 2025. https://arxiv.org/abs/2409.11360 (B)
- I, ChatGPT: linguistic properties and human experiences of human- versus AI-generated stories. Humanities and Social Sciences Communications, 2025. https://www.nature.com/articles/s41599-025-06341-2 (B)
- Peng u. a.: Not X, but When: Diagnosing a Mandarin LLM Writing Tic through Contextual Appropriateness. 2026. https://arxiv.org/abs/2610.22249 (P)
- Kobak u. a.: Delving into LLM-assisted writing in biomedical publications through excess vocabulary. Science Advances 11(27), 2025. https://doi.org/10.1126/sciadv.adt3813 (B)
- Holzwarth, González-Márquez und Kobak: Folgestudie zum LLM-Vokabular in Volltexten. 2026. https://arxiv.org/abs/2608.10715 (P)
- Yakura u. a.: Empirical evidence of Large Language Model's influence on human spoken communication. 2025. https://arxiv.org/abs/2409.01754 (P)
- Graphite: AI Tells und Opus 5.5 Update, September und Oktober 2026, zusammengefasst unter https://blog.pebblous.ai/report/opus-5-5-em-dash-ai-tells-drift/en/ (A, Sekundärquelle)

Überarbeitung und Qualität

- Chakrabarty, Laban und Wu: Can AI writing be salvaged? Mitigating Idiosyncrasies and Improving Human-AI Alignment in the Writing Process through Edits. CHI 2025. https://arxiv.org/abs/2409.14509 (B)
- Shaib u. a.: Measuring AI „Slop“ in Text. 2025. https://arxiv.org/abs/2509.19163 (P)
- Paech u. a.: Antislop. ICLR 2026. https://arxiv.org/abs/2510.15061 (B)

Erkennung durch Menschen und Detektoren

- Russell, Karpinska und Iyyer: People who frequently use ChatGPT for writing tasks are accurate and robust detectors of AI-generated text. ACL 2025. https://arxiv.org/abs/2501.15654 (B)
- Fiedler und Döpke: Do humans identify AI-generated text better than machines? Evidence based on excerpts from German theses. International Review of Economics Education 49, 2025. (B)
- Milička u. a.: Studie zum Erlernen der Erkennung tschechischer KI-Texte. 2025. https://arxiv.org/abs/2505.01877 (P)
- Jabarian und Imas: Artificial Writing and Automated Detection. NBER Working Paper 34223, 2025. https://www.nber.org/papers/w34223 (P)
- Karr u. a.: Why AI Detection Fails for Academic Integrity. 2026. https://arxiv.org/abs/2608.11256 (P)
- Liang u. a.: GPT detectors are biased against non-native English writers. Patterns, 2023. https://doi.org/10.1016/j.patter.2023.100779 (B)

Herkunft und Recht

- Anthropic: How Claude marks AI-generated content. Geprüft am 6. November 2026. https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content (A)
- Google: SynthID. https://ai.google.dev/responsible/docs/safeguards/synthid (A)
- OpenAI: EU text provenance. https://openai.com/index/eu-text-provenance/ (A, Seite war beim Abruf nicht lesbar; Inhalt nur aus Suchergebnissen bekannt)
- C2PA-Spezifikation 2.4, Anhang A.8 zu Text. https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html (Standard)
- EU AI Act, Art. 50. https://artificialintelligenceact.eu/article/50/ (R)
- Europäische Kommission: FAQ zum Code of Practice on Transparency of AI-Generated Content. https://digital-strategy.ec.europa.eu/en/faqs/signing-code-practice-transparency-ai-generated-content (R, Erläuterung)
