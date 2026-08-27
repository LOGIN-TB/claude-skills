# Quellenregister für die deutsche/DACH-Edition

Stand der redaktionellen Prüfung: 13.08.2026.

Dieses Register nennt autoritative Einstiege. Es ist keine Rechtsberatung und keine abschließende Quellenliste. Vor einer konkreten Veröffentlichung oder externen Aktion sind Fassung, Geltungsbereich, Rechtsprechung, Behördenpraxis und Plattformregeln aktuell zu prüfen.

## Deutschland und Europäische Union

- **UWG § 7 – unzumutbare Belästigungen:** <https://www.gesetze-im-internet.de/uwg_2004/__7.html>
  - Arbeitsrelevanz: elektronische Werbung, ausdrückliche Einwilligung und kumulative Bestandskundenausnahme.
- **UWG § 6 – vergleichende Werbung:** <https://www.gesetze-im-internet.de/uwg_2004/__6.html>
  - Arbeitsrelevanz: gleicher Bedarf, objektive wesentliche und nachprüfbare Eigenschaften, Verwechslung, Rufausnutzung und Herabsetzung.
- **UWG § 5a – Irreführung durch Unterlassen:** <https://www.gesetze-im-internet.de/uwg_2004/__5a.html>
  - Arbeitsrelevanz: wesentliche Informationen und Kenntlichmachung eines kommerziellen Zwecks.
- **TDDDG § 25 – Schutz der Privatsphäre bei Endeinrichtungen:** <https://www.gesetze-im-internet.de/ttdsg/__25.html>
  - Arbeitsrelevanz: Speicherung von oder Zugriff auf Informationen in Endeinrichtungen sowie gesetzliche Ausnahmen.
- **DDG § 5 – allgemeine Informationspflichten:** <https://www.gesetze-im-internet.de/ddg/__5.html>
  - Arbeitsrelevanz: leicht erkennbare, unmittelbar erreichbare und ständig verfügbare Anbieterinformationen bei einschlägigen digitalen Diensten.
- **DSGVO, amtlicher EU-Rechtstext:** <https://eur-lex.europa.eu/eli/reg/2016/679/oj>
  - Arbeitsrelevanz: Grundsätze, Rechtsgrundlagen, Transparenz, Rechte betroffener Personen, Auftragsverarbeitung, Sicherheit und Drittlandübermittlungen; Artikel 7 insbesondere für Bedingungen und Nachweis einer Einwilligung.
- **Bundesbeauftragte für den Datenschutz und die Informationsfreiheit:** <https://www.bfdi.bund.de/>
- **Datenschutzkonferenz der unabhängigen Aufsichtsbehörden:** <https://www.datenschutzkonferenz-online.de/>

## Suche, Plattformen und technische Richtlinien

- **Google Search Central – KI-Funktionen und Website:** <https://developers.google.com/search/docs/appearance/ai-features>
  - Arbeitsrelevanz: normale Suchberechtigung und menschenorientierte SEO als Grundlage; aktuelle Google-Angaben vor Aussagen zu KI-Funktionen prüfen.
- **Google Search Essentials:** <https://developers.google.com/search/docs/essentials>
- **Google-Richtlinien für strukturierte Daten:** <https://developers.google.com/search/docs/appearance/structured-data/sd-policies>
- **OpenAI-Crawler:** <https://platform.openai.com/docs/bots>

## E-Mail-Format und Zustellbarkeit

- **RFC 5322 – Internet Message Format:** <https://www.rfc-editor.org/rfc/rfc5322.html>
  - Fassung: Standards Track, Oktober 2008. Geprüft am 27.08.2026.
  - Arbeitsrelevanz: Aufbau der Kopfzeilen sowie Faltung und Entfaltung. Belegte Passage: Entfalten heißt „simply removing any CRLF that is immediately followed by WSP".
- **RFC 8058 – Signaling One-Click Functionality for List Email Headers:** <https://www.rfc-editor.org/rfc/rfc8058.html>
  - Fassung: Standards Track, Januar 2017. Geprüft am 27.08.2026.
  - Arbeitsrelevanz: Ein-Klick-Abmeldung. Belegte Passage: Ein Absender setzt „one List-Unsubscribe header field and one List-Unsubscribe-Post header field". `List-Unsubscribe-Post` allein ist ein defekter Abmeldeweg.
- **Microsoft – Anti-spam message headers:** <https://learn.microsoft.com/en-us/defender-office-365/message-headers-eop-mdo>
  - Fassung: Seitenstand 27.07.2026, zuletzt aktualisiert 12.08.2026. Geprüft am 27.08.2026.
  - Arbeitsrelevanz: Bedeutung von `X-Forefront-Antispam-Report` und `Authentication-Results`. Belegte Einschränkung: Zu `SCL` heißt es, der Wert bestimme in Cloud-Organisationen nicht, ob eine Nachricht als Spam gilt; stattdessen sind `CAT` und `DIR` heranzuziehen. `SCL` daher nicht als Schwellenwert auslegen.
  - Offene Auslegungsfrage: Die Seite beschreibt die Kopfzeilen, nicht die Gewichtung einzelner Inhaltsmerkmale. Aussagen darüber, warum eine bestimmte Nachricht eingestuft wurde, bleiben Beobachtung.

Für soziale Netzwerke, Werbeplattformen, E-Mail-Anbieter und generative Medienwerkzeuge ist jeweils die aktuelle offizielle Dokumentation des tatsächlich verwendeten Dienstes maßgeblich. Sekundäre Blogbeiträge oder Anbieterbenchmarks sind keine ausreichende Grundlage für rechtliche Freigaben oder garantierte Ergebnisse.

## Zitier- und Prüfregel

Für wesentliche oder rechtlich sensible Aussagen werden mindestens festgehalten:

- genaue URL oder amtliche Fundstelle;
- Titel und Herausgeber;
- geprüfte Fassung oder Datum;
- wörtlich belegte relevante Passage;
- Geltungsbereich und offene Auslegungsfrage;
- verantwortliche Person oder Rolle für die abschließende Freigabe.
