# Bildproduktionsliste – Made in Time, aktueller Stand 09.11.2026

**Aktuelle Nutzerentscheidungen nach dem Boston-Nachtrag:** **12/30 Bilder „Passt“**, **5/30 „Neu machen“**, **13/30 noch ohne aktuelles Prüfurteil**. Das Projekt bleibt bei **30 einzigartigen Szenen (16 P + 6 T + 8 E)**. Die früheren Zwischenstände 4/26, 11/6/13 und 6/13 sind **nicht mehr aktuell**. **Formale historische/technische Spielfreigaben: 0/30.**

**Neu:** Der Nutzer hat die neue Boston-Fassung `nahtloses_panorama_der_boston_tea_party.png` mit „okay passt, nächstes bild“ akzeptiert – **E01 wechselt nur in die visuelle Positivliste**, ohne Browser-/Kugel-QA zu behaupten. **E03 Suez 1869** erhielt einen neuen fotorealistischen Kandidaten, **der wegen eines sichtbaren 360°-Nahtfehlers durchfiel**. E03 bleibt in der Remake-Liste. [Suez-Research/QA](scene-research/E03_Suez_1869_REWORK_QA.md).

**[Gemini-Handoff für 5 Remakes + 13 offene Bilder](team/GEMINI_IMAGE_HANDOFF_CURRENT.md)** · [Maschinenlesbare individuelle Statusdaten](team/ACTIVE_SCENES_30.json) · [30er-Masterplan](SCENE_MASTERPLAN_30.md) · [aktuelles GitHub-Issue #18](https://github.com/Matteo-Winter/FactoryGuessr/issues/18).

## A. 12 visuell akzeptierte Bildfassungen

| ID | Jahr | Ort | Motiv | Datei laut Nutzer | Status |
|---|---:|---|---|---|---|
| **P01** | 1660 | Niederlande, Zaandam/Zaanstreek | Holzbretter | `zaandam-saegemuehle.jpg` | **Passt** (nur visuell) |
| **P02** | 1680 | Italien, Murano bei Venedig | Glasgefäße | `murano-glas.jpg` | **Passt** (nur visuell) |
| **P03** | 1700 | China, Jingdezhen | Porzellan | `jingdezhen-porzellan.jpg` | **Passt** (nur visuell) |
| **P04** | 1700 | Barbados, St. James / Zuckerrohrgürtel | Rohrzucker | `barbados-zucker.jpg` | **Passt** (nur visuell) |
| **P05** | 1840 | Großbritannien, Manchester / Lancashire (Pilot) | Baumwollgarn und Stoff | `gb-1840-textile-mill.jpg` | **Passt** (nur visuell) |
| **P09** | 1910 | Guatemala, Karibikküste / Puerto-Barrios-Region (Pilot) | Bananen für den Export | `gt-1910-banana-packing.jpg` | **Passt** (nur visuell) |
| **P10** | 1913 | USA, Highland Park / Detroit | Automobile | `automobilfabrik.png` | **Passt** (nur visuell) |
| **P13** | 2015 | China, Shenzhen / Perlflussdelta (Pilot) | Elektronikgeräte | `cn-2015-electronics-assembly.jpg` | **Passt** (nur visuell) |
| **T01** | 1670 | Niederlande, Amsterdam/Oostenburg | VOC-Werft und Handel | `amsterdam-voc-werft.png` | **Passt** (nur visuell) |
| **T03** | 1780 | Heutiges Indien, Kalkutta/Kolkata, Hooghly | East India Company und Flusshandel | `kalkutta-handel.png` | **Passt** (nur visuell) |
| **T04** | 1820 | China, Guangzhou/Kanton | Thirteen Factories / Canton-System | `kanton-handel.png` | **Passt** (nur visuell) |
| **E01** | 1773 | USA, Boston/Griffin's Wharf | Boston Tea Party | `nahtloses_panorama_der_boston_tea_party.png` | **Passt** (nur visuell) |

**Wichtig:** Die drei bisherigen technischen Pilot-IDs `gb-1840-textile-mill`, `gt-1910-banana-packing` und `cn-2015-electronics-assembly` entsprechen den aktiven IDs **P05, P09 und P13**. Sie sind keine zusätzlichen Level.

## B. 5 ausdrücklich zur Neuerstellung angeforderte Bildfassungen

| ID | Jahr | Ort | Motiv | Datei laut Nutzer | Status |
|---|---:|---|---|---|---|
| **T05** | 1975 | Niederlande, Rotterdam/Eemhaven | Containerhafen | `rotterdam-container.webp` | **Neu machen** |
| **E03** | 1869 | Ägypten, Suezkanal | Eröffnung des Suezkanals | `suezkanal.png` | **Neu machen** |
| **E04** | 1929 | USA, New York/Wall Street | Börsencrash | `new-york-boerse.png` | **Neu machen** |
| **E05** | 1954 | Guatemala, Guatemala-Stadt | Sturz von Jacobo Árbenz | `guatemala-1954.png` | **Neu machen** |
| **E07** | 2013 | Bangladesch, Savar/Rana Plaza | Einsturz Rana Plaza | `review-rana-plaza.webp` | **Neu machen** |

Für E03 ist das neue Probebild `E03_Suez_1869_PHOTO_V1_ORIGINAL_1774x887.png` als **nicht freigegebener Kandidat** dokumentiert. Die 3D-Vorlage ist korrekt sphärisch gerendert, doch das Fotobild hat eine **inhaltlich nicht durchgehende 180°-Naht** (Farbkante 6,63×). Lokale Glättungen mit gespiegelten/gestreckten Regionen wurden verworfen. Die alte Datei `suezkanal.png` wurde damit **nicht** erfolgreich ersetzt.

## C. 13 aktive Szenen ohne Urteil in der aktuellen Nutzerliste

| ID | Jahr | Ort | Motiv | Datei laut Nutzer | Status |
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

**„Kein Prüfurteil“ bedeutet nicht, dass kein Bild existiert oder der Nutzer es abgelehnt hat**. Kollege soll ein möglicherweise schon erstelltes Bild zuerst vorlegen und nur bei Bedarf eine neue Version erzeugen.

## D. Varianten und zusätzliche Testmotive (keine neuen Level)

| Datei | Nutzerurteil | Zuordnung | Konsequenz |
|---|---|---|---|
| `review-perlfluss-alternative.png` | Passt | T04 | Zweite akzeptierte Bildvariante für T04, kein zusätzliches Level. Finale Variantenauswahl noch nicht dokumentiert. |
| `review-venedig.webp` | Neu machen | P02 | Die Hauptversion P02/murano-glas.jpg passt bereits; diese Alternativfassung nicht verwenden. |
| `review-marktplatz-1400.webp` | Neu machen | Außerhalb der 30er-Liste | Kein aktiver 30er-Szeneneintrag; nicht ohne neue Projektentscheidung als Level neu erzeugen. |
| `review-machu-picchu.webp` | Neu machen | Außerhalb der 30er-Liste | Kein aktiver 30er-Szeneneintrag; nicht ohne neue Projektentscheidung als Level neu erzeugen. |
| `review-regenwald-2015.webp` | Neu machen | Außerhalb der 30er-Liste | Kein aktiver 30er-Szeneneintrag; nicht ohne neue Projektentscheidung als Level neu erzeugen. |
| `review-usa-railway.webp` | Neu machen | Außerhalb der 30er-Liste | Kein aktiver 30er-Szeneneintrag; nicht ohne neue Projektentscheidung als Level neu erzeugen. |

Für T04 ist `review-perlfluss-alternative.png` eine zweite akzeptierte **Bildvariante desselben Kanton-Levels**, kein 31. Level. Für P02 ist die alternative Venedig-/Murano-Fassung abgelehnt, die gewählte Hauptfassung jedoch akzeptiert. Marktplatz 1400, Machu Picchu, Regenwald 2015 und Eisenbahnbau USA sind **keine aktiven Bildaufträge**.

## E. Gemeinsamer Vibe und verpflichtende Bild-QA

**Historischer Dokumentarfilm als immersives Erlebnis:** fotorealistisch, glaubwürdig beleuchtet, Menschen und Abläufe natürlich und sinnvoll belebt; Werkzeuge, Rohstoffe, Ware, Gebäude, Wetter und Kleidung exakt an Ort und Epoche angepasst. Keine leeren dekorativen Produktionshallen, keine austauschbare Sepiatönung, keine erfundenen Logos/Jahreszahlen als Spoiler. Unterschiedliche Länder und Epochen brauchen eigene atmosphärische und architektonische Handschrift.

**Echte 360°-Ansicht:** ein fester Augenpunkt, **equirectangular 360°×180°**, vollständig räumliche Umgebung einschließlich Rückseite, Zenit und Nadir. In einem perspektivisch entzerrten Pannellum-Viewer müssen Schiffe, Masten, Kräne, Balken, Menschen und Ufer plausibel aussehen. **Linke/rechte Bildkante müssen nicht nur farblich, sondern inhaltlich zusammenpassen**; doppelte Spiegelräume, gestreckte Köpfe und Häuser, abrupt endendes Wasser und Wolkenwirbel sind FAIL. Vor Erzeugung historische Faktenkarte und nach jedem Bild mindestens zwölf QA-Blickrichtungen sowie lokale Browserprüfung. Native 4K bevorzugt; Upscale ehrlich ausweisen.

**Gewalt und Kolonialgeschichte:** keine romantisierte Sklaverei, keine voyeuristischen Opferbilder, keine fiktiven angeblichen Originalfotos. Eine Simulation ist als historisch informierte KI-Rekonstruktion zu kennzeichnen.

## F. Verfügbarkeit, Rechte und Freigabe

Die ursprüngliche Nutzerprüfung enthält **Dateinamen und Bewertungen**, nicht automatisch Bildbytes im GitHub-Repository. Die E01- und E03-Chat-Bilder sind ebenfalls noch **keine** in `public/` geprüften Assets. Alte Datei-Hashes nicht ohne Datenvergleich auf neue Namen übertragen. Im Spiel `approved_panorama_count=0`, keine Merge-/Deploy-/`ready`-Aktion ohne ausdrückliche fachliche und technische Abnahme.

**Aktuelle Produktionsaufgabe des Kollegen mit Gemini: 18 offene Motive (5 Remakes + 13 ohne Urteil).**
