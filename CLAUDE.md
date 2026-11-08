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
