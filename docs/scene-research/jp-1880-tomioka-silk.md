# P06 – Tomioka Seidenhaspelei, Japan, ca. 1880

**Aktiver Plan:** [30 Szenen](../SCENE_MASTERPLAN_30.md) · **Kategorie:** Produktion · **Zuständigkeit:** Projektleitung · **Status:** `3d_candidate` (kein fotorealistisch freigegebenes Panorama) · Stand 09.11.2026.

## Vor dem Bild verifiziert

- Tomioka Silk Mill in Gunma öffnete 1872 als staatliche Meiji-Modellfabrik, übernahm **französische Seidenhaspelmaschinen und Dampfantrieb**. Die Handarbeit bestand darin, Seidenfäden aus Kokons zu lösen und auf Wickler/Spulen zu führen. **Produziert wird Rohseide, nicht Baumwollstoff oder gewebte Seide.**
- Die lange Werkshalle hatte ein hohes, von **Holzfachwerk-/Dachbindern ohne mittlere Stützen** getragenes Dach, Ziegelwände und große Fenster; traditionelle japanische und westliche Bauelemente wurden kombiniert. Arbeiterinnen waren wesentlicher Teil der Produktion.
- **Vorsicht mit modernen Museumsfotos:** die heute an vielen Aufnahmen erkennbaren automatischen Haspelmaschinen kamen laut Japan Tourism Agency **erst in den 1960ern** hinzu und passen **nicht zu 1880**.
- Die Anlage ist eine historisch belegte Referenz, aber unser Bild ist eine **künstlerisch informierte Kompositrekonstruktion**, keine exakte Vermessung der realen Fabrik.

### Institutionelle Referenzen
1. [UNESCO: Tomioka Silk Mill and Related Sites](https://whc.unesco.org/en/list/1449/) — Technologie-Transfer aus Frankreich, Rohseide und frühe Meiji-Industrialisierung.
2. [Japan Tourism Agency: Reeling Silk at the Tomioka Silk Factory](https://www.mlit.go.jp/tagengo-db/en/H30-00386.html) — 1872, Dampf-/Haspelmaschinen, Arbeiterinnen, Wickelvorgang.
3. [Japan Tourism Agency: Tomioka Silk Mill and Silk Industrial Heritage Sites](https://www.mlit.go.jp/tagengo-db/en/R2-00047.html) — Hallenstruktur, Gebäude und Bauformen.
4. [Japan Tourism Agency original handout](https://www.mlit.go.jp/tagengo-db/common/001559355.pdf) — ausdrücklich alte Anlage gegenüber 1960er-Automatikmaschinen.
5. [JSME: Silk reeling machines of the Okaya Silk Museum](https://www.jsme.or.jp/kikaiisan/heritage_046_en.html) — technisch belegter früher französischer Haspelmaschinentyp.

## Sichtbares Spielmotiv und 360°-Plan

- **0° vorne:** lange, von Holzfachwerk getragene Haspelhalle; Seidenkokons und Arbeitstische nahe der Kamera.
- **±90°:** links und rechts historisch inspirierte französische Mehrfach-Haspelgeräte, Wasserbecken, Seidenkokons, Wickelspulen, Arbeiterinnen mit plausibler Meiji-Arbeitskleidung.
- **180° hinten:** durchgehende rückwärtige Hallenstruktur ohne zerschnittene Maschine/Person.
- **Zenit/Nadir:** Dachbinder/Decke und Holzboden korrekt aus **einem einzigen 3D-Kamerazentrum** projiziert.
- **ZuWi-Lerninhalt:** staatlich gelenkter Technologietransfer, Globalisierung des Rohseidenhandels, Industrialisierung und Ausbildung von Arbeiterinnen; nach Auflösung sachlich erklären.

## Konkrete Ausführung (09.11.2026)

**Chat-Artefakt:** `Made_in_Time_Tomioka_P06_1880_3D_QA.zip`, SHA-256 `82253f2e936cc28582b1a0c8f344a59d6d7b7bd057fcbbbe347491498e302d1b`. **Noch nicht auf GitHub hochgeladen**, nur im Chat zum lokalen Import.

- Frei reproduzierbares VTK-/NumPy-3D-Modell in `build_tomioka_1880.py`, gemeinsame Cubemap-Projektion `render_support.py`, synthetische Holz-/Ziegel-/Dachmaterialien `tomioka_materials.py`; 5.744 Rendering-Actors.
- Fester Kamerastandpunkt `(0,-3.2,1.7)` m. 6 konsistente 90°-Cubefaces aus derselben Kamera, **native** equirectangular **4096×2048**. Das ist eine echte räumlich projizierte 3D-Datei, nicht ein 1774×887-Foto auf 4K hochskaliert.
- Der **Textursampling**-Übergang verursachte zunächst Farbkontrast, nicht geschnittene 3D-Bauteile. `repair_texture_seam.py` gleicht nur die Farben innerhalb von 96 px an jedem Rand periodisch an. Die finale Quelle `P06_Tomioka_1880_3D_NATIVE_SEAM_FIXED_4096x2048.png` SHA-256 `ca0fbed622d6e831eba97a102f0a5630b74c781b04582feb01f1ec6cbe1d2ab5`; JPG SHA-256 `e73de53ace4257de48b100468e7e558c9c6993a7a1d09e8def8bf85ae36de8dc`.
- 12 sphärisch exportierte QA-Ansichten: vorn, hinten, links, rechts, hintere Naht bei pitch±55°, Zenit, Nadir, Dachschrägen, Naht-Nahaufnahme. **3D-Perspektivansichten sind geometrisch konsistent, kein erkennbarer struktureller Formbruch an der Naht.** Die gemessene Pixelkante ist nach der harmonischen Korrektur 0,0× – **kein alleiniger Beweis**, sondern gegen die 3D-Quelle und Perspektivansichten geprüft.
- **Fotorealistischer ImageGen-Versuch** `P06_PHOTOSTYLE_REJECTED_1774x887.png`: 1774×887, relativer Nahtkontrast **2,486×**, künstlich wirbelnde Balken im Zenith. Also ausdrücklich **VERWORFEN als 360°-Panorama**, nur als Stilreferenz im ZIP.
- Geometrisches Modell ist **noch sehr einfach / stilisiert** und der genaue historische Maschinenaufbau nicht vermessungsgenau. Trotz nativer 4K-Geometrie **kein fotorealistischer oder historischer QA-PASS**. QA erfolgte per Bild-/Ray-Prüfung; **kein interaktiver Browser-PASS behauptet**.

## Nächster überprüfbarer Schritt

**Kein neues 2:1-Foto frei erfinden.** In einem separaten `claude/P06-tomioka-pbr`-Branch das beigefügte Python-/VTK-3D-Modell bzw. einen GLTF-/Blender-Import mit **tatsächlichen geometrieerhaltenden PBR-Materialien**, Maschinen-/Menschen-Assets und Tageslicht aufwerten. Ziel: optische Nähe zum ImageGen-Fotostil **ohne** die geraden Hallenbalken, die Maschinen, Naht und Dachpole zu verzerren. Historische Einzelmechanik weiterhin gegen die Meiji-Französisch-Technologie prüfen; kein später automatisierter Reeler und keine Baumwoll-Webstühle. Danach native equirectangulare 4K-Ausgabe, 12 QA-Ansichten und lokalen Pannellum-Drehtest.

**Status `public/data/scenes.json` unverändert:** `target_scenes=30`, `approved_panorama_count=0`; bestehende Piloteinträge/Dateien unangetastet, nichts gemergt/deployt, keine kostenpflichtigen Dienste.