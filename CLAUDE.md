# Claude Code – Zusammenarbeit an Made in Time

Projekt: `Matteo-Winter/FactoryGuessr` (privat), Spieltitel **Made in Time – Guess where. Guess when.**

## Arbeitsweise

- **GitHub ist die gemeinsame und maßgebliche Projektquelle.** Keine eigenständigen, dauerhaft abweichenden ZIP-Versionen als Endprodukt.
- ChatGPT: Anforderungen, Recherche, Bildpipeline, Code-Review und fachliche Freigabe bei Übergabe.
- Claude Code: lokale Implementierung, Bildintegration, Browser-/Rendering-Tests sowie technische Fehlerbehebung.
- Jede größere Claude-Code-Aufgabe wird als GitHub Issue beschrieben. Erstelle einen `claude/<kurzer-thema>`-Branch vom aktuellen `main`; Änderungen als Pull Request auf `main`, mit `Closes #N` oder `Refs #N` und prüfbarem Testbericht.
- **Nicht direkt auf `main` arbeiten, nicht automatisch mergen, nicht force-pushen.** Bei unklaren Anforderungen im Issue nachfragen statt sie zu erfinden. Vor Beginn `git fetch`, Branch und sauberen Status prüfen.
- Nach der PR-Erstellung ChatGPT im Chat den PR-Link und die Testergebnisse geben, damit der Code und die Bilder geprüft werden können. Kein automatischer Austausch zwischen zwei laufenden KI-Chats wird behauptet.

## Produkt- und Technikentscheidungen

- Ziel: **mindestens 60 unterschiedliche Produktionsstätten**, ca. 1600–2026, mindestens verschiedene Epochen, Länder und Industrien. Schwerpunkt ZuWi: *Von Handelskompanien zu Multinational Corporations*.
- V1: **360°-Panorama** mit fixer Kameraposition (Maus ziehen, Zoom, Vollbild); kein frei begehbares, geometrisch rekonstruiertes 3D.
- Für Street-View-artiges Weitergehen sind später *mehrere* konsistente Kamera-Standpunkte und Hotspots nötig. Nicht vortäuschen, dass ein einzelnes 2D-Bild dies bereits bietet.
- Derzeit drei vorbereitete Szenen in `public/data/scenes.json`:
  - `gb-1840-textile-mill`: Textilfabrik Großbritannien ~1840
  - `gt-1910-banana-packing`: Bananen-Packhaus Guatemala ~1910
  - `cn-2015-electronics-assembly`: Elektronikmontage China ~2015
- Die drei KI-Bilder sind **Testkandidaten**, nicht auf authentische equirectangulare Geometrie, Nahtlosigkeit oder historische Korrektheit freigegeben. `2:1` allein ist kein Qualitätsnachweis. Freigabe-Status nicht voreilig auf `ready` setzen.
- Bestehende Daten und Bildprompts bewahren. Besonders `public/data/scenes.json` ist die ausführliche, maßgebliche Fassung; sie darf **nicht durch eine vereinfachte Test-ZIP-Fassung überschrieben** werden.
- Vercel: statisches Hosting über `public/` (`vercel.json`), ohne notwendiges Backend; **kein Deployment ohne expliziten Auftrag**.
- Keine Secrets committen; keine kostenpflichtigen API-Aufrufe ohne Freigabe.

## Maßgeblicher Motivplan und Produktionsfreigabe (09.11.2026)

- **[docs/SCENE_MASTERPLAN_60.md](docs/SCENE_MASTERPLAN_60.md)** ist der abgestimmte **Entwurf** mit 60 geplanten Produktionsszenen über sechs Epochen. Die Auswahl soll **leicht verständliche Produkte** und faire Orts-/Zeitsignale liefern, keine 60 austauschbaren Fabrikhallen.
- **Nicht alle 60 Szenen auf einmal generieren.** Pro Motiv zuerst regional und historisch verifizieren (mindestens eine institutionelle/archivarische Quelle, idealerweise zwei unabhängige Quellen), per Faktenkarte festhalten, sichtbares Hauptprodukt, Ort, Jahr, passende Maschinen, Kleidung/Transport/Energiequelle und Anachronismen prüfen. Erst dann Rendering und 360°-QA.
- Bei den älteren Szenen ist das Rateland der **heutige Staat**, damals abweichende Herrschaftsformen werden nach dem Raten aufgeklärt. Keine zeitfremden Flaggen, Schildaufschriften, geographische Stereotype oder erfundene Firmenbezüge einsetzen.
- Die bereits vorhandenen 3 Pilot-IDs in `public/data/scenes.json` bleiben erhalten: `gb-1840-textile-mill`, `gt-1910-banana-packing`, `cn-2015-electronics-assembly`. Die Nutzerbewertung „Bild gut genug“ betrifft **nur den visuellen Stil** des jüngsten Textilmühlenkandidaten; noch keine automatische technische/historische Freigabe. `approved_panorama_count` bleibt 0, bis QA und explizite Freigabe erfüllt sind.
- Die Liste darf gemeinsam angepasst werden, aber **keine `ready`-Statusänderungen, keine neuen produktiven Bildpfade und kein Deployment** ohne eigenen Prüfauftrag.

## Parallele Szenenproduktion (30/30)

- **[Team-Split](docs/team/SCENE_SPLIT_30_30.md)**, **[ältere Szenen – Projektleitung](docs/team/OLDER_30_LEAD.md)** und **[neuere Szenen – Kollege](docs/team/NEWER_30_COLLEAGUE.md)** sind verbindliche Entwürfe für die Arbeitsteilung. Bei Jahrgleichheit 1925 gehören Paris/Französische Mode (Master-Nr. 32) zum älteren Team und São-Paulo-Kaffee (Nr. 34) zum neueren Team.
- **[3D-/360°-Produktionsprompt und Quality Gates](docs/team/PRODUCTION_PLAYBOOK_360.md)** ist für beide Teams verpflichtend. Nicht einfach freie 2:1-Bilder als geometrisch korrekt ausgeben. Gerade Maschinen/Balken/Flügel müssen in der **Pannellum-Perspektive** plausibel sein.
- Die Szene-Sperren beziehen sich auf die **Master-Nummern** (nicht die Zeilennummer nach Sortierung). Claude Code und ChatGPT können reviewen; nur zuständiger Besitzer ändert die Produktionskandidaten. Abstimmung für gemeinsame `public/data/scenes.json`-Änderungen notwendig.
- Für Kollegen-Repositories pro Szene `colleague/scene-NN-...`-Feature-Branch und PR; für Claude-Code-Aufgaben weiterhin `claude/...`. Keine automatische `ready`-Freigabe und kein Deployment.

## Lokaler Start

```bash
python3 -m http.server 8000 --directory public
```

Anschließend `http://localhost:8000`. Dokumentation: `README.md`, `docs/LOCAL_360_TEST.md`, `docs/PANORAMA_PIPELINE.md`.

## Übergabestandard

PR-Beschreibung:
1. Was wurde konkret implementiert und welche Dateien geändert?
2. Welcher Test wurde wirklich ausgeführt (Befehle, Browser, Erfolg/Fehler)?
3. Funktionieren alle drei Panoramen, Maussteuerung, Zoom, Vollbild und Seam-Check tatsächlich?
4. Welche grafischen oder geometrischen Fehler bleiben?
5. Ist der Branch gepusht und der Git-Arbeitsbaum sauber?
6. Hinweis: keine ungeprüfte Behauptung `real 3D` oder `historisch authentisch`.
