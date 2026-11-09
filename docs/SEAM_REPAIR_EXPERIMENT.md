# Experiment: lokale 360°-Nahtreparatur (nl-1660-wind-sawmill)

Stand 09.11.2026 · Refs #6 · **Ergebnis: Naht farblich repariert, strukturell INCONCLUSIVE; Motiv historisch FAIL (kein Paltrok). Bild nicht freigegeben.**

## Verfahren

`scripts/experimental_seam_repair.py` ist kostenlos und läuft lokal mit NumPy, SciPy und Pillow, ohne KI-Modell und ohne Netzwerk.

1. Das Bild wird zyklisch um die halbe Breite verschoben, sodass die Naht bei ±180° in der Bildmitte liegt.
2. Pro Zeile und Farbkanal wird der Sprung über die Naht gemessen, abzüglich des natürlichen lokalen Gradienten.
3. Die Korrektur ±Sprung/2 wird als harmonisches Feld (Laplace-Lösung, DCT entlang der Höhe) in ein Band von ±`--band` Pixeln verteilt. Sie gilt exakt an der Naht und läuft am Bandrand auf 0 aus. Feine Anteile klingen nach wenigen Pixeln ab, Farb- und Helligkeitsversätze verteilen sich weich. Konturen und Textur im Band bleiben erhalten, außerhalb des Bands bleibt das Bild bitgleich (das Skript prüft das).
4. Das Bild wird zurückverschoben und verlustfrei als PNG gespeichert.

```bash
python3 scripts/experimental_seam_repair.py qa-candidates/<bild>.jpg qa-candidates/<bild>-seamfix.png --band 160
python3 scripts/check_panorama.py qa-candidates/<bild>-seamfix.png
python3 scripts/export_panorama_views.py qa-candidates/<bild>-seamfix.png
```

**Grenze:** Das Verfahren erfindet oder verschiebt keine Inhalte. Formen, die auf beiden Seiten verschieden sind (Wolkenumriss, abgeschnittenes Objekt), bleiben als Bruch sichtbar.

## Messung: Kandidat `nl-1660-wind-sawmill-upscaled-4096x2048.jpg`

SHA-256 `37bb3c94…dacdd`, 4096×2048, hochskaliert, kein Original-PNG verfügbar. Der Kandidat bleibt unverändert, die Reparatur ist eine separate Datei.

| Messung | Vorher | Nachher (Band 64 / 160 / 320) |
|---|---|---|
| `check_panorama.py`: Naht/normal | 3,739 (`SEAM_COLOR_DISCONTINUITY`) | 0,367 (keine Warnung) |
| `export_panorama_views.py`: Nahtsprung/normal | 3,962 | 0,252 |
| Unabhängiger Kontrollwert: geglättete Spalten 7 px auseinander, Naht/normal (1,0 = typisch) | 1,39 | 1,14 |
| Polzeilen-Kennwert | 4,646 / 9,274 | unverändert (±0,03) |

Die ersten beiden Metriken messen genau den Pixelsprung, den das Verfahren ausgleicht. Ihr Wert unter 1 ist deshalb **kein Qualitätsnachweis**. Der Kontrollwert misst über 7 px hinweg. Er sinkt von 1,39 auf 1,14, der Rest von etwa 14 % entspricht dem verbleibenden inhaltlichen Bruch. Die Bandbreite ändert die Werte kaum. 160 px sehen am natürlichsten aus, bei 64 px bleibt im Himmel ein leichter Helligkeitsverlauf sichtbar.

## Sichtprüfung (Vorher/Nachher, auch 1:1 und dreifach vergrößert)

- **Himmel:** Die harte Helligkeits- und Farbkante ist verschwunden. Eine Wolke endet allerdings genau an der Naht, in der Vergrößerung bleibt der Umriss sichtbar.
- **Ufer, Wiese, Horizont:** Sie laufen jetzt durchgehend weiter. Horizont und Uferlinie lagen schon vorher auf gleicher Höhe.
- **Boot und Stämme:** Die Farbkante ist weg, die Stammenden sind leicht versetzt. Bei normalem Blickfeld fällt das kaum auf.
- **Fass:** Der linke Rand des Fasses ist exakt an der Naht senkrecht abgeschnitten. Dieser Formbruch bleibt.
- **Boden:** Die Diele läuft weiter, es gibt keine Streifen-Artefakte.
- **Zenit und Nadir:** unverändert, ohne neue Fehler.
- **Windrad und Säge:** Sie liegen außerhalb des Bands und sind unverändert. Der verformte Flügel bleibt.

**Bewertung Naht: INCONCLUSIVE.** Farbe und Helligkeit sind repariert, im Viewer fällt die Naht bei normalem Blickfeld kaum noch auf. Zwei inhaltliche Formbrüche (Wolke, Fass) bleiben bei Nahsicht erkennbar. Für eine saubere Naht bräuchte es ein Inpainting der Formen, also ein lokales KI-Modell. Ein solches ist hier nicht installiert (kein torch, kein OpenCV), und eine Installation ist nicht freigegeben.

## Historische Prüfung der Bauform: FAIL

Laut Faktenkarte (`docs/scene-research/nl-1660-wind-sawmill.md`) und Zaanse Schans (*Sawmill De Gekroonde Poelenburg*: „The entire 'paltrok mill' turns on a ring of rollers“, Arbeitsboden „open on three sides“) sitzt bei einem Paltrok der Mühlenkörper mit den Flügeln **direkt auf** dem Sägeboden. Der ganze Bau dreht sich gemeinsam auf einem Rollenkranz, die Kurbelwelle unter den Flügeln treibt die Sägerahmen an.

Im Kandidaten ist das nicht so:
- Die Sägehalle ist ein **separater** Holzschuppen mit gebogenem Dach.
- Die grüne Windmühle steht **daneben** auf eigenem Bock wie eine Bockwindmühle (Standerdmolen) und hat keine sichtbare mechanische Verbindung zur Säge.
- Die Zahnräder im Schuppen haben keine nachvollziehbare Antriebsquelle.
- Ein Flügel ist verformt.

Das Bild zeigt also keine zusammenhängende Paltrokmühle. Die Nahtreparatur ändert daran nichts. **Empfehlung: Motiv neu erzeugen** mit einem Prompt, der Mühlenkörper, Flügel und offenen Sägeboden als *ein* Gebäude festlegt. Die Nahtreparatur kann danach auf den neuen Kandidaten angewendet werden.

## Status

- `public/` und `scenes.json` sind unverändert, weiter 0/60 `ready`.
- Kandidat und Reparaturergebnisse liegen nur lokal in `qa-candidates/` und `qa-output/` (von git ignoriert).
- Tests: `tests/test_experimental_seam_repair.py` mit 5 Tests (Farbsprung entfernt, nur das Band verändert, nahtloses Bild bleibt praktisch gleich, Fehlereingaben, CLI). Gesamte Suite: 21/21 OK.
