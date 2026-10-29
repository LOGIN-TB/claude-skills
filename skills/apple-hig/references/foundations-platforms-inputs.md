# Apple HIG — Grundlagen, Plattformen und Eingaben

## Abdeckung und Verwendung

Primärquellen: am 29. Oktober 2026 abgerufene Apple-DocC-Daten; vollständiges Inventar siehe `source-map.md`. Rekursiv ausgewertet wurden alle **43 Seiten** unter `getting-started`, `foundations` und `inputs`, einschließlich der drei Übersichten. Jede Seite erhält unten genau einen Themenblock mit ihrer tatsächlichen Manifest-URL. **Apple-Empfehlung** paraphrasiert die Quelle; **Engineering-Ableitung** bezeichnet eigene Umsetzungsvorschläge, nicht zusätzliche Apple-Vorgaben. Pro Originalseite bleibt der gesamte Themenblock unter 150 Wörtern.

**Grenzen:** Diese Referenz dokumentiert den recherchierten Snapshot, keine erneute Live-Verifikation. Insbesondere neuartige Geräte-/API-Angaben wie iPhone Duo und Touch-Mac sind quellenstandsabhängig, nicht eigenständig verifizierte Produktverfügbarkeiten. Vor Implementierung SDK, OS-Version, Hardwarefähigkeit und API-Verfügbarkeit prüfen. Verlinkte externe Entwicklerdokumentation, Videos und HIG-Bereiche außerhalb der drei Teilbäume sind nicht vollständig untersucht. Bilder/Animationen wurden nicht visuell bewertet. Die Textableitung lässt Tabellen und manche Inline-Code-/Linktexte aus; verwendete Maße wurden deshalb im Original-JSON kontrolliert. Vollständige Typografiestil-, Asset- und Gestentabellen werden bewusst nicht reproduziert.

**Zahlen nicht vereinheitlichen:** Die Accessibility-Control-Tabelle unterscheidet Standard und Minimum; die Spiele-Einstiegsseite formuliert 44×44 pt dagegen pauschaler, während Game Controls häufige und sekundäre Aktionen unterscheidet. Diese Unterschiede bleiben erhalten. Die Accessibility-Kontrasttabelle hat überlappende Angaben zu Schriftgröße und Bold; daraus wird hier keine neue allgemeine Formel abgeleitet. Points, Pixel, Winkel und Meter nicht gleichsetzen. Ungefährwerte und kontextuelle Beispiele sind keine universellen Grenzwerte. HIG-Empfehlungen allein belegen weder WCAG-Konformität noch Sicherheits- oder App-Store-Freigabe.

## Operative Regeln nach Originalseite

### Plattform zuerst

Quelle: [4] https://developer.apple.com/design/human-interface-guidelines/getting-started

**Apple-Empfehlung:** Entwirf für die Konventionen jeder unterstützten Plattform, statt eine Oberfläche unverändert zu portieren.

**Engineering-Ableitung:** Halte vor Implementierung Zielplattformen, Nutzungssituation und primäre Eingaben fest; gemeinsame Geschäftslogik bedeutet nicht identische Navigation.

### Entscheidungsprinzipien

Quelle: [27] https://developer.apple.com/design/human-interface-guidelines/design-principles

**Apple-Empfehlung:** Priorisiere Zweck, Selbstbestimmung, Verantwortung, Vertrautheit, Flexibilität, Einfachheit, handwerkliche Qualität und Freude. Erhalte Kontext, ermögliche Fehlerkorrektur, begründe Datenzugriff und verwende konsistente Rückmeldungen. Einfachheit bedeutet zweckmäßige Konzentration, nicht bloße Reduktion.

**Engineering-Ableitung:** Begründe eigene Komponenten gegenüber Systemkomponenten. Akzeptanzkriterien müssen Kernaufgabe, Rückweg, Fehlererholung, alternative Eingaben und reale Nutzung abdecken; Dekoration darf keine Aufgabe verzögern.

### iOS

Quelle: [29] https://developer.apple.com/design/human-interface-guidelines/designing-for-ios

**Apple-Empfehlung:** Konzentriere die Oberfläche auf Hauptaufgaben; halte Zusatzaktionen leicht auffindbar. Unterstütze Orientierungswechsel, Dark Mode und Dynamic Type. Berücksichtige ein- und beidhändige Nutzung, gut erreichbare mittlere/untere Bereiche sowie vertraute Zurück- und Listen-Wischgesten. Integriere Gerätedaten nur mit Erlaubnis.

**Engineering-Ableitung:** Teste den Hauptablauf einhändig und nach App-Wechsel. Halte Zustand unabhängig von der jeweiligen View-Struktur; ergänze Gesten durch sichtbare Aktionen.

### iPadOS

Quelle: [30] https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados

**Apple-Empfehlung:** Nutze die große Fläche für Inhalte statt zusätzliche Modalität. Unterstütze wechselnde Fensterkonfigurationen, Orientierung und mehrere Eingabeformen einschließlich Pencil, Touch, Tastatur und Zeigegerät; berücksichtige deren Kombination. Gestalte Dichte passend zu Betrachtungsabstand und Eingabe.

**Engineering-Ableitung:** Implementiere adaptive Mehrspaltenansichten, nicht ein vergrößertes iPhone. Teste Größenänderungen während Bearbeitung und Wechsel zwischen Eingabegeräten ohne Funktionsverlust.

### macOS

Quelle: [32] https://developer.apple.com/design/human-interface-guidelines/designing-for-macos

**Apple-Empfehlung:** Nutze größere Flächen, weniger Navigationstiefe und Modalität. Unterstütze frei verwaltbare Fenster, Vollbild, Menüleistenbefehle, Tastaturkürzel, präzise Auswahl und Anpassbarkeit. Der vorliegende Quellenstand behandelt auch Macs mit Touchdisplay: Touch bleibt sekundär; größere Trefferflächen und temporär expandierende Controls sollen die vertraute Dichte erhalten.

**Engineering-Ableitung:** Keine mobile Vollbildnavigation erzwingen. Prüfe Fensterzustände, Menüverfügbarkeit und Tastaturbedienung; Touch-Unterstützung nur nach tatsächlichen Zielgeräte- und SDK-Fähigkeiten implementieren.

### tvOS

Quelle: [33] https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos

**Apple-Empfehlung:** Gestalte für Lesbarkeit aus Raumdistanz, Siri Remote und das systemeigene Fokusmodell. Hervorhebung und Vergrößerung sollen Orientierung erhalten. Unterstütze einfache Anmeldung, gemeinsam verwendete Anmeldung und Profilwechsel beim Wechsel der betrachtenden Person.

**Engineering-Ableitung:** Teste alle relevanten Ansichten ausschließlich mit Fernbedienung, einschließlich Rückweg und langen Inhaltslisten. Verwechsle Fokus nicht mit Aktivierung; prüfe große fokussierte Assets auf Überlappung.

### visionOS

Quelle: [34] https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos

**Apple-Empfehlung:** Wähle die geringste für einen Moment sinnvolle Immersion; Standardaufgaben gehören bevorzugt in Fenster. Halte Inhalte bequem im Sichtfeld, vermeide abrupte Bewegung und unterstütze indirekte Gesten mit ruhenden Händen. Direkte Interaktion nur in Reichweite und nicht über längere Zeit erzwingen.

**Engineering-Ableitung:** Trenne Fenster-, Volumen- und Immersive-Space-Aufgaben ausdrücklich. Prüfe visuelle und körperliche Belastung auf Hardware, nicht nur im Simulator; verlange keine Fortbewegung, um Grundfunktionen zu erreichen.

### watchOS

Quelle: [35] https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos

**Apple-Empfehlung:** Biete kurze, auf einen Blick verständliche Interaktionen und flache Hierarchien. Nutze die Digital Crown für vertikale Navigation, Complications und wertvolle Benachrichtigungen für direkten Nutzen. Die App soll eigenständig funktionieren; Materialien und Hintergrundfarben unterstützen Orientierung.

**Engineering-Ableitung:** Reduziere jeden Bildschirm auf eine unmittelbar erkennbare Aufgabe. Prüfe schnelle Wiederaufnahme und sinnvolle Nutzung ohne geöffnetes iPhone; übertrage nicht die vollständige Desktop-Informationsarchitektur.

### Spiele über Plattformen

Quelle: [28] https://developer.apple.com/design/human-interface-guidelines/designing-for-games

**Apple-Empfehlung:** Ermögliche schnellen Spielbeginn, gute Gerätestandards und Lernen im Spiel. Menüs müssen verschiedene Seitenverhältnisse und Safe Areas berücksichtigen. Unterstütze die primären Eingaben jeder Plattform, gut lesbaren Text und anpassbare Steuerung. Diese Seite fordert für iOS-Buttons mindestens 44×44 pt.

**Engineering-Ableitung:** Behandle Controller als optional, sofern keine ausdrücklich unterstützte Controllerpflicht gewählt wurde. Prüfe Fortschrittserhalt, Unterbrechungen und Menübedienung getrennt vom Gameplay. Die pauschale 44-pt-Aussage dieser Seite nicht mit differenzierteren Control-Tabellen verschmelzen.

### iPhone Duo — quellenstandsabhängig

Quelle: [31] https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo

**Apple-Empfehlung:** Die lokale Seite beschreibt Innen-/Außendisplay, Faltregionen und seitliche Systemleisten. Erhalte Funktion und Zustand über Größenwechsel hinweg; nutze Size Classes, Safe Areas und reservierte Regionen statt Displayabfragen. System-Split-Views passen sich an; Arrangement Views organisieren Inhalte, nicht Navigation. Seitliche Leisten bleiben wegen Hardwarebezug auch in RTL auf derselben Seite.

**Engineering-Ableitung:** Diese Angaben ausdrücklich als Inhalt des gelieferten Snapshots behandeln. Vor Umsetzung genannter APIs deren SDK-Verfügbarkeit prüfen. Teste Falten, Kameraaktivierung, Split View, Toolbar-Overflow und Zustandserhalt; keine eigene Gerätetyp-Heuristik oder ungeprüfte API-Nachbildung.

### Grundlagen als Querschnitt

Quelle: [3] https://developer.apple.com/design/human-interface-guidelines/foundations

**Apple-Empfehlung:** Die Übersichtsseite verknüpft grundlegende Gestaltungsthemen; sie enthält keine eigenständigen Detailmaße.

**Engineering-Ableitung:** Wende die folgenden Regeln gemeinsam an: Ein Layoutentscheid beeinflusst Lesbarkeit, Eingabe, Materialkontrast und Zugänglichkeit. Keine isolierte „Accessibility-Nacharbeit“ nach fertigem Design.

### Accessibility und Control-Größen

Quelle: [8] https://developer.apple.com/design/human-interface-guidelines/accessibility

**Apple-Empfehlung:** Unterstütze alternative Wahrnehmung und Bedienung, aussagekräftige Labels, Untertitel und visuelle Ergänzungen zu Audio. Vergrößerung idealerweise mindestens 200 %, auf watchOS 140 %. Respektiere Reduce Motion; vermeide unnötig zeitgesteuertes Schließen. Teste assistive Technologien mit Accessibility Inspector.

Control-Tabelle aus Original-JSON, jeweils Standard / Minimum:

| Plattform | Größe in pt |
|---|---|
| iOS, iPadOS | 44×44 / 28×28 |
| macOS | 28×28 / 20×20 |
| tvOS | 66×66 / 56×56 |
| visionOS | 60×60 / 28×28 |
| watchOS | 44×44 / 28×28 |

**Engineering-Ableitung:** Standardgrößen bevorzugen; Tabellenminimum ist kein pauschaler Designzielwert. Prüfe reale Trefferflächen, Abstände und alternative Aktionen. Assistive Access nennt doppelte Bestätigung schwer rückgängig machbarer Aktionen ausdrücklich für diesen Modus, nicht für jede Oberfläche.

### App-Icons

Quelle: [13] https://developer.apple.com/design/human-interface-guidelines/app-icons

**Apple-Empfehlung:** Halte Identität und Kernformen über Plattformen und Erscheinungsvarianten konsistent. Liefere unmaskierte Ebenen; das System übernimmt Maskierung und dynamische Effekte. Icon Composer bietet auf iOS, iPadOS, macOS und watchOS Kontrolle über Ebenen; tvOS und visionOS verwenden Bildstapel. Vermeide unnötigen Text und vorgerenderte Effekte, die mit Systemeffekten kollidieren.

**Engineering-Ableitung:** Teste kleine Darstellungen, Maskierung, dunkle/getönte Varianten und Parallax-Cropping. Asset-Erzeugung plattformspezifisch halten; keine einzige fertig abgerundete PNG-Datei als universelles Icon-System behandeln.

### Marke ohne Plattformbruch

Quelle: [18] https://developer.apple.com/design/human-interface-guidelines/branding

**Apple-Empfehlung:** Marke soll Inhalte nicht verdrängen. Setze Akzentfarbe gezielt ein, verwende vertraute Komponenten und konsistente Sprache. Eigene Schriften müssen lesbar und zugänglich bleiben; unnötige Logos und Branding auf Launch Screens vermeiden.

**Engineering-Ableitung:** Definiere Marken-Tokens für Inhalt und Akzente, ohne Semantik oder Verhalten von Systemkomponenten umzudeuten. Begründe jede vom System abweichende Control-Gestaltung.

### Semantische Farbe

Quelle: [24] https://developer.apple.com/design/human-interface-guidelines/color

**Apple-Empfehlung:** Nutze Systemfarben nach ihrer Bedeutung, nicht als kopierte RGB-Werte. Eigene Farben benötigen helle, dunkle und kontrastverstärkte Varianten; selbst ein einfarbiges Erscheinungskonzept braucht Varianten für adaptive Liquid-Glass-Kontexte. Farbe nie als einzigen Informationsträger verwenden. Glas-Akzente auf wirklich wichtige Aktionen oder Status begrenzen.

**Engineering-Ableitung:** Teste Farben mit bewegtem Hintergrund, wechselnden Materialien und mehreren Displays. Hinterlege semantische Tokens statt geräteweiter Hex-Konstanten; prüfe Status auch ohne Farberkennung.

### Dark Mode

Quelle: [26] https://developer.apple.com/design/human-interface-guidelines/dark-mode

**Apple-Empfehlung:** Folge grundsätzlich der Systemeinstellung und vermeide eine separate App-Einstellung. Prüfe Light/Dark und Kombinationen mit Increase Contrast und Reduce Transparency. Farben nicht schlicht invertieren. Diese Seite nennt mindestens 4,5:1 Kontrast und strebt für eigene Vorder-/Hintergrundfarben 7:1 an, besonders bei kleinem Text. visionOS und watchOS unterstützen laut Seite keinen gesonderten Dark Mode.

**Engineering-Ableitung:** Teste Umschalten bei laufender App. Diese Kontrastempfehlung nicht als vollständige WCAG-Konformitätsprüfung verkaufen; die Accessibility-Tabelle besitzt anders formulierte, teils überlappende Größen-/Gewichtszeilen. Für konkrete Compliance separate normative Prüfung durchführen.

### Interface-Icons

Quelle: [52] https://developer.apple.com/design/human-interface-guidelines/icons

**Apple-Empfehlung:** Nutze einfache erkennbare Metaphern, konsistente Strichstärken, Perspektive und optische Ausrichtung. Stimmen Icon und Text semantisch zusammen, sollen auch ihre Gewichte harmonieren. Eigene Icons bevorzugt als Vektoren; Accessibility-Beschreibungen und nötige Lokalisierung vorsehen. Standardkomponenten verwalten Auswahlzustände normalerweise selbst.

**Engineering-Ableitung:** Prüfe Icons bei kleinster Darstellung, hoher Textgröße und RTL. Dekorative und interaktive Icons semantisch unterscheiden; ein unbeschriftetes Symbol nicht ohne Verständlichkeitsprüfung als alleinige Aktion einsetzen.

### Bilder und Auflösung

Quelle: [54] https://developer.apple.com/design/human-interface-guidelines/images

**Apple-Empfehlung:** Points sind keine universellen Pixel: auf zweidimensionalen Plattformen hängt die Zuordnung vom Display ab, in visionOS vom Winkel. Liefere passende Bitmap-Skalierungen und Farbprofile, prüfe echte Geräte. visionOS bevorzugt skalierbare Vektoren; räumliche Fotos/Szenen möglichst separat statt dicht im Fließinhalt zeigen. tvOS-Layer brauchen einen opaken Hintergrund und Cropping-Sicherheit.

**Engineering-Ableitung:** Keine Layoutkonstanten aus Bildpixeln ableiten. Prüfe Speicher-/Laufzeitkosten hochauflösender Assets und Lesbarkeit über räumlichen Bildern; nicht jedes Bild ungeprüft maximal auflösen.

### Immersion

Quelle: [56] https://developer.apple.com/design/human-interface-guidelines/immersive-experiences

**Apple-Empfehlung:** Bevorzuge Shared Space oder Mixed-Immersion zum Einstieg. Immersion gezielt für wertvolle Momente einsetzen und Ein-/Ausstieg durch klare Aktionen ermöglichen. Progressive/volle Immersion setzt eine ungefähr 1,5-Meter-Grenze um die anfängliche Kopfposition; Mixed verhält sich anders. Vermeide erzwungene Fortbewegung, abrupte Übergänge und verdeckte reale Umgebung.

**Engineering-Ableitung:** Immersionswechsel als explizite Zustandsmaschine modellieren; Fortschritt und Rückkehrziel sichern. Die Systemgrenze ist keine zugesicherte sichere Bewegungsfläche. Tracking-Ausfälle und Wiederzentrieren prüfen; Hardwarekomfort ist ein eigenes Abnahmekriterium.

### Inklusion

Quelle: [57] https://developer.apple.com/design/human-interface-guidelines/inclusion

**Apple-Empfehlung:** Verwende verständliche, respektvolle Sprache und vielfältige Darstellungen. Hinterfrage stereotype Annahmen über Familien, Fähigkeiten, Bildung oder Identität. Erfrage Geschlecht nur bei tatsächlichem Bedarf. Internationalisierung umfasst Sprache, Zahlen, Zeit, Währung und kulturelle Farbbedeutungen; Barrierefreiheit gehört von Anfang an dazu.

**Engineering-Ableitung:** Teste Formulare mit unterschiedlichen Namens- und Familienmodellen, langen Übersetzungen und wechselnden Regionen. Aus illustrativen Beispielen keine restriktiven Validierungsregeln übernehmen.

### Adaptives Layout

Quelle: [60] https://developer.apple.com/design/human-interface-guidelines/layout

**Apple-Empfehlung:** Leite Struktur aus verfügbarem Raum und Size Classes ab, nicht aus Modellnamen oder Orientierung. Beachte Safe Areas, RTL und Textvergrößerung; Funktion bleibt beim Resizing erhalten. Trenne Controls und Inhalt, nutze Systemeffekte statt opaker Unterlagen. tvOS: Hauptinhalt oben/unten 60 pt, seitlich 80 pt einrücken. visionOS: ausreichend Abstand, etwa mindestens 60 pt zwischen Button-Mittelpunkten. watchOS: grundsätzlich höchstens drei Glyphen- oder zwei Textbuttons nebeneinander.

**Engineering-Ableitung:** Teste kleinste/größte Fenster, alle Size-Class-Kombinationen, lange Lokalisierungen und große Schrift. Hintergrund darf bis zum Rand reichen, kritischer Inhalt nicht blind in unsichere Bereiche. Textcontainer wachsen lassen; keine feste Zeilenhöhe als Lösung für Überlauf.

### Materialien und Liquid Glass

Quelle: [70] https://developer.apple.com/design/human-interface-guidelines/materials

**Apple-Empfehlung:** Liquid Glass trennt Controls/Navigation vom Inhalt; nicht als allgemeines Material für Inhaltskarten einsetzen. Ausnahme: vorübergehend interaktive Teile etwa von Slidern/Toggles. Standardkomponenten übernehmen Systemverhalten. Regular bevorzugen, wenn Lesbarkeit gefährdet ist; Clear nur über visuell reichen Medien. Bei hellem Hintergrund kann eine dunkle Schicht mit 35 % Deckkraft helfen; nicht zusätzlich nötig bei ausreichend dunklem Inhalt oder eigener AVKit-Abdunklung. Standardmaterialien gliedern Inhalt. visionOS-Glas ist eigenständig adaptiv, nicht frei veränderbares Fensterdesign.

**Engineering-Ableitung:** Keine flächendeckende Glas-Ästhetik erzeugen. Prüfe Live-Hintergründe, Reduce Transparency und Increase Contrast. APIs und Fallbacks nach Deployment Target auswählen; eigene Blur-Rezepturen nicht als äquivalentes Liquid Glass ausgeben.

### Bewegung

Quelle: [73] https://developer.apple.com/design/human-interface-guidelines/motion

**Apple-Empfehlung:** Animation soll Status, Rückmeldung oder Kontext vermitteln, nicht dekorativ verzögern. Halte Feedback kurz, unterbrechbar und konsistent zur Geste. Biete andere Informationskanäle. In visionOS periphere Bewegung und rotierende virtuelle Welten vermeiden; stationäre Referenzen helfen. Die Seite warnt besonders vor anhaltender Oszillation um 0,2 Hz.

**Engineering-Ableitung:** Definiere für jeden eigenen Effekt Zweck und bewegungsarme Alternative. Teste schnelle Folgeaktionen, Abbruch und Reduce Motion. Aus der beispielhaften Spiele-Framerate dieser Seite keine universelle Performance-Vorgabe für räumliche Apps ableiten.

### Datenschutz im Interaktionsdesign

Quelle: [87] https://developer.apple.com/design/human-interface-guidelines/privacy

**Apple-Empfehlung:** Frage nur benötigte Daten kontextbezogen an und erläutere den Zweck konkret. Bevorzuge lokale Verarbeitung, Systemauthentifizierung und Keychain für Geheimnisse. Keine manipulativen Vorabdialoge. Ein notwendiger Berechtigungs-Vorabdialog soll mit einer klaren Weiter-Aktion den Systemdialog öffnen, nicht eine Erlaubnis vortäuschen. Blickdaten vor Aktivierung bleiben in visionOS systemseitig geschützt.

**Engineering-Ableitung:** Teste Verweigerung, spätere Rechteänderung und reduzierte Funktionalität. API-Verfügbarkeit, Berechtigungen und Sicherheitsanforderungen separat prüfen; HIG ersetzt kein Datenschutz-/Security-Audit. Die spezielle Vorabdialog-Regel nicht auf gewöhnliche modale Abläufe übertragen.

### RTL ohne pauschales Spiegeln

Quelle: [91] https://developer.apple.com/design/human-interface-guidelines/right-to-left

**Apple-Empfehlung:** Nutze automatische Spiegelung standardkonformer Layouts. Spiegele Navigation, Fortschritt und leserichtungsabhängige Symbole, nicht Ziffernfolgen innerhalb einer Zahl, Fotos, Logos oder reale Richtungsangaben. Absatzsprache kann andere Ausrichtung als der umgebende Kontext erfordern; Listen bleiben konsistent ausgerichtet.

**Engineering-Ableitung:** Verwende leading/trailing statt festem left/right, aber keine globale Grafiktransformation. Teste gemischte Schriften, Telefonnummern und gerichtete Controls. Hardwaregebundene Ausnahmen wie die Duo-Leisten getrennt behandeln.

### SF Symbols

Quelle: [95] https://developer.apple.com/design/human-interface-guidelines/sf-symbols

**Apple-Empfehlung:** Wähle Symbol, Gewicht, Maßstab und Rendering passend zu Bedeutung und benachbartem Text. Hierarchical vermittelt Hierarchie, Variable Color Veränderung. Verfügbarkeit hängt von Systemversion ab; lokale Sprachvarianten werden unterstützt. Eigene Symbole benötigen zugängliche Beschriftung und Tests. Symbolnutzung für App-Icons, Logos oder Marken ist laut Seite untersagt; geschützte Apple-Symbole dürfen nicht beliebig verändert werden.

**Engineering-Ableitung:** Prüfe jedes Symbol und jeden Effekt gegen das Deployment Target, liefere gegebenenfalls einen semantisch passenden Fallback. Animations- und Renderingprüfung für Light/Dark und große Schrift vorsehen; Lizenzprüfung nicht durch technische Verfügbarkeit ersetzen.

### Räumliche Anordnung

Quelle: [100] https://developer.apple.com/design/human-interface-guidelines/spatial-layout

**Apple-Empfehlung:** Wichtiges zentriert im Sichtfeld platzieren, aber nicht starr am Kopf verankern. Tiefenstaffelung nur mit Nutzen, Text möglichst ohne Tiefe. Dynamische Skalierung erhält Bedienbarkeit bei wechselnder Entfernung; feste Skalierung sparsam für maßstabsgetreue Objekte. Für reguläre Buttons nennt die Seite mindestens 60 pt Mittelpunktabstand und mindestens 16 pt Zwischenraum.

**Engineering-Ableitung:** Keine festen Annahmen über das individuelle Sichtfeld treffen: Das System liefert es nicht. Prüfe Verdeckung, indirekte Auswahl und räumliche Repositionierung; zusätzliche Fenster sind kein Ersatz für Informationshierarchie.

### Typografie und Größen

Quelle: [104] https://developer.apple.com/design/human-interface-guidelines/typography

**Apple-Empfehlung:** Nutze semantische Textstile und gut lesbare Gewichte. Eigene Schriften müssen Größenanpassung und Bold Text unterstützen. Große Schrift braucht umbrechende/wachsende Layouts, nicht bloß kleinere Schrift. Dynamic Type gilt laut Seite für iOS, iPadOS, tvOS, visionOS und watchOS, nicht macOS. Systemfonts über APIs beziehen, nicht einbetten.

Original-JSON: empfohlene Standard-/Mindestschriftgröße, nicht universelle Body-Vorgabe:

| Plattform | pt Standard / Minimum |
|---|---|
| iOS, iPadOS | 17 / 11 |
| macOS | 13 / 10 |
| tvOS | 29 / 23 |
| visionOS | 17 / 12 |
| watchOS | 16 / 12 |

**Engineering-Ableitung:** Teste tatsächliche Textstile bei allen unterstützten Größen. Auf macOS bedarf gewünschte Textvergrößerung einer passenden eigenen Lösung; Minimum nicht als bevorzugte Fließtextgröße verwenden.

### UX-Texte

Quelle: [109] https://developer.apple.com/design/human-interface-guidelines/writing

**Apple-Empfehlung:** Schreibe klar, knapp, handlungsorientiert und mit konsistenter Terminologie. Ton passt zur Situation; Labels erklären Aktionen. Fehler sollen nahe am Problem eine Lösung nennen, ohne Schuldzuweisung. Leere Zustände brauchen einen nächsten Schritt. Passe Eingabebegriffe an das Gerät an; verlinke Einstellungen direkt statt lange Navigationsanleitungen zu geben.

**Engineering-Ableitung:** Pflege ein lokalisiertes Begriffssystem und teste Fehlermeldungen samt Recovery-Aktion. Beispiele für Passwörter oder Namen sind keine Produktanforderungen. Prüfe Labels auch ohne Bildkontext und mit Screenreader.

### Eingaben als Fähigkeiten

Quelle: [5] https://developer.apple.com/design/human-interface-guidelines/inputs

**Apple-Empfehlung:** Die Übersicht verknüpft unterstützte Interaktionsarten; ihre Existenz bedeutet nicht Verfügbarkeit auf jeder Plattform oder jedem Gerät.

**Engineering-Ableitung:** Führe eine Capability-Matrix pro Zielplattform und Hardwarevariante. Jede wesentliche Aktion braucht einen erreichbaren Standardpfad; Spezialhardware ergänzt ihn statt ihn stillschweigend vorauszusetzen.

### Action Button

Quelle: [9] https://developer.apple.com/design/human-interface-guidelines/action-button

**Apple-Empfehlung:** Unterstütze wesentliche wiederkehrende Aufgaben über App Shortcuts, nicht bloß App-Start. Kurze Aktionslabels beginnen mit einem Verb; die Seite nennt maximal drei Wörter. Vermeide doppelte Einrichtungshinweise. Auf watchOS müssen Folgeaktionen logisch zur primären Aufgabe passen; Beenden bevorzugt in der Oberfläche statt über weitere Tastendrücke.

**Engineering-Ableitung:** Nur auf unterstützten iPhone-/Watch-Modellen anbieten. Prüfe Aufruf außerhalb der App und ohne Blick auf den Bildschirm. Pausieren ist bei Tauchfunktionen ausdrücklich eine mögliche Ausnahme, kein blind anzuwendender Standard.

### Apple Pencil und Scribble — iPadOS

Quelle: [16] https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble

**Apple-Empfehlung:** Erlaube unmittelbares Markieren und Pencil-Bedienung der Controls. Beachte beide Hände. Hover erklärt eine mögliche Markierung, löst aber keine Aktion aus. Double Tap respektiert Einstellungen; Squeeze bleibt kurz und nichtdestruktiv; Barrel Roll beeinflusst Markierungen, nicht Navigation. Scribble funktioniert in Standard-Textkomponenten außer Passwortfeldern. Felder während des Schreibens nicht verschieben, skalieren oder automatisch scrollen.

**Engineering-Ableitung:** Nutze PencilKit/Standardfelder, wo geeignet. Teste Handschrift bei Layoutwechsel und Undo/Redo in kompakter Umgebung. Feature-Verfügbarkeit modellabhängig prüfen; Druck, Hover oder Squeeze nicht für jeden Pencil voraussetzen.

### Camera Control — unterstützte iPhones

Quelle: [19] https://developer.apple.com/design/human-interface-guidelines/camera-control

**Apple-Empfehlung:** Nutze kurze Labels und SF Symbols, keine eigenen Symbole. Slider brauchen verständliche Einheiten und sinnvolle markante Werte. Halte den Overlaybereich frei und vermeide doppelte Controls. Controls je Kameramodus aktivieren/deaktivieren; die Seite erlaubt kein Hinzufügen/Entfernen zur Laufzeit. Unterstütze gegebenenfalls eine Locked-Capture-Erweiterung.

**Engineering-Ableitung:** Teste Hoch-/Querformat, große Schrift, Zustandswechsel und Sperrbildschirmaufruf. Die im Snapshot genannten Modellbeispiele nicht als vollständige aktuelle Hardwareliste verwenden; echte Capability- und API-Prüfung erforderlich.

### Digital Crown

Quelle: [36] https://developer.apple.com/design/human-interface-guidelines/digital-crown

**Apple-Empfehlung:** Auf watchOS dient Drehen primär vertikaler Navigation und kann ohne Navigationskonflikt Daten steuern. Rückmeldung folgt der Drehgeschwindigkeit; ergänze Touchbedienung. Crown-Drücken bleibt dem System vorbehalten. Auf visionOS steuert die Crown Systemfunktionen wie Immersion und Neuzentrierung, nicht frei definierte App-Aktionen.

**Engineering-Ableitung:** Trenne Drehereignisse von systemreservierten Tastendrücken. Teste Werteauswahl, Scrollen und haptische Rastung; keine visionOS-Crown-Callback-Funktion erfinden.

### Blickinteraktion — visionOS

Quelle: [39] https://developer.apple.com/design/human-interface-guidelines/eyes

**Apple-Empfehlung:** Blick markiert ein Ziel, die eigentliche Aktion folgt durch Interaktion. Das System liefert keine Blickposition vor dem Tap; eigene Hover-Effekte laufen außerhalb des App-Prozesses. Platziere länger betrachtete Inhalte möglichst mindestens einen Meter entfernt. Nutze klare gerundete Zielbereiche und ausreichend Abstand; die Seite nennt 16 pt Rand oder 60 pt Mittelpunktabstand.

**Engineering-Ableitung:** Blick-Hover nicht als Analytics-Event oder Geschäftslogik-Trigger implementieren. Gruppiere Bild und Label zu einem Ziel. Prüfe Blickkomfort auf Hardware und halte Fokus für Tastatur/Controller logisch getrennt vom Hover-Effekt.

### Fokus und Auswahl

Quelle: [42] https://developer.apple.com/design/human-interface-guidelines/focus-and-selection

**Apple-Empfehlung:** Verwende Systemeffekte und ändere Fokus nicht ohne Anlass. Auf tvOS muss die gerichtete Navigation alle relevanten Elemente erreichen; Auswahl/Aktivierung kann eine zusätzliche Geste verlangen. Auf iPadOS bewegt Tab zwischen Fokusgruppen, Pfeiltasten innerhalb einer Gruppe. visionOS-Blick-Hover ist nicht das Tastatur-/Controller-Fokussystem.

**Engineering-Ableitung:** Teste Fokusreihenfolge, Entfernung des fokussierten Elements und Rückkehr aus Modalen. Die Kennzeichnung „nicht unterstützt“ für iOS/watchOS bezieht sich auf dieses Fokusmodell, nicht auf fehlende Accessibility-Navigation. Full Keyboard Access gesondert testen, nicht ausschalten.

### Spielsteuerung

Quelle: [44] https://developer.apple.com/design/human-interface-guidelines/game-controls

**Apple-Empfehlung:** Unterstütze plattformübliche Eingaben und passe Hinweise dem aktiven Controller an. Touch-Spielcontrols: häufige Aktionen mindestens 44×44 pt, weniger wichtige mindestens 28×28 pt. Sichtbare Druckzustände und ergänzendes Feedback anbieten. Controller automatisch erkennen; Pflichtcontroller in tvOS/visionOS klar kommunizieren. Tastaturbelegung soll anpassbar sein.

**Engineering-Ableitung:** Teste Controllerwechsel und Verbindungsverlust samt Menübedienung. Tabellenmapping im JSON: A aktiviert, B bricht ab/geht zurück; tatsächliche Geräteglyphen anzeigen, nicht überall dieselben Buchstaben. Touch-Mindestwerte nicht pauschal auf alle Plattformen übertragen.

### Gesten

Quelle: [46] https://developer.apple.com/design/human-interface-guidelines/gestures

**Apple-Empfehlung:** Erhalte Bedeutung vertrauter Gesten und reservierte Systemgesten. Eigene Gesten nur für echten Bedarf, leicht erlernbar und nie als einziger wichtiger Zugangsweg. visionOS bevorzugt indirekte Standardgesten; eigenes Handtracking benötigt Full Space und Erlaubnis. macOS-Touch soll Trefferflächen verbessern, nicht die komplette Oberfläche vergrößern. watchOS-Double-Tap darf die erwartete Scroll-/Tabnavigation nicht durch eine primäre Aktion verdrängen.

**Engineering-Ableitung:** Teste Gesture-Konflikte, gleichzeitige Eingaben, Abbruch und sichtbare Alternativen. Kein Hand-, Körperhaltungs- oder Mehrfingerzwang für Grundfunktionen; Zugänglichkeit mit systemreservierten Gesten gemeinsam prüfen.

### Bewegungssensoren

Quelle: [48] https://developer.apple.com/design/human-interface-guidelines/gyro-and-accelerometer

**Apple-Empfehlung:** Verwende Bewegungsdaten nur für erkennbaren Nutzen und mit erklärtem Zugriffsgrund. Außerhalb aktiven Gameplays direkte Oberflächensteuerung per Gyroskop/Beschleunigung möglichst vermeiden: Präzision, körperliche Anforderungen und Energieverbrauch können problematisch sein.

**Engineering-Ableitung:** Der Text nennt iOS, iPadOS und watchOS sowie tvOS über Siri Remote; „keine zusätzlichen Plattformhinweise“ belegt keine universelle Sensorverfügbarkeit. Prüfe Hardwarefähigkeit und Ausweichbedienung; fehlende Daten dürfen keine Sackgasse erzeugen.

### Tastaturen

Quelle: [58] https://developer.apple.com/design/human-interface-guidelines/keyboards

**Apple-Empfehlung:** Bewahre Standardkürzel und unterstütze Full Keyboard Access, wo verfügbar. Eigene Kürzel für häufige Spezialbefehle; Modifier-Reihenfolge Control, Option, Shift, Command. Beachte unterschiedliche Tastaturlayouts und lasse das System lokalisieren. iPadOS-Fokusnavigation für Inhalte und Full Keyboard Access für sämtliche Controls sind unterschiedliche Mechanismen. visionOS-Kürzeltitel müssen ohne Untermenükontext verständlich sein.

**Engineering-Ableitung:** Teste ohne Maus inklusive Modalen und Textfeldern. Prüfe deutsche und andere Layouts; globale Tastaturhandler dürfen Texteingabe und Systemkürzel nicht verschlucken. Aus fehlender Standard-Tab-Navigation eines Controls kein Accessibility-Verbot ableiten.

### Nearby Interaction

Quelle: [76] https://developer.apple.com/design/human-interface-guidelines/nearby-interactions

**Apple-Empfehlung:** Nähe, Richtung und Kontext sollen einen nachvollziehbaren Nutzen liefern; kontinuierliches visuelles, akustisches oder haptisches Feedback hilft. Biete immer einen anderen Aufgabenweg. Entfernung/Richtung können durch Lage und Hindernisse unzuverlässig werden. iPhone liefert Distanz und Richtung; Apple Watch Distanz, wobei beteiligte Watch-Apps im Vordergrund sein müssen.

**Engineering-Ableitung:** Behandle Richtung als optional, nicht als stets vorhandenen Messwert. Prüfe Berechtigungsverweigerung, Unterbrechung und fehlende UWB-Unterstützung. Keine universelle iPad-Unterstützung aus dem knappen Plattformabschnitt ableiten.

### Zeigegeräte

Quelle: [84] https://developer.apple.com/design/human-interface-guidelines/pointing-devices

**Apple-Empfehlung:** Bewahre Systemgesten und konsistente Modifier-Aktionen über Eingabegeräte hinweg. Auf iPad ergänzt der Zeiger Touch; verwende passende Standardeffekte statt dekorativer Cursor. Bei Touch-fähigem macOS brauchen essenzielle Hover-Controls einen zugänglichen Offenlegungspfad, etwa Antippen und Kontextmenü; bestehende Auswahl erhalten. visionOS koordiniert Zeiger, Blick und Gesten systemseitig.

**Engineering-Ableitung:** Teste Hover-freie Bedienung, Mehrfachauswahl und wechselnde Geräte. Die im iPad-Abschnitt genannten ungefähr 12/24 pt Hit-Region-Padding sind kontextuelle Richtwerte, keine pauschalen Button-Abstände. Vergrößerung darf Nachbarinhalte nicht überdecken.

### Fernbedienung — tvOS

Quelle: [89] https://developer.apple.com/design/human-interface-guidelines/remotes

**Apple-Empfehlung:** Nutze vertraute Wisch-/Druckaktionen und konsistente Fokusrichtung. Druck ist eine absichtliche Aktivierung; versehentliche Berührungen dürfen nicht ungewollt auslösen. Back führt normalerweise zum hierarchischen Elternbildschirm, nicht zwingend zum chronologisch vorherigen. Während Gameplay öffnet es ein Pausemenü; dort setzt erneutes Back das Spiel fort. Play/Pause muss Medien erwartungsgemäß steuern.

**Engineering-Ableitung:** Teste Fernbedienung allein, Navigation bis Home und unbeabsichtigte Touch-Eingaben. EPG-Tasten kontextabhängig prüfen: im Guide blättern, bei laufendem Inhalt Kanal wechseln.

## Sources

[3] https://developer.apple.com/design/human-interface-guidelines/foundations
[4] https://developer.apple.com/design/human-interface-guidelines/getting-started
[5] https://developer.apple.com/design/human-interface-guidelines/inputs
[8] https://developer.apple.com/design/human-interface-guidelines/accessibility
[9] https://developer.apple.com/design/human-interface-guidelines/action-button
[13] https://developer.apple.com/design/human-interface-guidelines/app-icons
[16] https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble
[18] https://developer.apple.com/design/human-interface-guidelines/branding
[19] https://developer.apple.com/design/human-interface-guidelines/camera-control
[24] https://developer.apple.com/design/human-interface-guidelines/color
[26] https://developer.apple.com/design/human-interface-guidelines/dark-mode
[27] https://developer.apple.com/design/human-interface-guidelines/design-principles
[28] https://developer.apple.com/design/human-interface-guidelines/designing-for-games
[29] https://developer.apple.com/design/human-interface-guidelines/designing-for-ios
[30] https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados
[31] https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo
[32] https://developer.apple.com/design/human-interface-guidelines/designing-for-macos
[33] https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos
[34] https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos
[35] https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos
[36] https://developer.apple.com/design/human-interface-guidelines/digital-crown
[39] https://developer.apple.com/design/human-interface-guidelines/eyes
[42] https://developer.apple.com/design/human-interface-guidelines/focus-and-selection
[44] https://developer.apple.com/design/human-interface-guidelines/game-controls
[46] https://developer.apple.com/design/human-interface-guidelines/gestures
[48] https://developer.apple.com/design/human-interface-guidelines/gyro-and-accelerometer
[52] https://developer.apple.com/design/human-interface-guidelines/icons
[54] https://developer.apple.com/design/human-interface-guidelines/images
[56] https://developer.apple.com/design/human-interface-guidelines/immersive-experiences
[57] https://developer.apple.com/design/human-interface-guidelines/inclusion
[58] https://developer.apple.com/design/human-interface-guidelines/keyboards
[60] https://developer.apple.com/design/human-interface-guidelines/layout
[70] https://developer.apple.com/design/human-interface-guidelines/materials
[73] https://developer.apple.com/design/human-interface-guidelines/motion
[76] https://developer.apple.com/design/human-interface-guidelines/nearby-interactions
[84] https://developer.apple.com/design/human-interface-guidelines/pointing-devices
[87] https://developer.apple.com/design/human-interface-guidelines/privacy
[89] https://developer.apple.com/design/human-interface-guidelines/remotes
[91] https://developer.apple.com/design/human-interface-guidelines/right-to-left
[95] https://developer.apple.com/design/human-interface-guidelines/sf-symbols
[100] https://developer.apple.com/design/human-interface-guidelines/spatial-layout
[104] https://developer.apple.com/design/human-interface-guidelines/typography
[109] https://developer.apple.com/design/human-interface-guidelines/writing
