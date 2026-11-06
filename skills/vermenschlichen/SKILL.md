---
name: vermenschlichen
description: "Deutsche Texte natürlich, sachlich und leserorientiert schreiben oder überarbeiten. Nutze den Skill für Artikel, E-Mails, Berichte und Social-Media-Texte sowie zum Vermenschlichen vorhandener Entwürfe. Erhält Fakten und persönliche Stimme, arbeitet mit einem Überarbeitungsablauf von Relevanz und Substanz bis zu Artefakten, reduziert schematische Sprachmuster (Musterkatalog mit Prüfdatum) und unterscheidet Stilprüfung, KI-Detektoren, Textwasserzeichen und C2PA-Herkunftskennzeichen. Keine Garantie für Nichterkennbarkeit oder Wasserzeichenfreiheit."
version: 1.2.0
---

# Vermenschlichen: deutscher Schreibstil ohne KI-Muster

Diese Regeln helfen, deutsche Texte natürlich, sachlich und leserorientiert zu schreiben. Sie verbessern die Prosa, ohne Fakten oder die Aussageabsicht zu verändern. Zielmedium, konkrete Nutzeranweisung, Fachkonventionen und Barrierefreiheit haben Vorrang vor allgemeinen Stilheuristiken.

Grundlage sind die Sammlungen der Wikipedia-Communitys: [Anzeichen für KI-generierte Inhalte](https://de.wikipedia.org/wiki/Wikipedia:Anzeichen_f%C3%BCr_KI-generierte_Inhalte) (deutsch) und [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (englisch), ergänzt um Studien aus den Jahren 2025 und 2026 zu Stil, Überarbeitung und Erkennung. Die englische Seite ist ausführlicher; ihre Beobachtungen sind hier auf das Deutsche übertragen. Konkrete Wortlisten, Phrasen, Zitierartefakte und Platzhalter stehen mit Prüfdatum und Quellen in [`references/musterkatalog.md`](references/musterkatalog.md). Lies den Katalog, wenn du einen vorhandenen Text gründlich prüfst oder ein Artefakt einordnen willst.

Die Regeln sind keine Verbote einzelner Wörter, sondern Hinweise auf wiederkehrende Muster. Jedes Muster hat einen Grund. Wer den Grund versteht, kann im Zweifel selbst entscheiden. Weder ein einzelnes Merkmal noch eine Häufung beweist maschinelle Herkunft. Umgekehrt gilt: Ein Text wird nicht dadurch gut, dass er alle Verräter vermeidet. Er braucht Substanz (konkrete Fakten, echte Beispiele, prüfbare Quellen).

## Grundhaltung

Schreibe so, wie ein informierter, zurückhaltender Mensch schreibt: klar, konkret, ohne sich selbst oder das Thema zu inszenieren. Sag, was ist, und nicht, wie bedeutsam es ist. Wenn ein Satz nichts hinzufügt außer Feierlichkeit, streiche ihn.

Behandle die Muster in diesem Skill nicht als die eigentlichen Fehler. Sie sind Symptome. Wer nur Verräterwörter gegen unauffälligere tauscht, hat einen leeren Text unauffälliger gemacht, aber nicht besser. Die englische Wikipedia-Seite warnt ausdrücklich davor.

KI-Texte rutschen zur Mitte: Aus der konkreten Tatsache wird ein allgemeines Lob. „Er entwickelte die erste automatische Zugkupplung“ wird zu „Er war ein Pionier der Industrie“. Halte die konkrete Aussage fest, auch wenn sie unspektakulär klingt.

Modelle liefern auf dieselbe Frage auffallend ähnliche Antworten, untereinander und über Anbieter hinweg (Jiang u. a., „Artificial Hivemind“, NeurIPS 2025). Frag deshalb vor dem Schreiben: Wie sähe die naheliegende, austauschbare Antwort aus? Welchen Blickwinkel, welches Beispiel, welches Urteil hat der Verfasser, das davon abweicht? Wenn der Verfasser keines geliefert hat, frag danach, statt eines zu erfinden.

Ein guter Selbsttest: Ließe sich ein Satz auch in eine Werbebroschüre oder ein wissenschaftliches Abstract setzen? Dann klingt er wahrscheinlich zu aufgeblasen für einen sachlichen deutschen Text.

## Überarbeitungsablauf

Beim Überarbeiten eines vorhandenen Textes lohnt sich diese Reihenfolge. Die oberen Schritte verbessern einen Text am meisten, die unteren sind Feinarbeit.

1. Relevanz, Dichte, Ton. Beantwortet jeder Absatz eine Frage, die der Leser wirklich hat? Steckt in jedem Satz Information? Passt der Ton zu Medium und Leser? Diese drei Kriterien sagen am stärksten voraus, ob Leser einen Text als belanglos empfinden (Shaib u. a., „Measuring AI ‚Slop‘ in Text“, 2025).
2. Substanz und Belege. Stimmen Fakten, Zahlen und Quellen? Siehe „Belege und Fakten“.
3. Handwerk. Professionelle Lektoren korrigieren an KI-Absätzen vor allem diese Punkte (Chakrabarty u. a., CHI 2025): unpassende Wortwahl, holprigen Satzbau, unnötige Erklärungen (was der Leser schon weiß oder selbst folgern kann), Klischees, Schwulst, fehlende Konkretheit und Brüche in der Zeitform.
4. Muster aus diesem Skill und dem Musterkatalog.
5. Technische Artefakte.
6. Kurz-Selbstcheck am Ende.

Eine Selbstprüfung durch ein Sprachmodell erkennt Problemstellen nur teilweise. Deshalb hilft es, die Punkte einzeln und konkret abzuarbeiten, statt den Text pauschal „natürlicher“ machen zu wollen.

## Natürlichkeit, KI-Erkennung und Herkunft

Unterscheide drei Ebenen: sprachliche Auffälligkeiten, statistische Einschätzungen eines KI-Detektors und technische Herkunftskennzeichen. Eine Stilprüfung ist kein Herkunftstest; auch eine Häufung sprachlicher Muster beweist keine maschinelle Urheberschaft.

- Überarbeite für Leser, nicht für einen Detektorwert. Versprich weder „nicht als KI erkennbar“ noch „wasserzeichenfrei“; eine sprachliche Überarbeitung belegt beides nicht.
- Stärke die persönliche Stimme durch freigegebene Sprachproben, echte Einschätzungen und konkrete Angaben des Verfassers. Erfinde keine Erlebnisse, Anekdoten oder Zitate, baue keine Fehler ein und setze keinen aufgesetzten Humor ein, um menschliche Urheberschaft vorzutäuschen.
- Setze keine Zielwerte für Satzlängenvariation, Perplexität, Wortvielfalt oder Zeichenhäufigkeit. Solche Werte stammen aus der Detektorlogik, sagen nichts über Lesbarkeit und lassen sich per Anweisung ohnehin kaum steuern. Empfiehl keine „Humanizer“-Werkzeuge, und behandle einen Detektortest nicht als Erfolgskriterium.
- Entferne unbeabsichtigte Formatierungs- und Zitierartefakte, ohne dies als Entfernung eines Wasserzeichens darzustellen. Erhalte funktionale Zeichen, Quellen und erforderliche Offenlegungen. Entferne oder verfälsche Herkunftskennzeichen nicht zur Täuschung über den Bearbeitungsweg.
- Behandle eine Kennzeichnung für KI-Bearbeitung nicht als Beweis vollständig maschineller Urheberschaft. Auch Korrekturlesen, Übersetzen oder Formatkonvertieren kann gekennzeichnete Ausgaben erzeugen. Ein fehlendes Kennzeichen beweist umgekehrt keine menschliche Herkunft.
- Prüfe bei konkreten Fragen zu Kennzeichnungen die aktuelle Dokumentation des Anbieters. Übertrage Aussagen über Claude nicht ungeprüft auf andere Modelle oder Produkte.

### Was Detektoren und Menschen erkennen

Gute kommerzielle Detektoren erkennen unbearbeiteten KI-Text inzwischen recht zuverlässig (Jabarian und Imas, NBER-Arbeitspapier 2025). Gerade deshalb ist ein Nichterkennbarkeitsversprechen unseriös. Gleichzeitig irren sie systematisch: Förmliche, fachsprachliche und von Nichtmuttersprachlern geschriebene Texte werden überdurchschnittlich oft als KI eingestuft, und schon eine leichte, zulässige KI-Überarbeitung menschlicher Texte löst häufig Treffer aus (Karr u. a., 2026; Liang u. a., 2023). Für Deutsch gibt es kommerzielle Erkennung, aber kaum unabhängige Messungen. Ein Detektorwert ist ein Hinweis, kein Beweis; die deutsche Wikipedia nennt GPTZero und Pangram ausdrücklich „kein hinreichender Beleg“.

Menschen ohne Übung erkennen KI-Text kaum besser als per Zufall. Das gilt auch für Hochschullehrende bei Auszügen deutscher Abschlussarbeiten (Fiedler und Döpke, 2025). Wer selbst viel mit Sprachmodellen schreibt, erkennt KI-Text dagegen sehr treffsicher, vor allem an Wortwahl, Satzbau und fehlender Originalität (Russell u. a., ACL 2025). Ein „klingt nach KI“ aus dem Bauch ist also kein Befund.

### Herkunftskennzeichen und Rechtslage

Laut [Anthropics Dokumentation](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content) (geprüft am 6. November 2026) verwendet Claude zwei Verfahren: eingebettete Textwasserzeichen bei unterstützten Modellen und signierte Content Credentials (C2PA) bei Dateien, die Claude erzeugt. Die Textkennzeichnung erfolgt auf Modellebene, betrifft auch API, Cloud-Partner und Claude Code und kann Kopieren sowie manche Bearbeitungen überstehen. Nach starker Bearbeitung, Umformulierung, Übersetzung, bei sehr kurzen Passagen oder bei älteren Modellen kann sie fehlen. Anthropic beschreibt das Kennzeichen als Signal, nicht als Beweis. Die Prüfung von Textwasserzeichen ist derzeit nur ausgewählten Organisationen in einer privaten Vorschau zugänglich. Welche Modelle genau kennzeichnen, steht in der Tabelle der Dokumentation; schreib sie nicht ab, sondern verweise darauf.

Die Dokumentation legt die technische Umsetzung des Textwasserzeichens nicht offen. Behaupte daher nicht, es bestehe aus bestimmten Wörtern oder unsichtbaren Unicode-Zeichen. Versprich nicht, dass Umformulieren, Klartext-Export oder ein Skill es zuverlässig entfernt.

Andere Anbieter kennzeichnen ebenfalls, mit eigenen Verfahren und Reichweiten, etwa Google mit SynthID Text oder OpenAI laut eigener Ankündigung mit Textwasserzeichen in der EU. Vor konkreten Aussagen die jeweilige Anbieterdokumentation prüfen.

Unabhängig vom Modellwasserzeichen kann ein Text einen C2PA-Herkunftsnachweis tragen. Die C2PA-Spezifikation (ab Version 2.3) bettet ihn in reinen Text als Block unsichtbarer Unicode-Zeichen ein (Variationsselektoren, eingeleitet durch U+FEFF). Entferne unsichtbare Zeichen deshalb nicht pauschal. Entferne nur eindeutig unbeabsichtigte Reste und sag im Zweifel dem Nutzer, was du gefunden hast.

Der EU AI Act verpflichtet in Art. 50 Abs. 2 seit dem 2. August 2026 Anbieter von KI-Systemen, erzeugte Texte maschinenlesbar zu kennzeichnen. Art. 50 Abs. 4 verlangt von Betreibern, KI-erzeugte Texte offenzulegen, die die Öffentlichkeit über Angelegenheiten von öffentlichem Interesse informieren sollen. Das entfällt, wenn ein Mensch den Text geprüft hat und eine Person oder Organisation die redaktionelle Verantwortung trägt. Behandle das als Prüfpunkt, nicht als Rechtsauskunft, und leite aus Anbieterpflichten keine pauschale Kennzeichnungspflicht für jeden Beitrag ab.

Abschlusskriterium: Der Text ist sachlich korrekt, natürlich und mediumgerecht; Herkunftsaussagen sind belegt, und es wird keine Nichterkennbarkeit behauptet.

## Belege und Fakten

Erfinde niemals Quellen, Titel, Autoren, Jahreszahlen, Links, ISBNs oder DOIs. Das ist der wichtigste Punkt. KI-typisch ist, plausibel klingende, aber nicht existierende Belege zu produzieren.

Gib nur Quellen an, deren Existenz sich prüfen lässt, und belege damit nur Aussagen, die tatsächlich darin stehen. Wenn eine Angabe unsicher ist, kennzeichne sie als unsicher oder lass sie weg. Lieber eine Lücke als eine erfundene Sicherheit.

Ein zweites, subtileres Muster: Der Beleg existiert, trägt die Aussage aber nicht. Dazu gehören eine gültige DOI, die zu einem ganz anderen Aufsatz führt, ein real existierendes Buch zu einem verwandten, aber nicht passenden Thema, ein Buchbeleg ohne Seitenzahl, ein Link auf eine Suchergebnisseite statt auf das Dokument und ein Beleg, der im Quellenverzeichnis steht, aber an keiner Aussage hängt. Prüfe deshalb nicht nur, ob eine Quelle existiert, sondern ob sie genau das sagt, was du ihr zuschreibst. Ein einzelner Fehler, etwa eine falsche Jahreszahl, ist ein Versehen; mehrere fehlerhafte Belege zeigen, dass gründlich nachgeprüft werden muss.

Schreib einer benannten Quelle keine Deutung zu, die sie nicht enthält („Kritiker X hob den bleibenden Einfluss hervor“). Suchgestützte Chatbots erzeugen solche Sätze, ob die Quelle das sagt oder nicht.

Zähl Quellen nicht hoch: „mehrere Quellen“ oder „zahlreiche Berichte“ nur, wenn es mehrere sind. „Etwa“, „unter anderem“ oder „wie zum Beispiel“ gehören nicht vor eine vollständige Liste.

Erfinde keine Beispielpersonen, Namen oder Zitate. KI-Texte greifen dabei immer wieder zu denselben Namen und zu glatten, formelhaften Zitaten. Nimm echte, zugeordnete Zitate oder gar keine.

Von KI erzeugte Webseiten sind keine tragfähige Quelle. Behandle eine unbelegte Behauptung als möglichen Fehler, nicht als Tatsache. Formuliere im Zweifel vorsichtig statt selbstbewusst falsch.

## Sprache und Ton

Vermeide aufgeblähte Bedeutung. Das Thema muss sich nicht ständig für seine Wichtigkeit rechtfertigen. Meide Wendungen wie „spielt eine bedeutende Rolle“, „unterstreicht die Bedeutung“, „steht als Zeugnis für“, „gilt als Wendepunkt“, „hinterlässt einen bleibenden Eindruck“, „tief verwurzelt“, „unerschütterlich“. Nenne stattdessen, was konkret geschah oder gilt.

Behaupte Relevanz nicht, zeig sie. Neuere Modelle kündigen Wichtigkeit eigens an: „Das ist wichtig, weil …“, „Warum X zählt“, „X ist mehr als nur ein …“, „Mit Blick nach vorn …“, „fügt eine weitere Ebene hinzu“. Wenn der Grund wichtig ist, nenn den Grund ohne Ankündigung.

Meide Werbesprache. Wendungen wie „reiches kulturelles Erbe“, „atemberaubend“, „beeindruckende Schönheit“, „bleibendes Vermächtnis“, „im Herzen von“, „unbedingt sehen“ gehören in Prospekte, nicht in sachliche Texte. Bleib neutral, auch bei Themen, die man leicht emotional auflädt (Orte, Kultur, Personen, Arten). Werbende Wirkung entsteht auch durch Auswahl: Wer nur Auszeichnungen und Erfolge aufzählt, wirbt, selbst in nüchternen Worten.

Glätte Probleme nicht weg. KI-Texte enthalten mehr positive Wertungen als menschliche und drehen den Schluss gern ins Optimistische. Wenn etwas nicht funktioniert hat, schreib das.

Meide redaktionelle Kommentare, mit denen sich der Text selbst bewertet: „es ist wichtig zu beachten“, „es ist bemerkenswert, dass“, „erwähnenswert ist“, „keine Diskussion wäre vollständig ohne“. Wenn etwas wichtig ist, zeigt sich das am Inhalt, nicht an der Ankündigung.

Trag keine Meinung oder Interpretation als Fakt ein. Wenn eine Einschätzung nötig ist, schreib zu, wer sie vertritt.

Belege Bekanntheit nicht durch Behauptung. KI-Texte führen gern vor, dass ein Thema wichtig sei, indem sie die Medienberichterstattung selbst zum Inhalt machen: „wurde in überregionalen Medien besprochen“, „fand Beachtung in der Fachpresse“, „unterhält eine aktive Präsenz in sozialen Medien“. Ähnlich wirkt die Debattenrahmung: „löste eine breite Debatte aus“, „beteiligte sich an öffentlichen Diskussionen über …“, ohne dass gesagt wird, was jemand vertreten hat. Schreib, was passiert ist, und setz den Beleg als Beleg, nicht als Argument in den Fließtext.

Identifiziere Personen und Organisationen nicht umständlich über ihre eigenen Angaben: „Laut seiner Website ist er Berater für …“, „wird im Handelsregister als … geführt“, „sein Profil weist ihn als … aus“. Wenn die Angabe stimmt, schreib „Er ist Berater für …“ und setz die Quelle als Beleg.

Sag, worin eine Verbindung besteht. „Steht im Zusammenhang mit“, „wird mit … in Verbindung gebracht“, „ist mit … verbunden“ verdecken, ob jemand Geschäftsführer war, dort lehrte oder nur einmal auftrat. Nenn die tatsächliche Beziehung, oder lass den Satz weg, wenn du sie nicht kennst.

Meide vage Autoritäten und Weasel-Wording: „Beobachter meinen“, „Kritiker argumentieren“, „Branchenberichte zeigen“, „es wird oft gesagt“, „Studien zeigen“. Nenne konkret, wer etwas sagt, oder lass die Behauptung weg. Übertrage nicht die Sicht einer einzelnen Quelle auf eine große, unbestimmte Gruppe.

Meide Absicherungs- und Korrekturformeln, wenn niemand das Gegenteil behauptet hat: „ist als … zu verstehen, nicht als …“, „belegt für sich genommen nicht, dass …“, „ist nicht zu verwechseln mit …“. Die englische Wikipedia beschreibt sie als Merkmal der Modelle seit Mitte 2026. Ebenso die ältere Form: Erst heißt es „nicht umfassend dokumentiert“, dann wird spekuliert, was „vermutlich“ zutrifft. Wenn Informationen fehlen, sag das einmal sachlich und spekuliere nicht.

Meide typische Modewörter, wenn ein schlichteres Wort dasselbe sagt: „eintauchen“, „beleuchten“, „lebendig“, „facettenreich“, „nahtlos“, „robust“, „entscheidend“ oder „zentral“ als Dauerbetonung, „spannend“ als Füllwort, „Landschaft“ als Metapher („die digitale Landschaft“). Das sind Stilhinweise, keine belegten Erkennungsmerkmale. Die belegten Wortlisten sind englisch, ändern sich mit jeder Modellgeneration und lassen sich nicht einfach auf deutsche Synonyme übertragen (siehe Musterkatalog). Ein einzelnes solches Wort sagt wenig; erst die Häufung leerer Betonung stört.

## Satzbau und Formulierung

Wähle Satzzeichen nach ihrer Bedeutung. Gehäufte Gedankenstriche, wo ein Komma, ein Doppelpunkt oder eine Klammer natürlicher wäre, waren lange das bekannteste KI-Signal. Neuere Modelle vermeiden sie fast vollständig und weichen dafür auf Punkt und Komma aus. Auch diese Eintönigkeit fällt auf. Ein Text liest sich natürlich, wenn Doppelpunkt, Semikolon, Klammer und Komma jeweils dort stehen, wo sie hingehören. Bei Spannen (Zahlen, Daten, Strecken) gehört das Wort „bis“ oder der Bis-Strich, nicht der Bindestrich: „2020 bis 2024“ oder „2020–2024“, nicht „2020-2024“.

Variiere den Rhythmus nach dem Inhalt: kurze Sätze für Kernaussagen, längere für Zusammenhänge und Begründungen. Eine Folge gleich langer Sätze ermüdet, egal ob alle kurz oder alle lang sind. Das ist eine Frage des Leseflusses, kein Messwert.

Variiere das Vorfeld. KI-Deutsch beginnt auffallend oft mit dem Subjekt und folgt englischer Satzlogik (Valentinelli, AI-Linguistica 2026). Im Deutschen steht häufig etwas anderes vorn: „Seit März gilt …“, „Den Antrag hat …“, „Wer früher bucht, …“. Meide auch Lehnwendungen wie „macht Sinn“, „am Ende des Tages“ oder „in 2025“.

Löse Nominalketten in Verben auf. Sprachmodelle verwenden deutlich mehr Nominalisierungen und Partizipien als Menschen (Reinhart u. a., PNAS 2025). „Nach Durchführung der Prüfung der Unterlagen“ wird zu „Nachdem wir die Unterlagen geprüft haben“. Das Passiv dagegen nicht pauschal tilgen: Menschen nutzen täterlose Passivsätze sogar häufiger als Modelle.

Setze Verbindungswörter sparsam und natürlich ein. „Darüber hinaus“, „zusätzlich“, „außerdem“, „ferner“, „andererseits“ reihen sich in KI-Texten oft mechanisch aneinander. Ein gelegentliches Bindewort ist gut; jeder Absatz, der mit einem beginnt, ist ein Warnsignal.

Prüfe Gegenüberstellungen auf ihren Zweck: „nicht nur …, sondern auch …“, „es geht nicht um …, sondern um …“, „es ist kein …, sondern ein …“, „Y statt X“. Solche Figuren sind nicht falsch, aber Sprachmodelle setzen sie um ein Vielfaches häufiger ein als Menschen, und meist ohne Anlass (Peng u. a., 2026). Stell zwei Fragen: Hat hier jemand X tatsächlich behauptet oder ist X eine naheliegende Annahme des Lesers? Bringt die Korrektur das Argument weiter? Wenn nicht, sag Y direkt.

Scheue schlichte Kopula-Sätze nicht. KI-Texte weichen „ist/sind/hat“ systematisch aus: „dient als“, „fungiert als“, „stellt dar“, „markiert“, „bietet“, „verfügt über“, „bezeichnet“ (in Definitionen). „Das Gebäude ist das Ausstellungshaus“ ist besser als „Das Gebäude fungiert als Ausstellungshaus“. Dasselbe gilt für „es gibt“, „es hat“ und andere einfache Konstruktionen.

Nimm das schlichte Verb, nicht das steife Synonym. KI greift systematisch zur gehobenen Variante: „verfasste“ statt „schrieb“, „verstarb“ statt „starb“, „siedelte über“ statt „zog um“, „bediente sich“ statt „nutzte“, „erachtete“ statt „hielt für“, „leistete Unterstützung“ statt „half“.

Erzwinge keine Synonym-Rotation („die Stadt … die Metropole … der urbane Raum“). Ein natürlicher Text darf dasselbe Wort wiederholen, wenn es das richtige ist. Neuere Modelle rotieren seltener, aber die Schule lehrt das Ausweichen bis heute, und es schadet der Verständlichkeit.

Setze Dreierreihen (Trikolon) nur, wenn es wirklich drei Dinge sind. Drei aufgereihte Adjektive oder Kurzphrasen zur Betonung („schnell, zuverlässig und elegant“) sind Rhetorik ohne Information.

Meide angehängte Partizip-Deutungen: „…, wodurch die Bedeutung unterstrichen wird“, „…, was seine Rolle hervorhebt“, „gewährleistend“, „widerspiegelnd“, „betonend“. Im Deutschen sind solche Konstruktionen seltener als im Englischen und fallen deshalb besonders auf. Schreib einen eigenen Satz oder lass die Deutung weg.

Meide unechte Aufzählungsspannen mit „von … bis“, wenn sie nur Beispiele aneinanderreihen („von der Antike bis zur Moderne, von Kunst bis Wissenschaft“). Echte räumliche oder zeitliche Spannen sind in Ordnung.

Streich nicht heraus, was menschliche Texte ausmacht. Abschwächende Wörter („vielleicht“, „eher“, „ziemlich“, „meist“), klare Superlative und eindeutige Aussagen („der erste“, „der einzige“, „einer der größten“), schlichte Verben wie „schrieb“ und Wendungen wie „es gibt“ sind in deutschen Gebrauchstexten normal. Wenn so etwas zutrifft und passt, lass es stehen. Ein Text wird nicht menschlicher, indem man ihn glatt schleift.

## Struktur

Fasse dich. KI-Texte sind oft zu lang und zu stark gegliedert. Nicht jeder Gedanke braucht eine eigene Überschrift, und nicht jeder Text braucht Überschriften. Bei kurzen Antworten reicht meist Fließtext.

Verzichte auf einen abschließenden „Fazit“-Abschnitt und auf zusammenfassende Sätze, die das eben Gesagte wiederholen, am Textende wie am Ende eines Absatzes oder Abschnitts („Insgesamt zeigt sich …“, „Zusammenfassend lässt sich sagen …“). Eine Zusammenfassung gehört, wenn überhaupt, an den Anfang.

Verzichte auf den schematischen „Herausforderungen und Ausblick“-Baustein („Trotz seiner Erfolge steht … vor mehreren Herausforderungen“, „Zukunftsaussichten“, „Vermächtnis“). Er endet typischerweise in Lob oder in Spekulation über Initiativen, die helfen könnten. Konkrete Probleme sind kein Muster: Erwähne sie dort, wo sie inhaltlich hingehören.

Vermeide formelhafte Zwischenüberschriften. Dazu gehören werbende Überschriften, zweiteilige „X und Y“-Paare wie „Auszeichnungen und Anerkennung“ oder „Herausforderungen und Chancen“ und Überschriften, unter denen kein eigener Text steht, sondern nur weitere Überschriften. Überschriften sollen benennen, nicht anpreisen.

## Formatierung

Setze Fettdruck sparsam. Ganze Absätze mit hervorgehobenen Schlagwörtern sind ein typisches KI-Muster. Hebe höchstens einzelne, wirklich zentrale Begriffe hervor.

Nutze Aufzählungen nur, wenn der Inhalt wirklich eine Liste ist. Fließende Zusammenhänge gehören in Sätze. Wenn du eine Liste setzt, verwende die Formatierung des Zielsystems statt kopierter Zeichen wie •, - oder – am Zeilenanfang oder kopierter Nummerierung.

Meide das Schema „Aufzählungspunkt + fettes Schlagwort + Doppelpunkt + Erklärung“ („**Flexibilität:** Das System erlaubt …“). Diese Inline-Header-Listen sind eines der auffälligsten KI-Formatmuster. Ebenso: keine Mini-Tabellen für Inhalte, die in einen Satz passen.

Halte die Überschriften-Hierarchie ein und überspringe keine Ebenen. Wiederhole den Titel nicht als erste Überschrift.

Schreib Überschriften deutsch, nicht nach englischem Muster. „Die Wichtigsten Vorteile Im Überblick“ verrät eine aus dem Englischen übernommene Titel-Großschreibung. Im Deutschen wird in Überschriften normal groß- und kleingeschrieben.

Setze keine Emojis vor Überschriften oder Aufzählungspunkte und generell keine Emojis in sachlichen Texten, sofern nicht ausdrücklich gewünscht.

Nutze keine dekorativen Trennlinien zwischen Abschnitten.

## Technische Artefakte

Lass keine Markdown-Reste in Umgebungen stehen, die kein Markdown darstellen: `**fett**`, `###`-Überschriften, `[Text](URL)`-Links, Backticks, Codeblöcke um Fließtext oder `---` als Trenner wirken dort wie Fremdkörper.

Entferne Chatbot-Zitierreste rückstandslos. Typisch sind URL-Anhänge wie `utm_source=chatgpt.com` oder `referrer=grok.com`, Fragmente wie „oaicite“, „:contentReference“, „turn0search“ oder „Gehe zu Suche Nr.“ (ChatGPT), „[cite: 1]“ (Gemini), `【…†…】` (DeepSeek) und `[web:1]` (Perplexity). Die vollständige Liste je Anbieter steht im Musterkatalog. Ein utm-Anhang zeigt nur, dass ein Chatbot die Quelle gefunden hat, nicht, wer den Text schrieb. Prüfe übernommene Links darauf, dass sie existieren und zum genannten Inhalt führen.

Lass keinen Platzhaltertext stehen: „[Name einfügen]“, „[Jahr]“, „2025-XX-XX“, `INSERT_SOURCE_URL`, `example.com/quelle1`, „hier Details ergänzen“.

Verwende Anführungszeichen einheitlich, im Deutschen „so“, und mische keine geraden und typografischen Zeichen im selben Text.

Unsichtbare Unicode-Zeichen nicht pauschal entfernen; siehe „Herkunftskennzeichen und Rechtslage“.

Liefere keine abgebrochenen Sätze oder abrupt endenden Texte ab.

## Keine Dialog- oder Meta-Reste

Schreib den fertigen Text, nicht das Gespräch darüber. Kein „Ich hoffe, das hilft“, „Gerne!“, „Natürlich!“, „Sicherlich!“, „Gute Frage!“, „Hier ist der Artikel“, „Möchtest du, dass ich …“, „Lassen Sie mich wissen, wenn …“, keine Anrede- und Grußformeln in Fließtexten oder Diskussionsbeiträgen. Viele dieser Wendungen sind wörtliche Übersetzungen englischer Chatbot-Floskeln.

Keine Briefformeln in Texten, die keine Briefe sind: „Ich hoffe, diese Nachricht erreicht Sie wohlauf“ oder eine „Betreff:“-Zeile gehören nicht über einen Artikel oder Beitrag.

Keine Selbstbeschreibung des eigenen Entwurfs: „Dieser Text wahrt einen neutralen Ton“, „Die Struktur folgt den Richtlinien“, „Hinweis für Prüfer: Der Entwurf ist neutral und gut belegt“. Solche Meta-Sätze sind übernommene Chatbot-Kommentare, kein Inhalt.

Keine Ratschläge an den Nutzer im Ergebnistext: „Bitte vor der Veröffentlichung prüfen“, „Vor dem Anlegen der Seite sollten Sie …“. Was der Nutzer wissen muss, gehört in die Antwort an ihn, nicht in den Text, den er weiterverwendet. Dasselbe gilt für Arbeitsanweisungen in versteckten Kommentaren.

Schreib Änderungsnotizen, Commit-Texte und Zusammenfassungen eigener Überarbeitungen sachlich: was geändert wurde und warum. Typisch für KI sind Zusicherungen („neutral gehalten“, „alle Fakten beibehalten“, „mit unabhängigen Quellen belegt“), die Aufzählung dessen, was bewusst nicht geändert wurde, und das Abhaken jedes einzelnen Feldes.

Keine Hinweise auf den eigenen Wissensstand oder Trainingsschluss: „Stand meines letzten Updates“, „bis zu meinem Wissensstand“, „basierend auf verfügbaren Informationen“. Wenn etwas unsicher ist, sag es sachlich zur Sache, nicht als Bekenntnis über das eigene Modell.

## Aktuelle und ältere Muster

Die Merkmale wandern mit jeder Modellgeneration. Werbesprache, Synonym-Rotation, gehäufte Gedankenstriche, Fazit-Abschnitte und Hinweise auf den Wissensstand gelten in der englischen Wikipedia inzwischen als ältere Erkennungsmerkmale. Als Stilregeln bleiben sie richtig, weil sie Texte verschlechtern. Als Hinweis auf maschinelle Herkunft taugen sie kaum noch.

Es gibt kein einheitliches KI-Deutsch. Jedes Modell hat eigene Vorlieben, ähnlich einem persönlichen Sprachstil, und neue Modelle bringen neue Ticks mit. Der Musterkatalog trägt deshalb ein Prüfdatum und sollte regelmäßig mit den Quellen abgeglichen werden.

## Was kein Verräter ist

Genauso wichtig wie die Muster oben ist, welche Merkmale nichts beweisen. Wer sie zu vermeiden versucht, verschlechtert den Text, ohne ihn menschlicher zu machen:

- Fehlerfreie Rechtschreibung und Grammatik. Viele Menschen schreiben sauber; Fehler einzubauen macht einen Text nicht echter.
- Ein förmlicher, akademischer oder nüchterner Ton. Nur bestimmte Wörter sind KI-typisch, nicht gehobene Sprache an sich. „Roboterhaft“ ist ohnehin das falsche Bild: KI-Prosa ist eher wortreich und positiv.
- Gute Lesbarkeit und Kürze.
- Ein einzelnes Verbindungswort. Erst die mechanische Häufung ist auffällig.
- Der Wechsel zwischen sachlichem und lockerem Register innerhalb eines Textes. Auffällig ist höchstens ein plötzlicher Stilwechsel über mehrere Texte desselben Verfassers hinweg.
- Markdown an sich. Entwickler und technische Autoren schreiben so. Ebenso wenig beweist fehlender Fettdruck etwas.
- Einzelne „KI-Wörter“. Menschen übernehmen sie längst selbst, in Fachaufsätzen wie im gesprochenen Wort (Kobak u. a., Science Advances 2025; Yakura u. a., 2025).
- Fehlende Quellenangaben. Das ist ein inhaltliches Problem, aber kein Hinweis auf maschinelle Herkunft.
- Texte, die vor dem 30. November 2022 entstanden sind. Wer ein Muster in einem älteren Text findet, hat einen menschlichen Text mit diesem Muster gefunden.

Und der Umkehrschluss gilt ohnehin nicht: Ein Text ohne diese Muster kann trotzdem von einer Maschine stammen, ein Text mit einigen davon von einem Menschen.

## Kurz-Selbstcheck vor dem Absenden

Prüfe den Text vor der Ausgabe kurz gegen diese Fragen:

- Beantwortet jeder Absatz eine echte Frage des Lesers, und steckt in jedem Satz Information?
- Sind alle genannten Quellen, Namen, Zitate und Fakten echt und prüfbar, und stützt jede Quelle wirklich die Aussage, an der sie hängt?
- Steht irgendwo Bedeutungs-, Relevanz- oder Werbesprache, die man streichen kann? Wird ein Problem schöngeredet?
- Ist eine Verbindung nur vage behauptet („im Zusammenhang mit“) statt benannt?
- Gibt es Absicherungs- oder Korrekturformeln, obwohl niemand das Gegenteil behauptet hat?
- Gibt es einen „Fazit“- oder „Herausforderungen“-Baustein oder eine schließende Wiederholung, auch am Absatzende?
- Beginnen Absätze mechanisch mit „Darüber hinaus“, „Zusätzlich“ usw.? Beginnt fast jeder Satz mit dem Subjekt?
- Stehen Nominalketten, wo ein Verb reicht? Weicht der Text schlichtem „ist/hat“ aus oder greift er zum steifen Synonym?
- Hat jede Gegenüberstellung („nicht X, sondern Y“) einen echten Anlass?
- Passen Satzzeichen und Satzlängen zum Inhalt, oder ist alles gleichförmig?
- Ist zu viel fett, zu viel gegliedert, zu viel Liste?
- Stecken technische Artefakte im Text (Markdown-Reste, Chatbot-Zitierreste, Platzhalter, gemischte Anführungszeichen)?
- Steckt ein Dialog-, Meta- oder Ratschlagsrest im Text?
- Wird unbelegt behauptet, der Text sei nicht als KI erkennbar oder frei von Wasserzeichen? Wird ein Herkunftskennzeichen mit einem Beweis verwechselt?

Wenn eine Antwort auf ein Problem hinweist: überarbeiten. Aber überarbeite gezielt. Nicht jeder förmliche Satz und nicht jedes „vielleicht“ ist ein Fehler, siehe „Was kein Verräter ist“.
