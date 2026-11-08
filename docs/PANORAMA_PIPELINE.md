# 360°-Bildpipeline für Made in Time

## Technische Entscheidung (V1)

**Interaktive Panoramen, keine frei begehbare 3D-Geometrie.** Der Browser dreht ein statisches equirectangulares Bild (Longitude 360°, Latitude 180°) mithilfe von [Pannellum](https://pannellum.org/). Spezifikation: JPEG oder PNG, Breite = 2 × Höhe; bevorzugt 4096×2048 oder 8192×4096. Die linke/rechte Bildkante müssen nahtlos ineinander übergehen. Ein beliebiges breites Foto ist **kein** korrektes 360°-Panorama.

## Status und Ziele

- **60 Level sind das Ziel, nicht der bisherige Ist-Stand.**
- **3 Pilot-Szenenkonzepte** stehen in `public/data/scenes.json`: Großbritannien 1840, Guatemala 1910, China 2015.
- **0 verifizierte, fertige Panoramen**. Drei KI-generierte 2:1-Testbilder liegen im Repository, jedoch keines ist historisch oder panorama-geometrisch freigegeben.
- **Alle 60 konkreten Szenen** sind als **Entwurf** in [SCENE_MASTERPLAN_60.md](SCENE_MASTERPLAN_60.md) geplant (6/8/14/10/12/10); vor dem Rendering jeder Szene ist historische Quellenprüfung erforderlich.

## Produktion je Szene

1. **Historisches Briefing** erstellen: Land (heute / damaliger Staat), ca. Jahr, klar erkennbares Hauptprodukt, regionale Architektur/Landschaft, reale Maschinen und Arbeitsweise der Zeit; mindestens eine institutionelle/archivarische Bild- oder Sachquelle plus möglichst einen weiteren Beleg **vor der Generierung**. Zwei faire Orts- und zwei Epoche-Hinweise festlegen und Anachronismen explizit ausschließen. [60er-Masterplan](SCENE_MASTERPLAN_60.md).
2. **Prompts/Referenzen erstellen** und als `concept` speichern. Keine impliziten Behauptungen über bestimmte Unternehmen.
3. **360°-Panorama erzeugen**, z. B. mit Skybox AI oder anderem Anbieter, der *tatsächliche* equirectangulare Panoramen exportiert. Alternativ können lizenzierte reale Panoramen verwendet werden.
4. **Export lokal validieren**: tatsächliche Dateidimension 2:1, ausreichende Auflösung, korrekte Projektion, nahtloser 0°/360°-Übergang, keine sichtbar deformierten Personen/Maschinen, keine modernen Gegenstände in historischen Leveln.
5. **Im Browser umsehen**: Viewer öffnen, oben/unten sowie die Naht prüfen. Land und Zeitraum dürfen nicht auf Flaggen/Schildern direkt zu lesen sein.
6. **Historische Plausibilität und Rechte prüfen**: Datierung, regionale Aussagekraft, KI-/Fotorechte und Nutzung für den Uni-Kurs dokumentieren. Bilderkennbar KI-generiert -> als Rekonstruktion kennzeichnen.
7. **Freigeben**: Erst nach allen Prüfungen `scene_status` auf `ready` setzen und den Pfad zur real vorhandenen Datei aktualisieren.

## Akzeptanzkriterien Pilot

- Drei verschiedene Epochen, Länder und Industrien.
- 3/3 exportierte und tatsächlich drehbare 360°-Panoramen.
- Jedes Bild ist historisch plausibel und in der Szene mit `composite_reconstruction` gekennzeichnet.
- Kein KI-Bild behauptet, einen konkret identifizierten historischen Betrieb wahrheitsgetreu darzustellen.
- Spieler kann Land und Epoche abgeben und eine belegbare Lern-Erklärung sehen.
- Erst danach die restlichen 57 Szenen in Batches erzeugen und qualitätsprüfen.

## Ordner und Hosting

Im Repository werden nur Inhalte aus `public/` auf der Website veröffentlicht. `vercel.json` setzt **Other** (statisches HTML) und `public` als Output Directory; es ist weder Node noch ein Build erforderlich.

- `public/index.html`: Spiel-Prototyp und Panorama-Viewer.
- `public/data/scenes.json`: öffentlich sichtbare Leveldaten.
- `public/assets/panoramas/`: 360°-Panoramabilder (2:1, equirectangular).
- `public/assets/thumbnails/`: optionale Vorschauen.
- `docs/`, `scripts/`: nur im Repository, nicht im öffentlichen Webverzeichnis.

**Hinweis:** Prompts und Daten in `public/data/scenes.json` sind öffentlich abrufbar. Später bei Bedarf vom Client nutzbare Metadaten und private Generierungsvorgaben trennen. Niemals API-Tokens in `public/` speichern.

## Kosten, Konten, Zugangsdaten

Drittanbieter-Generierung kann kostenpflichtig sein. Die konkreten API-Endpunkte, Eingabeformate, Preise, Credits und Nutzungsrechte müssen jeweils **vor dem ersten kostenpflichtigen Aufruf** gegen die aktuelle Anbieterdokumentation verifiziert werden. Niemals API-Keys in HTML, Screenshots oder Git-Commits speichern. Für kommerzielle spätere Nutzung die Bedingungen gesondert prüfen.

## Geplante Epochenmischung (60 Ziel-Level)

| Zeitraum | Szenen | Hinweise |
| --- | ---: | --- |
| 1600–1749 | 6 | Manufakturen, Zucker- und Rohstoffverarbeitung, koloniale Produktionsstätten |
| 1750–1849 | 8 | Mechanisierung, frühe Fabriken |
| 1850–1913 | 14 | Industrialisierung, Eisenbahn, koloniale Rohstoffe |
| 1914–1945 | 10 | Massenproduktion, Kriegswirtschaft |
| 1946–1989 | 12 | Dekolonisierung, Fertigungsverlagerung |
| 1990–2026 | 10 | Globale Wertschöpfungsketten, Automatisierung |

Diese Verteilung ist eine **Projektplanung** mit 60 konkreten Motivvorschlägen in [SCENE_MASTERPLAN_60.md](SCENE_MASTERPLAN_60.md), keine bereits freigegebene Bilddatenbank. Die Herkunft eines KI-Komposits ist die *historisch modellierte Szene*, nicht der reale Aufnahmeort.
