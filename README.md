# Made in Time — FactoryGuessr

**Guess where. Guess when.**

Ein historisches GeoGuessr-artiges Lernspiel für die ZuWi-Vertiefung **„Von Handelskompanien zu Multinational Corporations“**: In einer drehbaren Produktionsszene erraten Spielende das Land und die Epoche. Danach folgt eine kurze Einordnung zu Arbeitsbedingungen, Industrie, Kolonialismus, Unternehmensmacht oder globalen Lieferketten.

## Festgelegter Umfang

- Ziel: **mindestens 60 unterschiedliche spielbare Szenen**, ca. **1600–2026**, aus mehreren Regionen und Industriezweigen.
- **[Masterplan mit 60 konkreten Szenen, Ländern, Jahren, Produkten und Bildhinweisen](docs/SCENE_MASTERPLAN_60.md)** — Entwurf der Motivliste, keine automatische Bild- oder Geschichtsfreigabe. Vor jedem einzelnen Rendering wird eine geprüfte historische Faktenkarte angelegt.
- V1 verwendet **360°-Panoramen (equirectangular, 2:1)** mit fester Kameraposition, **keine frei begehbaren 3D-Modelle**.
- Historische Betriebe dürfen **plausible, KI-generierte Kompositszenen** sein. Diese werden als *Rekonstruktion* gekennzeichnet – nicht als echte historische Fotografien.
- Informationen wie Land, Zeitraum und Lernkontext werden getrennt vom KI-Bild geprüft.
- Keine automatischen Behauptungen über konkrete Unternehmen, die nicht belegt sind.

**Projektstatus:** 3 erste Szenenkonzepte mit je einem KI-generierten 2:1-Testbild im Repository, **0/60 historisch und geometrisch freigegebene Panoramen**. Bilder werden erst nach Sichtprüfung als `ready` markiert.

## Repository

- `public/data/scenes.json` — Pilot-Szenenkonzepte, Metadaten, Prompts, Bildpfade und Freigabestatus.
- `docs/PANORAMA_PIPELINE.md` — Generierungs- und Qualitätskontrollprozess.
- `scripts/generate_skybox.py` — lokaler Prompt-/Job-Exporter für eine spätere manuelle Panorama-Generierung (**ohne API-Aufruf und ohne Kosten**).
- `public/assets/panoramas/` — Panoramabilder; derzeit drei KI-generierte 2:1-Testbilder (nicht freigegeben).
- `public/index.html` — erster 360°-Browser-Viewer mit Bild-Upload und Probe-Ratefunktion.

## Lokal starten

```bash
git clone https://github.com/Matteo-Winter/FactoryGuessr.git
cd FactoryGuessr
python3 -m http.server 8000 --directory public
```

Dann `http://localhost:8000` öffnen. Für den 360°-Viewer wird die Pannellum-Bibliothek (v2.5.7) über das jsDelivr-CDN geladen. Zusätzlich kann man ein eigenes lokales equirectangulares Testbild hochladen.

## Interaktive 360°-Testversion (drei Szenen)

Die drei KI-generierten **2:1-Testbilder** (1774 × 887 px) liegen im Repository unter `public/assets/panoramas/`. Es muss nichts mehr manuell kopiert werden.

Zum Testen im geklonten Repository:

1. `python3 -m http.server 8000 --directory public` ausführen.
2. `http://localhost:8000` öffnen, Szene wählen, per Maus drehen/zoomen, Vollbild testen und **Naht prüfen**.

Historischer Hinweis: Die Bilder wurden ursprünglich als ZIP aus dem ChatGPT-Chat übergeben; dieses ZIP enthielt auch einen alternativen, CDN-unabhängigen WebGL-Viewer. Das ZIP ist nicht mehr der Einstieg – maßgeblich ist dieses Repository.

Schritt-für-Schritt-Anleitung und technische Grenzen: [docs/LOCAL_360_TEST.md](docs/LOCAL_360_TEST.md).

**Ein 360°-Bild ist nicht dasselbe wie ein frei begehbares 3D-Modell.** Die KI-Bilder sind noch nicht auf vollständige 360°-Nahtlosigkeit geprüft und bleiben deshalb Testmaterial (0/60 freigegeben).

## Auf Vercel bereitstellen (noch nicht deployed)

1. Auf [vercel.com/new](https://vercel.com/new) das private GitHub-Repository `Matteo-Winter/FactoryGuessr` importieren und gegebenenfalls den Zugriff für Vercel erlauben.
2. Einstellungen: **Root Directory:** `./`, **Framework Preset:** `Other`, **Build Command:** leer/kein Build, **Output Directory:** `public`. `vercel.json` definiert Framework und Output Directory bereits.
3. Auf **Deploy** klicken. Bei späteren Pushes auf `main` kann Vercel automatisch neue Versionen deployen, sobald die Git-Integration eingerichtet ist.

Das Repository wurde lediglich vorbereitet: **Es ist noch kein Deployment ausgeführt worden.** Fehlt für eine Szene die Bilddatei oder kann der Browser sie nicht darstellen, zeigt der Viewer eine Fehlermeldung statt eines Panoramas.

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

## Arbeitsteilung: 2 Personen, 60 Szenen

Die geplanten 60 Motive sind **chronologisch in genau 30 ältere und 30 neuere Szenen** geteilt. Die Master-Nummern bleiben stabil. Die Grenze ist 1925 (Paris 1925 = ältere Liste, Kaffee Brasilien 1925 = neuere Liste).

- **[Beide Teams, Aufteilungsregel und Arbeitsregeln](docs/team/SCENE_SPLIT_30_30.md)**
- **[Ältere 30 – Projektleitung](docs/team/OLDER_30_LEAD.md)**
- **[Neuere 30 – Kollege](docs/team/NEWER_30_COLLEAGUE.md)**
- **[Ausführlicher 3D-first-360°-Masterprompt für alle Bilder](docs/team/PRODUCTION_PLAYBOOK_360.md)**

Vor **jeder** Bildgenerierung historische Quellen-Faktenkarte, danach echte zusammenhängende 3D-Geometrie, native Kugelprojektion und die vollständige 360°-QA. Kein 2:1-Bild allein als „3D“ und kein Pixel-Nahtwert allein als Freigabe. **Alle bisherigen Bilder bleiben bis zur individuellen Abnahme Kandidaten.**

## 360°-Qualitätskontrolle und nächste Bildpipeline

- [Recherche: native 360°-Generatoren, Preise und 1-Szenen-Testplan](docs/360_GENERATION_OPTIONS_2026-11-08.md)
- [Aktuelle Arbeitsaufgabe für Claude Code: Issue #3](https://github.com/Matteo-Winter/FactoryGuessr/issues/3)
- Die Bilder sind weiterhin **nicht** historisch/optisch freigegeben (0/60), obwohl der Viewer technisch funktioniert.

Optionale lokale Diagnostik (Pillow und NumPy, **keine** API-Aufrufe):

```bash
python3 -m pip install -r requirements-qa.txt
python3 scripts/check_panorama.py public/assets/panoramas/*.jpg
python3 scripts/export_panorama_views.py public/assets/panoramas/*.jpg   # Prüfansichten nach qa-output/
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Die Ergebnisse zeigen Bildgröße, Farbbruch an der 360°-Naht und Hinweise auf problematische Pole. `export_panorama_views.py` rechnet echte perspektivische Ansichten (yaw 0/90/180/270, Zenit, Nadir, Naht-Nahaufnahme) plus ein Prüfblatt `contact_sheet.jpg`, geometrisch identisch mit dem Pannellum-Viewer. Prüfablauf für einen neuen 4K-Kandidaten: [docs/PANORAMA_QA_PROBES.md](docs/PANORAMA_QA_PROBES.md). **Kein Messwert ersetzt die Sichtprüfung im Viewer; das Skript kann Bilder ausdrücklich nicht freigeben.**

## Arbeitsprinzip

**Zuerst den 60er-Masterplan als gemeinsame Motivliste verwenden, dann jeweils eine historische Faktenkarte (Produkt, Region, Jahr, passende Maschinen, 2 Orts- und 2 Zeitmerkmale, überprüfbare Quellen) erstellen, dann erst das Bild generieren und QA ausführen.** Die bestehende britische Textilmühle ist als visueller Stilversuch vom Nutzer ausreichend bewertet; das allein ersetzt keine historische oder equirectangulare Freigabe. Bilder sollen sich weltweit und über Epochen unterscheiden und vor der Auflösung keine Ortsnamen/Flaggen als Spoiler zeigen.

Quellen zur Technik:
- [Blockade Labs: Skybox AI](https://www.blockadelabs.com/)
- [Blockade Labs API-Dokumentation](https://docs-staging.blockadelabs.com/api/skybox.html)
- [Pannellum (MIT)](https://pannellum.org/)
