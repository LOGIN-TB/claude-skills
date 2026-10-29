# Apple HIG: Patterns und Technologies — operative Referenz

## Anwendung und Aussagegrenzen

Basis sind am 29. Oktober 2026 abgerufene Apple-DocC-Originaldaten. Die Quellenlinks stammen aus dem maschinellen Inventar in `source-map.md`. Dies ist eine seitenvollständige, bewusst verdichtete Arbeitsreferenz, keine vollständige Übersetzung sämtlicher Absätze, Maßtabellen oder API-Dokumentationen. Pro Originalseite bleiben die folgenden Karten einschließlich Aktivierung und Test unter 150 Wörtern; keine längeren Originalzitate.

**Leseschlüssel:** „Umsetzung (HIG)“ verdichtet Apples Empfehlungen. „Aktivierung (Engineering-Ableitung)“ übersetzt den Nutzungskontext in eine Agentenentscheidung. Sämtliche Tests und zusätzlich ausdrücklich so markierte Regeln sind eigene Engineering-Ableitungen, keine von Apple vorgeschriebenen Testverfahren. „Erwägen“ bleibt eine Option und wird nicht zu einer Produktpflicht aufgewertet.

**Engineering-Ableitung — Gate vor Implementierung:** Zielplattform, unterstützte Betriebssystemversionen, Nutzungsaufgabe, vorhandene Architektur, Hardware, Berechtigungen und Entitlements erfassen. Technologieintegration nur bei belegtem Produktbedarf oder ausdrücklichem Auftrag hinzufügen; nicht, weil eine HIG-Seite existiert. Keine automatischen Konten, KI-Funktionen, Cloud-Synchronisation, Käufe, Tracking-, Gesundheits-, NFC- oder Smart-Home-Funktionen. Eine HIG-Nennung ist kein Nachweis aktueller API-Verfügbarkeit. SDK-Dokumentation und projektbezogene Anforderungen vor Implementierung gezielt prüfen. Ausnahme vom „optionalen Feature“-Denken: VoiceOver-Zugänglichkeit ist Qualitätsarbeit an vorhandener UI, kein optionales Upsell-Feature.

**Engineering-Ableitung — Prüfprotokoll:** Jede anwendbare Karte wird im Audit mit `pass / fail / not_tested / blocked / not_applicable` geführt; Umsetzung und tatsächliche Prüfung getrennt dokumentieren. Nur tatsächlich ausgeführte Tests als bestanden markieren. Simulator, Gerät und manuelle Assistenztechnik-Prüfung unterscheiden. Die hier genannten Tests sind Testaufträge; sie wurden in diesem Skill-Referenz nicht an einer App ausgeführt.

## Patterns

### patterns — Patterns
Quelle: [6] https://developer.apple.com/design/human-interface-guidelines/patterns

- **Aktivierung (Engineering-Ableitung):** Eine Nutzeraufgabe, Interaktion oder ein Ablauf wird entworfen oder verändert.
- **Umsetzung (HIG):** Die Kategorie bündelt Gestaltungshinweise zu wiederkehrenden Aufgaben und Erlebnissen; die passende Unterseite für den konkreten Ablauf heranziehen.
- **Test (Engineering-Ableitung):** Geänderte User Flows den folgenden Karten zuordnen; fehlende Zuordnung oder begründetes „nicht anwendbar“ sichtbar dokumentieren.

### charting-data — Charting data
Quelle: [22] https://developer.apple.com/design/human-interface-guidelines/charting-data

- **Aktivierung (Engineering-Ableitung):** Daten sollen Trends, Vergleiche oder Veränderungen verständlich machen.
- **Umsetzung (HIG):** Diagramme für eine erkennbare Aussage einsetzen; für reine Datenausgabe können Listen oder Tabellen geeigneter sein. Geläufige Diagrammtypen, klare Überschriften, Einheiten und hilfreiche Erläuterungen bevorzugen. Detailfülle schrittweise offenlegen. Zusammengehörige Ansichten desselben Datensatzes durch konsistente Farben, Markierungen und Beschriftung verbinden. Diagrammgröße an Lesbarkeit und Interaktion ausrichten. Beschreibender Begleittext ersetzt keine Accessibility-Labels und zugänglichen Datenpunkte.
- **Test (Engineering-Ableitung):** Aussage ohne Farbe erklären lassen; mit VoiceOver Werte und Beziehungen erschließen. Leere, dichte, negative und extreme Werte prüfen. Übersicht und Detailansicht müssen denselben Datensatz und dieselbe Bedeutung vermitteln.

### collaboration-and-sharing — Collaboration and sharing
Quelle: [23] https://developer.apple.com/design/human-interface-guidelines/collaboration-and-sharing

- **Aktivierung (Engineering-Ableitung):** Inhalte können geteilt oder gemeinsam bearbeitet werden.
- **Umsetzung (HIG):** System-Teilen-Oberfläche gut erreichbar anbieten; „Kopie senden“ und Zusammenarbeit nur gemäß unterstützter Funktionalität darstellen. Berechtigungen knapp und verständlich zusammenfassen; Zugriffs- und Bearbeitungsoptionen überschaubar halten. Nach Beginn der Zusammenarbeit den Collaboration-Button sichtbar machen, möglichst beim Teilen-Button. Eigene Popover-Aktionen auf Wesentliches begrenzen. Eigene Kollaborationsinfrastruktur benötigt für diese Integration Universal Links. Auf visionOS pausiert die Shared-Space-Bildschirmfreigabe beim Wechsel in einen Full Space.
- **Test (Engineering-Ableitung):** Einladung, Nur-Lesen, Bearbeiten, Teilnehmerentzug und Kopieversand separat prüfen; Links müssen den richtigen Inhalt öffnen. Zugriff nach Entzug tatsächlich verweigern, nicht nur UI ausblenden.

### drag-and-drop — Drag and drop
Quelle: [37] https://developer.apple.com/design/human-interface-guidelines/drag-and-drop

- **Aktivierung (Engineering-Ableitung):** Menschen ordnen, verschieben, kopieren oder übertragen Inhalte.
- **Umsetzung (HIG):** Drag-and-drop breit unterstützen, aber gleichwertige Alternativen anbieten. Innerhalb eines Containers ist Verschieben, zwischen Containern meist Kopieren erwartbar; zwischen Apps wird kopiert. Gültige Ziele, Einfügeposition, Transferfortschritt und Fehlschlag klar rückmelden. Mehrfachauswahl und Undo unterstützen, soweit sinnvoll. Mehrere Datenrepräsentationen nach Qualität anbieten und die reichhaltigste kompatible annehmen. Auswahlzustand nach dem Drop erhalten; bei angeschlossener Tastatur Option beim Ablegen auswerten. macOS-Hintergrundauswahl nicht unnötig aktivieren. Nicht auf tvOS/watchOS übertragen.
- **Test (Engineering-Ableitung):** Gleicher/fremder Container, andere App, ungültiges Ziel, Teilmenge, Abbruch, langsamer Transfer, Undo und Tastatur-/VoiceOver-Alternative durchspielen. Quellinhalt darf bei gescheitertem Transfer nicht verloren gehen.

### entering-data — Entering data
Quelle: [38] https://developer.apple.com/design/human-interface-guidelines/entering-data

- **Aktivierung (Engineering-Ableitung):** Ein Formular oder anderer Eingabeschritt benötigt Nutzerdaten.
- **Umsetzung (HIG):** Bereits verfügbare Informationen nicht erneut abfragen; geschützte Daten nur mit erforderlicher Zustimmung beziehen. Benötigte Daten eindeutig benennen. Auswahlmöglichkeiten, Einfügen und Drag-and-drop statt unnötigem Tippen ermöglichen. Sensible Eingaben mit sicheren Feldern schützen; Passwörter nicht selbst vorbelegen, sondern Authentifizierung beziehungsweise Schlüsselbund nutzen. Werte dynamisch validieren. Weiter-Aktionen erst ermöglichen, wenn erforderliche Eingaben vorliegen. Auf macOS kann ein Erweiterungs-Tooltip abgeschnittene Feldinhalte zeigen.
- **Test (Engineering-Ableitung):** Pflicht-/Optionalfelder, Einfügen, AutoFill, ungültige und korrigierte Werte, Tastaturnavigation und sichere Darstellung prüfen. Fehlermeldung und Korrekturmöglichkeit müssen verständlich bleiben; fehlerhafte Eingabe darf nicht kommentarlos verschwinden.

### feedback — Feedback
Quelle: [40] https://developer.apple.com/design/human-interface-guidelines/feedback

- **Aktivierung (Engineering-Ableitung):** Aktionen verändern Zustand, scheitern, benötigen Zeit oder können Daten vernichten.
- **Umsetzung (HIG):** Zugängliche, konsistente Rückmeldung möglichst im Kontext integrieren. Alerts für kritische, möglichst handlungsfähige Information reservieren. Vor unerwartetem, irreversiblem Datenverlust warnen; erwartete Routinefolgen nicht ständig bestätigen lassen. Bedeutenden Abschluss kenntlich machen. Nicht ausführbare Befehle erklären und gegebenenfalls einen Lösungsweg zeigen. Rückmeldung nicht ausschließlich akustisch, haptisch oder farblich transportieren. Unbestimmte Fortschrittsanzeigen auf watchOS vermeiden.
- **Test (Engineering-Ableitung):** Erfolg, Fehler, deaktivierter Befehl und gefährliche Aktion jeweils ohne Ton, ohne Haptik und mit VoiceOver prüfen. Prüfen, ob Bestätigungen echte Risiken schützen oder nur Routinearbeit unterbrechen.

### file-management — File management
Quelle: [41] https://developer.apple.com/design/human-interface-guidelines/file-management

- **Aktivierung (Engineering-Ableitung):** Die App erzeugt, öffnet, bearbeitet oder synchronisiert Dokumente.
- **Umsetzung (HIG):** System-Dateibrowser, Öffnen-/Sichern-Ansichten, Menüs und Tastaturbefehle bevorzugen. Arbeit regelmäßig und bei Kontextwechsel automatisch sichern. Dateiendungen standardmäßig verbergen, Nutzerpräferenz respektieren. Quick Look für Vorschau und gegebenenfalls eigene Dateitypen erwägen. Ein eigener Browser muss Plattform-Dateisystemkonventionen erhalten. Provider-Erweiterungen zeigen nur passende Dateien, erlauben Zielwahl und duplizieren nicht die Host-Toolbar. Unter macOS bei deaktiviertem Autosave ungesicherte Änderungen sichtbar machen und Verlust verhindern; Sichern ermöglicht Name, Format und Ort.
- **Test (Engineering-Ableitung):** Bearbeiten, Schließen, Appwechsel, Wiederöffnen, Zielwahl, schreibgeschützte Datei, Offline-Dokument und Vorschau prüfen. Autosave-Ausfall darf nicht als erfolgreiches Sichern erscheinen.

### going-full-screen — Going full screen
Quelle: [47] https://developer.apple.com/design/human-interface-guidelines/going-full-screen

- **Aktivierung (Engineering-Ableitung):** Eine unterstützte Plattform und Aufgabe profitieren von Vollbild.
- **Umsetzung (HIG):** System-Vollbild verwenden und den Einstieg sowie Ausstieg den Menschen überlassen. Layout anpassen, Fenster dabei nicht eigenmächtig umdimensionieren. Wesentliche Aktionen erreichbar halten; temporär verborgene Bedienelemente leicht wieder anzeigen lassen. Nach Appwechsel den vorherigen Kontext fortsetzen. Außer in Spielen Dock-Zugriff ermöglichen. Auf macOS Standard-Fensterknopf, Menü und Tastaturweg unterstützen; keine automatische Änderung des Anzeigemodus. Dieses Pattern nicht mit visionOS-Immersion gleichsetzen.
- **Test (Engineering-Ableitung):** Eintritt, Kontrollanzeige, Appwechsel, Rückkehr und expliziten Ausstieg prüfen. Wiedergabeende darf nicht unerwartet Vollbild beenden; Tastaturzugriff muss erhalten bleiben.

### launching — Launching
Quelle: [59] https://developer.apple.com/design/human-interface-guidelines/launching

- **Aktivierung (Engineering-Ableitung):** Kaltstart, Wiederstart oder Wiederherstellung wird implementiert.
- **Umsetzung (HIG):** Möglichst schnell eine benutzbare erste Ansicht zeigen und vorherigen Zustand wiederherstellen. Wo erforderlich, Launch Screen nahezu wie die erste Ansicht gestalten; keine eigene Werbe-, Text- oder Logoinszenierung, sofern diese nicht fester Bestandteil der ersten Ansicht ist. Onboarding und eventueller Splash gehören nach den technischen Start. Richtige Orientierung berücksichtigen. macOS, visionOS und watchOS benötigen keinen Launch Screen. Auf visionOS den Einstieg im Shared Space erwägen, auch bei späterer Immersion.
- **Test (Engineering-Ableitung):** Kalt-/Warmstart, Rotation, Zustandswiederherstellung und Start bei langsamem Netz messen. Auf Blitzwechsel, künstliche Wartezeit, nicht lokalisierbaren Launch-Text und blockierendes Onboarding prüfen.

### live-viewing-apps — Live-viewing apps
Quelle: [63] https://developer.apple.com/design/human-interface-guidelines/live-viewing-apps

- **Aktivierung (Engineering-Ableitung):** Live-TV oder andere laufende Programme sind Kerninhalt.
- **Umsetzung (HIG):** Live-Inhalte prominent, schnell abspielbar und von Abrufvideo unterscheidbar darstellen. Kanalwechsel sofort visuell bestätigen. Elektronischer Programmführer zeigt aktuellen Kanal, Sendung und Zeit; Browsen soll laufenden Inhalt möglichst erhalten. Kategorien in Guide und Wiedergabe-Footer konsistent halten. Beim Verlassen des Live-Kontexts Audio stoppen. Nur bei vorhandenem Cloud-DVR Aufnahme, Serienoptionen, Wiedergabe, Löschung und Speicherverwaltung anbieten.
- **Test (Engineering-Ableitung):** Live/VOD-Unterscheidung, langsamen Kanalwechsel, EPG-Rückkehr und Audio beim Tabwechsel prüfen; DVR-Optionen dürfen keine unimplementierte Aufnahme suggerieren.

### loading — Loading
Quelle: [64] https://developer.apple.com/design/human-interface-guidelines/loading

- **Aktivierung (Engineering-Ableitung):** Daten, Assets oder Medien werden asynchron verfügbar.
- **Umsetzung (HIG):** Früh sichtbaren Inhalt oder passende Platzhalter zeigen und andere Aufgaben während des Ladens ermöglichen. Große Assets möglichst im Hintergrund herunterladen. Fortschritt und erwartbare Wartezeit ehrlich kommunizieren: bestimmter Fortschritt bei bekanntem Umfang, sonst unbestimmt. Spiele können passende eigene Ladeansichten verwenden. watchOS-Ladeanzeigen möglichst vermeiden; bei unvermeidbarer kurzer Wartezeit sind sie besser als eine leere Ansicht.
- **Test (Engineering-Ableitung):** Sofortantwort, langsames Netz, Offline, Fehler, erneuten Versuch und Abbruch prüfen. Kein erfundener Prozentwert; Platzhalter müssen sich zuverlässig in Inhalt oder verständlichen Fehlerzustand verwandeln. Die watchOS-Ausnahme mit der strengeren Feedback-Empfehlung abwägen, nicht pauschal einen Spinner einsetzen.

### managing-accounts — Managing accounts
Quelle: [67] https://developer.apple.com/design/human-interface-guidelines/managing-accounts

- **Aktivierung (Engineering-Ableitung):** Konten sind für Kernfunktionen notwendig oder bereits vorhanden.
- **Umsetzung (HIG):** Anmeldung möglichst spät verlangen und Nutzen erklären. Ohne Sign in with Apple auf den genannten Plattformen Passkeys bevorzugen; bei weiter benötigten Passwörtern Zwei-Faktor-Authentifizierung ergänzen. Nur tatsächlich verfügbare Authentifizierungsmethoden benennen. Kontoerstellung muss einen auffindbaren Löschweg haben, nicht bloß Deaktivierung; nötigenfalls direkt zur Löschseite verlinken. Löschdauer, Abschluss und verbleibende Abrechnung erklären. Sign-in-with-Apple-Tokens bei Löschung widerrufen. Geplante Löschung darf Sofortlöschung nicht ersetzen. TV-Provider-Abmeldung nicht mit Datenschutzschaltern verwechseln.
- **Test (Engineering-Ableitung):** Gastnutzung, Methodenwechsel, fehlende Biometrie, Löschung und laufendes Abo prüfen. App und Website müssen einen konsistenten Löschweg bieten; Löschung darf nicht fälschlich als Abokündigung bestätigt werden.

### managing-notifications — Managing notifications
Quelle: [68] https://developer.apple.com/design/human-interface-guidelines/managing-notifications

- **Aktivierung (Engineering-Ableitung):** Das Produkt benötigt zeitnahe Informationen außerhalb der aktuellen Ansicht.
- **Umsetzung (HIG):** Berechtigung einholen und systemweite Zustellplanung sowie Fokus respektieren. Kommunikation von sonstigen Mitteilungen unterscheiden. Unterbrechungsniveau nach tatsächlicher Dringlichkeit wählen: passiv, aktiv, zeitkritisch oder kritisch. Zeitkritisch nur für unmittelbar relevante Ereignisse; niemals für Marketing. Kritische Mitteilungen benötigen ein Entitlement. Werbung erfordert Zustimmung und eine in der App zugängliche Änderungsmöglichkeit für die Benachrichtigungswahl.
- **Test (Engineering-Ableitung):** Verweigerte/entzogene Berechtigung, Fokus, geplante Zustellung und Marketing-Abwahl prüfen. Payloads auf falsche Dringlichkeit untersuchen; Produktfunktion darf ohne Werbeeinwilligung nicht unnötig blockieren.

### modality — Modality
Quelle: [72] https://developer.apple.com/design/human-interface-guidelines/modality

- **Aktivierung (Engineering-Ableitung):** Eine klar begrenzte Aufgabe oder kritische Entscheidung muss vorübergehend fokussiert werden.
- **Umsetzung (HIG):** Modalität nur mit erkennbarem Vorteil einsetzen. Kurze, verständliche Aufgaben bevorzugen; keine zweite App in einem Modal bauen. Umfangreiche Aufgaben können eine Vollbildpräsentation benötigen; separate Fenster sind auf geeigneten Plattformen eine Alternative. Aufgabe klar benennen und einen offensichtlichen Abschluss-/Abbruchweg bieten. Vor verlustbehaftetem Schließen nötigenfalls bestätigen lassen. Erst das aktuelle Modal beenden, bevor ein weiteres präsentiert wird.
- **Test (Engineering-Ableitung):** Öffnen, Erledigen, Abbrechen, interaktives Schließen und ungesicherte Änderungen testen. Fokus und Ausgangskontext müssen wiederhergestellt werden. Verschachtelte Präsentationen und unentrinnbare Zustände gezielt suchen.

### multitasking — Multitasking
Quelle: [74] https://developer.apple.com/design/human-interface-guidelines/multitasking

- **Aktivierung (Engineering-Ableitung):** Appwechsel, mehrere Fenster oder parallele Mediennutzung sind möglich.
- **Umsetzung (HIG):** Aufmerksamkeitsgebundene Tätigkeiten bei Verlassen geeignet pausieren und fortsetzbar halten; angestoßene Aufgaben soweit möglich im Hintergrund abschließen. Lange Audio-Unterbrechungen anders behandeln als kurze Ansagen. Layout an Fenstergrößen anpassen, statt gewählte Multitasking-Konfiguration zu erraten. Systemverhalten nicht aushebeln. Auf visionOS Video nicht wegen eines Blickwechsels pausieren; Audio-Ducking und das Pausieren beim Schließen des Now-Playing-Fensters berücksichtigen.
- **Test (Engineering-Ableitung):** Mehrere Fenster, Größenwechsel, Hintergrund-/Vordergrundwechsel, Picture in Picture und kurze/lange Audio-Unterbrechungen prüfen. Zustände verschiedener Dokumentfenster dürfen sich nicht unbeabsichtigt überschreiben.

### offering-help — Offering help
Quelle: [78] https://developer.apple.com/design/human-interface-guidelines/offering-help

- **Aktivierung (Engineering-Ableitung):** Eine konkrete Funktion bleibt trotz klarer Oberfläche erklärungsbedürftig.
- **Umsetzung (HIG):** Kontextbezogene, inklusive Hilfe mit konsistenter Sprache und Bildern anbieten. Keine Anleitung für ohnehin bekannte Systembedienung schreiben. Tipps auf einfache Funktionen begrenzen, kurz und handlungsorientiert formulieren und über passende Auslöseregeln zielgerichtet anzeigen. Tooltips beschreiben die Aktion des interessierenden Controls statt dessen Namen zu wiederholen; bei Bedarf zustandsabhängig formulieren. Direkte Bildwiederholung zwischen Control und Tipp vermeiden.
- **Test (Engineering-Ableitung):** Erfahrene und neue Nutzung, erledigte Tipps, relevante Zustände und Assistenztechnik prüfen. Ein Tipp darf keine wichtige Aktion verdecken oder nach erfolgreicher Nutzung ständig wiederkehren.

### onboarding — Onboarding
Quelle: [79] https://developer.apple.com/design/human-interface-guidelines/onboarding

- **Aktivierung (Engineering-Ableitung):** Einstieg oder notwendige Voraussetzungen lassen sich nicht ausreichend im normalen Ablauf vermitteln.
- **Umsetzung (HIG):** Erst nach dem Start beginnen. Möglichst durch Benutzung und kontextuelle Tipps lehren; separate Tutorials optional machen. Unverzichtbare Einführung kurz halten, nicht zum Auswendiglernen zwingen. Nichtessenzielle Konfiguration verschieben, sinnvolle Voreinstellungen wählen. Große Downloads, Lizenzdetails, frühe Bewertungs- oder Kaufaufforderungen nicht zum Hindernis machen. Nur tatsächlich vorab benötigte private Ressourcen rechtfertigen integrierte Berechtigungsanfragen.
- **Test (Engineering-Ableitung):** Erster Start, Überspringen, Wiederkehr, verweigerte Berechtigung und langsamen Download prüfen. Kernnutzen muss ohne unnötige Vorbereitung erreichbar sein; ein übersprungenes Tutorial darf kein dauerhaftes Wissensloch erzeugen.

### playing-audio — Playing audio
Quelle: [81] https://developer.apple.com/design/human-interface-guidelines/playing-audio

- **Aktivierung (Engineering-Ableitung):** Die App erzeugt oder spielt Audio.
- **Umsetzung (HIG):** Audio-Kategorie passend zur Funktion wählen. Systemlautstärke nicht eigenmächtig ändern; nötigenfalls relative Pegel anpassen. System-Lautstärke-/Routing-Bedienung und vertraute Transportbefehle bevorzugen. Audio-Steuerelemente nicht umdeuten. Unterbrechungen und Wiederaufnahme bewusst behandeln; nach temporärer Belegung andere Audio-Apps freigeben. Routing ermöglichen. Auf visionOS räumliche Quellen passend zum Inhalt gestalten und wichtige Informationen zusätzlich nichtakustisch vermitteln. Systemverhalten beim Blickwechsel oder Fensterschließen respektieren.
- **Test (Engineering-Ableitung):** Stummschaltung, Hintergrundmusik, Anruf, kurze Navigationsansage, Kopfhörerentfernung, Route-Wechsel und Remote-Befehle prüfen. Wiederaufnahme darf weder überraschend erfolgen noch andere Wiedergabe unbeabsichtigt verdrängen.

### playing-haptics — Playing haptics
Quelle: [82] https://developer.apple.com/design/human-interface-guidelines/playing-haptics

- **Aktivierung (Engineering-Ableitung):** Taktile Rückmeldung unterstützt eine konkrete Interaktion auf geeigneter Hardware.
- **Umsetzung (HIG):** Systemmuster entsprechend ihrer Bedeutung verwenden; etwa Ergebnis, physische Kollision und Auswahländerung nicht vertauschen. Konsistent, meist kurz und ergänzend zu anderer Rückmeldung einsetzen. Abschalten ermöglichen; die App muss ohne Haptik funktionieren. Kamera, Mikrofon und Bewegungssensoren nicht durch Vibration beeinträchtigen. Eigene Muster nur bei sinnvollem Mehrwert; Plattform-/Controller-Möglichkeiten unterscheiden.
- **Test (Engineering-Ableitung):** Auf echter Hardware mit und ohne Haptik prüfen. Erfolg und Fehler müssen weiterhin eindeutig sein; wiederholte Aktionen dürfen nicht ermüden oder Aufnahme/Sensordaten stören.

### playing-video — Playing video
Quelle: [83] https://developer.apple.com/design/human-interface-guidelines/playing-video

- **Aktivierung (Engineering-Ableitung):** Video ist Inhalt oder Bestandteil eines Ablaufs.
- **Umsetzung (HIG):** Systemplayer und erwartete Eingaben bevorzugen; ursprüngliches Seitenverhältnis erhalten. Konkurrierendes Audio vermeiden. Beim Einstieg aus der TV-App erwarteten Inhalt direkt zeigen, möglichst fortsetzen und beim Verlassen einen passenden Kontext bereitstellen. Ladeunterbrechungen minimieren. Auf visionOS Wiedergabe und Immersion nicht überraschend starten, Umgebung und Controls zugänglich lassen; für Scrubbing geeignete Vorschaubilder liefern. Auf watchOS kurze Clips bevorzugen. Poster müssen zum Inhalt passen, nicht Systembuttons imitieren.
- **Test (Engineering-Ableitung):** Fortsetzen, sofortigen Ausstieg, Untertitel, Audioauswahl, Tastatur/Remote, Verhältniswechsel und langsames Streaming prüfen. Vollimmersiver Einstieg benötigt bewusste Nutzerentscheidung.

### printing — Printing
Quelle: [86] https://developer.apple.com/design/human-interface-guidelines/printing

- **Aktivierung (Engineering-Ableitung):** Druckbare Dokumente und eine unterstützte Plattform machen Drucken sinnvoll.
- **Umsetzung (HIG):** System-Druckdialog und vertraute Positionen verwenden, auf macOS insbesondere das Datei-Menü. Bei unmöglichem Druck Aktionen plattformgerecht deaktivieren oder entfernen. Nur passende, vom Drucker unterstützte Optionen anbieten. Eigene macOS-Optionen in eigener Kategorie, seltene Optionen getrennt darstellen; Abhängigkeiten verständlich machen. Systemeinstellungen nicht duplizieren; Vorschau und dokumentbezogene Speicherung erwägen. Nicht für tvOS/watchOS anbieten.
- **Test (Engineering-Ableitung):** Kein Dokument, kein Drucker, Seitenbereich, Duplex-Abhängigkeit, Abbruch und Vorschau prüfen; nicht unterstützte Kombinationen dürfen nicht stillschweigend akzeptiert werden.

### ratings-and-reviews — Ratings and reviews
Quelle: [88] https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews

- **Aktivierung (Engineering-Ableitung):** Ein Produktauftrag sieht eine Bewertungsanfrage vor und Nutzungserfahrung liegt vor.
- **Umsetzung (HIG):** Erst nach erkennbarem Engagement und an natürlichen Unterbrechungspunkten fragen, nie direkt beim Erststart oder während Onboarding. Nicht drängen oder laufende Arbeit unterbrechen. System-Prompt bevorzugen und dessen Entscheidung über Anzeige respektieren. Ein Zurücksetzen der zusammengefassten Bewertung gegen die dann geringere Bewertungsmenge abwägen.
- **Test (Engineering-Ableitung):** Erststart, laufende Aufgabe, wiederholte Nutzung und unterdrückten Systemdialog prüfen. Funktionsfortschritt darf nicht davon abhängen, ob der Bewertungsdialog tatsächlich erscheint oder beantwortet wird.

### searching — Searching
Quelle: [92] https://developer.apple.com/design/human-interface-guidelines/searching

- **Aktivierung (Engineering-Ableitung):** Inhalt muss auffindbar sein oder Dokumente benötigen eine Suche.
- **Umsetzung (HIG):** Wichtige Suche prominent und möglichst über einen gemeinsamen Einstieg anbieten. Lokale Suche nur mit eindeutigem Suchbereich. Vorschläge und Verlauf können Tipparbeit senken; Privatsphäre beachten und Verlauf löschbar machen. Suchbare Inhalte für Spotlight erschließen, passende Metadaten bereitstellen. Bei eigenen Dateitypen Vorschau/Quick Look und Metadatenimport berücksichtigen. System-Öffnen-/Sichern-Ansichten mit vorhandener Suche bevorzugen.
- **Test (Engineering-Ableitung):** Globale/lokale Bereiche, leere Ergebnisse, Vorschläge, Verlaufslöschung und Spotlight-Zielöffnung prüfen. Nach Wechsel des Bereichs darf die UI nicht Ergebnisse aus dem vorherigen Bereich als aktuelle ausgeben.

### settings — Settings
Quelle: [94] https://developer.apple.com/design/human-interface-guidelines/settings

- **Aktivierung (Engineering-Ableitung):** Eine sinnvolle, wiederkehrende Nutzerpräferenz ist tatsächlich erforderlich.
- **Umsetzung (HIG):** Gute Defaults und wenige Einstellungen bevorzugen. Systemweite Präferenzen respektieren, nicht als irreführende Kopien anbieten. Aufgabenbezogene Optionen direkt im betroffenen Kontext platzieren; allgemeine seltene Optionen in App-Einstellungen. Sehr seltene Optionen gegebenenfalls in Systemeinstellungen. macOS: App-Menü und Command-Komma, stabile Pane-Navigation, passender Fenstertitel und zuletzt verwendetes Pane. watchOS fügt keine eigenen Bereiche zur System-Settings-App hinzu; wenige wesentliche Optionen im App-Kontext anbieten.
- **Test (Engineering-Ableitung):** Frische Installation ohne Konfiguration nutzen; Systempräferenzen ändern; Persistenz, Tastaturöffnung und Wiederöffnung prüfen. Eine globale Einstellung darf nicht unbeabsichtigt als dokumentbezogene Option wirken.

### undo-and-redo — Undo and redo
Quelle: [105] https://developer.apple.com/design/human-interface-guidelines/undo-and-redo

- **Aktivierung (Engineering-Ableitung):** Änderbare Inhalte oder reversible Aktionen sind vorhanden.
- **Umsetzung (HIG):** Mehrstufiges Rückgängig/Wiederholen erlauben und Zielaktion verständlich benennen. Ergebnis sichtbar machen, auch wenn der betroffene Bereich außerhalb des sichtbaren Ausschnitts liegt. Zusammenhängende Änderungen gegebenenfalls sinnvoll gruppieren. Standardgesten und Tastaturbefehle erhalten; zusätzliche Toolbar-Buttons nur bei Bedarf. macOS-Befehle gehören ins Bearbeiten-Menü mit Command-Z beziehungsweise Shift-Command-Z. Dieses Systempattern nicht unverändert auf tvOS/watchOS übertragen.
- **Test (Engineering-Ableitung):** Mehrere Änderungen, gruppierte Anpassungen, neue Änderung nach Undo, unsichtbaren Zielbereich und Dokumentwechsel testen. Redo muss korrekte Daten wiederherstellen; Undo darf kein anderes Dokument verändern.

### workouts — Workouts
Quelle: [108] https://developer.apple.com/design/human-interface-guidelines/workouts

- **Aktivierung (Engineering-Ableitung):** Eine unterstützte Fitness-App zeichnet echte Trainingseinheiten auf.
- **Umsetzung (HIG):** In aktiven watchOS-Sessions wichtige Messwerte und gut erreichbare Start-/Pause-/Ende-Controls zeigen, irrelevante Navigation zurücknehmen. Aktive Sitzung visuell unterscheiden und Statusänderungen rückmelden. Ausfall einzelner Sensorwerte verständlich erklären. Abschlusszusammenfassung bereitstellen; versehentlich extrem kurze Sitzungen verwerfen oder nachfragen. Bewegungsgeeignete große, kontrastreiche Darstellung wählen. Activity-Ringe nur für ihre dokumentierte Bedeutung nutzen.
- **Test (Engineering-Ableitung):** Start, Pause, Fortsetzen, Ende, Sensorverlust und versehentlichen Kurzstart prüfen. Zusammenfassung darf fehlende Messwerte nicht als echte Nullmessung darstellen.

## Technologies — bedarfsgesteuert, nicht als Feature-Checkliste

### technologies — Technologies
Quelle: [7] https://developer.apple.com/design/human-interface-guidelines/technologies

- **Aktivierung (Engineering-Ableitung):** Ein bestätigter Anwendungsfall benötigt eine Apple-Technologie.
- **Umsetzung (HIG):** Die Kategorie beschreibt integrierbare Technologien, Funktionen und Dienste; sie verlangt nicht, alle davon einzubauen.
- **Test (Engineering-Ableitung):** Vor jeder Integration Nutzungsnutzen, Zielplattform, Verfügbarkeit, Berechtigungen, Entitlements und Verhalten ohne Feature festhalten. Ohne begründeten Bedarf keine neuen Framework-Abhängigkeiten, Prompts oder Produktabläufe ergänzen.

### airplay — AirPlay
Quelle: [10] https://developer.apple.com/design/human-interface-guidelines/airplay

- **Aktivierung (Engineering-Ableitung):** Bestehende Medienwiedergabe soll auf externe Geräte übertragen werden.
- **Umsetzung (HIG):** Systemplayer, hohe Inhaltsauflösung, Streaming und Spiegelung bevorzugen. Nur erwartete Medien übertragen, nicht beiläufige UI-Loops. Remote-Befehle unterstützen; Wiedergabe bei Gerätesperre oder Hintergrundwechsel erhalten. Andere Audiowiedergabe nicht grundlos unterbrechen. Weitere App-Nutzung während Wiedergabe ermöglichen. Offizielle AirPlay-Darstellung verwenden; keine eigenen interaktiven Controls mit AirPlay-Icon oder -Namen erfinden. Nicht für watchOS annehmen.
- **Test (Engineering-Ableitung):** Empfängerwechsel, Sperre, Hintergrund, Remote-Pause und Rückkehr testen. Private beziehungsweise rein lokale UI-Inhalte dürfen nicht versehentlich als externe Medien ausgegeben werden.

### always-on — Always On
Quelle: [11] https://developer.apple.com/design/human-interface-guidelines/always-on

- **Aktivierung (Engineering-Ableitung):** Vorhandene iPhone-Lockscreen-/Watch-Oberflächen erscheinen auf Always-On-fähiger Hardware.
- **Umsetzung (HIG):** Sensible Daten verbergen; kontextuell sinnvolle Informationen etwa im Training weiterhin ablesbar halten. Wesentliches lesbar, Sekundäres gedimmt darstellen. Layout beim Übergang stabil halten, Interaktivität eher deaktiviert darstellen als Elemente abrupt entfernen. Bewegung sanft auslaufen lassen und Aktualisierungen sparsam halten. Nutzerentscheidung zum Abschalten respektieren.
- **Test (Engineering-Ableitung):** Aktiv-, gedimmten und wieder aktivierten Zustand auf Gerät prüfen. Datenschutzredaktion, Lesbarkeit und stabile Positionen vergleichen; geheime Werte dürfen nicht kurz während des Übergangs sichtbar werden.

### app-clips — App Clips
Quelle: [12] https://developer.apple.com/design/human-interface-guidelines/app-clips

- **Aktivierung (Engineering-Ableitung):** Eine kurze, kontextuelle Aufgabe oder Demo benötigt Zugang ohne Vollinstallation.
- **Umsetzung (HIG):** Klein, unmittelbar nutzbar, linear und auf Abschluss konzentriert gestalten; nicht bloß Werbung oder Webview-Hülle. Direkt passenden Inhalt öffnen. Kontoerstellung vermeiden, datensparsame Zahlung ermöglichen. Voll-App erst passend und unaufdringlich empfehlen; Mitteilungen auf die Aufgabe begrenzen. Kartenbild und Kurztext informativ gestalten. Generierte App Clip Codes unverändert gemäß Vorgaben einsetzen: guter Kontrast, geeignete Oberfläche, ausreichende Größe/Freiräume, ungehinderte Scanposition; Druckworkflow verifizieren.
- **Test (Engineering-Ableitung):** Aufruf aus verschiedenen Kontexten, Aufgabenerfolg ohne Konto, Zustandsübergang zur Voll-App und reale gedruckte Codes testen. Installationswerbung darf den Abschluss nicht verdrängen.

### apple-in-app-purchase — In-app purchase
Quelle: [14] https://developer.apple.com/design/human-interface-guidelines/apple-in-app-purchase

- **Aktivierung (Engineering-Ableitung):** Der beauftragte Ablauf verkauft digitale Inhalte oder Abonnements über In-App Purchase.
- **Umsetzung (HIG):** Nutzen vor Kauf erfahrbar machen; präzise Produkte und Gesamt-Abrechnungspreise zeigen. Systembestätigung verwenden. Abos klar unterscheidbar, Laufzeit, Verlängerung, Probezeit und Kosten transparent darstellen. Bestehenden Abonnenten keine neue Anmeldung aufdrängen. Verwaltung, Kündigung und Rückerstattungsanfrage leicht erreichbar machen; keine eigene Zusage zu Apples Erstattungspolitik. Family Sharing bei Unterstützung erklären, Käufer und Familienmitglieder unterscheiden. Angebotscodes verständlich erläutern und Freischaltung unmittelbar nutzbar machen. watchOS darf Pflichtinformationen nicht weglassen.
- **Test (Engineering-Ableitung):** Kaufabbruch, ausstehende Zahlung, vorhandenes Abo, Familienzugriff, Codeeinlösung, Verlängerung und Kündigungsweg testen. Keine lokale Erfolgsanzeige ohne bestätigte Berechtigung.

### apple-pay — Apple Pay
Quelle: [15] https://developer.apple.com/design/human-interface-guidelines/apple-pay

- **Aktivierung (Engineering-Ableitung):** Physische Waren, passende Dienstleistungen oder Spenden werden im bestätigten Checkout bezahlt; digitale Inhalte nicht automatisch diesem Flow zuordnen.
- **Umsetzung (HIG):** Unterstützung prüfen; wenn aktive Karten per API geprüft werden, Apple Pay als primäre Option anbieten. Offizielle Button-API nutzen; Markenzeichen ist kein Zahlungsbutton. Produktvarianten und nötige Vorentscheidungen vor dem Payment Sheet erfassen. Keine Kontoerstellung erzwingen, nur erforderliche Daten abfragen. Betrag, Händler, Gebühren, Rabatte und mögliche spätere Kosten eindeutig zeigen. Fehler, Fortschritt und Zahlungsergebnis im Systemflow melden, anschließend Bestätigung anzeigen.
- **Test (Engineering-Ableitung):** Nicht unterstütztes Gerät, fehlende Einrichtung, Coupon, Versandänderung, Autorisierungsabbruch und Verarbeitungsfehler prüfen. Endsumme und tatsächliche Bestellung müssen übereinstimmen; Wiederholung darf keine Doppelbestellung erzeugen.

### augmented-reality — Augmented reality
Quelle: [17] https://developer.apple.com/design/human-interface-guidelines/augmented-reality

- **Aktivierung (Engineering-Ableitung):** Ein begründeter räumlicher Anwendungsfall benötigt AR auf geeigneter Hardware.
- **Umsetzung (HIG):** Gerätefähigkeit prüfen; iOS/iPadOS-Kamera-AR nicht ungeprüft auf visionOS übertragen. Umgebung und virtuelle Objekte priorisieren, Text und Controls sparsam halten. Sicherheit, Komfort und unterschiedliche reale Räume berücksichtigen; Bewegung schrittweise einführen. Coaching, verständliche Platzierung, direkte Manipulation und klare Tracking-Rückmeldung anbieten. Unsichere Flächengrenzen nicht als präzise Geometrie behandeln. Relokalisierung abbrechbar und Neustart möglich machen. AR-Glyphen/Badges ausschließlich bestimmungsgemäß verwenden.
- **Test (Engineering-Ableitung):** Schlechte Beleuchtung, kleine Fläche, Trackingverlust, Unterbrechung, Relokalisierungsabbruch und kollidierende Gesten auf Gerät prüfen. Nutzer dürfen weder durch virtuelle Hindernisse noch unerwartete Bewegung gefährdet werden.

### carekit — CareKit
Quelle: [20] https://developer.apple.com/design/human-interface-guidelines/carekit

- **Aktivierung (Engineering-Ableitung):** Eine iOS/iPadOS-Anwendung unterstützt einen konkreten Pflege- oder Gesundheitsplan.
- **Umsetzung (HIG):** Gesundheitsdaten schützen, Datenschutz erklären und Zugriff bedarfsgerecht anfragen; Freigaben über System-Datenschutzverwaltung führen. Aufgabenansichten nach Zweck wählen: einfacher Schritt, Anleitung, Ereignisprotokoll, Checkliste oder Raster. Schritte präzise und leicht verständlich beschreiben. Diagramme mit klaren Einheiten, Legenden und erkennbaren Trends gestalten; große Datenmengen verdichten. Passende Kontaktansichten für Betreuungspersonen anbieten, Mitteilungen reduzieren und Branding zurückhalten.
- **Test (Engineering-Ableitung):** Verweigerte Datenfreigabe, mehrschrittige Aufgabe, Ereignisprotokoll und Kontaktaktion prüfen. Diagramme auf fehlende Werte und Mehrdeutigkeit testen; Farbe darf keine alleinige medizinische Aussage tragen.

### carplay — CarPlay
Quelle: [21] https://developer.apple.com/design/human-interface-guidelines/carplay

- **Aktivierung (Engineering-Ableitung):** Ein bestätigter, geeigneter Fahrzeug-Anwendungsfall wird per CarPlay unterstützt.
- **Umsetzung (HIG):** Fahrkontext und minimale Ablenkung priorisieren; Systemtemplates verwenden. Bedienung und Fehlerbehandlung im Fahrzeug ermöglichen, nicht zum verbundenen iPhone schicken. Einrichtung vor Fahrtantritt erledigen; auch bei gesperrtem iPhone funktionsfähig bleiben. Audio erst auf Wunsch starten, nach ausreichendem Laden abspielen und Unterbrechungen angemessen behandeln. Klare, schnell erfassbare Inhalte, helle/dunkle Darstellung und passende hochauflösende Assets bereitstellen.
- **Test (Engineering-Ableitung):** Gesperrtes/unzugängliches iPhone, Fehler, Audio-Unterbrechung und verschiedene Displays prüfen; Lichtverhältnisse sicher im stehenden Fahrzeug testen, nicht während eigener Fahrt.

### game-center — Game Center
Quelle: [43] https://developer.apple.com/design/human-interface-guidelines/game-center

- **Aktivierung (Engineering-Ableitung):** Ein Spiel benötigt soziale Funktionen, Fortschritt, Ranglisten oder Multiplayer-Aktivitäten.
- **Umsetzung (HIG):** Access Point in Menüs platzieren und Nachbarcontrols freihalten; bei geöffnetem Overlay Pausieren erwägen. Offizielle Assets und Begriffe verwenden. Achievements mit nachvollziehbarem Fortschritt und Reihenfolge gestalten. Passenden Ranglistentyp wählen, mehrere Listen sinnvoll gruppieren. Challenges auf vergleichbare Versuche statt lebenslangen Fortschritt ausrichten. Party Codes und direkte Spieleinstiege unterstützen. watchOS besitzt keine aufrufbare System-Game-Center-UI.
- **Test (Engineering-Ableitung):** Overlay, Achievement-Zustand, Ranglistenperiode, manuelle Codeeingabe und spätes Beitreten prüfen. Abgemeldete beziehungsweise nicht unterstützte Konfiguration darf das lokale Spiel nicht unerwartet blockieren.

### generative-ai — Generative AI
Quelle: [45] https://developer.apple.com/design/human-interface-guidelines/generative-ai

- **Aktivierung (Engineering-Ableitung):** Generative Funktion ist ausdrücklich begründet; nicht als Standarddekoration einbauen.
- **Umsetzung (HIG):** KI-Einsatz, Fähigkeiten, Grenzen und Datenverwendung transparent machen. Menschen kontrollieren Ergebnis und folgenreiche Aktionen; vor irreversiblen oder problematischen Handlungen Zustimmung einholen. Ohne KI beziehungsweise bei Abwahl eine gute Erfahrung erhalten. Modelle und Datensätze bewusst evaluieren, Inklusion und Datenschutz berücksichtigen. Halluzinationen, schädliche Ausgaben und Urheberrechtsreplikation reduzieren. Ergebnisse verfeinerbar und rücknehmbar machen; Blockaden, Generierungszeit und Korrekturen erklären. Feedback ermöglichen.
- **Test (Engineering-Ableitung):** Abwahl, Nichtverfügbarkeit, Halluzination, schädliche Anfrage, langsame Generierung, Abbruch und Rücknahme prüfen. Externe Schreibaktionen dürfen nicht allein durch erzeugten Text ungeprüft ausgeführt werden.

### healthkit — HealthKit
Quelle: [49] https://developer.apple.com/design/human-interface-guidelines/healthkit

- **Aktivierung (Engineering-Ableitung):** Eine bestätigte Gesundheitsfunktion benötigt entsprechende Daten auf unterstützter Plattform.
- **Umsetzung (HIG):** Klare Datenschutzinformationen liefern, Zugriff erst bei Bedarf mit verständlichem Zweck anfragen und Freigaben der Systemverwaltung überlassen. Activity-Ringe nur für Move, Exercise und Stand einer Person nutzen, nie als Dekoration oder Branding; Farben und Freiräume erhalten. Apple-Health-Icon unverändert und nicht als Button einsetzen. Nutzerseitig Apple Health beziehungsweise die systemgerechte lokalisierte Bezeichnung verwenden, nicht den Frameworknamen als Produktbezeichnung.
- **Test (Engineering-Ableitung):** Teilweise/entzogene Freigaben, fehlende Daten und Ringdarstellung prüfen. Nichtverfügbarkeit darf nicht als gemessener Gesundheitszustand ausgegeben werden; keine selbstgebauten Freigabeschalter suggerieren Systemberechtigung.

### homekit — HomeKit
Quelle: [50] https://developer.apple.com/design/human-interface-guidelines/homekit

- **Aktivierung (Engineering-Ableitung):** Die App steuert oder konfiguriert kompatible Geräte in einem Zuhause.
- **Umsetzung (HIG):** Hierarchie aus Zuhause, Räumen, Geräten und Diensten respektieren; mehrere Zuhause unterstützen. System-Setup bevorzugen, Zugriff erklären und keine unnötigen Konten oder Personendaten verlangen. Namenswahl nach HomeKit-Regeln erleichtern; Ortsinformation nicht in Gerätenamen duplizieren. Setup-Entscheidungen erhalten. Bei Datenkonflikten HomeKit Vorrang geben; Änderungen an dessen Datenbank mit Zustimmung durchführen. Zusätzliche Shortcuts nur für nicht abgedeckte gerätespezifische Funktionen. Kamerabilder nicht verdecken, Mikrofonaktion nur bei bidirektionalem Audio.
- **Test (Engineering-Ableitung):** Mehrere Zuhause, Umbenennen, verweigerter Zugriff, offline befindliches Zubehör und Datenkonflikte prüfen. Anzeigezustand muss zum tatsächlich gesteuerten Gerät passen.

### icloud — iCloud
Quelle: [51] https://developer.apple.com/design/human-interface-guidelines/icloud

- **Aktivierung (Engineering-Ableitung):** Geräteübergreifende Inhalte oder Zustandsfortsetzung sind bestätigte Anforderungen.
- **Umsetzung (HIG):** Synchronisation möglichst transparent halten, nicht Dokument für Dokument konfigurieren lassen. Aktuelle Inhalte, Suchbarkeit und sinnvolle geräteübergreifende Einstellungen unterstützen; große Downloads gegebenenfalls steuerbar machen. Bezahlten Speicher nicht mit reproduzierbaren Ressourcen verschwenden. Offline-/deaktivierten Zustand unaufdringlich erklären. Konflikte früh automatisch oder verständlich auflösen. Vor Dokumentlöschung warnen, dass sie iCloud und weitere Geräte betrifft, und bestätigen lassen.
- **Test (Engineering-Ableitung):** Zwei Geräte, gleichzeitige Bearbeitung, Offlineänderung, erneute Verbindung, Speicherknappheit und synchronisierte Löschung testen. Kein stilles Überschreiben; lokale Einstellungen nicht ohne Produktentscheidung global synchronisieren.

### id-verifier — ID Verifier
Quelle: [53] https://developer.apple.com/design/human-interface-guidelines/id-verifier

- **Aktivierung (Engineering-Ableitung):** Ein iPhone-basierter Vor-Ort-Prozess muss mobile Identität oder Mindestalter prüfen.
- **Umsetzung (HIG):** Nur benötigte Attribute anfordern; für Altersgrenze keinen vollständigen Geburtstag verlangen. Display Only hält Identitätsdaten in der Systemansicht. Data Transfer nur bei rechtlicher Prüfnotwendigkeit und erforderlichem zusätzlichem Entitlement verwenden. Organisationsdarstellung bei Berechtigung registrieren. Klar beschriftete Verifikationsaktion ohne Apple-Logo oder Kommunikationssymbol anbieten. Visuellen Abgleich mit eindeutigem Bestätigen/Ablehnen unterstützen.
- **Test (Engineering-Ableitung):** Altersgrenze, verweigerte Präsentation, Nichtübereinstimmung und Entitlement-Fehlen prüfen. Bei Display Only dürfen Identitätsdaten nicht als App-verfügbare Nutzdaten behandelt werden.

### imessage-apps-and-stickers — iMessage apps and stickers
Quelle: [55] https://developer.apple.com/design/human-interface-guidelines/imessage-apps-and-stickers

- **Aktivierung (Engineering-Ableitung):** Ein bestätigtes Messaging-Erlebnis oder Stickerangebot benötigt eine Erweiterung.
- **Umsetzung (HIG):** Auf eine primäre Erfahrung konzentrieren; vorhandenen App-Inhalt gegebenenfalls nutzbar machen. Wesentliche Funktionen im kompakten Zustand bereitstellen, Texteingabe gewöhnlich in die erweiterte Ansicht legen. Ausdrucksstarke, inklusive und vielseitig einsetzbare Sticker gestalten; jeden Sticker mit lokalisierter Alternativbeschreibung versehen. Asset-Größen gemäß Originaltabellen wählen.
- **Test (Engineering-Ableitung):** Kompakt/erweitert, Texteingabe, Sticker-Versand und VoiceOver in mehreren Sprachen prüfen. Beschreibungen müssen den Ausdruck vermitteln, nicht lediglich Dateinamen vorlesen.

### live-photos — Live Photos
Quelle: [62] https://developer.apple.com/design/human-interface-guidelines/live-photos

- **Aktivierung (Engineering-Ableitung):** Die App zeigt, bearbeitet oder teilt Live Photos.
- **Umsetzung (HIG):** Anpassungen auf alle Frames anwenden und den vollständigen Live-Photo-Inhalt bewahren. Download und Abspielbarkeit erkennbar machen, konsistente Kennzeichnung gegenüber Standfotos verwenden. Teilen angemessen unterstützen und in nicht unterstützten Umgebungen ein normales Foto zeigen. visionOS kann Live Photos anzeigen, aber nicht aufnehmen.
- **Test (Engineering-Ableitung):** Bearbeitung, Export/Teilen, noch laufenden Download, Wiedergabe und Standbild-Fallback prüfen. Bewegung oder Ton dürfen nicht unbemerkt beim Roundtrip verloren gehen.

### mac-catalyst — Mac Catalyst
Quelle: [65] https://developer.apple.com/design/human-interface-guidelines/mac-catalyst

- **Aktivierung (Engineering-Ableitung):** Eine iPad-App wird gezielt mit Catalyst für macOS adaptiert.
- **Umsetzung (HIG):** Drag-and-drop, Tastaturnavigation, Multitasking und mehrere Fenster berücksichtigen. Idiom bewusst wählen; bei Mac-Idiom Layout, Schriftgrößen, Bilder und Ansichten vollständig prüfen. Navigation und wesentliche Tab-Aktionen erreichbar halten. Mac-App-Icon, Menüs und Toolbar angemessen gestalten; Bedienelemente von unteren/seitlichen Rändern gegebenenfalls nach oben verlagern. Nicht bloß eine Touch-Oberfläche unverändert auf den Mac übertragen.
- **Test (Engineering-Ableitung):** Maus-only, Tastatur-only, verschiedene Fenstergrößen, Menübefehle, Navigation und mehrere Dokumentfenster testen. iPad-spezifische Annahmen über Abstände und Eingabegeräte gezielt suchen.

### machine-learning — Machine learning
Quelle: [66] https://developer.apple.com/design/human-interface-guidelines/machine-learning

- **Aktivierung (Engineering-Ableitung):** Eine bestätigte Funktion verwendet Vorhersagen, Empfehlungen oder Erkennung.
- **Umsetzung (HIG):** Rolle, Sichtbarkeit, Proaktivität, Datenschutz und Fehlerfolgen zuerst bestimmen. Explizites Feedback freiwillig und verständlich gestalten, Korrekturen wirksam und rücknehmbar machen. Implizite Signale datensicher, aktuell und ohne einengende Bestätigungsschleifen nutzen. Kalibrierung kurz, erklärbar, abbrechbar und löschbar halten. Unsicherheit verständlich statt durch irreführende Zahlen kommunizieren; schwache Ergebnisse gegebenenfalls zurückhalten. Optionen unterscheidbar und vielfältig anbieten. Grenzen erklären; schlechte Qualität nicht durch ständige Nutzerkorrektur kompensieren.
- **Test (Engineering-Ableitung):** Fehlklassifikation, niedrige Konfidenz, Präferenzwechsel, Kalibrierungsabbruch und Feedback-Rücknahme prüfen. Verbesserung einer Metrik darf andere Gruppen oder Fehlerklassen nicht unbemerkt verschlechtern.

### maps — Maps
Quelle: [69] https://developer.apple.com/design/human-interface-guidelines/maps

- **Aktivierung (Engineering-Ableitung):** Geografischer Kontext oder Ortsauswahl trägt zur Aufgabe bei.
- **Umsetzung (HIG):** Karte in der Regel interaktiv gestalten, passenden Schwerpunkt wählen und Auswahl klar hervorheben. Überlappende Punkte clustern, Apple-Logo und Rechtshinweis sichtbar halten. Eigene Annotationen/Overlays kontrastreich integrieren. Place Cards dürfen den betreffenden Ort nicht verdecken oder Informationen unnötig duplizieren. Indoor-Karten brauchen passende Zoomdetails und bei mehreren Etagen eine Etagenwahl. Die beschriebene watchOS-`WKInterfaceMap`-Ansicht ist ein statischer Ausschnitt mit Öffnung in Maps, keine frei navigierbare Karte.
- **Test (Engineering-Ableitung):** Dichte Punkte, Place Card, kleine Fenster, Etagenwechsel und rechtliche Kennzeichnungen prüfen. Alle wichtigen Orte müssen im vorgesehenen Watch-Ausschnitt sichtbar sein.

### nfc — NFC
Quelle: [77] https://developer.apple.com/design/human-interface-guidelines/nfc

- **Aktivierung (Engineering-Ableitung):** Unterstützte Hardware soll reale Objekte per NFC auslesen.
- **Umsetzung (HIG):** In-App-Scan und auf geeigneten Geräten Hintergrundlesen unterstützen. Verständliche kurze Anweisung mit benanntem Objekt geben; Nähe genügt, keine Berührung verlangen. Fachbegriffe wie NFC/Tag nicht unnötig zur Nutzersprache machen. Hintergrundlesen ist nicht unter allen Bedingungen verfügbar, etwa bei gleichzeitigem Scan-Sheet, Wallet-/Kameranutzung oder bestimmten Sperrzuständen. Gerätefähigkeit separat prüfen, nicht aus dem Plattformkapitel ableiten.
- **Test (Engineering-Ableitung):** In-App- und Hintergrundscan, inkompatibles Objekt, wiederholten Scan und blockierende Gerätezustände prüfen. Ohne Hintergrundlesen muss ein auffindbarer manueller Scanweg bleiben.

### photo-editing — Photo editing
Quelle: [80] https://developer.apple.com/design/human-interface-guidelines/photo-editing

- **Aktivierung (Engineering-Ableitung):** Eine Photos-Bearbeitungserweiterung ist ausdrücklich vorgesehen.
- **Umsetzung (HIG):** Änderungen vor Abschluss als Vorschau zeigen. Bei Abbruch nach tatsächlichen Bearbeitungen vor Verlust warnen; unveränderte Sitzung ohne unnötige Bestätigung verlassen. Keine zweite obere Toolbar hinzufügen, weil der Host bereits eine stellt. App-Icon auch für die Erweiterung verwenden. Die Originaldatei bleibt bei Speicherung der Bearbeitung erhalten.
- **Test (Engineering-Ableitung):** Änderung/Abbruch mit und ohne Bearbeitung, Vorschau, Speichern und Originalwiederherstellung prüfen. Host- und Erweiterungscontrols dürfen nicht doppelt oder widersprüchlich auftreten.

### researchkit — ResearchKit
Quelle: [90] https://developer.apple.com/design/human-interface-guidelines/researchkit

- **Aktivierung (Engineering-Ableitung):** Eine konkret geplante Studie benötigt eine ResearchKit-Erfahrung.
- **Umsetzung (HIG):** Reihenfolge einhalten: Einführung, Eignungsprüfung, informierte Einwilligung, anschließend Geräte-/Datenberechtigungen. Studie vor Einwilligung verständlich erklären, lange Unterlagen gliedern und gegebenenfalls Verständnis prüfen. Befragungen ansprechend, aktive Aufgaben eindeutig gestalten. Profil zur Verwaltung studienbezogener Personendaten und Dashboard zur nachvollziehbaren Fortschrittsdarstellung nutzen.
- **Test (Engineering-Ableitung):** Nicht geeignete Teilnahme, verweigerte Einwilligung, abgelehnte Datenberechtigung, unterbrochene Aufgabe und Wiederaufnahme prüfen. Keine Forschungsdaten vor der vorgesehenen Einwilligung erheben; medizinische, ethische und rechtliche Freigaben gesondert nachweisen.

### shareplay — SharePlay
Quelle: [96] https://developer.apple.com/design/human-interface-guidelines/shareplay

- **Aktivierung (Engineering-Ableitung):** Menschen sollen eine Aktivität synchron in Echtzeit gemeinsam erleben.
- **Umsetzung (HIG):** Aktivität klar beschreiben, Start/Beitritt vereinfachen und plattformübergreifend gestalten. Änderungen für alle verständlich machen; bei gemeinsamen Videos Picture in Picture berücksichtigen. visionOS: Einstieg bevorzugt aus Fenster, gemeinsamer räumlicher Kontext, natürliche Konfliktlösung, individuelle Komfort-/Accessibility-Wahl und leichtes Verlassen/Wiederbeitreten. Immersionswechsel während Aufgaben opt-in. Auch Personen ohne räumliche Persona unterstützen. Sitzrollen nicht an Plätze koppeln; eigene Templates mit real zusammenstehenden Menschen und ausreichendem Abstand planen.
- **Test (Engineering-Ableitung):** Später Beitritt, Ausstieg/Wiederbeitritt, gemischte Geräte, konkurrierende Änderungen und Immersionsablehnung prüfen. Lokale Präferenzen dürfen andere Teilnehmer nicht unnötig umstellen.

### shazamkit — ShazamKit
Quelle: [97] https://developer.apple.com/design/human-interface-guidelines/shazamkit

- **Aktivierung (Engineering-Ableitung):** Audioerkennung mit Shazam- oder eigenem Katalog erfüllt eine konkrete Aufgabe.
- **Umsetzung (HIG):** Wenn das Mikrofon benötigt wird, Zugriff mit verständlichem Zweck anfragen. Nur so lange aufnehmen, wie für die Erkennung nötig, und danach sofort stoppen. Erkannte Titel nur nach Opt-in in der iCloud-Bibliothek speichern.
- **Test (Engineering-Ableitung):** Verweigerte Mikrofonfreigabe, Erfolg, kein Treffer, Abbruch und Bibliotheks-Opt-out prüfen. Mikrofonaktivität muss nach Ende der benötigten Aufnahme aufhören; ohne Zustimmung darf kein Titel gespeichert werden.

### sign-in-with-apple — Sign in with Apple
Quelle: [98] https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple

- **Aktivierung (Engineering-Ableitung):** Ein begründeter Kontoflow integriert diese Authentifizierung.
- **Umsetzung (HIG):** Anmeldung an konkreten Wert knüpfen und möglichst verzögern; nach erfolgreichem Abschluss direkt willkommen heißen und Anmeldestatus zeigen. Bestehende Konten gegebenenfalls verknüpfen. Kein zusätzliches Passwort verlangen und private Relay-Adresse nicht durch erzwungene persönliche Adresse ersetzen. Pflichtdaten von empfohlenen Daten unterscheiden; optionale Datenerhebung verschieben und erklären. Button prominent darstellen; Systembutton bevorzugen, eigene Varianten nur innerhalb der detaillierten Logo-, Titel-, Größen- und Abstandsregeln.
- **Test (Engineering-Ableitung):** Neue Anmeldung, vorhandenes Konto, Relay-Adresse, Abbruch und erneute Anmeldung prüfen. Kontoverknüpfung darf keine fremden Inhalte freigeben; dekorative Button-Nachbildungen vermeiden.

### siri — Siri
Quelle: [99] https://developer.apple.com/design/human-interface-guidelines/siri

- **Aktivierung (Engineering-Ableitung):** Häufige, klar beschreibbare App-Aktionen sollen über Siri erreichbar sein.
- **Umsetzung (HIG):** App-Funktionen und Inhalte über passende App Intents verfügbar machen. Bekannte Begriffe und relevante Inhalte verwenden; keine Werbung einschleusen. Systemantworten bevorzugen. Eigene Antworten kurz, verständlich, inklusiv sowie visuell und gesprochen brauchbar gestalten. Bei zu vielen Optionen offen nachfragen. Geräteunabhängig formulieren, App-Namen nicht ständig wiederholen, Fehler mit hilfreicher Erklärung behandeln und Jugendschutz respektieren.
- **Test (Engineering-Ableitung):** Mehrdeutige Anfrage, fehlende Parameter, nicht vorhandenen Inhalt, Ablehnung und Fehler in visueller wie gesprochener Ausgabe prüfen. Intent darf nur die tatsächlich gewünschte Aktion ausführen.

### tap-to-pay-on-iphone — Tap to Pay on iPhone
Quelle: [103] https://developer.apple.com/design/human-interface-guidelines/tap-to-pay-on-iphone

- **Aktivierung (Engineering-Ableitung):** Eine Händler-App soll Zahlungen direkt auf geeignetem iPhone annehmen.
- **Umsetzung (HIG):** Geschäftsbedingungen vor Kundenkontakt und nur durch Administratoren akzeptieren lassen; Tutorial für unterstützte Zahlungsmittel anbieten. Checkout-Option auch vor Aktivierung auffindbar halten, Konfiguration möglichst früh starten. Einfacher Wechsel zu anderen unterstützten Annahmewegen. Endbetrag und Voraboptionen vor dem Zahlungsbildschirm festlegen. Autorisierungsfortschritt, Erfolg/Ablehnung und handlungsfähige Fehler deutlich zeigen. Betragslose Kartenlese- und Loyalty-Flows eindeutig von Bezahlung unterscheiden.
- **Test (Engineering-Ableitung):** Nichtadministrativer Nutzer, laufende Konfiguration, abgelehnte Karte, Unterbrechung und Ersatz-Zahlweg prüfen. Keine Erfolgsmeldung vor bestätigter Autorisierung; Wiederholung muss vor Doppelbelastung schützen.

### voiceover — VoiceOver
Quelle: [106] https://developer.apple.com/design/human-interface-guidelines/voiceover

- **Aktivierung (Engineering-Ableitung):** Jede neue oder geänderte Nutzeroberfläche; kein optionales Produktfeature.
- **Umsetzung (HIG):** Wesentliche Controls mit passenden Alternativlabels und bedeutungstragende Bilder mit Beschreibungen versehen. Dekoration aus der Navigation ausschließen. Diagramme vollständig zugänglich machen. Überschriften, Gruppierung, Reihenfolge und Verknüpfungen so definieren, dass Struktur navigierbar wird. Sichtbare Layout-/Inhaltsänderungen angemessen melden, Rotor unterstützen. Auf visionOS erhalten eigene Gesten bei aktivem VoiceOver nicht standardmäßig Handinput; alternative Interaktion berücksichtigen.
- **Test (Engineering-Ableitung):** Kernaufgabe ausschließlich mit VoiceOver durchführen: Auffinden, Werte ändern, Fehler verstehen, Modal schließen. Fokusverlust, doppelte Labels und unverständliche Grafiken beheben; Custom-Gesten dürfen kein exklusiver Zugang sein.

### wallet — Wallet
Quelle: [107] https://developer.apple.com/design/human-interface-guidelines/wallet

- **Aktivierung (Engineering-Ableitung):** Pässe, Bestellverfolgung oder eine ausdrücklich benötigte Wallet-Identitätsprüfung gehören zum Produkt.
- **Umsetzung (HIG):** Pass hinzufügen anbieten, verwandte Pässe gruppieren, bestehende öffnen und aktuell halten. Ablauf melden; vor Löschen Zustimmung holen. Vorderseite übersichtlich, erkennbar und kontrastreich gestalten; Passstil und Assettabellen einhalten, Watch-Darstellung berücksichtigen. Bestellungen unmittelbar bereitstellen, Status aktuell halten, Händlerkontakt und Verwaltungslink anbieten; doppelte Mitteilungen vermeiden. Identitätsprüfung nur bei Geräteunterstützung, zum benötigten Zeitpunkt und mit minimalen Daten; Zweck und Speicherfrist offenlegen, passenden Systembutton wählen.
- **Test (Engineering-Ableitung):** Bereits vorhandenen Pass, Update, Ablauf, Löschung, Watch-Zuschnitt, Teilversand und verweigerte Identitätsfreigabe prüfen. Unbeauftragte Teilfunktionen nicht zusätzlich implementieren.

## Coverage, Spannungen und verbleibende Lücken

- **Coverage:** Rekursive `children`-Traversal des lokalen Manifests ergibt für Patterns 26 Seiten einschließlich Kategorie (25 Unterseiten), für Technologies 30 einschließlich Kategorie (29 Unterseiten). Alle 56 Seiten sind oben mit Source URL, Aktivierung, Umsetzungsregel und Testauftrag erfasst. Die beiden Bäume überschneiden sich nicht. Fehlende Manifest-Einträge oder gemeldete Abruffehler in diesen Bäumen: keine.
- **Verdichtung:** „Vollständig“ bezeichnet hier die Abdeckung aller navigationsverlinkten Seiten, nicht jede einzelne Apple-Empfehlung. Besonders große Seiten wie App Clips, Apple Pay, Wallet, Machine Learning und SharePlay enthalten weitere Detailregeln. Bei Aktivierung die jeweilige Originalseite einschließlich verschachtelter JSON-Abschnitte nachladen. Insbesondere keine Assetmaße, Druckkalibrierungswerte, Codecprofile oder Plattformverfügbarkeit aus den Kurzregeln erfinden.
- **Kontext statt Pauschalregel:** Allgemeines Feedback vermeidet überflüssige Löschbestätigungen; iCloud verlangt eine Erklärung der geräteübergreifenden Löschfolge. watchOS soll Ladeindikatoren möglichst vermeiden, erlaubt in Loading aber eine Anzeige statt leerem Bildschirm bei unvermeidbarer kurzer Wartezeit. Live-TV kann einen schnellen automatischen Einstieg erwägen; visionOS-Immersion darf nicht überraschend starten. Solche Regeln gelten in ihrem jeweiligen Kontext.
- **Nicht eigenständig geprüft:** Bilder, visuelle Vorher-/Nachher-Beispiele und Videos wurden nicht visuell auditiert. Spezifische Asset- und Maßtabellen sind nicht vollständig in diese maximal 150 Wörter langen Karten übertragen. Verlinkte SDK-Dokumentationen, externe Programmleitfäden, Entitlement-Anträge, regionale Anforderungen und aktuelle App-Store-/Zahlungsregeln sind nicht Teil dieses lokalen Quellen-Drafts.
- **Technische Lücke:** HIG-Text ist Designanleitung, kein ausführbarer API-Vertrag. Gerade einzelne Frameworks, Hardwarebedingungen und neue Plattformfunktionen müssen vor Codeänderung gegen das tatsächliche Deployment-Target und die offizielle Entwicklerdokumentation geprüft werden. „No additional considerations“ beweist keine API-Verfügbarkeit auf jedem Gerät einer Plattform.
- **Verifikation:** Es wurde keine App gebaut und kein UI-, Hardware-, Zahlungs-, Gesundheits- oder Accessibility-Test ausgeführt. Die Testpunkte sind explizite Engineering-Ableitungen für den späteren Coding-Agenten. Die Referenz dokumentiert keine bestandenen App-Tests.

## Sources

[6] https://developer.apple.com/design/human-interface-guidelines/patterns
[7] https://developer.apple.com/design/human-interface-guidelines/technologies
[10] https://developer.apple.com/design/human-interface-guidelines/airplay
[11] https://developer.apple.com/design/human-interface-guidelines/always-on
[12] https://developer.apple.com/design/human-interface-guidelines/app-clips
[14] https://developer.apple.com/design/human-interface-guidelines/apple-in-app-purchase
[15] https://developer.apple.com/design/human-interface-guidelines/apple-pay
[17] https://developer.apple.com/design/human-interface-guidelines/augmented-reality
[20] https://developer.apple.com/design/human-interface-guidelines/carekit
[21] https://developer.apple.com/design/human-interface-guidelines/carplay
[22] https://developer.apple.com/design/human-interface-guidelines/charting-data
[23] https://developer.apple.com/design/human-interface-guidelines/collaboration-and-sharing
[37] https://developer.apple.com/design/human-interface-guidelines/drag-and-drop
[38] https://developer.apple.com/design/human-interface-guidelines/entering-data
[40] https://developer.apple.com/design/human-interface-guidelines/feedback
[41] https://developer.apple.com/design/human-interface-guidelines/file-management
[43] https://developer.apple.com/design/human-interface-guidelines/game-center
[45] https://developer.apple.com/design/human-interface-guidelines/generative-ai
[47] https://developer.apple.com/design/human-interface-guidelines/going-full-screen
[49] https://developer.apple.com/design/human-interface-guidelines/healthkit
[50] https://developer.apple.com/design/human-interface-guidelines/homekit
[51] https://developer.apple.com/design/human-interface-guidelines/icloud
[53] https://developer.apple.com/design/human-interface-guidelines/id-verifier
[55] https://developer.apple.com/design/human-interface-guidelines/imessage-apps-and-stickers
[59] https://developer.apple.com/design/human-interface-guidelines/launching
[62] https://developer.apple.com/design/human-interface-guidelines/live-photos
[63] https://developer.apple.com/design/human-interface-guidelines/live-viewing-apps
[64] https://developer.apple.com/design/human-interface-guidelines/loading
[65] https://developer.apple.com/design/human-interface-guidelines/mac-catalyst
[66] https://developer.apple.com/design/human-interface-guidelines/machine-learning
[67] https://developer.apple.com/design/human-interface-guidelines/managing-accounts
[68] https://developer.apple.com/design/human-interface-guidelines/managing-notifications
[69] https://developer.apple.com/design/human-interface-guidelines/maps
[72] https://developer.apple.com/design/human-interface-guidelines/modality
[74] https://developer.apple.com/design/human-interface-guidelines/multitasking
[77] https://developer.apple.com/design/human-interface-guidelines/nfc
[78] https://developer.apple.com/design/human-interface-guidelines/offering-help
[79] https://developer.apple.com/design/human-interface-guidelines/onboarding
[80] https://developer.apple.com/design/human-interface-guidelines/photo-editing
[81] https://developer.apple.com/design/human-interface-guidelines/playing-audio
[82] https://developer.apple.com/design/human-interface-guidelines/playing-haptics
[83] https://developer.apple.com/design/human-interface-guidelines/playing-video
[86] https://developer.apple.com/design/human-interface-guidelines/printing
[88] https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews
[90] https://developer.apple.com/design/human-interface-guidelines/researchkit
[92] https://developer.apple.com/design/human-interface-guidelines/searching
[94] https://developer.apple.com/design/human-interface-guidelines/settings
[96] https://developer.apple.com/design/human-interface-guidelines/shareplay
[97] https://developer.apple.com/design/human-interface-guidelines/shazamkit
[98] https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple
[99] https://developer.apple.com/design/human-interface-guidelines/siri
[103] https://developer.apple.com/design/human-interface-guidelines/tap-to-pay-on-iphone
[105] https://developer.apple.com/design/human-interface-guidelines/undo-and-redo
[106] https://developer.apple.com/design/human-interface-guidelines/voiceover
[107] https://developer.apple.com/design/human-interface-guidelines/wallet
[108] https://developer.apple.com/design/human-interface-guidelines/workouts
