# Made in Time — FactoryGuessr

**Guess where. Guess when.**

Ein historisches GeoGuessr-artiges Lernspiel für die ZuWi-Vertiefung **„Von Handelskompanien zu Multinational Corporations“**: In einer drehbaren Produktionsszene erraten Spielende das Land und die Epoche. Danach folgt eine kurze Einordnung zu Arbeitsbedingungen, Industrie, Kolonialismus, Unternehmensmacht oder globalen Lieferketten.

## Festgelegter Umfang

- Ziel: **mindestens 60 unterschiedliche spielbare Szenen**, ca. **1600–2026**, aus mehreren Regionen und Industriezweigen.
- V1 verwendet **360°-Panoramen (equirectangular, 2:1)** mit fester Kameraposition, **keine frei begehbaren 3D-Modelle**.
- Historische Betriebe dürfen **plausible, KI-generierte Kompositszenen** sein. Diese werden als *Rekonstruktion* gekennzeichnet – nicht als echte historische Fotografien.
- Informationen wie Land, Zeitraum und Lernkontext werden getrennt vom KI-Bild geprüft.
- Keine automatischen Behauptungen über konkrete Unternehmen, die nicht belegt sind.

**Projektstatus:** 3 erste Szenenkonzepte angelegt, **0/60 freigegebene 360°-Bilddateien**. Bilder werden erst nach Sichtprüfung als `ready` markiert.

## Repository

- `public/data/scenes.json` — Pilot-Szenenkonzepte, Metadaten, Prompts, Bildpfade und Freigabestatus.
- `docs/PANORAMA_PIPELINE.md` — Generierungs- und Qualitätskontrollprozess.
- `scripts/generate_skybox.py` — lokaler Prompt-/Job-Exporter für eine spätere manuelle Panorama-Generierung (**ohne API-Aufruf und ohne Kosten**).
- `public/assets/panoramas/` — später die tatsächlichen JPG/PNG-Panoramen.
- `public/index.html` — erster 360°-Browser-Viewer mit Bild-Upload und Probe-Ratefunktion.

## Lokal starten

```bash
git clone https://github.com/Matteo-Winter/FactoryGuessr.git
cd FactoryGuessr
python3 -m http.server 8000 --directory public
```

Dann `http://localhost:8000` öffnen. Für den 360°-Viewer wird einmalig die Pannellum-Bibliothek über ein CDN geladen. Solange keine Panoramabilder vorhanden sind, kann man ein lokales equirectangulares Testbild hochladen.

## Interaktive 360°-Testversion (drei Szenen)

Es gibt drei KI-generierte **2:1-Testbilder** als separates ZIP im zugehörigen Chat. Im Repository bleibt der Viewer bis zum Einfügen dieser Bilddateien ohne Panorama. Im ZIP ist außerdem ein vollständig lokaler, CDN-unabhängiger WebGL-Viewer enthalten.

Zum Testen im geklonten Repository:

1. Die drei JPG-Dateien aus dem ZIP nach `public/assets/panoramas/` kopieren.
2. `python3 -m http.server 8000 --directory public` ausführen.
3. `http://localhost:8000` öffnen, per Maus drehen/zoomen und **Naht prüfen**.

Schritt-für-Schritt-Anleitung und technische Grenzen: [docs/LOCAL_360_TEST.md](docs/LOCAL_360_TEST.md).

**Ein 360°-Bild ist nicht dasselbe wie ein frei begehbares 3D-Modell.** Die KI-Bilder sind noch nicht auf vollständige 360°-Nahtlosigkeit geprüft und bleiben deshalb Testmaterial (0/60 freigegeben).

## Auf Vercel bereitstellen (noch nicht deployed)

1. Auf [vercel.com/new](https://vercel.com/new) das private GitHub-Repository `Matteo-Winter/FactoryGuessr` importieren und gegebenenfalls den Zugriff für Vercel erlauben.
2. Einstellungen: **Root Directory:** `./`, **Framework Preset:** `Other`, **Build Command:** leer/kein Build, **Output Directory:** `public`. `vercel.json` definiert Framework und Output Directory bereits.
3. Auf **Deploy** klicken. Bei späteren Pushes auf `main` kann Vercel automatisch neue Versionen deployen, sobald die Git-Integration eingerichtet ist.

Das Repository wurde lediglich vorbereitet: **Es ist noch kein Deployment ausgeführt worden.** Ohne fertige Bilddateien wird im Viewer die Platzhalteransicht angezeigt.

## Bilder einfügen

- Echte geprüfte 360°-Datei (2:1) nach `public/assets/panoramas/<scene-id>.jpg` speichern.
- Eintrag in `public/data/scenes.json` ergänzen bzw. nach Prüfung `scene_status` auf `ready` setzen.
- `panorama_path` bleibt relativ zur Website, z.B. `assets/panoramas/gb-1840-textile-mill.jpg`. Nicht `public/` in den Bild-URL schreiben.
- `public/assets/thumbnails/` ist für spätere Vorschaubilder vorbereitet.

## Bilder generieren

```bash
python3 scripts/generate_skybox.py gb-1840-textile-mill
```

Das exportiert den Prompt und die Bildvorgaben (**kein API-Aufruf, keine Kosten**). Zur anschließenden manuellen Generierung und Qualitätsprüfung siehe `docs/PANORAMA_PIPELINE.md`. Niemals Zugangsdaten ins Repo oder ins Frontend schreiben.

## Arbeitsprinzip

**Zuerst 3 Panoramen erfolgreich generieren und im Browser testen, anschließend auf mindestens 60 skalieren.** Historisch plausible Details sind wichtiger als erfundene Beschilderungen, die sofort die richtige Antwort verraten.

Quellen zur Technik:
- [Blockade Labs: Skybox AI](https://www.blockadelabs.com/)
- [Blockade Labs API-Dokumentation](https://docs-staging.blockadelabs.com/api/skybox.html)
- [Pannellum (MIT)](https://pannellum.org/)
