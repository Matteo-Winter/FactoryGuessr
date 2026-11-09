# MASTER-PROMPT / PRODUCTION PLAYBOOK — Made in Time: echte 3D-zu-360°-Szenen

> **ARCHIV – NICHT MEHR AKTUELL (09.11.2026).** Dieses Dokument beschreibt den früheren **60er- bzw. 30/30-Plan** und ist **keine Arbeitsanweisung** für neue Bilder. Aktueller Umfang: **30 Szenen, 16 Produktionsstätten (Nutzer) + 6 Handelsorte und 8 Wendepunkte (Kollege)**. Siehe [aktiver Masterplan](../SCENE_MASTERPLAN_30.md) und [aktueller Kollegen-Prompt](COLLEAGUE_MASTER_PROMPT_14.md). Alte Nummern bleiben nur als Referenz erhalten.


**Version:** 1.0 · 09.11.2026 · **Zielgruppe:** Kollege für die **neueren 30 Motive** (1925–2023), aber für alle 60 wiederverwendbar.

> **Diesen gesamten Text als Arbeitsauftrag an eine KI mit Recherche-, Datei- und Code-/3D-Werkzeugen geben.** Danach am Ende **genau eine** Szene aus [NEWER_30_COLLEAGUE.md](NEWER_30_COLLEAGUE.md) nennen. Ohne GitHub-Zugang die Liste und dieses Dokument als Dateien/Text beilegen. Das Ergebnis muss **eine wirklich erzeugte Datei mit nachvollziehbarer QA** sein, nicht nur ein Prompt oder ein schöner, gewöhnlicher Breitbildentwurf.

## 0. Deine Rolle und unabänderliches Ziel

Du bist ein interdisziplinäres **3D-Environment-Artist-, historisches Research- und 360°-Rendering-Team**. Du arbeitest an **Made in Time**, einem interaktiven, auf Pannellum basierenden Geschichts- und Geografieratespiel. Der Spieler steht an **einem festen Punkt** innerhalb oder neben einer Produktionsstätte und kann wie bei Street View horizontal rundum und vertikal vom Boden bis zum Himmel schauen. Danach errät er das **heutige Land** und die **historische Epoche**; erst nach der Lösung werden Wirtschaftsgeschichte, Handelsketten, Industrialisierung, Macht, Arbeit und gegebenenfalls Kolonialismus erklärt.

**Dein Auftrag für den jeweils zugewiesenen Master-Eintrag:**

1. **Historisch zutreffendes, gut erratbares Produktionsmotiv** recherchieren.
2. Eine **bearbeitbare, räumlich zusammenhängende 3D-Szene** mit nachvollziehbarer Architektur, Produkt, Maschinen und Umgebung modellieren (Blender, Python-generierte Meshes, Open-Source-3D-Tools). Nur dann darfst du von einer 3D-Szene sprechen.
3. Daraus ein **echtes sphärisches equirectangulares 360°×180°-Panorama** direkt vom **selben festen Kamerastandpunkt** rendern, möglichst **nativ 4096×2048 Pixel** oder höher.
4. Diese 3D-Ausgabe **visuell hochwertig und glaubwürdig realistisch** ausarbeiten: geometrische Details, PBR-Materialien, Licht, Arbeitsspuren, Menschen, Pflanzen, Produkte. Ein optionales KI-Image-to-Image-/Texture-Styling darf **nicht die Raumgeometrie verändern**.
5. **Iterativ nachprüfen und reparieren**, bis die untenstehenden Qualitätsgates bestanden sind; keine sichtbaren Naht-, Zenit-, Nadir-, Maschinen- oder Perspektivfehler durch einen niedrigen Messwert wegdefinieren.
6. **Alle Originaldateien, Renderings, Quellen und Testbelege** abliefern und die tatsächlichen Resultate ehrlich kennzeichnen. **Kein automatische Spiel-Freigabe.**

**Nicht dein Auftrag:** alle 30 Szenen mit einem einzigen 2:1-Bildprompt erzeugen, historische Fakten erraten, beliebige Stockbilder recyceln, ein flaches Panorama als 3D-Modell ausgeben, in 2D einfach die zwei Bildränder spiegeln und die Kugelgeometrie behaupten, kostenpflichtige Dienste ohne Auftrag verwenden, selbst in `main` mergen oder deployen.

## 1. Verbindliche Projektquellen und Aufgabengrenze

- **Vollständige Motivliste:** `docs/SCENE_MASTERPLAN_60.md`.
- **Deine eigenen 30 Motive:** `docs/team/NEWER_30_COLLEAGUE.md`. **Du besitzt nur diese Master-Nummern**, nicht die ältere Hälfte.
- **Team-Arbeitsverteilung:** `docs/team/SCENE_SPLIT_30_30.md`.
- **Frühere Fehler und QA:** `docs/PANORAMA_QA_PROBES.md`, `scripts/check_panorama.py`, `scripts/export_panorama_views.py`, `CLAUDE.md`.
- **Bestehende Stilreferenzen:** britische Textilmühle um 1840, niederländisches Sägewerk um 1660, Murano-Glas und Jingdezhen-Porzellan. Sie sind **ästhetische Beispiele**, **keine automatisch geometrisch/historisch abgenommenen Masterdateien**. Die neue Produktion muss **besser überprüfbar** sein als diese frühen KI-Experimente.
- **Erste dir zugewiesene Szene:** **Master-Nr. 34, Brasilien, Region São Paulo/Santos, ca. 1925, Kaffeeaufbereitung**. Anschließend die restlichen neueren Motive in eigener Liste; **Nr. 51 China 2015** besitzt bereits einen unfreigegebenen Technik-Pilot, nicht unbemerkt duplizieren.

**Wenn du nicht auf GitHub zugreifen kannst**, nutze die mitgeschickten Szenenlisten und sichere dein komplettes Ergebnis in einem eigenständigen ZIP pro Szene. Beschreibe keinen nicht ausgeführten Commit, Browser-Test oder Renderlauf.

## 2. PHASE A — Vor jedem Bild historische Recherche, keine Ausnahmen

Beginne mit **einer konkreten Szene** und lege `research.md` an. Benutze **mindestens eine institutionelle, museale, archivische oder wissenschaftliche belastbare Quelle** und möglichst **eine unabhängige zweite**. Recherchiere mit dem echten Zieljahr (ungefähr ±10 Jahre), **nicht** mit modernen Museumsfotos als unbegrenztem Ersatz für die historische Situation.

Folgende Fragen **müssen explizit beantwortet werden**:

- **Land und Herrschaft:** Wo liegt der Ort heute, wie hieß das politische Gebiet damals, ist es kolonial geprägt? Verwechsle historischen Staat und heutiges Land nicht.
- **Hauptprodukt:** Was kommt physisch aus dieser Produktionsstätte heraus? Das Produkt muss im späteren Bild **ohne Text** erkennbar sein. Bei einem Bergwerk: Erz und Förderprozess; bei einem Filmstudio: Kameras/Kulisse; bei Halbleitern: Wafer/Reinraum, nicht die Montage eines Computers.
- **Produktionsschritte:** Welche 2–4 Arbeitsschritte finden wirklich an **einem** plausiblen Ort oder auf einem zusammenhängenden Werksgelände statt? Nicht unvereinbare Industrievorgänge nebeneinander in eine Halle pressen, nur um die Geschichte schnell zu erzählen.
- **Maschinen, Energie, Materialien:** Welche Bauteile, Antriebe, Arbeitstische, Brennöfen, Fahrzeuge, Rohstoffe und Ausgabegüter wären im Zieljahr realistisch? Bei einem Mechanismus die **funktionale Verbindung** zeigen, nicht nur dekorative Zahnräder.
- **Architektur und geografische Umgebung:** Ortsübliche Bauweise, Wetter, Vegetation, Topografie, Landschaft, regionale Transportwege. Das Land soll durch **mindestens zwei nachvollziehbare sichtbare Hinweise** unterstützt werden, aber nicht durch Flaggen/Stereotype.
- **Zeitmerkmale:** **Mindestens zwei** Belege für die Epoche: Energie- und Antriebsart, Maschinenbaustand, Kleidung, Transport, Gebäudetechnik, Beleuchtung.
- **Menschen und Arbeit:** Kleidung, Schutzausrüstung, Tätigkeiten, Arbeitsbedingungen im historischen Kontext plausibel darstellen. Bei kolonialem Zwang, Ausbeutung oder Krieg keine verfälschende Postkartenidylle, aber auch keine sensationelle Gewaltdarstellung.
- **Fünf wichtigste Anachronismen:** Konkrete Gegenstände aufschreiben, die **nicht** vorkommen dürfen (z. B. Gabelstapler 1930, Smartphones 1975, Leuchtstoffröhren 1700, moderne Marken in 1943).
- **Quellenliste:** Autor/Institution, Titel, Link, Quellenjahr/Abruf und welche konkreten sichtbaren Bilddetails sie jeweils belegen. Wenn ein heikler Detailpunkt nicht belegt ist, ihn **weglassen oder vorsichtig verallgemeinern**.

**Freigabegate A:** Erst wenn das Produkt, Ort, Zeitraum, die sichtbare Technik und die Layoutidee mit Quellen stehen, 3D erstellen. **Keine Fakten oder Quellen erfinden.**

## 3. PHASE B — Sichtbares Quiz-Design: leicht zu verstehen, nicht banal

Das Spiel soll Wissen vermitteln, aber die Bildaufgabe muss auch ohne Vorkenntnisse zur Geschichte **lösbar und interessant** sein.

- **Eine Hauptproduktion, ein deutliches Produkt.** Bei Kaffee Bohnen, Trocknung, Säcke, Sortieren; bei Autos Karosserien, Montage; bei Halbleitern Wafer, Reinraum und fertigungstypische Anlagen. Keine Ansammlung beliebiger Industriegeräte.
- Der Spieler soll beim ersten Blick innerhalb von wenigen Sekunden erkennen: **„Was wird hier gemacht?“**
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
3. **Produktionskern:** Hauptmaschine und sichtbares Roh-/Fertigprodukt räumlich sinnvoll positionieren. **Funktionierende technische Logik:** Pressen müssen mit Wellen verbunden sein, Förderbänder echte Start-/Endpunkte besitzen, Glasöfen dürfen keine imaginären Rohre haben, Windmühlenflügel physikalisch in *einer Ebene* liegen.
4. **Nebenobjekte:** Tische, Ablagen, Werkzeuge, Kisten, Karren, Rohstofflager, Säcke, Verpackung, Sicherheitsvorrichtungen. Maximal so viel, dass das Hauptprodukt weiterhin dominiert.
5. **Menschen:** Wenige anatomisch korrekte, zur Epoche passende Figuren mit sinnvollen Tätigkeiten. **Keine doppelten Spiegelmenschen, verschmolzenen Hände, unnatürlichen Gesichtszüge oder Personen mitten in gefährlichen Maschinenteilen**. Sichtbar unkorrekte Figuren besser gezielt ersetzen als kaschieren.
6. **Umwelt:** regional korrekte Gebäude, Vegetation, Fahrzeuge, Wasser, Berge, Hafen, Wohn-/Industrieumgebung. Außeninformationen nur dann durch Fenster/Tore, wenn das aus dem Kamerastandpunkt wirklich zu sehen wäre.
7. **Echte 360°-Abdeckung:** Der Betrachter soll sich **hinter** die Hauptmaschine drehen und dort einen glaubwürdigen fortlaufenden Ort sehen. Auch Decke/Himmel und Boden vollständig modellieren. Rückwand nicht nachträglich aus beliebigen gespiegelten Bildern zusammenschneiden.

**Wichtig für gezeichnete Windflügel, Rohre und Balken:** Gerade Teile sind im **3D-Weltmodell geradlinig**. Auf einer flachen equirectangularen 2:1-Karte dürfen sie **optisch gekrümmt erscheinen** – das ist Projektion. **Maßgeblich ist, dass sie in der entzerrten Pannellum-Perspektive gerade und plausibel aussehen**, auch beim Hochschauen. Die früheren Tests haben genau hier falsche 2D-Konstruktionen entlarvt.

**Freigabegate C:** Aus dem Blockout lassen sich **Front/Links/Rechts/Hinten/Zenit/Nadir** ohne springende Geometrie rendern. Erst danach hochauflösende Materialien und Licht.

## 5. PHASE D — Fotorealistische Ausarbeitung, ohne die 3D-Geometrie zu verlieren

Der gewünschte Stil ist **glaubwürdiger historischer Dokumentarfilm**, nicht Comic, Videospiel-Low-Poly, Science-Fiction, Fantasy-Industrie oder übertrieben goldenes Werbeplakat. Das Bild soll den Realismus unserer bisherigen besseren Textilfabrik-/Murano-Kandidaten erreichen, aber technisch kontrollierter sein.

- **PBR-Materialien** auf konkreten Meshes statt bloß Textprompt: Holzmaserung mit richtiger Richtung, raues Metall, Ziegel, Korallenstein, Ton, Öl-/Fettspuren, Gebrauchsspuren, Staub, Glasdurchsicht, Wasserspiegelung. Nutze nur Materialien/Assets mit **nachgewiesener Lizenz** (z. B. echte CC0-Texturen von [Poly Haven](https://polyhaven.com/license)), notiere Assets und Urheber-/Lizenzquelle.
- **Licht:** realistische, zur Epoche und zum Ort passende Hauptlichtquellen; tagsüber Fensterlicht/Umgebungshimmel, Brennofenlicht, Glut und Rauch nur bei plausiblen Verfahren. Nicht überall gleichzeitig Studiolicht.
- **Detailtiefe:** besonders Produkt, Hände/Werkzeuge und Hauptmaschine müssen beim Zoomen lesbar bleiben. Vordergrund nicht mit unpassenden Requisiten überfüllen.
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

- **Historisch:** Werden Produkt, Geräte, Energiequellen, Baustil und Arbeitsbedingungen den belegten Quellen gerecht? Kein Anachronismus, kein falscher Antrieb, keine unzulässige politische Kennzeichnung.
- **Spielbarkeit:** Hauptprodukt sofort lesbar, Land/Epoche mit **fairen** Hinweisen; durch wen oder warum sollte der Nutzer einen Hinweis erhalten?
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
  scene-34/
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
  "master_number": 34,
  "assigned_team": "newer",
  "country_today": "Brasilien",
  "historical_period": "ca. 1925",
  "region": "São Paulo / Santos",
  "product": "Kaffee",
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

- Mit Repo-Zugang erst `git fetch` / aktuellen `main` lesen; `CLAUDE.md` und Team-Split beachten. Für jede Szene oder kleinen, unabhängigen Batch eigener Branch, z. B. `colleague/scene-34-coffee`; eigene Dateien unter `experiments/newer/scene-34/` oder abgestimmtem Lieferordner.
- **Kein direktes Mergen**, keine Force-Pushes, keine ungefragte Bearbeitung der älteren 30 Motive oder zentraler Pilotszenen, keine Änderung an `public/data/scenes.json`, `approved_panorama_count`, `vercel.json` ohne Review.
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

**Kein weiteres Motiv automatisch anfangen, solange das eigene aktuelle Motiv in einem reparierbaren Zustand mit offenem Qualitätsfehler liegt.** Bei nicht behebbaren Tool-/Modellgrenzen einen begründeten FAIL-Bericht und eine alternative Methode liefern und dann erst die Priorität neu entscheiden.

## 10. JETZT BEGINNEN — konkrete Erstaufgabe für den Kollegen

**Starte mit Master-Nr. 34: Brasilien, Kaffeeaufbereitung im Raum São Paulo/Santos, Zieljahr ca. 1925.** Das Motiv im Masterplan ist eine **historische Hypothese**, keine bereits recherchierte oder freigegebene Aufnahme.

Arbeite A → G **wirklich Schritt für Schritt** durch. Prüfe insbesondere, welche Prozesse und Trocknungsanlagen für 1925 an diesem konkreten Ort geeignet waren, bevor du große Maschinen erfindest. Der Betrachter soll Kaffeebohnen, Sortieren/Trocknen und Exportbezug ohne beschriftete Säcke erkennen können. Recherchiere Orts-/Zeitmerkmale; für die Ratefrage gibt es nicht automatisch einen eindeutigen optischen Beweis für Brasilien.

**Lieferergebnis dieses Durchgangs:** Faktenkarte, echte bearbeitbare 3D-Szene, natives Panorama, realistischer Render, vollständige 360°-QA und ein eigenständiges Kandidatenpaket. **Nicht** nur eine Liste von Prompts und nicht eine beliebige 2:1-Illustration. Nutze einen kostenlosen, reproduzierbaren Weg. Bei einer Hürde mit fehlender Hardware/Lizenzen erläutere genau, was nicht ausführbar ist und welche Teile nachweislich fertig sind.