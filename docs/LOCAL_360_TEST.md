# Made in Time: echte lokale 360°-Vorschau

## Was die Vorschau kann

Die drei generierten **2:1-Testpanoramen** (1774 × 887 Pixel) sind für einen praktischen Rundumblick im Browser vorgesehen:

| ID | Historisch plausibles Komposit |
|---|---|
| `gb-1840-textile-mill` | Britische Textilmühle, ca. 1840 |
| `gt-1910-banana-packing` | Bananen-Packhaus in Guatemala, ca. 1910 |
| `cn-2015-electronics-assembly` | Elektronikmontage in China, ca. 2015 |

**0/60 Bilder sind historisch und panorama-geometrisch freigegeben.** Ein korrektes Seitenverhältnis (2:1) beweist noch keine nahtlose equirectangulare Projektion. Insbesondere die Verbindungsstelle zwischen Bild links/rechts muss durch Drehen auf 180° geprüft werden.

## Test in diesem Repository

1. Repository lokal klonen:

   ```bash
   git clone https://github.com/Matteo-Winter/FactoryGuessr.git
   cd FactoryGuessr
   ```

2. Die drei **JPG-Bilddateien aus dem im Chat bereitgestellten 360°-Test-ZIP** in `public/assets/panoramas/` ablegen. Die Dateien müssen genau so heißen:

   ```text
   public/assets/panoramas/gb-1840-textile-mill.jpg
   public/assets/panoramas/gt-1910-banana-packing.jpg
   public/assets/panoramas/cn-2015-electronics-assembly.jpg
   ```

3. Im Terminal starten:

   ```bash
   python3 -m http.server 8000 --directory public
   ```

4. Im Browser **http://localhost:8000** öffnen. `file://` direkt öffnen reicht nicht, weil die Szenendaten über HTTP geladen werden.

5. Mit der Maus ziehen, mit dem Mausrad zoomen, `Naht prüfen` drücken und alle 3 Szenen wechseln.

Der im Repository installierte Browser-Viewer nutzt **Pannellum per CDN** (Internetverbindung nötig). Im ZIP liegt **alternativ** eine vollständige, ebenfalls lokale WebGL-Version **ohne CDN**. Die beiden Viewer erfüllen dieselbe Testaufgabe, verwenden aber verschiedene Rendertechniken.

## Der entscheidende Unterschied: 360° vs. echtes 3D

- **360°-Bild:** Das Bild wird als Umgebung auf einer virtuellen Kugel angezeigt. Du kannst umsehen, hoch und runter schauen und zoomen. Die Kamera bleibt an einem Punkt; es gibt **keine** echte Tiefengeometrie.
- **Street-View-Navigation:** Für das Weitergehen müssen wir später **mehrere Panoramen verschiedener Kamerapositionen** aufnehmen oder generieren und mit klickbaren Übergangspunkten verknüpfen.
- **Frei begehbare 3D-Welt:** Dafür ist eine vollständige 3D-Rekonstruktion mit konsistenter Geometrie erforderlich; die drei Bilder allein leisten das nicht.

## Freigabe vor Veröffentlichung

- Bildtatsächlich mit Maus in alle Richtungen prüfen (Naht, Boden, Decke).
- Geometrie-Artefakte und anachronistische Maschinen prüfen.
- Nur `scene_status: "ready"` verwenden, wenn alle Prüfungen bestanden sind.
- Keine Quelle als echte historische Fotografie ausgeben, wenn sie KI-generiert ist.
- Dieser Test ist ein Prototyp, **kein** fertig validiertes Set von 60 Fabrikszenen.
