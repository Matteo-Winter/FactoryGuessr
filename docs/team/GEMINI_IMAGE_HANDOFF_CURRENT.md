# Gemini-Übergabe – aktueller Bildauftrag nach Prüfung vom 9. November 2026

**VERBINDLICH AB SOFORT: Das Projekt besteht weiter aus 30 verschiedenen historischen 360°-Leveln.** Die neue Nutzerprüfung ergibt **11 visuell akzeptierte Bilder, 6 klar abgelehnte Bilder und 13 offene/unbeurteilte aktive Szenen**. **Dein Auftrag als Kollege: 6 Bilder überarbeiten / neu generieren und 13 offene Szenen erstellen bzw. zur Prüfung bringen.** Nicht die frühere, nun überholte Aufgabe „26 neu“ ausführen.

**Lese-Reihenfolge:**
1. [Bildstatus, Dateinamen und zusätzliche Bildvarianten](../IMAGE_PRODUCTION_STATUS_30.md) – maßgebliche Quelle.
2. [Datenliste mit individuellen Review-Entscheidungen](ACTIVE_SCENES_30.json) – `visualReview.verdict`.
3. [Vollständiger historischer Szenenplan mit Inhalt/Lernziel](../SCENE_MASTERPLAN_30.md).
4. [Ausführliche spezielle 3D- und Ereignis-Anleitung](COLLEAGUE_MASTER_PROMPT_14.md) – die dort **alte** 14-Bilder-Zuständigkeit ist überholt; nur technische und historische Qualitätsregeln weiterverwenden.
5. [GitHub Issue #18](https://github.com/Matteo-Winter/FactoryGuessr/issues/18) – aktuelle Aufgabencheckliste.

## A. 6 schlechte Versionen – diese Bilder jetzt neu machen

| ID | Jahr | Ort | Inhalt | Abgelehnte Datei |
|---|---:|---|---|---|
| **T05** | 1975 | Niederlande, Rotterdam/Eemhaven | Containerhafen | `rotterdam-container.webp` |
| **E01** | 1773 | USA, Boston/Griffin's Wharf | Boston Tea Party | `boston-tea-party.jpg` |
| **E03** | 1869 | Ägypten, Suezkanal | Eröffnung des Suezkanals | `suezkanal.png` |
| **E04** | 1929 | USA, New York/Wall Street | Börsencrash | `new-york-boerse.png` |
| **E05** | 1954 | Guatemala, Guatemala-Stadt | Sturz von Jacobo Árbenz | `guatemala-1954.png` |
| **E07** | 2013 | Bangladesch, Savar/Rana Plaza | Einsturz Rana Plaza | `review-rana-plaza.webp` |

**Was „Neu machen“ heißt:** historische Szene/ID **beibehalten**, nur die fehlerhafte Bildversion ersetzen. Bitte keine Auswechslung der Event-Themen ohne Rücksprache. Fehler im neuen Bild selbst beheben, nicht erst nach Übergabe dokumentieren und abbrechen.

## B. 13 weitere offene Szenen – zur Prüfung bringen

| ID | Jahr | Ort | Inhalt | Letzter bekannter Datei-Status |
|---|---:|---|---|---|
| **P06** | 1880 | Japan, Tomioka, Gunma | Rohseide | Kein Dateiname im aktuellen Review |
| **P07** | 1890 | Deutschland, Ruhrgebiet | Stahl | Kein Dateiname im aktuellen Review |
| **P08** | 1900 | DR Kongo (heutiges Staatsgebiet), Äquatorregion / Kongobecken | Naturkautschuk | Kein Dateiname im aktuellen Review |
| **P11** | 1970 | Ghana, Takoradi / Tema | Kakaomasse und Kakaobutter | Kein Dateiname im aktuellen Review |
| **P12** | 1975 | Saudi-Arabien, Ostprovinz / Dhahran | Erdöl | Kein Dateiname im aktuellen Review |
| **P14** | 2018 | Bangladesch, Dhaka | T-Shirts und Kleidung | Kein Dateiname im aktuellen Review |
| **P15** | 2023 | Taiwan, Hsinchu | Halbleiterchips | Kein Dateiname im aktuellen Review |
| **P16** | 2023 | Chile, Salar de Atacama | Lithiumsalz-Vorprodukte | Kein Dateiname im aktuellen Review |
| **T02** | 1750 | Heutiges Ghana, Cape Coast Castle | Atlantische Handelsfestung | Kein Dateiname im aktuellen Review |
| **T06** | 2015 | Singapur, Pasir Panjang | Globaler Containerumschlag | Kein Dateiname im aktuellen Review |
| **E02** | 1791 | Heutiges Haiti, Saint-Domingue | Beginn der Haitianischen Revolution | Kein Dateiname im aktuellen Review |
| **E06** | 1980 | Polen, Gdańsk/Danzig | Solidarność-Werftstreiks | Kein Dateiname im aktuellen Review |
| **E08** | 2021 | Ägypten, Suezkanal | Ever-Given-Blockade | Kein Dateiname im aktuellen Review |

Hier liegt **kein Urteil in der neuen Liste** vor. Wenn du bereits ein Bild hast, zur Prüfung vorlegen; andernfalls mit Gemini erstellen. **Nicht** als explizit abgelehnt ausgeben.

## C. 11 akzeptierte Referenzbilder – nicht wieder neu erzeugen

| ID | Originaldatei laut Nutzerprüfung |
|---|---|
| P01 | `zaandam-saegemuehle.jpg` |
| P02 | `murano-glas.jpg` |
| P03 | `jingdezhen-porzellan.jpg` |
| P04 | `barbados-zucker.jpg` |
| P05 | `gb-1840-textile-mill.jpg` |
| P09 | `gt-1910-banana-packing.jpg` |
| P10 | `automobilfabrik.png` |
| P13 | `cn-2015-electronics-assembly.jpg` |
| T01 | `amsterdam-voc-werft.png` |
| T03 | `kalkutta-handel.png` |
| T04 | `kanton-handel.png` |

Die Bilder wurden per **Dateinamen und Review-Ergebnis** übermittelt. Die tatsächlichen Dateien liegen nicht automatisch in GitHub und sind nicht dadurch technisch verifiziert. Für einen konsistenten Stil bitte diese **Originaldateien** (nicht alte, möglicherweise abweichende Testbilder) vom Nutzer beziehen, wenn verfügbar.

## D. Look & Feel – so sollen die neuen 360°-Szenen aussehen

**Vibe:** „Ich stehe gerade wirklich dort“ – glaubwürdige, dichte **historische Dokumentarfilm-Realistik**, lebendiges, zeittypisches Arbeiten/Handeln/Entdecken statt glatter Showroom- oder Computerspielästhetik. Menschen haben **sinnvolle Handlungen**: an echten Maschinen, Werkbänken, Schiffen, Waren, bei einer Demonstration oder in einer konkret belegbaren historischen Situation. Details sollen aufmerksames Erkunden belohnen: Rohstoffe, fertige Produkte, Werkzeuggebrauch, richtige Kleidung, Materialalterung, Maschinenlogik, regionale Architekturen und Transportwege.

**Stilkonstanz ohne Einheitsfilter:** Die akzeptierten Beispiele kombinieren authentisches Material, schöne natürliche Lichtführung, dichtes aber lesbares Geschehen und visuell sofort erkennbare Produkte. Ein venezianischer Glasofen darf warm glühen, eine 1840er Textilhalle Staub in Fensterstrahlen haben; ein 1970er Hafen, ein Halbleiterreinraum 2023 oder ein politischer Wendepunkt brauchen **ihre eigene sachlich passende** Farb- und Lichtwelt. **Nicht alle Orte sepiafarben färben.**

**ZuWi:** Wir zeigen nicht nur Gebäude, sondern *wer produziert, wer kontrolliert Handel und Logistik, welche Arbeitsbedingungen herrschen und was sich historisch geändert hat*. Die Szene muss Land und Epoche erratbar machen, ohne triviale Flaggen, Jahreszahlen, Firmenschilder, Cities im Bild oder künstliche Text-Hinweise.

### Historische Sorgfalt
Vor jedem neuen Bild mindestens ein institutionell/museal/archivisch belastbarer Quellenbeleg und wenn möglich unabhängige Zweitquelle; notieren: Land damals/heute, Jahr, örtliche Gebäude, typische Produkte/Handlungen, historische Technik/Fahrzeuge/Kleidung, zwei geografische Hinweise und zwei Zeit-Indizien sowie 5 anachronistische Elemente, die nicht gezeigt werden dürfen. Bei Katastrophen und Gewalt/Eingriffen keine erfundenen konkreten Opfer oder vermeintlichen Originalfotos erzeugen. Als **KI-Rekonstruktion** kennzeichnen.

### Räumlicher / technischer Standard
1. **Eine Kamera an einem plausiblen Augenpunkt**, über volle **360° horizontal / 180° vertikal**. Ziel ist eine echte sphärisch-equirectangulare Ansicht, **nicht** eine normale breite 2:1-Fotografie.
2. **3D-Blockout / strukturtreue Vorlage zuerst**, in Blender oder gleichwertigem Verfahren, oder ein anderer nachgewiesen geometrisch konsistenter 360°-Erzeugungsweg. KI-Realismus darf Kamera-/Bauteilposition und Proportionen nicht beliebig verändern.
3. Motiv logisch über Rundumblick verteilen: vorne Kernhandlung; seitlich ergänzende Schritte/Umgebung; hinten eine sinnvolle, wirklich passende Rückseite. Naht darf **keine** Personen, Gebäude, Kräne oder Maschinen halbieren. Decken-/Himmels-**Zenit**, Boden-**Nadir**, rechte/linke Meridian-Kante und interne Übergänge kontrollieren.
4. **Per perspektivischem View testen**: yaw 0, ±90, 180, ±180 bei pitch ±55, senkrecht oben/unten und Zoom. Gerade Dachträger, Kräne, Segelmasten und Maschinen müssen *im Viewer* korrekt aussehen. Ein mathematischer Nahtquotient allein ist **kein** PASS; gespiegelte Hallen oder Fahrzeuge sind ebenfalls Fehler.
5. Möglichst **native 4096×2048 Pixel**, tatsächliche Pixelmaße angeben; Upscaling getrennt kennzeichnen. Realistischen Render zusammen mit Quelle, Quellenliste, Perspektiven-Kontaktsheet, QA-Report und nachvollziehbaren Nutzungsrechten liefern.
6. **Kein selbstständiges `ready`, GitHub-Merge oder Deployment.** Nutzer sieht und entscheidet zuerst die tatsächlichen Bilddateien. Auch ein optisch akzeptiertes Bild braucht die separate technische/historische Freigabe.

### Priorität
**Zuerst die sechs abgelehnten Bilder** (damit die vorhandenen konkreten Review-Fehler behoben werden), anschließend die 13 offenen. Ideal: Erster verbesserter Kandidat **E01 Boston Tea Party**, mit vollständiger Recherche und echter 360°-QA, bevor mehrere Varianten unkontrolliert gesammelt werden. Bereits akzeptierte Bilder nicht noch einmal neu bauen.

## E. Abgabe

Für **jede ID**: `research.md`, historische Quellen und Prompt, tatsächliche Bilddatei, gegebenenfalls 3D-Quelle, `qa/contact_sheet.jpg` (Front/Links/Rechts/Naht/Zenit/Nadir), `qa/report.md` mit FAIL/PASS/NICHT GETESTET, echte Maße und Vergleich zur abgelehnten Fassung. GitHub-Feature-Branch + PR oder eigenständiges ZIP, falls nötig. Die ursprüngliche Szene-ID beibehalten, damit sich das Bild ins Spiel einpflegen lässt.

**Nicht neu als zusätzliche Level erstellen:** `review-perlfluss-alternative.png` ist ein **alternatives T04** und darf nicht als T07 erscheinen; `review-venedig.webp` ist eine abgelehnte P02-Alternative trotz akzeptiertem P02; Marktplatz 1400, Machu Picchu, Regenwald 2015, Eisenbahnbau USA gehören **nicht** zur aktiven 30er-Liste.
