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

- `data/scenes.json` — Pilot-Szenenkonzepte, Metadaten, Prompts, Bildpfade und Freigabestatus.
- `docs/PANORAMA_PIPELINE.md` — Generierungs- und Qualitätskontrollprozess.
- `scripts/generate_skybox.py` — lokaler Prompt-/Job-Exporter für eine spätere manuelle Panorama-Generierung (**ohne API-Aufruf und ohne Kosten**).
- `assets/panoramas/` — später die tatsächlichen JPG/PNG-Panoramen.
- `index.html` — erster 360°-Browser-Viewer mit Bild-Upload und Probe-Ratefunktion.

## Lokal starten

```bash
git clone https://github.com/Matteo-Winter/FactoryGuessr.git
cd FactoryGuessr
python3 -m http.server 8000
```

Dann `http://localhost:8000` öffnen. Für den 360°-Viewer wird einmalig die Pannellum-Bibliothek über ein CDN geladen. Solange keine Panoramabilder vorhanden sind, kann man ein lokales equirectangulares Testbild hochladen.

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
