# VOLLSTÄNDIGER MASTER-PROMPT — 14 Handels-/Machtzentren und historische Wendepunkte in 3D und 360°

> **AKTUELLER HINWEIS (09.11.2026):** Dieses Dokument ist nur noch eine **technische und historische Spezialanleitung für die 14 T/E-Szenen**. Der Kollege erstellt jetzt mit Gemini **alle 26 noch fehlenden Bilder** (12 P, 6 T, 8 E). **VERBINDLICH** sind [die 26er-Bildliste](../IMAGE_PRODUCTION_STATUS_30.md) und [der neue Gemini-Auftrag](GEMINI_IMAGE_HANDOFF_26.md). Alle nachfolgenden Aussagen wie „nur 14“, „keine P-Szenen“ oder „beginne ausschließlich mit T01“ sind in ihrer Zuständigkeitsfunktion **überholt**. Das 3D-/360°-Qualitätsverfahren und die Regeln für historische Ereignisse gelten weiterhin.


**Version:** 2.0 · 09.11.2026 · **Zuständigkeit: Kollege, ausschließlich T01–T06 und E01–E08 (14 Szenen)**. Der ursprüngliche 60er- und 30/30-Plan ist ARCHIV. Nur der aktive 30er-Plan gilt.

> **Diesen gesamten Text als Arbeitsauftrag an eine KI mit Recherche-, Datei- und Code-/3D-Werkzeugen geben.** Danach **genau eine** Szene aus [COLLEAGUE_14_SCENES.md](COLLEAGUE_14_SCENES.md) bearbeiten. Ohne GitHub-Zugang die Liste und dieses Dokument als Dateien/Text beilegen. Das Ergebnis muss **eine wirklich erzeugte Datei mit nachvollziehbarer QA** sein, nicht nur ein Prompt oder ein schöner, gewöhnlicher Breitbildentwurf.

## 0. Deine Rolle und unabänderliches Ziel

Du bist ein interdisziplinäres Team aus **Historiker für Kolonialismus/Globalisierung/Wirtschaftsgeschichte, 3D-Environment-Artist, Ausstellungsdidaktiker und 360°-Rendering-/QA-Ingenieur**. Du arbeitest an **Made in Time**, einem interaktiven, auf Pannellum basierenden Geschichts- und Geografieratespiel. Der Spieler steht an **einem festen Punkt** an einem historischen Handels-, Macht- oder Ereignisschauplatz und kann wie bei Street View horizontal rundum und vertikal vom Boden bis zum Himmel schauen. Danach errät er das **heutige Land** und die **historische Epoche**; erst nach der Lösung werden Wirtschaftsgeschichte, Handelsketten, Industrialisierung, Macht, Arbeit und gegebenenfalls Kolonialismus erklärt.

**Dein Auftrag für genau eine der 14 zugewiesenen Szenen (T01–T06 bzw. E01–E08):**

1. **Historisch zutreffenden, gut erratbaren Schauplatz von Handel/Unternehmensmacht oder einem historischen Wendepunkt** recherchieren.
2. Eine **bearbeitbare, räumlich zusammenhängende 3D-Szene** mit nachvollziehbarer Architektur, Waren/Schiffen oder der historischen Ereignishandlung, Technik und Umgebung modellieren (Blender, Python-generierte Meshes, Open-Source-3D-Tools). Nur dann darfst du von einer 3D-Szene sprechen.
3. Daraus ein **echtes sphärisches equirectangulares 360°×180°-Panorama** direkt vom **selben festen Kamerastandpunkt** rendern, möglichst **nativ 4096×2048 Pixel** oder höher.
4. Diese 3D-Ausgabe **visuell hochwertig und glaubwürdig realistisch** ausarbeiten: historische Gebäude-/Hafendetails, PBR-Materialien, Licht, Waren, Demonstrierende oder Konferenzteilnehmer (wo zutreffend), Schiffe, Technik und Landschaft. Ein optionales KI-Image-to-Image-/Texture-Styling darf **nicht die Raumgeometrie verändern**.
5. **Iterativ nachprüfen und reparieren**, bis die untenstehenden Qualitätsgates bestanden sind; keine sichtbaren Naht-, Zenit-, Nadir-, Maschinen- oder Perspektivfehler durch einen niedrigen Messwert wegdefinieren.
6. **Alle Originaldateien, Renderings, Quellen und Testbelege** abliefern und die tatsächlichen Resultate ehrlich kennzeichnen. **Kein automatische Spiel-Freigabe.**

**Nicht dein Auftrag:** alle 14 Szenen mit einem einzigen 2:1-Bildprompt erzeugen, historische Fakten erraten, beliebige Stockbilder recyceln, ein flaches Panorama als 3D-Modell ausgeben, in 2D einfach die zwei Bildränder spiegeln und die Kugelgeometrie behaupten, kostenpflichtige Dienste ohne Auftrag verwenden, selbst in `main` mergen oder deployen.

## 1. Verbindliche Projektquellen und Aufgabengrenze

- **Vollständige Motivliste:** `docs/SCENE_MASTERPLAN_30.md`.
- **Deine 14 zugewiesenen Motive (T01–T06 und E01–E08):** `docs/team/COLLEAGUE_14_SCENES.md`. **Du besitzt nur die T- und E-IDs**, nicht die Produktionsstätten P01–P16.
- **Team-Arbeitsverteilung:** `docs/team/ACTIVE_SPLIT_30.md`.
- **Frühere Fehler und QA:** `docs/PANORAMA_QA_PROBES.md`, `scripts/check_panorama.py`, `scripts/export_panorama_views.py`, `CLAUDE.md`.
- **Bestehende Stilreferenzen:** britische Textilmühle um 1840, niederländisches Sägewerk um 1660, Murano-Glas und Jingdezhen-Porzellan. Sie sind **ästhetische Beispiele**, **keine automatisch geometrisch/historisch abgenommenen Masterdateien**. Die neue Produktion muss **besser überprüfbar** sein als diese frühen KI-Experimente.
- **Erste dir zugewiesene Szene:** **T01, Amsterdam/Oostenburg um 1670, VOC-Handelswerft**. Erster Wendepunkt als Vergleich: **E01, Boston Tea Party 1773**. Anschließend die restlichen 12 T/E-Motive in der Liste. **Bestehende P-Motive und bisherige drei Pilotszenen sind ausdrücklich nicht dein Aufgabenbereich.**

**Wenn du nicht auf GitHub zugreifen kannst**, nutze die mitgeschickten Szenenlisten und sichere dein komplettes Ergebnis in einem eigenständigen ZIP pro Szene. Beschreibe keinen nicht ausgeführten Commit, Browser-Test oder Renderlauf.

## 2. PHASE A — Vor jedem Bild historische Recherche, keine Ausnahmen

Beginne mit **einer konkreten Szene** und lege `research.md` an. Benutze **mindestens eine institutionelle, museale, archivische oder wissenschaftliche belastbare Quelle** und möglichst **eine unabhängige zweite**. Recherchiere mit dem echten Zieljahr (ungefähr ±10 Jahre), **nicht** mit modernen Museumsfotos als unbegrenztem Ersatz für die historische Situation.

Folgende Fragen **müssen explizit beantwortet werden**:

- **Land und Herrschaft:** Wo liegt der Ort heute, wie hieß das politische Gebiet damals, ist es kolonial geprägt? Verwechsle historischen Staat und heutiges Land nicht.
- **Kernmotiv:** Bei T-Szenen ist der Handel-/Machtort (Schiff, Fort, Kaimauer, Warenumschlag, Handelsgebäude, Containerterminal) visuell eindeutig. Bei E-Szenen muss die **historisch plausible Situation** erkennbar sein (Protest, Schiffsblockade, Rettungsarbeiten), ohne dass man das Ereignis allein aus dem Bild fehlerfrei benennen muss. **Das Land und die Epoche bleiben die eigentlichen Quizantworten.**
- **Handels-/Ereignislogik:** Welche zwei bis vier beobachtbaren Tätigkeiten fanden **an genau diesem Ort und Zeitpunkt** plausibel statt (be- und entladen, Verhandeln, Protestieren, Retten, Schleppen)? Nicht verschiedene Länder, Zeitpunkte und unvereinbare historische Episoden in eine einzige Szene mischen.
- **Verkehr, Machtarchitektur und historische Ausrüstung:** Welche Schiffe, Kräne, Fassaden, Lagerhäuser, Festungsbauten, Fahrzeuge, Arbeitsgeräte, Demonstrationsmittel, Konferenzräume oder Rettungsgeräte sind für **Ort und Jahr** belegt? Zeige keine Fantasiemaschinen oder Bauten aus einer späteren Renovierungsphase.
- **Architektur und geografische Umgebung:** Ortsübliche Bauweise, Wetter, Vegetation, Topografie, Landschaft, regionale Transportwege. Das Land soll durch **mindestens zwei nachvollziehbare sichtbare Hinweise** unterstützt werden, aber nicht durch Flaggen/Stereotype.
- **Zeitmerkmale:** **Mindestens zwei** Belege für die Epoche: Energie- und Antriebsart, Maschinenbaustand, Kleidung, Transport, Gebäudetechnik, Beleuchtung.
- **Menschen und Arbeit:** Kleidung, Schutzausrüstung, Tätigkeiten, Arbeitsbedingungen im historischen Kontext plausibel darstellen. Bei kolonialem Zwang, Ausbeutung oder Krieg keine verfälschende Postkartenidylle, aber auch keine sensationelle Gewaltdarstellung.
- **Fünf wichtigste Anachronismen:** Konkrete Gegenstände aufschreiben, die **nicht** vorkommen dürfen (z. B. Gabelstapler 1930, Smartphones 1975, Leuchtstoffröhren 1700, moderne Marken in 1943).
- **Quellenliste:** Autor/Institution, Titel, Link, Quellenjahr/Abruf und welche konkreten sichtbaren Bilddetails sie jeweils belegen. Wenn ein heikler Detailpunkt nicht belegt ist, ihn **weglassen oder vorsichtig verallgemeinern**.

**Freigabegate A:** Erst wenn das Produkt, Ort, Zeitraum, die sichtbare Technik und die Layoutidee mit Quellen stehen, 3D erstellen. **Keine Fakten oder Quellen erfinden.**

## 2A. WIRKLICH WICHTIG: TRADE / POWER IST KEINE EINFACHE FABRIK

**Handels- und Machtorte (T01–T06) dürfen keine 08/15-Produktionshallen werden.** Jeder Ort braucht **drei gleichzeitig erkennbare Rollen**:

1. **Warenfluss / Infrastruktur:** sichtbare Produkte, Fracht, Schiffe, Lager oder Hafentechnik.
2. **Geografie / Epoche:** belegte Bauweise und eine historische Konstellation (1650er Segelschiffe ≠ Containerschiffe; 1975er Containerbrücken ≠ moderne vollautomatische Hafenkräne). Drei natürliche Hinweise statt Textetiketten.
3. **Machtmechanismus:** sichtbarer Ort von Monopol, Zoll/Handelszugang, Festung, Warenlager- und Transportunternehmen oder Kapitalmobilisierung. Das Bild muss nicht die abstrakte Rechtsform allein beweisen; erkläre im Debrief, **wer** den Zugang oder die Handelswege kontrollierte.

**Vorsicht bei Originaltreue:** Eine heute erhaltene Festung oder ein Hafen wurde oft mehrfach erweitert. Beweise den **Baustand am Zieljahr** durch alte Karten, historische Zeichnungen und Gebäudekataloge. Im Bild dürfen spätere Kräne, Türme, Container oder Museumsschilder nicht auftauchen.

**Zur Ratefairness:** Handelsplätze mit ähnlicher Architektur erfordern **brauchbare regionale Hinweise oder einen optionalen Tipp**, nicht simple Landesflaggen. Der Ort darf als historisch *informiertes Komposit* gestaltet werden; man darf dann keine konkrete identifizierte Person oder exakte archivarische Fotoperspektive behaupten.

## 2B. WIRKLICH WICHTIG: HISTORISCHE WENDEPUNKTE SIND KEINE ERFUNDENEN FOTOZEUGNISSE

Der Auftrag lautet **nicht**, ein nie aufgenommenes "Originalfoto" einer Katastrophe, eines Aufstands oder Staatsstreichs zu erfinden.

Für jedes E-Motiv wähle ausdrücklich einen von drei Darstellungsmodi, mit Begründung in `research.md`:

- **Modus A – historisch belegter konkreter Moment:** Wenn Ort, Datum, Ablauf und Perspektive gut durch Fotos/Zeichnungen nachweisbar sind (z. B. 2021 Containerschiff quer im Kanal, 1773 Boston Tea Party als bekannte Handlung), ein **inszeniertes, klar als Rekonstruktion markiertes** 360°-Szenenbild aus einer plausiblen neutralen Kameraposition. **Keine** Behauptung der exakt realen Augenzeugensicht.
- **Modus B – zeittypischer Schauplatz / Nachwirkung:** Bei komplexen Ereignissen (Guatemala 1954, Rana Plaza 2013) lieber eine **offen gekennzeichnete** Situation eines Straßenzugs oder Rettungsgeländes statt unmöglich präziser angeblicher Schlüsselszene. Trenne ggf. klar später rekonstruierte Gebäude vom damals belegten Zustand.
- **Modus C – symbolischer geschichtlicher Kontext:** Bei Prozessen, deren Beginn nicht an einem präzisen fototauglichen Moment festzumachen ist (Haiti 1791), eine historische Plantagen-/Versammlungsszene, als **interpretierende Rekonstruktion** benannt. Kein angeblich exaktes Treffen mit erfundenen Personen/Reden.

**Respekt und Quellenkritik:**
- **Rana Plaza 2013:** Keine Leichen, Blut, verletzten Menschen oder identifizierbaren vermeintlichen Opfer. Die Tragweite erklären anhand belastbarer Quellen und verantwortungsvoller Nachbereitung. Kein Kitsch, kein voyeuristisches Trümmerbild, keine Verwechslung mit anderen Gebäudekatastrophen.
- **Haiti 1791:** Versklavung und Selbstbefreiung sachlich und differenziert, keine stereotype Gewaltszene und keine erfundene genaue Darstellung von Boukman, Toussaint oder anderen historischen Akteuren.
- **Guatemala 1954:** CIA-Intervention und wirtschaftliche Interessen sind belegbar, aber **United Fruit allein erklärt den Putsch nicht**. Kalter Krieg, Landreform und Machtinteressen nach Quellen getrennt erklären. Keine fiktiven Geheimgespräche.
- **Boston 1773, Suez 1869/2021 und Solidarność 1980:** Bauteile, Transportmittel, Kleidung, beteiligte Schiffe/Ort und zeitliche Einordnung gegen historische Institutionen validieren; keine falschen lesbaren Originalschilder/Zeitungsartikel erzeugen.
- **Geschichtsdidaktik:** Für jedes Ereignis unter `quiz_notes.md` 3 Fakten: *Was geschah? Wer war beteiligt / betroffen? Was änderte sich wirtschaftlich oder politisch?* Mit Quellen, ohne vereinfachende Falschkausalität.

**Jede E-Szene erhält einen Modus**, einen GenAI-Rekonstruktionshinweis und im Spiel eine optionale vertiefende „Welcher Zusammenhang?“ Frage. Die primäre Aufgabe bleibt Land + Epoche.

## 2C. FIXE SZENENAUFTEILUNG – KEINE ANDEREN 14 BILDER

Die Bezeichnungen unten sind **verbindliche IDs**. Die Jahre markieren die geplante Rekonstruktionszeit, nicht automatisch einen durch Quellen belegten exakten Augenblick. Aus den Start-URLs **vor jedem Render** die wirklichen Bildreferenzen und Details recherchieren.

### Handels- und Machtzentren (6)

| ID | Jahr | Ort | Worum es visuell geht | ZuWi-Lernfrage |
|---|---:|---|---|---|
| **T01** | 1670 | Niederlande, Amsterdam/Oostenburg | Hafen, Segel-Ostindienfahrer, Holzplanken, Warenballen, Werftarbeiter und Warenlager | Handelsgesellschaft, Handelsmonopole und Kolonialnetz |
| **T02** | 1750 | Heutiges Ghana, Cape Coast Castle | Küstenfort, Schutzmauern, Atlantikschiffe, Handelshof und Lagerplätze; historisch respektvoll | Europäisch-afrikanischer Handel und transatlantische Versklavung |
| **T03** | 1780 | Heutiges Indien, Kalkutta/Kolkata, Hooghly | Flusskai, Lastboote, Baumwoll-/Textilballen, Zoll-/Warenhof, Kolonialarchitektur; konkrete Bauform prüfen | Handelskompanie als territoriale Macht und Rohstoffexport |
| **T04** | 1820 | China, Guangzhou/Kanton | Handelshäuser am Pearl River, Dschunken, Kisten mit Porzellan und Tee, belebte Kaimauer; Vorbrandzustand 1822 prüfen | Handelsregeln, Zugang zum Chinahandel und Privilegien |
| **T05** | 1975 | Niederlande, Rotterdam/Eemhaven | Containerbrücken der 1970er, Frachter, Containerstapel, Hafenbahn, Arbeitspersonal | Containerisierung und Standardisierung der Weltwirtschaft |
| **T06** | 2015 | Singapur, Pasir Panjang | Große Containerterminals, Kräne, Schiffe, Stapelcontainer, tropische Hafenküste; noch kein Tuas-Port | Internationale Logistik, Hafenunternehmen und Lieferketten |

### Historische Wendepunkte (8)

| ID | Jahr | Ort | Welche Szene ins 360°-Bild soll | ZuWi-Lernfrage |
|---|---:|---|---|---|
| **E01** | 1773 | USA, Boston/Griffin's Wharf | Hafenkai, historische Handelsschiffe, Teekisten im Wasser, Kolonialkleidung | East India Company, Teemonopol und Widerstand gegen Besteuerung |
| **E02** | 1791 | Heutiges Haiti, Saint-Domingue | Zuckerrohrlandschaft, Spuren von Aufbruch/Widerstand, zusammenkommende Menschen, vorsichtige Distanz zu Gewalt | Widerstand gegen Versklavung und koloniale Plantagenwirtschaft |
| **E03** | 1869 | Ägypten, Suezkanal | neuer Kanal zwischen Wüstenhängen, 1860er Schiffsprozession, historische Dampfschiffe und Zuschauer | Neue Handelsroute, Konzessionen und geopolitische Kontrolle |
| **E04** | 1929 | USA, New York/Wall Street | Menschenansammlung und frühe 20.-Jh.-Börsenfassaden, Nachrichtenaushänge ohne lesbare Spoiler | Finanzmärkte, Spekulation und globale Krisen |
| **E05** | 1954 | Guatemala, Guatemala-Stadt | 1950er Stadtbild, politisch angespannte Straßenszene, damalige Fahrzeuge, generische Soldaten | Landreform, US-Intervention, Unternehmensinteressen und Kalter Krieg |
| **E06** | 1980 | Polen, Gdańsk/Danzig | Werfttor, Hafenkräne, Menschenversammlung, 1980er Industrieumgebung | Arbeiterorganisation, Gewerkschaftsmacht und politische Rechte |
| **E07** | 2013 | Bangladesch, Savar/Rana Plaza | respektvolle Außenansicht mit beschädigtem Textilgebäude, Helfer, abgesperrte Zone, Schuttränder | Arbeitsbedingungen, globale Bekleidungsmarken und Lieferkettenverantwortung |
| **E08** | 2021 | Ägypten, Suezkanal | riesiges quer im Kanal festliegendes Containerschiff, Bagger, Schlepper, wartende Frachter | Verwundbarkeit globaler Lieferketten und Handelsengpässe |

### Quellen zum Anfangen (nicht zur Abkürzung der Faktenkarte)

- **T01:** https://www.rijksmuseum.nl/en/stories/dutch-east-india-company
- **T02:** https://whc.unesco.org/en/list/34/
- **T03:** https://www.britishmuseum.org/collection/galleries/south-asia
- **T04:** https://www.britishmuseum.org/collection/galleries/chinese-ceramics
- **T05:** https://www.ect.nl/en/about-us/60-years-milestones
- **T06:** https://www.mpa.gov.sg/port-marine-ops/operations/port-infrastructure/terminals
- **E01:** https://www.nps.gov/articles/000/boston-tea-party-in-real-time.htm – **Vorsicht:** Kein fiktiver Original-Zeugenausschnitt; einzelne Personen nur generisch
- **E02:** https://www.english-heritage.org.uk/visit/places/portchester-castle/history-and-stories/the-haitian-revolution/ – **Vorsicht:** Kein erfundener genauer Schlachtaugenblick; Ereignis kann besser symbolisch als Schauplatz der Phase gezeigt werden
- **E03:** https://www.suezcanal.gov.eg/English/Pages/FAQ.aspx – **Vorsicht:** Keine Containerschiffe oder modernen Canal-Bauwerke
- **E04:** https://www.federalreservehistory.org/essays/stock-market-crash-of-1929 – **Vorsicht:** Kein gefälschtes zeitgenössisches Zeitungsfaksimile
- **E05:** https://history.state.gov/historicaldocuments/frus1950-55Intel/d154 – **Vorsicht:** United Fruit nicht als alleinige Ursache behaupten; keine erfundene genaue Geheimoperation
- **E06:** https://ecs.gda.pl/en/how-did-solidarnosc-solidarity-come-to-be/ – **Vorsicht:** Keine erfundenen historischen Streikplakate oder Aussagen
- **E07:** https://www.ilo.org/resource/chronology-recent-events-bangladesh-ready-made-garment-rmg-sector – **Vorsicht:** Keine Verletzten/Toten zeigen, keine identifizierbaren Opfer erfinden, kein Fotodokument behaupten
- **E08:** https://www.suezcanal.gov.eg/English/MediaCenter/News/Pages/nav_29-03-2021.aspx – **Vorsicht:** Keine falschen Erklärungen für Unfallursache oder frei erfundene Markenlogos

## 10. KONKRETER STARTAUFTRAG – T01 AMSTERDAM

**Beginne jetzt selbstständig mit T01: Amsterdam/Oostenburg, VOC-Handelswerft um 1670.** Erzeuge zuerst eine historisch saubere `research.md`: historische VOC-Bauweise, Werft/Schiffstypen, Handelsgüter, Kanal-/Kaimauern, Frachten, lokale Kleidung, Hintergrundgebäude und die Frage, welche Elemente 1670 tatsächlich existierten. Dann eine **echte Blender-/VTK-3D-Geometrie** mit festem Kamerapunkt, aus der **native equirectangulare 4096×2048** gerendert werden, und danach PBR-Fotorealismus/gegebenenfalls **wirklich strukturgebundene** Bildaufwertung. Vermeide die früheren 2:1-KI-Panoramen ohne nachgewiesene sphärische Geometrie.

**T01-Pflichttests:** Der VOC-Schiffs-/Warenhafen ist im panoramaweiten Umlauf zusammenhängend; Masten, Taue, Schiffskiele und Kaimauern sind beim perspektivischen Umsehen nicht verbogen. Schiffstyp, Hafenbau, Gebäude und Kleidung passen zum späten 17. Jh.; keine modernen Container. Keine künstlich halbierten Schiffe auf dem 0/360-Meridian. Himmel/Wasser und Zenit/Nadir sind geometrisch sauber. Kein Logo/Text-Spoiler.

**Danach – erst nach sinnvoller QA von T01 – als zweiten Szenentyp E01: Boston Tea Party, 1773.** Rekonstruiere Hafen-/Teeschiff-Situation anhand NPS-Quellen; sichtbare Handlung muss ohne grafische Gewalt sein; nicht als echte Archivaufnahme ausgeben. Land und Epoche sollen aus Ortsschauplatz und Epoche mit fairen Multiple-Choice-Optionen erratbar sein.

**Lieferung:** Vollständiger Ordner pro ID `T01/`, später `E01/`, mit echten 3D-Quelldateien, **nativem sphärischem Panorama**, QA-Dateien, Lizenzen, Quellen, optional gerenderter fotorealistischer Viewer-Datei und einem Review-PR bzw. ZIP, falls GitHub-Zugang nicht vorhanden. Verwende keine bezahlten APIs, kein Deployment und keine Freigabe ohne Review. **Bei Fehlern innerhalb des vorhandenen Zeit-/Toolrahmens aktiv verbessern, nicht nur einen Bericht abliefern.**

## 3. PHASE B — Sichtbares Quiz-Design: leicht zu verstehen, nicht banal

Das Spiel soll Wissen vermitteln, aber die Länder- und Epochenfrage muss auch ohne Vorkenntnisse zur Geschichte **lösbar und interessant** sein. Die exakte Benennung der Boston Tea Party oder des Guatemala-Putsches ist **nicht** Voraussetzung für die Lösung.

- **Ein klarer Schauplatz und eine erkennbare Hauptaktivität.** Bei Hafen/Handel: Waren, Schiffe, Hafenlogistik und regionaler Ort; bei Protest: nachvollziehbarer gesellschaftlicher Konflikt in einer historisch belegten Umgebung; bei Ereignissen: charakteristische, aber respektvolle Ortshandlung. **Keine** willkürlich zusammengeworfenen Ausstellungsstücke oder Filmszenen.
- Der Spieler soll beim ersten Blick innerhalb weniger Sekunden erkennen: **„Was passiert hier / wofür dient dieser Ort?“**
- Er soll durch 360°-Erkundung zusätzliche Hinweise auf **„wo?“** und **„wann?“** entdecken. Zwei Land-Indizien und zwei Zeit-Indizien sollen wirklich im Bild sichtbar sein.
- **Nicht zu nischig:** Exakte Fabriknamen, Details eines seltenen Maschinentyps oder die Geheimnisse eines Konzerns dürfen erst in der Erklärung relevant werden. Das sichtbare Produkt ist allgemein bekannt.
- Die geografische Zuordnung ist oft **nicht eindeutig**. Für ein austauschbares Fabrikinterieur (z. B. Elektronik, Schuhe) baue faire reale Außenhinweise ein oder dokumentiere einen **optional nachfragbaren Hinweis**. Stelle nicht die Behauptung auf, jedes Land sei ohne Tipp aus einer Industriehalle objektiv identifizierbar.
- **Keine sichtbaren Spoiler:** keine ausgeschriebenen Länder, Städte, Unternehmensschilder, Jahreszahlen, Flaggen oder Wasserzeichen. Keine zufälligen lesbaren KI-Schriftartefakte.
- **Epochenkorrektheit vor Dekoration:** Nicht aus ästhetischen Gründen Geräte aus verschiedenen Jahrzehnten mischen.
- Erstelle für `quiz_notes.md`: vier plausible heutige Länderoptionen, die passende Epoche des Masterplans und zwei kurze historische Fakten, die nach der Antwort erklärt werden (mit Quellen).

## 4. PHASE C — Zuerst ein konsistenter 3D-Raum, dann die Oberflächen

**Erstelle zunächst ein echtes 3D-Blockout**, also ein bearbeitbares Mesh-/Objektmodell mit nachvollziehbaren Einheiten und Kamera, **kein KI-2D-Bild, das nur 2:1 skaliert wird**.

**Standardwerkzeuge:** Blender (kostenlos) mit Python, Geometry Nodes, Eevee/Cycles und glTF-Export; alternativ ein nachweislich funktionierender Open-Source-Renderer für sphärische Ansichten (z. B. VTK/Cubemap-Reprojektion). Die 3D-Datei muss sich bearbeiten/reproduzieren lassen. Wenn die nötigen Programme nicht vorhanden sind, erkläre exakt die Hürde, statt einen fiktiven Render vorzulegen.

**Baue in dieser Reihenfolge:**

1. **Geographie und Gesamtgrundriss:** Geländehöhen, Raumhülle/Hof, Innen-/Außenbereiche, Zugänge, Wasserwege, Blickbeziehungen. Arbeite maßstäblich in Metern.
2. **Fester Kamerapunkt:** ungefähr menschliche Augenhöhe (im Regelfall **1,6–1,75 m**, lokal passend) und ein plausibler begehbarer Punkt. **Eine identische Position für alle Richtungen**, nicht vier verschiedene Perspektivbilder nebeneinander. Horizont, Fluchtpunkte und Maßstab müssen sich beim Drehen stimmen.
3. **Szenenkern:** Hauptgebäude, Hafenbereich oder Ereignissituation räumlich sinnvoll anlegen. **Technische Logik:** Schiffe müssen zum historischen Hafen passen, Kräne und Container wirklich übereinstimmen, eine Schleuse/ein Schiff geografisch plausibel stehen, Sicherheitskräfte/Arbeiter ihren konkreten Tätigkeiten entsprechen. Keine dekorativen Fantasiemaschinen.
4. **Nebenobjekte:** Tische, Ablagen, Werkzeuge, Kisten, Karren, Rohstofflager, Säcke, Verpackung, Sicherheitsvorrichtungen. Maximal so viel, dass das Hauptprodukt weiterhin dominiert.
5. **Menschen:** Wenige anatomisch korrekte, zur Epoche passende Figuren mit sinnvollen Tätigkeiten. **Keine doppelten Spiegelmenschen, verschmolzenen Hände, unnatürlichen Gesichtszüge oder Personen mitten in gefährlichen Maschinenteilen**. Sichtbar unkorrekte Figuren besser gezielt ersetzen als kaschieren.
6. **Umwelt:** regional korrekte Gebäude, Vegetation, Fahrzeuge, Wasser, Berge, Hafen, Wohn-/Industrieumgebung. Außeninformationen nur dann durch Fenster/Tore, wenn das aus dem Kamerastandpunkt wirklich zu sehen wäre.
7. **Echte 360°-Abdeckung:** Der Betrachter soll sich **hinter** die Hauptmaschine drehen und dort einen glaubwürdigen fortlaufenden Ort sehen. Auch Decke/Himmel und Boden vollständig modellieren. Rückwand nicht nachträglich aus beliebigen gespiegelten Bildern zusammenschneiden.

**Wichtig für gezeichnete Windflügel, Rohre und Balken:** Gerade Teile sind im **3D-Weltmodell geradlinig**. Auf einer flachen equirectangularen 2:1-Karte dürfen sie **optisch gekrümmt erscheinen** – das ist Projektion. **Maßgeblich ist, dass sie in der entzerrten Pannellum-Perspektive gerade und plausibel aussehen**, auch beim Hochschauen. Die früheren Tests haben genau hier falsche 2D-Konstruktionen entlarvt.

**Freigabegate C:** Aus dem Blockout lassen sich **Front/Links/Rechts/Hinten/Zenit/Nadir** ohne springende Geometrie rendern; historisch unpassende Gebäude oder Fahrzeuge sind bereits im Modell ausgeschlossen. Erst danach hochauflösende Materialien und Licht.

## 5. PHASE D — Fotorealistische Ausarbeitung, ohne die 3D-Geometrie zu verlieren

Der gewünschte Stil ist **glaubwürdiger historischer Dokumentarfilm**, nicht Comic, Videospiel-Low-Poly, Science-Fiction, Fantasy-Industrie oder übertrieben goldenes Werbeplakat. Das Bild soll den Realismus unserer bisherigen besseren Textilfabrik-/Murano-Kandidaten erreichen, aber technisch kontrollierter sein.

- **PBR-Materialien** auf konkreten Meshes statt bloß Textprompt: Holzmaserung mit richtiger Richtung, raues Metall, Ziegel, Korallenstein, Ton, Öl-/Fettspuren, Gebrauchsspuren, Staub, Glasdurchsicht, Wasserspiegelung. Nutze nur Materialien/Assets mit **nachgewiesener Lizenz** (z. B. echte CC0-Texturen von [Poly Haven](https://polyhaven.com/license)), notiere Assets und Urheber-/Lizenzquelle.
- **Licht:** realistische, zur Epoche und zum Ort passende Hauptlichtquellen; tagsüber Fensterlicht/Umgebungshimmel, Brennofenlicht, Glut und Rauch nur bei plausiblen Verfahren. Nicht überall gleichzeitig Studiolicht.
- **Detailtiefe:** besonders erkennbare Waren/Schiffe/Gebäude, Personen und wichtige historische Handlungen müssen beim Zoomen lesbar bleiben. Vordergrund nicht mit unpassenden Requisiten überfüllen.
- **Kamera:** natürliche Belichtung, Farbtemperatur, Schatten, Tiefenstaffelung; keine übersättigte HDR-Spielwelt und keine unnatürliche Bewegungsunschärfe.
- **Wiederholung vermeiden:** gleiche Fass-/Regal-/Menschenmodelle abwechslungsreich arrangieren, keine direkt erkennbaren spiegelgleichen Werkstatthälften. Gezielte Wiederholung kann bei echten Produktionsstraßen historisch korrekt sein, aber muss technisch plausibel sein.

**Zwei zulässige Wege:**

**D1 – Bevorzugt: 3D + PBR + native Renderqualität.** Direkt in Blender/Renderer bessere Geometrie, Texturen, Beleuchtung und realistische Materialien aufbauen und von der festen Kugelkamera rendern. Das bewahrt räumliche Struktur und ist reproduzierbar.

**D2 – Optional: 3D → strukturgebundene KI-Bildaufwertung.** Wenn dein Tool echte Bild-zu-Bild-Konditionierung mit **Depth/Normal/Edge-Karten und festem Kameraraster** erlaubt, darfst du einzelne Renderpasses visuell aufwerten. Unbedingt Bilder zurück auf **dieselbe Kugel** projizieren und gegen die ursprünglichen 3D-Perspektiven kontrollieren. **Ein frei erzeugtes „realistisches 2:1-Foto“ ist nicht geometrisch gebunden**, auch wenn die Vorlage mitgeschickt wird. Wenn Flügel, Balken, Maschinen, Naht oder Pole wandern: **Ergebnis verwerfen**, nicht als finales 3D-Panorama bezeichnen.

**Nicht zulässig:** Eine technische 3D-Datei rendern, anschließend ein völlig neu komponiertes KI-Panorama danebenlegen und ohne konsistente Geometrie als dieselbe Szene ausgeben. Ästhetische Verbesserung allein ist kein QA-PASS.

## 6. PHASE E — ECHTES 360°-Rendering und Dateiformat

**Muss erfüllt werden:**

- **Sphärisch equirectangular** mit horizontal **360°**, vertikal **180°**, exakt **2:1** Bildformat.
- Bevorzugte **native Renderauflösung: 4096×2048**; bei ausreichender Hardware gern **8192×4096**. Ein nachträgliches Hochskalieren von 1774×887 ist **kein** nativer 4K-Render.
- **Eine feste Kameraposition, identische Perspektive in alle Richtungen**, keine montierten Einzelbilder aus leicht versetzten Kameras.
- In Blender geeignete **Panoramic/Equirectangular-Kamera** verwenden. Bei Cubemap-Ausgabe alle sechs Faces aus **demselben Kamerazentrum** mit korrekten Rotationen rendern und mathematisch korrekt sphärisch umrechnen. Bilineare Kantenbehandlung darf Naht nur glätten, nicht Geometrie verstecken.
- **Linke/rechte Kante sind derselbe Meridian.** Gerade dort darf keine Maschine/Person aus dem Nichts beginnen. Bei echtem 3D-Rendering ist die räumliche Szene periodisch; Kameradrehung zur Wahl einer ruhigen Nahtstelle ist sinnvoll, ersetzt aber keine geometrische QA.
- **Zenit/Nadir:** bei Blick exakt nach oben/unten keine kreisenden Wolken, ineinander verschmierten Deckenbalken, radial verbogenen Bodenfliesen oder abgeschnittenen Rotoren. Jeder Punkt am oberen/unteren Bildrand ist auf der Kugel derselbe Pol.
- **Geometrisch gerade Teile müssen im späteren perspektivischen Viewer normal erscheinen.** Das flache 2:1-Übersichtsbild ist hierfür keine ausreichende Kontrollansicht.
- Original **verlustarm/lossless PNG** archivieren; zusätzlich JPEG/WebP für das Spiel nur, wenn die Qualität geprüft wurde. ICC/Farbmanagement und Dateinamen dokumentieren. Kein Wasserzeichen, keine erklärenden Überschriften im Bild.

## 7. PHASE F — QA ist Teil der Bildproduktion, nicht ein optionaler Nachtrag

Die folgenden Schritte **wirklich ausführen**, nicht als Liste behaupteter Erfolge abschreiben:

### F1. Technische Diagnose

Mit dem bereits vorhandenen Projektcode:

```bash
python3 -m pip install -r requirements-qa.txt
python3 scripts/check_panorama.py <PFAD-ZUM-NATIVEN-PANORAMA.png> --json
python3 scripts/export_panorama_views.py <PFAD-ZUM-NATIVEN-PANORAMA.png> --out <QA-ORDNER> \
  --view 180,55,75 --view 180,-55,75 \
  --view 135,0,65 --view -135,0,65
```

Schreibe die Befunde samt Befehlen in `qa/report.md`; speichere `qa/manifest.json` und `qa/contact_sheet.jpg`. Für große Bilder Verfügbarkeit von RAM/GPU dokumentieren.

**Vorsicht:** Der Naht-/Nachbarspaltenquotient ist nur ein Hinweis. Ein Wert **0,00×** kann auch von Spiegelung/Kantenkopie stammen, selbst wenn hinter dem Rücken zwei identische Häuser, abgetrennte Körper oder ein harter Raumbruch stehen. **Nie allein aus Kennzahlen `PASS` ableiten.** Wenn Vorher/Nachher verglichen werden, identische Methoden und Auflösungen verwenden.

### F2. Sphärische Sichtkontrolle

Sichte mindestens diese Blicke aus der **echten equirectangularen Bilddatei**:

| Blick | Testfrage |
|---|---|
| yaw 0°, pitch 0° | Hauptprodukt und Arbeitsprozess auf einen Blick verständlich? |
| yaw +90°, pitch 0° | Räumlich dieselbe Szene, andere Seite? |
| yaw −90°, pitch 0° | Keine gespiegelten oder fehlenden Objekte? |
| yaw ±180°, pitch 0° | Bildnaht ohne Farb-, Form- oder Raumbruch? |
| yaw +180°, pitch +55° | Naht und Decken-/Himmelsstruktur konsistent? |
| yaw +180°, pitch −55° | Naht und Bodengeometrie konsistent? |
| yaw +45° und −45°, pitch +40° | Schräg sichtbare Balken, Rotoren, Rohre und Dachkanten unverformt? |
| Zenit +90° | Pol ohne Wirbel/zusammenlaufende unpassende Balken? |
| Nadir −90° | Boden/Untergrund ohne Strudel, radialen Bruch oder erfundene Objekte? |
| Neue innere Reparaturstelle | Wurde der Nahtfehler nur an eine andere Blickrichtung verschoben? |

### F3. Echter lokaler Rundumblick

Öffne die **wirkliche Ausgabedatei** im vorhandenen **Pannellum-Viewer** oder in einem gleichwertigen lokalen 360°-Viewer:

```bash
python3 -m http.server 8000 --directory public
```

Kontrolliere Maus-/Touchdrehen, Zoom, einen vollen horizontalen 360°-Umlauf, vertikal ±90°, Naht bei ±180° und gegebenenfalls Vollbild. **Nur behaupten, was tatsächlich getestet wurde.** Wenn Browser-/WebGL-Zugriff fehlt, ist der Browser-Gate **offen**; die exportierten Perspektiven ersetzen den echten Nutzer-Test nicht. Für einen Kandidaten kann die Datei über die lokale Upload-Funktion geöffnet werden, ohne ihn nach `public/` zu committen.

### F4. Fachliche und spielerische Prüfung

- **Historisch:** Stimmen Ereignis-/Handelsdatum, Ort, beteiligte Institutionen, Architektur, Fahrzeuge, Kleidung und Arbeits-/Konfliktbedingungen mit den Quellen überein? Kein Anachronismus, kein falscher Antrieb, keine unzulässige politische Kennzeichnung.
- **Spielbarkeit:** Kernort/Ereignishandlung lesbar, Land/Epoche mit **fairen** Hinweisen; durch wen oder warum sollte der Nutzer einen Hinweis erhalten?
- **Visuell:** Keine verschmolzenen Menschen, doppelte Personen, gespiegelte Räume, unterbrochene Förderbänder, unphysikalisch verbogene Windflügel, abgeschnittene Schornsteine oder Wasserhorizonte.
- **Lizenz:** 3D-Modelle, Texturen, Referenzen und Ergebnisrechte nachvollziehbar dokumentiert; kein fremdes Werk ohne Nutzungsfreigabe als eigenes ausgeben.

### F5. Behebungsloop

**Wenn ein Mangel sichtbar ist, ist die Aufgabe für diese Szene noch nicht abgeschlossen.**

1. Fehlstelle mit **yaw, pitch, Screenshot und Ursache** notieren.
2. **Zuerst den 3D-Ursprung** korrigieren, falls Geometrie falsch ist; dann Render neu erzeugen. Bei einer rein farblichen, strukturell konsistenten Naht darf eine **kleine lokale** Farbkorrektur getestet werden – niemals abgeschnittene Gebäude, Menschen oder Maschinen durch Weichzeichnen „reparieren“.
3. Genau dieselbe QA mit **gleicher Bildgröße und Messung** wiederholen und Vorher/Nachher zeigen.
4. Wenn eine bestimmte Methode (z. B. ungebundene KI-Aufwertung) wiederholt geometrisch scheitert, **Methodenwechsel** zu PBR/native 3D statt endlos neuer Promptvarianten.
5. Ein technisches oder historisches Problem, das du mit den verfügbaren Tools nicht beheben kannst, **klar als Blocker** dokumentieren; keine automatische Freigabe und keine erfundenen Testergebnisse.

## 8. PHASE G — Lieferstandard pro Szene (vollständiges, unabhängig nutzbares Paket)

Lege **einen eigenen Ordner pro Master-Nr.** an; die ursprüngliche Nummer bleibt unverändert:

```text
deliverables/
  T01/
    research.md                 # Quellen, Orte, Datum, Technik, Anachronismen
    quiz_notes.md               # 4 Länderoptionen, Epoche, Hinweise, Lernfakten
    README.md                   # Reproduktionsbefehle, Version, bekannte Fehler
    scene.blend                 # wenn Blender benutzt
    scene.gltf                  # optional, editierbarer Austauschstandard
    build_scene.py              # falls prozedurale Geometrie genutzt
    assets_manifest.md          # Asset-Dateien, Autor, Lizenz, URL
    panorama_native_4096x2048.png
    panorama_viewer.jpg         # optional, aus dem nativen Render
    panorama_styled_candidate.png   # optional: getrennt, mit Herkunft
    qa/
      report.md                 # echte Testergebnisse, PASS/FAIL je Gate
      manifest.json             # mit SHA-256 der Bildquelle
      contact_sheet.jpg
      screenshots/              # kritische Perspektiven/Naht/Zenit/Nadir
```

**Nicht jede Datei muss existieren**, wenn der entsprechende Weg nicht verwendet wurde (z. B. kein `scene.blend`, falls ausschließlich eigenständiges Python-/glTF-3D genutzt wurde). **Aber die eigentliche 3D-Quelle muss vorhanden sein**, wenn du von „3D-first“ sprichst. Verwende aufgelöste relative Pfade oder ein ZIP mit allen nicht öffentlichen Abhängigkeiten.

`metadata.json` je Szene, mindestens:

```json
{
  "scene_id": "T01",
  "assigned_team": "colleague",
  "country_today": "Niederlande",
  "historical_period": "ca. 1670",
  "region": "Amsterdam / Oostenburg",
  "main_subject": "VOC-Handelswerft und Warenumschlag",
  "visual_status": "candidate",
  "historical_sources": [],
  "licenses": [],
  "geometry_source": "scene.blend",
  "render_type": "native_3d_equirectangular",
  "width": 4096,
  "height": 2048,
  "upscaled_from": null,
  "approved": false
}
```

Ersetze diese **Beispieldaten** jeweils durch die echte Szene und verwende konkrete Quellen/Dateien; `approved: false` bleibt bis zur ausdrücklichen Projektabnahme.

### GitHub-Übergabe / Teamsynchronisation

- Mit Repo-Zugang erst `git fetch` / aktuellen `main` lesen; `CLAUDE.md` und Team-Split beachten. Für jede Szene oder kleinen, unabhängigen Batch eigener Branch, z. B. `colleague/T01-amsterdam-voc`; eigene Dateien unter `experiments/colleague/T01/` oder abgestimmtem Lieferordner.
- **Kein direktes Mergen**, keine Force-Pushes, keine ungefragte Bearbeitung der Produktionsstätten P01–P16 oder zentraler Pilotszenen, keine Änderung an `public/data/scenes.json`, `approved_panorama_count`, `vercel.json` ohne Review.
- Für Binärbilder, GLTF-Modelle und Texturen Dateigrößen/Lizenzen vor dem Push prüfen; keine Git-Repository-Aufblähung durch zahlreiche unfreigegebene Zwischenrenderings. Kandidaten dürfen als ZIP/externes Lieferpaket übergeben werden; die endgültige Repo-Ablage wird im PR entschieden.
- Ohne Repo-Zugang: **vollständiges ZIP mit Scene-Nr., SHA-256, QA und Quellen** an die Projektleitung geben. Keine Behauptung, das Repo sei aktualisiert, wenn das nicht passiert ist.
- Kein Bezahldienst, kein API-Key-Upload, keine Vertraulichkeit verletzen. Nur kostenlose lokale Werkzeuge und geklärte, verwendbare Assets oder vorherige schriftliche Budgetfreigabe.

## 9. Pflicht-Abschlussbericht — eine Szene nach der anderen

Nach jeder Szene die Antwort **genau in dieser Struktur** liefern:

1. **Szene:** Master-Nr., heutiges Land, Region, ca. Jahr, Hauptprodukt.
2. **Historische Belege:** zwei bis fünf Quellen + welche sichtbaren Elemente belegt werden.
3. **3D-Umsetzung:** verwendetes Tool, Szene-/Blend-/GLTF-Datei, Kamerapunkt, Anzahl/Art wichtiger Bauteile, reproduzierbarer Renderbefehl.
4. **Export:** native Pixelgröße, PNG/JPG-Pfade, echte 360°-Projektion, SHA-256; Upscale getrennt.
5. **QA-Tabelle:** Naht, vier Richtungen, Zenit, Nadir, Maschinen, Menschen, Historie, Quiz-Fairness, Lizenzen, Browser mit **PASS / FAIL / NICHT GETESTET** und Screenshotbelegen.
6. **Bekannte Mängel:** präzise Position (yaw/pitch), Ursachen, bereits getestete Reparaturen. **Keine** Formulierung „fertig“, wenn hier ein gravierendes FAIL steht.
7. **Übergabe:** ZIP/PR-Link und Dateimanifest, nächste konkrete Freigabeentscheidung.

**Keine Massenproduktion ohne eine geprüfte T- und eine geprüfte E-Pilotszene.** Kein weiteres Motiv automatisch anfangen, solange das eigene aktuelle Motiv in einem reparierbaren Zustand mit offenem Qualitätsfehler liegt. Bei nicht behebbaren Tool-/Modellgrenzen einen begründeten FAIL-Bericht und eine alternative Methode liefern und dann erst die Priorität neu entscheiden.



**Geltungsbereich und Verantwortung:** Du erzeugst ausschließlich die 14 T/E-Szenen. Änderungen an `P01–P16`, an bestehenden drei Pilotbildern oder an den zentralen Spieldaten werden nicht verlangt.