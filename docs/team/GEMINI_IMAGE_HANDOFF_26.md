# Gemini-Bildproduktion – Auftrag für die 26 fehlenden historischen 360°-Szenen

> **ÜBERHOLT seit der Nutzer-Bildprüfung vom 09.11.2026.** Diese frühere Liste mit **26 neu zu generierenden Bildern ist nicht mehr aktuell**. Es sind **11 Bilder visuell akzeptiert, 6 Versionen neu zu machen und 13 Szenen ohne aktuelles Urteil offen**. **Jetzt gilt [Gemini-Auftrag – 19 offene Arbeiten](GEMINI_IMAGE_HANDOFF_CURRENT.md)**, zusammen mit [dem Bildstatus](../IMAGE_PRODUCTION_STATUS_30.md). Die alten Anweisungen darunter sind nur Archiv und dürfen nicht als aktuelle Bild-To-do-Liste verwendet werden.


**[GitHub-Issue #18 für die gemeinsame Fortschrittsliste](https://github.com/Matteo-Winter/FactoryGuessr/issues/18)**.

**Aktiv ab 09.11.2026.** Dies ist die **verbindliche Übergabe** für den Kollegen. Sie ersetzt die frühere Anweisung, nur 14 Handels-/Ereignisbilder zu produzieren.

## Projekt und Dateien – bitte in dieser Reihenfolge lesen

1. **[Aktueller Produktionsstatus mit allen 30 Bildern und den 26 fehlenden](../IMAGE_PRODUCTION_STATUS_30.md)** – nur diese 26 produzieren.
2. **[Maschinenlesbare Statusliste](ACTIVE_SCENES_30.json)** – `image_status = needed` bedeutet: Bild erstellen.
3. **[Historischer Gesamtplan](../SCENE_MASTERPLAN_30.md)** – Ort/Jahr/Produkt bzw. Ereignis und visuelle Anker.
4. **[Bisherige vier akzeptierte Bildreferenzen](../IMAGE_PRODUCTION_STATUS_30.md#die-vier-bereits-akzeptierten-bildreferenzen)** – Stil- und Dichte-Vorbild, nicht 1:1 kopieren.
5. [Technische und historische ausführliche Anleitung für T/E](COLLEAGUE_MASTER_PROMPT_14.md) – weiterhin als Fachanhang für historische Handels- und Ereignisszenen nützlich, aber ihre frühere **14-Szenen-Zuständigkeit ist durch diesen Auftrag überholt**.

**Wichtig:** Die vier Originalbilder `P02/P03/P05/P10` sind im Nutzer-Chat hochgeladen, **nicht als Github-Bild-URLs**. Bitte den Nutzer um das ZIP `FactoryGuessr_Gemini_4_Referenzbilder.zip` bitten, wenn du sie als visuelle Referenz verwenden willst. Keine Behauptung, du hättest die Bilder selbst gesehen, solange sie dir nicht übergeben wurden.

## Präziser Bildstil

**Vibe:** glaubwürdiger, hochwertiger **immersiver historischer Dokumentarfilm**, mit sinnvollen Handlungen und großer materieller Dichte. Die vorhandenen Referenzen zeigen alte Werkstätten und Industrien, in denen Menschen **wirklich etwas tun**, mit Rohstoffen, Werkzeugen, Geräten, halbfertigen Produkten, echten Gebrauchsspuren und natürlich wechselnden Lichtstimmungen. Keine steril leere KI-Halle. Kamerahöhe menschlich, räumlich nachvollziehbar. Bei Industrie viele plausibel tätige Arbeiter, aber **nicht** willkürlich hunderte Menschen; bei Macht- und Ereignisszenen historisch angemessene Größenordnung und respektvolle Darstellung.

**Jeder Ort muss zeitlich und geografisch einzigartig wirken:** historische Werkstoffe, Maschinentypen, Kleidungsstücke, Architektur, Transporte, lokale Umgebung. Nicht alles als dieselbe Hallenform mit derselben sepiafarbenen Farbkorrektur rendern. Farb- und Lichtsprache der Realität des jeweiligen Ortes unterordnen. Bei modernen Fabriken lieber realistische Reinraum-/Industriebeleuchtung als nostalgisches Holz.

**Keine Spoiler im Bild:** Keine Jahreszahlen, Städtenamen, Flaggen oder Firmenschilder zur Erleichterung der Rateaufgabe, wenn sie den Ort direkt verraten; keine zufällig lesbaren generierten Textartefakte. Land und Epoche sollen aus dem **Bildinhalt** mit fairen Hinweisen ableitbar sein.

## Verbindlicher Ablauf je Szene – keine Abkürzungen

1. **Research-Gate:** Museum/Archiv/Fachquellen zur echten Region, Zeit und Tätigkeit prüfen; eine kurze `research.md` mit mindestens 2 Quellen, belegten Details und 5 gefährlichen Anachronismen. Bei historisch sensiblen Ereignissen ausdrücklich zwischen belegtem Vorgang und künstlerischer Rekonstruktion unterscheiden.
2. **360°-Layout:** Vor Generierung eine **zusammenhängende 3D-Raum-/Standpunktvorlage** planen (ideal: echte 3D-Blockout-Datei; bei anderer Gemini-360-Technik muss reale Kugelgeometrie unabhängig überprüfbar sein). Festlegen: 0° Hauptaktivität, ±90° Kontext, 180° ruhige Nahtzone, Zenit/Nadir plausibel. An den Rändern keine halbierten Maschinen, Gesichter oder markanten Gebäude.
3. **Realistische Generierung:** Gemini für die realistische, atmosphärische Darstellung benutzen, **an den belegten Aufbau und möglichst feste Geometriekontrollen gebunden**. Die Bildausgabe muss geometrisch als volle 360°×180°-Kugel funktionieren. Ein flaches Bild mit 2:1-Aspekt allein reicht nicht.
4. **QA direkt nach jedem Versuch:** tatsächliche Pixelgröße; technisch 2:1, Naht **inhaltlich und farblich**, Pole, vier Blickrichtungen, Dach/Boden/Kräne/Schiffe/Maschinen **im perspektivischen Viewer**. Niemals die Naht nur mit spiegelbildlichen Häusern, Menschen, Pressen, Schiffen reparieren. QA mithilfe der Repo-Skripte `scripts/check_panorama.py` und `scripts/export_panorama_views.py`, dann interaktiver Pannellum-Browsercheck. Fehler → **reparieren und wieder testen**; kein bloßes schön aussehendes Bild abgeben.
5. **Lieferung:** Natives Bild (bestenfalls 4096×2048, tatsächliche Größe angeben); ggf. 3D-Datei, Ursprungsdatei, `qa/contact_sheet.jpg`, `qa/report.md`, Quellen und eindeutige Szene-ID. User erhält die tatsächlichen Bilddateien, nicht nur Prompttexte. ZIP/Feature-Branch/PR. Keine eigenmächtige Änderung auf `main`, `ready` oder Deployment.
6. **Fortschritt:** Sobald der Nutzer ein Bild ausdrücklich visuell akzeptiert hat, Statusliste **nur nach belegter User-Entscheidung** aktualisieren; finaler Spiel-Status bleibt bis eigenständiger QA/Review offen.

## Besonderheiten der drei Motivarten

- **Produktion P (12 neue):** klar erkennbares Produkt, Maschinen und nachvollziehbarer Arbeitsschritt; Beschäftigte passend zur Epoche. Moderne Anlagen (Taiwan-Chipproduktion, Lithium) nicht wie 19.-Jh.-Fabrik ausstatten.
- **Handel/Macht T (6 neue):** Warenfluss + räumlich plausibler Hafen/Festung/Handelsplatz + Hinweis, wo Macht und Zugang organisiert wurden. Keine beliebige Fabrikhalle.
- **Ereignisse E (8 neue):** konkreter visueller historischer Moment oder bewusst als solche gekennzeichnete **Schauplatz-Rekonstruktion**. Kein falsches Augenzeugenfoto. Bei Haiti, Guatemala, Rana Plaza respektvoll, keine erfundenen Opfer/Schlüsselszenen oder stereotype Gewalt.

## Einstieg

**Bearbeite ausschließlich die `image_status=needed`-IDs, in Szenenreihenfolge; startbar mit P01 (niederländische Paltrokmühle um 1660).** P01 ist eine historische Maschinengeometrie-Falle: integrierte Windflügel/Sägeplattform, nicht Windmühle neben Sägehalle. Nutze vorhandene Faktenkarte `docs/scene-research/nl-1660-wind-sawmill.md`.

**Stelle zunächst eine der fehlenden Szenen mit vollständigem QA vor**, bevor große Stapel erstellt werden. Der Nutzer entscheidet Stil und Freigabe. Die vier akzeptierten Bilder werden NICHT neu generiert. Alle übrigen 26 bleiben auf `needed` bis zu einer neuen dokumentierten Auswahl.
