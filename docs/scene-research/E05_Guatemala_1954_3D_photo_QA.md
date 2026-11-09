# E05 – Guatemala-Stadt 1954: neue 3D-Referenz und fotorealistischer 360°-Kandidat

**Stand:** 09.11.2026 · Kategorie historischer Wendepunkt · **Status:** `candidate`, **noch nicht** vom Nutzer visuell akzeptiert und **nicht formell `ready`**. Die frühere Datei `guatemala-1954.png` war vom Nutzer als „Neu machen“ bezeichnet worden.

## Historische Faktenkarte (Recherche)
- **Zeitpunkt:** Juni 1954, Rücktritt des gewählten Präsidenten Jacobo Árbenz am **27.06.1954**; US-amerikanische CIA unterstützte den gewaltsamen politischen Umsturz. **Nicht** allein durch United Fruit erklären; Landreform, wirtschaftliche Interessen und Kalter Krieg sind getrennt zu behandeln.
- **Ort:** zentrale Plaza nahe dem Nationalpalast in Guatemala-Stadt (Palast eröffnet **1943**). Bild ist eine **künstlerisch plausible KI-Rekonstruktion**, weder eine tatsächliche Augenzeugenfotografie noch eine rekonstruierte konkrete Einzelhandlung vom 27. Juni.
- **Motiv:** zivile Menschenmengen, vorsichtige Militärpräsenz, Fahrzeuge der 1950er-Jahre, Reporter, belebter Hauptplatz; **keine Flaggen**, lesbaren Schilder, identifizierbare historische Personen, Verletzten oder Gewaltszenen.

**Institutionelle Quellen und historische Belege:**
- [Office of the Historian, Operation PBSUCCESS](https://history.state.gov//historicaldocuments/frus1950-55Intel/d154)
- [FRUS 1952–54, Guatemala](https://history.state.gov/historicaldocuments/frus1952-54Guat/d287)
- [Guatemala Kulturministerium: Palast 1939–1943](https://guatemala.gob.gt/palacio-nacional-de-la-cultura-un-tesoro-arquitectonico-de-la-cultura-y-el-patrimonio-de-guatemala/)
- [Guatemaltekische Regierung: charakteristisch grüne Palastfassade](https://prensa.gob.gt/comunicado/curiosidades-del-palacio-nacional-de-la-cultura-detalles-que-pocos-conocen)

## Erzeugte Bild- und Quelldateien

Das komplette Chat-Artefakt **`FactoryGuessr_E05_Guatemala_1954_3D_PHOTO_QA.zip`**, SHA256 `79475bd15e30fdbcad0fc25e4a36f7b63dd204dd3556495a0d184aa230989a2e`, ist **nicht automatisch im GitHub-Repository**. Kollege/Claude muss es bei Bedarf separat erhalten.

- `build_guatemala_1954.py` plus `render_support.py` erstellen **1.391 VTK-Geometrieobjekte** mit einem festen Kamerazentrum `(0,-4,1.65)` Meter; 6 Cube-Cameras, native sphärisch equirectangulare **4096×2048**. **3D-Referenz:** `E05_Guatemala_1954_3D_REFERENCE_NATIVE_4096x2048.png`, SHA256 `669371c992067edd2332a28878db1cbbe055da0a36aaa12a2b640ba7347573f1`.
- Fotorealistische KI-Ausgabe `E05_Guatemala_1954_PHOTO_CANDIDATE_ORIGINAL_1774x887.png`: **native 1774×887**, **nicht nachweislich geometriegebunden** und bezüglich einzelner Architekturdetails **abweichend** vom 3D-Modell. Zur fotografischen, nicht zur geometrischen Orientierung geeignet.
- `repair_seam_color.py` ändert **nur die ersten/letzten 18 Pixelspalten** für zyklische Farbanpassung (keine gespiegelten Personen oder Gebäude); `E05_Guatemala_1954_PHOTO_SEAM_CORRECTED_1774x887.png`, SHA256 `5791a6d4795777c9df3354654eed3548a7adde99d3bb60b20cef4f79dffe563d`.
- `E05_Guatemala_1954_VIEWER_UPSCALED_4096x2048.jpg`, SHA256 `7ed66f2cb464ad67b278f05180616417bf63ead3841dc1e421657bbb51d13cd8`, **hochskalierte Browserfassung, NICHT native 4K-Fotodetails**.
- `qa_photo_corrected/contact_12_views.jpg`: 12 entzerrte Perspektivproben (yaw 0, ±90, 180, 180 bei pitch ±55, Zenit, Nadir, vier Diagnosen). `preview.html` lässt Foto und 3D per lokalem Server in Pannellum 2.5.7 vergleichen.

## Tatsächliche technische Befunde

| Test | Ergebnis |
|---|---|
| Foto 1774×887: Roh-Naht/Kontaktspalten | Relative RGB-MAE **1,4587×** |
| Foto nach lokalem Pixel-Farbabgleich | Edge-Ratio **0,0×** **(durch Korrektur konstruiert, kein Geometrie-PASS)** |
| 4096×2048-JPG nach zyklischer Hochskalierung | Edge-Ratio **0,0267×**, **keine** nativen 4K-Fotodetails |
| Tatsächlich native 3D-Kugel | Naht **0×**, geometrisch kohärente 3D-Welt |
| Fotobild in 12 sphärisch berechneten Blickrichtungen | keine deutliche rückwärtige Innen-/Außen-Schnittstelle: Baum, arkadische Fassaden, Boden; **Restfehler möglich**, keine Browser-Verifikation |
| Originaltreue Palastarchitektur | **OFFEN**: das Fotobild zeigt eine helle, ornamental abweichende statt der historisch grünlichen Palastfassade |
| Vollständige Polgeometrie | **NICHT ABSCHLIESSEND BESTANDEN**: Blick am Nadir verzerrt teilweise Vordergrundfiguren |
| Unabhängiger Nutzer-Mac-Browser-PASS | **NICHT GETESTET** |
| Freigabe in `public/data/scenes.json` | **NEIN** |

**Nächste Aufgabe:** Bild im echten Browser prüfen und historischen Palastabgleich sowie die Polverzerrung beurteilen. Trotz sehr niedriger Pixelnaht **keine** automatische `ready`-Freigabe. Nutzer hat für E05 noch keine positive Neubewertung abgegeben.

