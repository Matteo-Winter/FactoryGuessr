# E03 – Eröffnung des Suezkanals 17.11.1869 – 3D-first Bildversuch und 360°-QA

**Aktiv:** E03, Ägypten/Port Said, 17. November 1869 · **Stand 09.11.2026** · **Vorheriger Nutzerentscheid:** „Neu machen“ für `suezkanal.png` · **Neuer Kandidat:** vorhanden, jedoch **360°-QA FAIL, nicht visuell vom Nutzer freigegeben**. Nicht in `public/` integrieren.

## Historisch überprüfte Grundidee

- Der **Suezkanal** wurde am **17. November 1869** offiziell mit einer Schiffsprozession eröffnet. Der kaiserliche französische Raddampfer **L'Aigle** mit Kaiserin Eugénie führte sie an.
- Eröffnung nahe Port Said: sandige Ufer/noch junger Kanal, Segel-Dampfschiffe, Zuschauer und Zeremonienpavillon aus den Tagen 16./17. November. **Kein** moderner Containerhafen, Betonriesenkanal, heutiger Frachter, Hotelkomplex oder 20./21.-Jh.-Hafenkran.
- Wirtschafts-/ZuWi-Aspekt: neue europäisch-asiatische Handelsroute, Baukonzession/Kapital, ägyptische Souveränität und spätere geopolitische/unternehmerische Machtstrukturen.
- **Rekonstruktionsstatus:** Dieses Spielbild ist ein künstlerisch informierter **KI-Komposit-Schauplatz**, **nicht** eine Original-Fotografie der tatsächlichen Feier; der 3D-Kamerastandpunkt ist nicht historisch vermessen.

### Institutionelle Quellen
1. [Suez Canal Authority – Canal History](https://www.suezcanal.gov.eg/English/About/SuezCanal/Pages/CanalHistory.aspx): Eröffnung 17.11.1869, L'Aigle, Ablauf, globale Bedeutung.
2. [Napoleon.org – Inauguration Ceremony at Port Said](https://www.napoleon.org/en/history-of-the-two-empires/paintings/inauguration-ceremony-of-the-suez-canal-at-port-said-17-november-1869/): zeremonieller Hafenstandort und Schiffsprozession, Unterscheidung 16./17. November.
3. [Napoleon.org – Captains letter (18.11.1869)](https://www.napoleon.org/wp-content/themes/napoleon/annexes/hors-serie/suez/en/html-content/inauguration/voyage/Ismailia_18-11-69.html): tatsächliche Raddampferbreite und Einfahrtsprobleme, keine moderne Schiffskonstruktion.
4. [Technisches Museum Wien – Archivfoto Port Said 16.11.1869](https://forschung.tmw.at/archive/content/titleinfo/68889): zeitgenössischer Bau-/Zeremonienkontext. **CC BY-NC**, daher nicht ungeprüft als frei kommerziell nutzbares Asset einsetzen.
5. [SCA historical photo gallery](https://www.suezcanal.gov.eg/English/MediaCenter/Pages/PhotoGallery.aspx?folder=Historical%2FOpening).

## Tatsächlich ausgeführte Schritte

1. **Eigene echte 3D-Geometrie** via Python/VTK (`build_suez_1869.py`) und `render_support.py`: eine zusammenhängende Wasserstraße, sandige Ufer, Tribüne, Zuschauer, drei historische Dampfer/Schiffe mit Takelage und Radmaschinengeometrie, Uferstützen; **fester Augenpunkt** `(-14.55, 8.1, 2.87)` im 3D-Weltmodell (1,6 m über Terrain).
2. Sechs Cube-Faces aus **derselben** Kamera und sphärisch auf **native 4096×2048** umgerechnet. Drehung der equirectangularen Kugel um 50° für eine bessere Hauptansicht mit Raddampfer. **QA:** native Raumreferenz ist geometrisch konsistent, unabhängig gerenderte 12 Perspektivansichten. Der am 0/360-Übergang gemessene Kontrastquotient beträgt im Ausgangsbild 0,116×, in der um 50° gedrehten Ansicht 1,288× (wechselnder, unkritischer Hintergrund, keine strukturelle Geometrienaht).
3. **Fotorealistische KI-Version als Stilinterpretation**, 1774×887 **native Bildpixel**, separat hochskaliertes 4096×2048 JPG für den 360°-Viewer. Schöne Hauptszene: Raddampfer mit Takelage/Radkasten, Schiffe im Konvoi, Publikum auf sandigem Ufer, Tageslicht. Die Bild-KI hat **keine nachweisbare exakte 3D-Raumprojektion** übernommen.
4. **12 echte sphärisch projizierte Perspektivansichten** des Fotokandidaten. **QA-FAIL** beim Blick nach hinten: Bildrandstoß zwischen Hafenwasser, Wüstenhang und Zuschauerpavillon; **Nahtkontrast 6,6288×** gegenüber durchschnittlichem benachbartem Pixelübergang (native 1774×887).
5. **Lokale Kanten-/Inhaltsreparaturen** mit 300, 400 und 480px ruhig gespannter Uferregion erzeugt, externes Original unverändert gelassen. Die Zahl 0,00× ließ sich technisch erreichen, **aber** die Verbindung löschte Teile der Tribüne und zeigte unnatürlich dehnende bzw. verschwimmende Menschen/Horizonte. **Alle diese Varianten explizit verworfen**, nicht als geometrisch sauber ausgegeben.
6. Weitere Bildgenerierungen produzierten fälschlich eine Boston-Tea-Party-Szene statt Suez; **vollständig verworfen** und **nicht** Teil des E03-Pakets.

### Prüftabelle

| Kriterium | Ergebnis |
|---|---|
| Historischer grober Schauplatz / Sujet | PASS mit Rekonstruktionsvorbehalt |
| Echte 3D-Raumreferenz, Kugelprojektion | PASS |
| Fotorealistische Darstellung der Hauptaktivität | KANDIDAT |
| Fotorealistische 0/360-Naht geometrisch | **FAIL** |
| Fotorealistische Quelle wirklich native 4K | **NEIN, 1774×887; JPG ist Upscale** |
| Perspektivansichten | 12 selbst gerendert |
| Interaktiver Browser / Pannellum auf Nutzer-Mac | **NICHT GETESTET** |
| Historische Detailabnahme und Bildlizenz | Offen |
| Formale Spiel- und Nutzerfreigabe | **Nein** |

### Artefakt (in Chat, noch nicht in GitHub als Binärdateien)

`Made_in_Time_E03_Suez_1869_REWORK_QA.zip`, **6.803.659 Bytes**, SHA-256 `88509c5a1f7ea5e4ef5145b69f0383819c4b649e9d440584def357de2351617d`.
Enthält: `build_suez_1869.py`, `render_support.py`, native 3D-Referenz `E03_Suez_1869_3D_FRONTROT_50_4096x2048.png`, originales Fotobild `E03_Suez_1869_PHOTO_V1_ORIGINAL_1774x887.png`, hochskalierte Testfassung, `preview.html` (Pannellum 2.5.7), QA-Report, zwölf Blickrichtungen je 3D/Fotobild, `QA_3D_VS_PHOTO.jpg`, Originalquellenbericht und Datei-Hashes.

**Nächster Schritt:** Verbindlich **geometrisch gebundene** Realistik aus 3D-/PBR-Rendern oder eine fachgerecht modellierte **komplette rückwärtige Fotobildhälfte**; nicht nur Farbbänder oder Spiegelkopien. Dann dieselbe 12-Blick-QA plus realer interaktiver Viewer, erst danach „Passt“ neu beim Nutzer einholen. E03 bleibt **„Neu machen“**.
