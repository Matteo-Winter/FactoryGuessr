# E01 – Boston Tea Party: neuer 3D-/Fotokandidat, QA noch nicht bestanden

**Stand:** 09.11.2026 · **Aktiver 30er-Szenenplan:** E01 · **User Review vorher:** `boston-tea-party.jpg` „Neu machen“ · **Status nach neuem Versuch:** `redo_requested / new_candidate_qa_failed`, **nicht** visuell neu abgenommen und **nicht `ready`**.

## Historisches Fundament

- Ort **Griffin's Wharf**, Boston, Province of Massachusetts Bay (heute USA), Abend **16. Dezember 1773**.
- Drei private Handelsschiffe **Dartmouth**, **Eleanor** und **Beaver**, Protest gegen Tea Act und privilegierte East India Company, Aktivisten zerstörten Tee und warfen ihn über Bord. Die Bildfiguren sind generisch und **nicht** als historische Porträts bestimmter Beteiligter auszugeben.
- Der geplante Spiel-Lernpunkt ist **Handelsmonopol, Besteuerung ohne parlamentarische Vertretung, koloniale Wirtschaft und Eskalation bis zur Revolution**, nicht ein romantisierter Piratenüberfall.
- Das Schiff-/Kai-/Gebäude-Layout ist ein **historisch informierter Komposit** und keine belegte Augenzeugenperspektive, kein authentisches Foto.

**Quellen:**
1. [The National Archives – The Boston Tea Party](https://www.nationalarchives.gov.uk/education/teaching-resources/boston-tea-party/)
2. [National Park Service – Boston Tea Party Timeline](https://home.nps.gov/articles/000/boston-tea-party-in-real-time.htm)
3. [Massachusetts Historical Society – Boston 1773: The Destruction of the Tea](https://www.historysource.org/history-source-sets/boston-tea-party)
4. [Massachusetts Secretary of the Commonwealth – Road to Revolution](https://www.sec.state.ma.us/divisions/commonwealth-museum/exhibits/online/the_boston_tea_party/the_boston_tea_party_11.htm)

## Tatsächliche Produktion im Chat

Die früher abgelehnte Datei `boston-tea-party.jpg` war weder als zugänglicher Upload noch im Repo-Baum vorhanden; **daher kein direkter Edit der Originaldatei**, sondern neuer Bildkandidat.

1. **Echte 3D-Blockout-Geometrie** aus eigener reproduzierbarer `build_boston_1773.py` (VTK), `render_support.py`. Ein zusammenhängender Quai, 3 Schiffe, 18.-Jh.-Lagerhäuser, Figuren und Teekisten. Kamera `(0.4,3.8,1.68)`, sechs Cubefaces und native **4096×2048 equirectangulare** Kugel.
2. Ein schönerer **fotorealistischer Kandidat**, inhaltlich plausibel auf das Thema ausgerichtet. Aber die KI-Ausgabe ist **1774×887** und **nicht geometrisch an die 3D-Datei gebunden**.
3. Zwölf sphärisch projizierte QA-Ansichten (yaw 0/±90/180, 180 bei pitch ±55, Zenit/Nadir, Naht-Nahblick, Dach/Schiffsmasten). Pixelkantenwert des Fotokandidaten **1,8002×** relativ zu gewöhnlichen Nachbarspalten. Das ist **kein Pass**.
4. Im rückwärtigen Perspektivblick bei yaw 180° trifft **Hafenwasser abrupt auf eine Lagerhauswand**; der 360°-Formbruch ist sichtbar. Weitere Bildgenerierungsvarianten wurden wegen zusätzlicher falscher Schilder, unpassend dramatisierter Verkleidungen und veränderter Geometrie **verworfen**.
5. Fotokandidat zusätzlich auf **4096×2048 hochskaliert** nur für den lokalen Viewer; **keine echten nativen 4K-Fotodetails**. `preview.html` mit Pannellum 2.5.7 sowie 12-Blick-Kontaktsheets und Originale sind im Chat-ZIP enthalten.

## Artefakt-Übergabe und Prüfsummen

**Im Chat, nicht in GitHub hochgeladen:** `FactoryGuessr_E01_Boston_1773_REWORK_CANDIDATE.zip` (8.105.342 Bytes), SHA-256 `e22a4eec95070a1287821cf914819e0eb299a74364c6eb8ad6959f222d07a0d5`.

- `E01_Boston_1773_PHOTO_V1_ORIGINAL_1774x887.png` SHA-256 `5b63e963bb16e6893bdfacfd53a03d20d9ff30f6fbc9ad9d2b2a34e5c7722c52`.
- `E01_Boston_1773_PHOTO_V1_UPSCALED_4096x2048.jpg` SHA-256 `1dc148ad52a920abd7fa0e659a1a33c1a6fb7428980a3c5d5e7b8499dca7e441`.
- `E01_Boston_1773_3D_BLOCKOUT_NATIVE_4096x2048.png` SHA-256 `eb60670870cb9c252c0aa8c729f033ecc93f91777e14fa18fb0a30d499f142ab`.
- `preview.html`, `build_boston_1773.py`, `render_support.py`, `export_12_views.py`, `qa_photo_v1/contact_12_views.jpg`, `qa_3d/contact_12_views.jpg`, `QA_3D_VS_PHOTO.jpg`, `QA_REPORT.json`, `RESEARCH.md`.

**Lokaler Viewer:** ZIP entpacken, in `E01_Boston_1773` `python3 -m http.server 8000` ausführen; `http://127.0.0.1:8000/preview.html` öffnen. 360°-Naht mit Button bei yaw 180° ansehen. **Kein echter interaktiver Browser-PASS aus der ChatGPT-Umgebung behauptet.**

## Gezieltes nächstes Qualitätsgate

**Keine falsche Bildfreigabe.** Um E01 endgültig zu beheben, muss die **fotorealistische** Rückansicht geometrisch neu aufgebaut bzw. mit nachweisbar strukturgebundener 3D-/Bildbearbeitung ersetzt werden, nicht nur der Pixelrand weicher gemacht. Die 3D-Raumreferenz ist für eine geometrisch konsistente Renderer-/PBR-Variante vorhanden. Danach visuell yaw 180°, pitch ±55°, alle Schiffsmasten, Zenit und Nadir im echten Pannellum-Viewer testen. Nutzerentscheidung „Passt“ erst nach Sichtung der tatsächlichen neuen Datei dokumentieren.

**Kein Merge, Deployment oder Status `ready` durchgeführt.** Die historische 30er-Motivliste bleibt unverändert.
