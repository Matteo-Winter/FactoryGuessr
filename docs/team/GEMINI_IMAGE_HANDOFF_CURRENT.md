# GEMINI-Auftrag – Made in Time, 17 offene Bilder (09.11.2026)

**Es gibt 30 aktive historische Szenen.** Nach dem zuletzt akzeptierten Wall-Street-Bild lautet die visuelle Nutzerprüfung **13 „Passt“, 4 „Neu machen“, 13 ohne aktuelles Urteil**. Daher **17 Arbeitspositionen** für den Kollegen. Das alte 26er-/19er-/18er-Briefing ist nicht mehr gültig.

**Lies zuerst:** [Verbindlicher 30er-Bildstatus](../IMAGE_PRODUCTION_STATUS_30.md) · [JSON mit Einzelurteilen](ACTIVE_SCENES_30.json) · [Historischer Masterplan](../SCENE_MASTERPLAN_30.md) · [Ereignis-/3D-QA-Anhang](COLLEAGUE_MASTER_PROMPT_14.md) · [Issue #18](https://github.com/Matteo-Winter/FactoryGuessr/issues/18).

## 4 explizit neu zu erstellende Bilder

- [ ] **T05 · 1975 · Niederlande, Rotterdam/Eemhaven — Containerhafen** (bisher: `rotterdam-container.webp`)
- [ ] **E03 · 1869 · Ägypten, Suezkanal — Eröffnung des Suezkanals** (bisher: `suezkanal.png`)
- [ ] **E05 · 1954 · Guatemala, Guatemala-Stadt — Sturz von Jacobo Árbenz** (bisher: `guatemala-1954.png`)
- [ ] **E07 · 2013 · Bangladesch, Savar/Rana Plaza — Einsturz Rana Plaza** (bisher: `review-rana-plaza.webp`)

**Vorhandene neue Kandidaten:**
- **E03 Suez 1869:** neue KI-Fotofassung wegen struktureller 360°-Bildnaht abgelehnt; [QA-Report](../scene-research/E03_Suez_1869_REWORK_QA.md).
- **E05 Guatemala 1954:** nun ein neuer 3D-first-Foto-Kandidat verfügbar; [technischer Bericht](../scene-research/E05_Guatemala_1954_3D_photo_QA.md). Fotostil visuell vielversprechend; schmale Randfarbe ausgeglichen, aber die fotorealistische Palastarchitektur weicht von der belegten grünlichen historischen Palastfassade ab. **Noch keine positive Nutzerentscheidung**, deshalb `Neu machen` weiter offen. Das ZIP ist im Chat, noch nicht in GitHub-Binärdaten.

## 13 weitere aktive Szenen ohne aktuelles Review

- [ ] **P06 · 1880 · Japan, Tomioka, Gunma — Rohseide**
- [ ] **P07 · 1890 · Deutschland, Ruhrgebiet — Stahl**
- [ ] **P08 · 1900 · DR Kongo (heutiges Staatsgebiet), Äquatorregion / Kongobecken — Naturkautschuk**
- [ ] **P11 · 1970 · Ghana, Takoradi / Tema — Kakaomasse und Kakaobutter**
- [ ] **P12 · 1975 · Saudi-Arabien, Ostprovinz / Dhahran — Erdöl**
- [ ] **P14 · 2018 · Bangladesch, Dhaka — T-Shirts und Kleidung**
- [ ] **P15 · 2023 · Taiwan, Hsinchu — Halbleiterchips**
- [ ] **P16 · 2023 · Chile, Salar de Atacama — Lithiumsalz-Vorprodukte**
- [ ] **T02 · 1750 · Heutiges Ghana, Cape Coast Castle — Atlantische Handelsfestung**
- [ ] **T06 · 2015 · Singapur, Pasir Panjang — Globaler Containerumschlag**
- [ ] **E02 · 1791 · Heutiges Haiti, Saint-Domingue — Beginn der Haitianischen Revolution**
- [ ] **E06 · 1980 · Polen, Gdańsk/Danzig — Solidarność-Werftstreiks**
- [ ] **E08 · 2021 · Ägypten, Suezkanal — Ever-Given-Blockade**

**Hier nicht fälschlich „abgelehnt“ behaupten:** Falls bereits ein Bild existiert, zuerst zeigen und prüfen lassen, nur nötigenfalls generieren.

## 13 positive visuelle Entscheidungen – nicht neu erstellen

- **P01**: `zaandam-saegemuehle.jpg`
- **P02**: `murano-glas.jpg`
- **P03**: `jingdezhen-porzellan.jpg`
- **P04**: `barbados-zucker.jpg`
- **P05**: `gb-1840-textile-mill.jpg`
- **P09**: `gt-1910-banana-packing.jpg`
- **P10**: `automobilfabrik.png`
- **P13**: `cn-2015-electronics-assembly.jpg`
- **T01**: `amsterdam-voc-werft.png`
- **T03**: `kalkutta-handel.png`
- **T04**: `kanton-handel.png`
- **E01**: `nahtloses_panorama_der_boston_tea_party.png`
- **E04**: `wall_street_im_börsencrash_1929.png`

**E04 Wall Street 1929 wurde ausdrücklich mit „perfekt“ bestätigt.** Technische Browser-/Geometrie-/Historien-QA bleiben trotzdem separat und `approved_panorama_count=0`.

## Stil / Vibe / Technik (verbindlich)

Extrem **fotorealistischer, historisch informierter Dokumentarfilm**: man steht in einer echten, plausiblen historischen Arbeits-, Handels- oder Ereignissituation. Keine leeren Hallen, keine generischen KI-Kulissen, keine willkürlich identischen braunen Farbfilter. Echte Handlung (arbeitende Personen, Transportschritte, lokale technische Objekte, glaubwürdige Menschenmengen), landschaftlich und architektonisch korrekte Umgebung der jeweiligen Region und Epoche. Keine Flaggen, keine lesbaren Orts-/Jahres-/Firmenspoiler.

**3D-first statt freiem 2:1-Weitwinkel:** historische Quellen zuerst, dann vollständige räumliche Anordnung von einem **festen Kamerastandpunkt**, echtes equirectangular 360×180°-Panorama, fotorealistisches Bild möglichst mit geometriegebundenem Stil. Nicht nur vorne korrekt: rechter und linker Bildrand **müssen derselbe physische Meridian** sein; auch 180°-Rückblick, Zenit und Nadir. Keine duplizierten Räume/Personen/Schiffe und keine gebogenen Maschinen im perspektivischen Viewer. Nach jeder Generierung mindestens zwölf sphärisch exportierte QA-Blicke (0/90/180/270, 180 bei pitch ±55, hoch, runter, Diagonalen), dazu lokaler Pannellum-Test, falls verfügbar. Pixelmaße ehrlich kennzeichnen: 1774×887 hochskaliert ist **nicht native 4K-Fotorealistik**.

Für jede Szene Recherche-Faktenkarte, echte Grafikdateien, ggf. 3D-Quelle, Quellen/Lizenzen, QA-Kontaktblatt, Vortest und GitHub-PR oder ZIP liefern. Bei nachgewiesenen Fehlern konkrete Verbesserung statt Pixel-Trick, **keine** selbstständige `ready`-Markierung, Merge oder Deployment. Der Nutzer bestimmt die visuelle Freigabe.

**Empfehlung:** E05-Nutzerprüfung erst einholen, dann die übrigen drei expliziten Remakes und anschließend die 13 offenen angehen.
