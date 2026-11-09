# VERBINDLICHER BILDSTATUS – Made in Time, 30 aktive Szenen

**Quelle: ausdrückliche Bildprüfung des Nutzers vom 09.11.2026.** Dies ist die maßgebliche Liste für die weitere Bildarbeit. **Es gibt 30 aktive Level (16 P + 6 T + 8 E), nicht 36/37.** Der Nutzer hat insgesamt **23 Bilddateien** beurteilt: **17 Bewertungen beziehen sich auf 17 unterschiedliche aktive Szenen**, dazu **6 weitere Varianten/Nebenmotive**.

**Ergebnis der aktiven 30 Szenen: 11 × „Passt“, 6 × „Neu machen“, 13 × kein aktuelles Prüfurteil.** Für den Kollegen bleiben **19 aktive Bearbeitungspunkte**: die sechs ausdrücklich abgelehnten Bilder neu generieren und die 13 noch offenen Szenen erstellen bzw. zur Prüfung vorlegen. **„Nicht gelistet“ bedeutet nicht automatisch „abgelehnt“ oder „Datei existiert nicht“.**

**Wichtig:** „Passt“ ist die **ausdrückliche visuelle Nutzerentscheidung**. Sie ersetzt **nicht** eine nachgewiesene 360°-Geometrie-/WebGL-/Historien-/Rechteprüfung und ist keine automatische `scene_status=ready`-Freigabe. Das produktive `public/data/scenes.json` bleibt bei `approved_panorama_count=0` bis zu eigenständiger Abnahme.

**[Gemini-Auftrag für die verbleibenden 19](team/GEMINI_IMAGE_HANDOFF_CURRENT.md)** · **[GitHub-Checkliste](https://github.com/Matteo-Winter/FactoryGuessr/issues/18)** · **[Maschinenlesbare Szenendaten](team/ACTIVE_SCENES_30.json)** · **[Historischer 30er-Plan](SCENE_MASTERPLAN_30.md)**.

## A. 11 visuell akzeptierte Szenen – Bilder erhalten, nicht automatisch neu generieren

| ID | Jahr | Land / Ort | Motiv | Datei laut Prüfung | Status |
|---|---:|---|---|---|---|
| **P01** | 1660 | Niederlande, Zaandam/Zaanstreek | Holzbretter | `zaandam-saegemuehle.jpg` | **Passt** (technische QA offen) |
| **P02** | 1680 | Italien, Murano bei Venedig | Glasgefäße | `murano-glas.jpg` | **Passt** (technische QA offen) |
| **P03** | 1700 | China, Jingdezhen | Porzellan | `jingdezhen-porzellan.jpg` | **Passt** (technische QA offen) |
| **P04** | 1700 | Barbados, St. James / Zuckerrohrgürtel | Rohrzucker | `barbados-zucker.jpg` | **Passt** (technische QA offen) |
| **P05** | 1840 | Großbritannien, Manchester / Lancashire (Pilot) | Baumwollgarn und Stoff | `gb-1840-textile-mill.jpg` | **Passt** (technische QA offen) |
| **P09** | 1910 | Guatemala, Karibikküste / Puerto-Barrios-Region (Pilot) | Bananen für den Export | `gt-1910-banana-packing.jpg` | **Passt** (technische QA offen) |
| **P10** | 1913 | USA, Highland Park / Detroit | Automobile | `automobilfabrik.png` | **Passt** (technische QA offen) |
| **P13** | 2015 | China, Shenzhen / Perlflussdelta (Pilot) | Elektronikgeräte | `cn-2015-electronics-assembly.jpg` | **Passt** (technische QA offen) |
| **T01** | 1670 | Niederlande, Amsterdam/Oostenburg | VOC-Werft und Handel | `amsterdam-voc-werft.png` | **Passt** (technische QA offen) |
| **T03** | 1780 | Heutiges Indien, Kalkutta/Kolkata, Hooghly | East India Company und Flusshandel | `kalkutta-handel.png` | **Passt** (technische QA offen) |
| **T04** | 1820 | China, Guangzhou/Kanton | Thirteen Factories / Canton-System | `kanton-handel.png` | **Passt** (technische QA offen) |

**Zuordnungen der alten Pilot-IDs:** `gb-1840-textile-mill` entspricht **P05**, `gt-1910-banana-packing` entspricht **P09**, `cn-2015-electronics-assembly` entspricht **P13**. Diese Pilot-IDs bleiben in der bisherigen Spieldatei erhalten. Dass die hochgeladenen Namen ähnlich sind, beweist **nicht**, dass die Dateibytes im Repository identisch sind.

## B. 6 ausdrücklich abgelehnte Bilder – neue Version anfordern

| ID | Jahr | Land / Ort | Motiv | Datei laut Prüfung | Status |
|---|---:|---|---|---|---|
| **T05** | 1975 | Niederlande, Rotterdam/Eemhaven | Containerhafen | `rotterdam-container.webp` | **Neu machen** |
| **E01** | 1773 | USA, Boston/Griffin's Wharf | Boston Tea Party | `boston-tea-party.jpg` | **Neu machen** |
| **E03** | 1869 | Ägypten, Suezkanal | Eröffnung des Suezkanals | `suezkanal.png` | **Neu machen** |
| **E04** | 1929 | USA, New York/Wall Street | Börsencrash | `new-york-boerse.png` | **Neu machen** |
| **E05** | 1954 | Guatemala, Guatemala-Stadt | Sturz von Jacobo Árbenz | `guatemala-1954.png` | **Neu machen** |
| **E07** | 2013 | Bangladesch, Savar/Rana Plaza | Einsturz Rana Plaza | `review-rana-plaza.webp` | **Neu machen** |

Diese sechs Bildversionen **nicht** als akzeptierte Versionen integrieren. Die **historischen Motive bleiben** im 30-Szenen-Plan; nur ihre derzeitige Bildfassung muss ersetzt werden.

## C. 13 aktive Szenen ohne Urteil in der aktuellen Prüfung – offen

| ID | Jahr | Land / Ort | Motiv | Datei laut Prüfung | Status |
|---|---:|---|---|---|---|
| **P06** | 1880 | Japan, Tomioka, Gunma | Rohseide | — | **Kein aktuelles Prüfurteil** |
| **P07** | 1890 | Deutschland, Ruhrgebiet | Stahl | — | **Kein aktuelles Prüfurteil** |
| **P08** | 1900 | DR Kongo (heutiges Staatsgebiet), Äquatorregion / Kongobecken | Naturkautschuk | — | **Kein aktuelles Prüfurteil** |
| **P11** | 1970 | Ghana, Takoradi / Tema | Kakaomasse und Kakaobutter | — | **Kein aktuelles Prüfurteil** |
| **P12** | 1975 | Saudi-Arabien, Ostprovinz / Dhahran | Erdöl | — | **Kein aktuelles Prüfurteil** |
| **P14** | 2018 | Bangladesch, Dhaka | T-Shirts und Kleidung | — | **Kein aktuelles Prüfurteil** |
| **P15** | 2023 | Taiwan, Hsinchu | Halbleiterchips | — | **Kein aktuelles Prüfurteil** |
| **P16** | 2023 | Chile, Salar de Atacama | Lithiumsalz-Vorprodukte | — | **Kein aktuelles Prüfurteil** |
| **T02** | 1750 | Heutiges Ghana, Cape Coast Castle | Atlantische Handelsfestung | — | **Kein aktuelles Prüfurteil** |
| **T06** | 2015 | Singapur, Pasir Panjang | Globaler Containerumschlag | — | **Kein aktuelles Prüfurteil** |
| **E02** | 1791 | Heutiges Haiti, Saint-Domingue | Beginn der Haitianischen Revolution | — | **Kein aktuelles Prüfurteil** |
| **E06** | 1980 | Polen, Gdańsk/Danzig | Solidarność-Werftstreiks | — | **Kein aktuelles Prüfurteil** |
| **E08** | 2021 | Ägypten, Suezkanal | Ever-Given-Blockade | — | **Kein aktuelles Prüfurteil** |

**Für diese 13 wurde in der neuen Nachricht kein Dateiname oder Urteil genannt.** Deshalb keine positive oder negative Qualitätsbehauptung. Sie bleiben auf der Kollegenliste, bis ein neues Bild oder eine ausdrückliche Prüfung vorliegt.

## D. Separat geprüfte Alternativen und Motive außerhalb der aktiven 30

| Aufnahme | Prüfung | Zuordnung | Entscheidung |
|---|---|---|---|
| `review-perlfluss-alternative.png` | Passt | T04 | Zweite akzeptierte Bildvariante für T04, kein zusätzliches Level. Finale Variantenauswahl noch nicht dokumentiert. |
| `review-venedig.webp` | Neu machen | P02 | Die Hauptversion P02/murano-glas.jpg passt bereits; diese Alternativfassung nicht verwenden. |
| `review-marktplatz-1400.webp` | Neu machen | Kein aktives Level | Kein aktiver 30er-Szeneneintrag; nicht ohne neue Projektentscheidung als Level neu erzeugen. |
| `review-machu-picchu.webp` | Neu machen | Kein aktives Level | Kein aktiver 30er-Szeneneintrag; nicht ohne neue Projektentscheidung als Level neu erzeugen. |
| `review-regenwald-2015.webp` | Neu machen | Kein aktives Level | Kein aktiver 30er-Szeneneintrag; nicht ohne neue Projektentscheidung als Level neu erzeugen. |
| `review-usa-railway.webp` | Neu machen | Kein aktives Level | Kein aktiver 30er-Szeneneintrag; nicht ohne neue Projektentscheidung als Level neu erzeugen. |

- **T04/Kanton:** `kanton-handel.png` ist die akzeptierte Hauptfassung, `review-perlfluss-alternative.png` eine ebenfalls akzeptierte Alternative. **Beide gehören zu T04**; für das Spiel wird später höchstens **eine** als Levelbild ausgewählt, nicht zwei Level.
- **P02/Murano:** `murano-glas.jpg` ist akzeptiert; die abgelehnte `review-venedig.webp`-Variante **nicht** neu erzeugen, weil der Hauptlevel bereits ein passendes Bild hat, sofern nicht ausdrücklich verlangt.
- **Marktplatz 1400, Machu Picchu, Regenwald 2015 und Eisenbahnbau USA** sind **keine aktiven 30er-Szenen**. Die Bewertung „Neu machen“ bezieht sich auf ihre Testbilder, **nicht** auf die Erteilung eines neuen Produktionsauftrags.

## Stil / Vibe – verbindlich für alle weiteren Gemini-Bilder

- **Fotorealistische historische Dokumentarfilm-Atmosphäre**: Betrachter steht mittendrin, nicht vor einer Bühnenkulisse; glaubwürdige, periodengerechte Objekte, Materialien, Licht und Gebrauchsspuren.
- **Lebendig und inhaltlich erkennbar:** Menschen bei sinnvoller Arbeit, Transport, Handel oder einer historisch plausiblen Handlung. Arbeiter und Werkzeuge wirklich an Produktionsschritten beteiligt; kein steriler, leerer Hallenraum, aber keine unnötig überfüllte Chaosfantasie.
- **Nicht alle Szenen in Sepia:** Glasofen/Murano warm, China-Werkstatt erdig, britische Textilhalle mit Staub/Lichtstrahlen; moderne Ports/Reinräume können kühl und funktional sein. Epochen und Orte brauchen eigene Bildsprache.
- **Historisch korrekt:** Produkte, Architektur, Maschinen, Verkehrsmittel, Kleidung, politische Epoche und lokale Landschaft **vorher recherchieren**; keine Logos/Flaggen/Jahreszahlen als Rätsel-Spoiler.
- **Echte 360°-Kugel:** ein fester Beobachtungspunkt, **equirectangular 360°×180°**, horizontale Naht **auch inhaltlich** zusammenhängend, Zenit und Nadir ohne Wirbel, Personen/Geräte/Gebäude beim Perspektivwechsel nicht verformt. Keine großen spiegelgleichen Bildhälften zur Nahtreparatur.
- **Qualitätsziel:** echte native 4096×2048-Auflösung wenn technisch machbar; hochskalierte Fotos **als Upscale kennzeichnen**. Wichtig ist die tatsächliche perspektivische Ansicht im Pannellum-Viewer, nicht nur der 2:1-Bildeindruck.
- **ZuWi / historischer Kontext:** Nach dem Raten Unternehmensmacht, Handel, Arbeitsbedingungen und Wendepunkte erklären. Kolonialismus, Versklavung, Streiks, Regierungswechsel und Katastrophen respektvoll, sachlich, nicht als fiktive authentische Augenzeugenaufnahme darstellen.

## Dateiverfügbarkeit und Governance

**Diese Bildprüfung enthält Dateinamen und Bewertungen, aber keine neu hochgeladenen Originalbytes der 23 genannten Dateien.** Die Namen liegen jetzt in GitHub, nicht notwendigerweise die Bilder. **Keine aktuellen Bildmaße/Hashes aus früheren Chat-Artefakten auf diese Dateinamen übertragen.** Für technische QA braucht der Kollege / Claude die tatsächlichen Originalbilder, nicht nur diese Liste.

Die historische Szenenauswahl und ihre P/T/E-IDs bleiben unverändert. Für jedes neue Bild: Recherche → räumlich kohärente 3D-/360°-Komposition → fotorealistische Ausarbeitung → echter Perspektiv-/Naht-/Pol-Test → Nutzerreview → separater Spiel-Release. Keine automatische `ready`-Markierung, kein ungefragter Merge oder Deployment.

**Noch offen:** 6 Remakes + 13 nicht beurteilte aktive Szenen = 19 Bearbeitungspunkte; **11** aktuelle Bildfassungen visuell akzeptiert; **0** formal veröffentlichte 360°-Level.
