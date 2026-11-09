# P11 – Kakaoverarbeitung in Ghana, Takoradi um 1970

**Aktiver 30-Szenen-Plan:** `P11` (früher Master-Nr. 44), Kategorie Produktionsstätte, Verantwortung Projektleitung. **Stand:** 09.11.2026. **Bildstatus:** `candidate`, NICHT `ready`, **0/30 offiziell freigegeben**.

## Historische Faktenkarte

- **Ort/Periode:** Takoradi, Republik Ghana, circa 1970. Dies ist **keine exakte Rekonstruktion einer identifizierten realen Werkshalle**; die Bildkomposition ist ein historisch informiertes Komposit.
- **Hauptprodukte:** Kakaomasse (cocoa liquor) und Kakaobutter als Halbfabrikate, nicht fertige Schokoladenriegel. Ein 1967 publizierter Beitrag zur Kakaoverarbeitungsindustrie berichtet von West Africa Mills in Takoradi seit den 1940er-Jahren und der Inbetriebnahme einer weiteren Fabrik im Dezember 1964.
- **Prozess:** Fermentierte/getrocknete Kakaobohnen kommen in Jutesäcken an; reinigen/sortieren, rösten, brechen/Schalen trennen, Nibs mahlen, Kakaomasse teilweise pressen und Kakaobutter abführen. Die 1970er Anlage wird mit älteren mechanischen Maschinen, Rösttrommel, Mahlwerk, Presse, Metallrohren, Vats und Teilewagen illustriert. Der genaue Maschinentyp und die wirkliche Raumanordnung sind **nicht historisch verifiziert**.
- **Sichtbare Ratehinweise:** Rohprodukt Bohnen; einige ganze Kakaoschoten in einer kleinen Probe als didaktische Veranschaulichung (kein historischer Beweis, dass frische Schoten massenhaft in der Fabrik angeliefert wurden); große Stahl-/Beton-Industriehalle der späten 1960er Jahre; Blick in tropischen Betriebshof mit älterem Lastwagen; keine Flaggen, Länderbeschriftungen oder Unternehmenlogos. Ghana ist **allein durch Kakaoverarbeitung nicht beweisbar**: optionaler Hinweis zur westafrikanischen Hafenregion.
- **ZuWi-Bezug:** Wertschöpfung im Kakao-Anbauland, industrielle Entwicklungsstrategien nach der Unabhängigkeit, Exportverarbeitung, internationale Preise/Wertschöpfungsketten.
- **Zeittypisch:** Stark mechanisierte Nachkriegsindustrie, ältere Kakaoröster/Pressen, Jutesäcke, einfacher Arbeitsschutz und 1960/70er Kleidung. Keine digitalen Steuerdisplays, LED-Leuchten, moderne Roboter, 2020er Containerterminal-Optik oder elektrische Edelstahl-Showküche.

## Quellen (Recherche 09.11.2026)

1. V. Garaj, *A note on the state of the cocoa processing industry in Ghana*, The Economic Bulletin of Ghana, 11(4), 1967. Takoradi: Industrie und Exportverarbeitung vor 1970. https://www.africabib.org/rec.php?RID=188914927
2. Kwaku Ofosu-Asare, *History of Cocoa Processing or Value-Adding in Ghana*, Forschung/Dissertation (2011), historische Firmen- und Fabrikentwicklung 1960er. https://westminsterresearch.westminster.ac.uk/download/f9a97d3f636d118df183ad0f03b40bd9c8d120eaa954e376e96f8dc94af0bc78/7559666/Kwaku_OFOSU-ASARE.pdf
3. *Potential for Upgrading in Financialised Agri-food Chains: The Case of Ghanaian Cocoa*, peer-reviewed Forschungsartikel, Geschichte/Global Value Chains. https://pmc.ncbi.nlm.nih.gov/articles/PMC7859721/
4. World Bank, *Cocoa Processing Company plant and energy systems*, Prozesskette und technische Komponenten als **spätere** Betriebsbeschreibung, **keine** Bildquelle von 1970. https://documents1.worldbank.org/curated/en/646341468771259669/pdf/multi-page.pdf
5. Ghana Free Zones Authority, *Cocoa Processing Company*, Thema Verarbeitung und Standort Tema **nur als Gegen-/Industriekontext**, nicht als Takoradi-Abbildung. https://gfza.gov.gh/enterprise/cocoa-processing-co-ltd/

## Tatsächlich ausgeführte Produktionsschritte

1. Forschungsbriefing anhand der Quellen, explizite Wahl **Takoradi** aus den im Masterplan zugelassenen Orten.
2. **Eigenständige VTK-3D-Raumwelt** (`build_scene.py`, `render_support.py`): 3.635 Actor-Objekte inklusive Lager, Röst-/Mahl-/Pressmaschinen, Pipework, Jutesäcke, Kakaoprodukte, Personen, Dachstruktur und Betriebshof; feste Kamera bei `(0.15, 7.75, 1.68)` Metern.
3. Aus einem **einzigen 3D-Kamerazentrum** sechs Cube-Faces und mathematisch equirectangular nach 4096×2048 projiziert. Einfache Naht-/Nachbarspaltenzahl **1.1834×** bei Native-PNG (heuristisch). Zwölf sphärisch korrekte Ansichten (Front, ±90°, Rückseite, ±55° Naht, Zenit/Nadir und Dachdiagonalen).
4. **Fotorealistische Stilausarbeitung anhand der 3D-Vorlage:** Ergebnis 1774×887 mit der gewünschten Reihenfolge (links Röster/Bohnen, rechts Pressen, mittig Arbeit/Gang und Materialtransport), **aber ohne nachgewiesene pixelgenaue 3D-Bindung**. Originaler 0/360-Nahtkontrast **5.1369×**; gegensätzliche Gebäudeteile (Presse vs. Ladehof).
5. **Mehrere lokale Reparaturansätze ausgeführt**: graph-cut mit periodischer Spiegelung auf rechter Seite wurde wegen doppelt vorhandener Lastwagen/Menschen verworfen. Eine zweite Variante mit rekonstruierter rückwärtiger Pressenreihe, strukturierter dunkler Trägersäule und enger innerer Graph-Cut-Verbindung wurde in zwölf QA-Ansichten und zusätzlich acht Zoomwinkeln überprüft.
6. Native reparierte Fotoquelle **1774×887** und separat **hochskaliertes** 4096×2048 Browser-JPEG geliefert. Die periodischen Kanten passen numerisch (0.0065× im JPEG); die niedrige Zahl stammt **aus der Bildkonstruktion** und ist **kein unabhängiger Nachweis physikalisch korrekter Vollkugelgeometrie**.

### Qualitatives Urteil – nicht zum Spiel freigeben

- **Gelungen:** klar erkennbarer Kakao-Halbproduktprozess, zeittypische Großfabrik mit vielen Tätigkeiten und Rohstoff-/Produktdetails, subjektiv fotorealistische Hauptansichten; die rohe harte Bildkante tritt in der reparierten Rückansicht nicht mehr auf.
- **Noch nicht bestanden:** Am rückwärtigen Meridian **wiederholte/spiegelsymmetrische Kakaopressen**, zusammengeführte Behälterformen im steilen Rückblick. Das muss bei einer weiteren, streng strukturgebundenen Bildbearbeitung behoben werden. Das 1774×887-KI-Foto **ist nicht** beweisbar als dieselbe geometrisch richtige 3D-Szene rekonstruiert. Exakter Fabrikstand 1970 nur plausibilisiert.
- **Browser/WebGL-Test auf Nutzer-Mac:** noch ausstehend, kein PASS behauptet.
- **Status unverändert:** `public/data/scenes.json`, Bildpfade, `approved_panorama_count=0`; kein Merge/Deployment/Bezahlaufruf.

## Artefakte (Chat-Download, nicht GitHub-Binärdateien)

`Made_in_Time_P11_Ghana_1970_3D_Photo_QA.zip`, **15.266.320 Bytes**, SHA256 `a3eb78adca16f014a62f951f960817e00fe9cdf16fa3da40e40e4af6f9a3d243`.

Enthalten: ursprünglicher und korrigierter fotorealistischer Kandidat, **echtes natives 4K-3D-Panorama**, vollständig ausführbarer 3D-/Kugelprojektionscode, 3D-Materialtextur, Reparaturskripte, 12+8 Perspektivansichten, Vorher/Nachher-Vergleich, QA-Report mit SHA-Werten, `preview.html` als lokaler Pannellum-2.5.7-Vergleichsviewer.

Für lokal: entpacken, im Ordner `P11_Ghana_Takoradi_1970` `python3 -m http.server 8000` starten, `http://127.0.0.1:8000/preview.html` öffnen. Insbesondere Yaw 180°, Pitch ±60° und den internen Graph-Cut-Übergang bei ca. Yaw −132° untersuchen.

**Nächster technischer Schritt:** Anstatt immer mehr Pressen zu spiegeln, das Photo-/3D-Mapping am rückwärtigen Meridian geometriestreu neu aufbauen oder PBR direkt auf 3D-Meshes anwenden; erst dann unabhängigen Browserpass und formale Bildfreigabe beantragen.
