# Perspektivische 360°-Prüfansichten (QA-Probes)

Stand: **08.11.2026** · Bezug: Issue #3 · Status der Bilder unverändert: **0/60 freigegeben**.

Dieses Dokument beschreibt das Werkzeug `scripts/export_panorama_views.py`, wie es validiert wurde, was es bei den drei Baseline-Bildern zeigt und **wie ein späteres, extern erzeugtes 4K-Panorama Schritt für Schritt geprüft wird**. Kein Schritt hier ruft einen kostenpflichtigen Dienst auf; kein Werkzeug setzt `ready` oder `approved`.

## 1. Was das Werkzeug macht

Aus einem equirectangularen Bild werden echte perspektivische (rektilineare) Ansichten berechnet. Jeder Ausgabepixel ist ein 3D-Sehstrahl, der um Pitch und Yaw gedreht, in Länge/Breite umgerechnet und bilinear aus dem Quellbild gelesen wird, mit horizontalem Umlauf über die Naht. **Das sind keine 2D-Ausschnitte.** Die Zenit- und Nadir-Ansicht zeigen genau das, was der Viewer beim Blick nach oben/unten zeigt.

Winkelkonvention wie im Pannellum-Viewer (`public/index.html`):

| Größe | Bedeutung |
|---|---|
| `yaw 0` | horizontale Bildmitte; positiv = nach rechts |
| `yaw ±180` | linke/rechte Bildkante = **Naht** |
| `pitch +90 / -90` | Zenit (oberste Zeile) / Nadir (unterste Zeile) |
| `hfov` | horizontales Sichtfeld in Grad |

Standardansichten (je 1024×1024 px, hfov 90°):
1. `front_yaw000`
2. `right_yaw090`
3. `seam_yaw180`
4. `left_yaw270`
5. `zenith_pitch+90`
6. `nadir_pitch-90`
7. `seam_closeup_yaw180` (hfov 40°)

Ausgabe je Bild in `qa-output/<name>/` (per `.gitignore` nicht im Repo):
- `NN_<ansicht>.png`
- `contact_sheet.jpg`: Prüfblatt mit equirectangularer Übersicht, nummerierten Blickpunkten und allen Ansichten. Die Naht-Meridiane (±180°) sind gestrichelt magenta markiert, auch in Zenit/Nadir, wo die Naht vom Pol zum Rand läuft.
- `manifest.json`:
  - SHA-256, Maße, Ansichten
  - `contains_seam` je Ansicht
  - Naht-Kennzahl
  - `"approved": false`, `"manual_qa_required": true`

```bash
python3 -m pip install -r requirements-qa.txt          # NumPy + Pillow, einmalig
python3 scripts/export_panorama_views.py public/assets/panoramas/*.jpg
python3 scripts/export_panorama_views.py <bild> --out qa-output/pilot --size 1024 --hfov 90
python3 scripts/export_panorama_views.py <bild> --view 180,0,20 --view=-45,-60,90   # Zusatzansichten yaw,pitch[,hfov]
```

Negative Yaw-Werte als `--view=-45,...` schreiben (mit `=`), sonst hält `argparse` sie für eine Option.

**Kennzahl `seam_view.seam_vs_ordinary_ratio`:**
- Gemessen in einer 40°-Perspektivansicht auf die Naht.
- Verglichen wird der Farbsprung über den Naht-Meridian mit dem Mittel aller übrigen Spaltenschritte (oberes/unteres Zehntel ausgenommen).
- Ein stetiges Panorama liegt bei ≈1.
- **Das ist ein Hinweis, kein Beweis.** Ein niedriger Wert kann auch daher kommen, dass die Naht zufällig in einer gleichförmigen Fläche liegt.

**Bewusst keine Pol-Kennzahl.** Zwei Kandidaten wurden an den Baseline-Bildern ausprobiert und verworfen, weil sie die sichtbar verdrehten Pole **nicht** von korrekten unterschieden:

| Ansatz | Ergebnis bei den Baseline-Bildern |
|---|---|
| Streuung in einer 3°-Kappe am Pol ÷ Kappen am Horizont | Faktor 0,30 bis 0,65: unauffällig |
| Anisotropie tangential/radial im Ring 5–25° um den Pol ÷ Horizont | Faktor 0,83 bis 1,36: unauffällig |

Der „Strudel“ dieser Bilder ist ein struktureller Fehler (spiralförmige Balken, radial gestreckte Kisten), keine statistische Textur-Auffälligkeit. **Pole werden deshalb ausschließlich per Auge geprüft.** Die vorhandene Pol-Zeilen-Metrik in `scripts/check_panorama.py` gab bei allen drei Bildern ebenfalls keine Warnung (Werte 2,9–9,5 < Schwelle 10).

## 2. Validierung

### 2.1 Pixelabgleich mit dem echten Viewer
Pannellum 2.5.7 (wie in `public/index.html`) wurde in Google Chrome (macOS, GPU) mit 512×512 px gerendert. Dieselben Winkel wurden mit dem Exporter gerendert. Quelle: `gb-1840-textile-mill.jpg`.

| yaw/pitch/hfov | mittl. Abweichung (0–255) | Kontrolle: gespiegelt | Kontrolle: 12 px versetzt |
|---|---:|---:|---:|
| 0/0/90 | **0,03** | 43,5 | 23,5 |
| 90/0/90 | **0,03** | 47,4 | 26,2 |
| 180/0/90 (Naht) | **0,03** | 41,7 | 25,0 |
| −90/0/90 | **0,03** | 59,4 | 28,2 |
| 180/0/40 (Naht nah) | **0,06** | 41,7 | 21,4 |
| 30/45/90 | **0,03** | 40,3 | 23,7 |
| −120/−50/70 | **0,04** | 34,5 | 20,5 |
| 0/90/90 (Zenit) | **0,03** | 32,0 | 17,9 |
| 0/−90/90 (Nadir) | **0,03** | 33,7 | 18,2 |

**Ergebnis:**
- Die Exporter-Ansichten sind praktisch pixelidentisch mit dem Viewer, einschließlich Zenit und Nadir. Das Prüfblatt zeigt also, was Spielende sehen.
- Die Kontrollspalten zeigen, dass der Vergleich Spiegelungen oder kleine Versätze sicher erkennen würde.
- Der Abgleich lief einmalig lokal (Playwright-Skript außerhalb des Repos). Er ist **kein** Teil der Unit-Tests, weil diese ohne Browser und Internet laufen sollen.

### 2.2 Unit-Tests (`tests/test_export_panorama_views.py`, 13 Tests)

Positives Testbild: Jeder Pixel kodiert seine 3D-Blickrichtung als RGB. Es ist auf der ganzen Kugel stetig, auch an Naht und Polen. So lässt sich jeder gerenderte Pixel zurückrechnen und **unabhängig vom Exporter** prüfen.
- Bildmitte zeigt in die verlangte Richtung (8 Richtungen inkl. Zenit/Nadir, < 1°).
- Sichtfeld entspricht `hfov` (40/90/120°, ±1°).
- Zeilen und Spalten sind Großkreise. Das ist die Eigenschaft einer echten Perspektivprojektion und schließt 2D-Ausschnitte aus.
- Orientierung: rechts = positiver Yaw, oben = positiver Pitch.
- Stetiges Panorama: kein Sprung an Naht, Zenit, Nadir; Naht-Kennzahl < 1,5.
- Bilineare Interpolation läuft über die Naht (kein künstlicher Sprung bei starkem Zoom).
- Ein Markierungspunkt landet dort, wo eine unabhängige Vorwärtsprojektion ihn erwartet (±2,5 px).
- Naht-Markierung nur in Ansichten, die die Naht enthalten.

Negative Testbilder:
- **Harte Naht:** Helligkeitsrampe, an ±180° dunkel/hell. Sprung > 140 sichtbar, Kennzahl > 10.
- **Falscher Pol:** gewöhnliche senkrechte Streifen in den obersten Zeilen, wie bei einem gestreckten Weitwinkelbild. Im Zenit-Zentrum ist die Streuung > 60, beim korrekten Bild < 8.

CLI: Dateien, Maße, Manifest mit `approved: false`, Fehlercode 1 bei unlesbarer Datei.

**Mutationstest:** Absichtlich eingebaute Fehler in einer Kopie des Exporters werden alle erkannt.

| Eingebauter Fehler | Ergebnis |
|---|---|
| Yaw-Vorzeichen vertauscht | 2 Tests schlagen fehl |
| Kein horizontaler Umlauf (Klemmen am Rand) | 1 Test schlägt fehl |
| Flacher 2D-Ausschnitt statt Kugelgeometrie | 4 Tests schlagen fehl |
| Pitch ignoriert | 4 Tests schlagen fehl |

### 2.3 Laufzeit (MacBook, Python 3.11, NumPy 2.4.6, Pillow 12.3.0)

| Eingabe | Zeit für 7 Ansichten + Prüfblatt | Max. Arbeitsspeicher |
|---|---:|---:|
| 1774×887 (Baseline) | ca. 3 s | – |
| 4096×2048 | 2,8 s | 0,37 GB |
| 8192×4096 | 3,1 s | 0,83 GB |

## 3. Befund der drei Baseline-Bilder (unverändert, nicht freigegeben)

| Szene | `check_panorama.py` Naht/Normal | Exporter Naht/Normal (40°-Ansicht) | Warnungen | Sichtbefund im Prüfblatt |
|---|---:|---:|---|---|
| gb-1840-textile-mill | 2,937 | 2,295 | BELOW_4K, SEAM_COLOR_DISCONTINUITY | Harter Bruch: Kesselfeuer links, Spinnerin rechts; Zenit mit spiralförmigen Balken und Riemen |
| gt-1910-banana-packing | 2,367 | 3,734 | BELOW_4K, SEAM_COLOR_DISCONTINUITY | Arbeiter und Kisten an der Naht zerschnitten; Nadir mit radial gestreckten Kisten und Planken |
| cn-2015-electronics-assembly | 1,844 | 1,977 | BELOW_4K, SEAM_COLOR_DISCONTINUITY | Bruch teils hinter Regalstütze verdeckt; trotzdem messbar |

Die Werte von `check_panorama.py` sind auf dem Mac identisch zu ChatGPTs Container-Lauf reproduziert worden. Die bestehenden 3 Tests bestehen ebenfalls.

**Grenzen:**
- Die Kennzahlen sind Farbstatistik. Sie erkennen keine Anachronismen, keine verzerrten Körper oder Maschinen und keine falsche Kamerahöhe.
- Ein guter Wert ist keine Freigabe.
- Pannellum-Bildern unter 4096 px Breite fehlt beim Zoomen Schärfe (1774 px ≈ 4,9 px/Grad). Das zeigt der Exporter ehrlich, kaschiert es aber nicht.

## 4. Prüfablauf für **einen** extern erzeugten 4K-Pilot

> **Stopp-Punkt vor jeder Generierung:** Die Erzeugung bei Skybox AI (oder einem anderen Anbieter) ist kostenpflichtig und braucht ein Konto. Das entscheidet ausschließlich der Nutzer.
>
> Entscheidungsvorlage (Zahlen aus `docs/360_GENERATION_OPTIONS_2026-11-08.md`, vor Kauf erneut prüfen):
> - Model 4 Standard = 3 Credits pro Versuch. Ein Pilot mit 1–3 Versuchen braucht 3–9 Credits.
> - Model 4 gibt es erst ab dem Standard-Abo (aktuell 60 USD/Monat für 300 Credits). Die 5 Gratis-Credits erlauben keinen Export.
> - Claude Code legt kein Konto an, fordert keinen Schlüssel an und speichert keinen.

### 4.1 Datei ablegen
1. Original-Download **unverändert** lokal ablegen, außerhalb von `public/`, damit nichts ungeprüft veröffentlicht wird:
   `qa-candidates/gb-1840-textile-mill__skybox-m4-standard__2026-MM-DD.jpg` (Ordner ist per `.gitignore` ausgeschlossen).
2. Die drei alten Bilder in `public/assets/panoramas/` bleiben als Baseline **unverändert**.
3. Ein freigegebener Pilot würde später unter neuem Namen eingecheckt, z. B. `public/assets/panoramas/gb-1840-textile-mill-v2.jpg`. Erst dann wird `panorama_path` angepasst. Das ist Sache des Freigabe-PRs, nicht dieses Ablaufs.

### 4.2 Herkunft festhalten (privat, nicht in `public/`)
Folgende Felder notieren:
- Anbieter, Modell, Style-ID und -Name
- Prompt und Negativ-Prompt (wörtlich)
- Seed bzw. Generation-ID
- Erzeugungsdatum
- verbrauchte Credits und Betrag
- Abo-Stufe
- Link und Abrufdatum der Nutzungsbedingungen
- SHA-256 der Originaldatei (steht in `manifest.json`)

Ohne vollständige Herkunft: **keine Freigabe**.

### 4.3 Automatische Vorprüfung (kostenlos)
```bash
mkdir -p qa-output
python3 scripts/check_panorama.py qa-candidates/<datei>.jpg --json > qa-output/pilot-check.json
python3 scripts/export_panorama_views.py qa-candidates/<datei>.jpg --out qa-output/pilot
python3 scripts/export_panorama_views.py qa-candidates/<datei>.jpg --out qa-output/pilot-extra --only-custom \
  --view 180,0,20 --view 180,60,60 --view=180,-60,60 --view 0,60,60 --view=0,-60,60
```
| Prüfpunkt | Erwartung | Bei Verfehlen |
|---|---|---|
| Maße | genau 2:1, mindestens **4096×2048** | Ablehnen (oder als Ansichtsprobe ohne Freigabe behalten) |
| `warnings` aus `check_panorama.py` | kein `NOT_2_TO_1`, kein `BELOW_4K` | Ablehnen |
| `SEAM_COLOR_DISCONTINUITY` / Exporter-Kennzahl ≥ 1,5 | idealerweise nicht vorhanden bzw. < 1,5 | Naht besonders genau ansehen; kein automatisches Aus, kein automatisches OK |

Die zusätzlichen Ansichten oben zeigen die Naht bei 20° (Nahaufnahme) und auf ±60° Neigung. Brüche zeigen sich oft erst oberhalb oder unterhalb des Horizonts.

### 4.4 Sichtprüfung (entscheidend; Prüfblatt und Live-Viewer)
Jeden Punkt mit **ja/nein + Bemerkung** dokumentieren. Ein „nein“ bei Naht, Zenit, Nadir oder Anachronismus heißt: **nicht freigeben.**

1. **Naht** (Ansichten 3, 7 und Zusatzansichten): durchgehende Linien, Wände, Maschinen und Personen über den Magenta-Meridian hinweg; kein Farb-, Licht- oder Perspektivsprung.
2. **Zenit** (Ansicht 5): geschlossene, plausible Decke; keine Spirale, kein Strudel, keine radial verschmierten Balken, kein Loch.
3. **Nadir** (Ansicht 6): plausibler Boden unter der Kamera; keine sternförmig gestreckten Objekte, keine zerschnittenen Maschinen oder Körper.
4. **Vier Richtungen** (Ansichten 1–4): ein einziger konsistenter Raum, durchgehender Horizont, gerade Senkrechten (Säulen, Fenster), Kamera auf plausibler Augenhöhe, keine doppelten Horizonte oder Collage-Kanten.
5. **Körper und Maschinen**: keine verschmolzenen Gliedmaßen, unmöglichen Getriebe oder Riemen ohne Rad. Mindestens drei Stellen mit `--view yaw,pitch,30` heranzoomen.
6. **Historische Plausibilität** (für 1840 Großbritannien):
   - keine Elektrik, Leuchtstoffröhren, Kunststoffe oder modernen Sicherheitszeichen
   - Kleidung, Maschinen (Spinnmaschinen und mechanische Webstühle der Zeit), Wellen- und Riemenantrieb und Architektur stimmig
   - kein lesbarer Text, keine Flagge, keine Jahreszahl, die das Quiz verrät
   - Fachliche Freigabe durch ChatGPT bzw. den Nutzer, nicht durch Claude Code allein.
7. **Live im Viewer:** `python3 -m http.server 8000 --directory public`, Kandidat über „Eigenes 360°-Testbild laden“ öffnen. Einmal 360° drehen, Zenit und Nadir ansehen, „Naht prüfen“, zoomen, Vollbild, mobil wischen. (Das Prüfblatt ist nachweislich pixelgleich zum Viewer; der Live-Check prüft zusätzlich die Bedienung.)

### 4.5 Rechte und Kosten
- Nutzungsbedingungen des Anbieters zur Erzeugungszeit sichern: kommerzielle bzw. Uni-Nutzung, Namensnennung, Weitergabe, Einschränkungen bei Referenzbildern.
- Tatsächliche Kosten des Pilots und hochgerechnete Kosten für 60 Szenen notieren, getrennt nach 1, 2 und 3 Versuchen pro Szene.

### 4.6 Ergebnis dokumentieren
PR mit:
- `manifest.json`-Auszug und `pilot-check.json`
- Prüfblatt (`contact_sheet.jpg`) plus Zusatzansichten als Anhang bzw. in privater Arbeitsdoku
- der ausgefüllten Sichtprüfungs-Tabelle (4.4)
- Herkunft (4.2)
- Kosten und Rechten (4.5)

`scene_status` bleibt `concept` und `approved_panorama_count` bleibt 0, bis Nutzer und ChatGPT die Freigabe ausdrücklich erteilen.

## 5. Nicht-Ziele und Grenzen

- Ein bestandenes 360°-Panorama erlaubt Umsehen und Zoomen von **einem festen Standpunkt**: kein Gehen, keine Parallaxe, kein „echtes 3D“.
- Das Werkzeug beurteilt keine historische Authentizität und keine Rechte.
- Die Pannellum-Gleichheit ist für Pannellum 2.5.7 und den equirectangularen Modus nachgewiesen. Bei einem Viewer-Wechsel muss der Abgleich (2.1) wiederholt werden.
