# Claude Code – Zusammenarbeit an Made in Time

## AKTUELLE Bildprüfung / Quellenstand (09.11.2026)
- **[Offizieller Bildstatus 13 visuell akzeptiert / 4 neu / 13 offen](docs/IMAGE_PRODUCTION_STATUS_30.md)**. Maßgeblich statt älterer 4/26-, 11/6-, 12/5- und 16/14-Datei-Aufteilungen.
- **E04 Wall Street 1929:** Nutzer hat das neu generierte Bild mit „perfekt“ visuell akzeptiert; keine formale Geometrie-/Historien-/Lizenzfreigabe folgern.
- **E05 Guatemala 1954:** neuer 3D-first-Fotokandidat mit 360°-Nahtglättung vorhanden, aber visuelle Abnahme und historische Palastgenauigkeit offen. [Ausführliche QA](docs/scene-research/E05_Guatemala_1954_3D_photo_QA.md). Kein neuer `ready`-Status. ZIP im Chat, nicht im Repository.
- **[Gemini-Auftrag für die 17 offenen Bilder](docs/team/GEMINI_IMAGE_HANDOFF_CURRENT.md)** · [GitHub Issue #18](https://github.com/Matteo-Winter/FactoryGuessr/issues/18). Keine weiteren 4/26- oder 12/5-Produktionsaufträge ausführen.


Projekt: `Matteo-Winter/FactoryGuessr` (privat), Spieltitel **Made in Time – Guess where. Guess when.**

## Arbeitsweise

- **GitHub ist die gemeinsame und maßgebliche Projektquelle.** Keine eigenständigen, dauerhaft abweichenden ZIP-Versionen als Endprodukt.
- ChatGPT: Anforderungen, Recherche, Bildpipeline, Code-Review und fachliche Freigabe bei Übergabe.
- Claude Code: lokale Implementierung, Bildintegration, Browser-/Rendering-Tests sowie technische Fehlerbehebung.
- Jede größere Claude-Code-Aufgabe wird als GitHub Issue beschrieben. Erstelle einen `claude/<kurzer-thema>`-Branch vom aktuellen `main`; Änderungen als Pull Request auf `main`, mit `Closes #N` oder `Refs #N` und prüfbarem Testbericht.
- **Nicht direkt auf `main` arbeiten, nicht automatisch mergen, nicht force-pushen.** Bei unklaren Anforderungen im Issue nachfragen statt sie zu erfinden. Vor Beginn `git fetch`, Branch und sauberen Status prüfen.
- Nach der PR-Erstellung ChatGPT im Chat den PR-Link und die Testergebnisse geben, damit der Code und die Bilder geprüft werden können. Kein automatischer Austausch zwischen zwei laufenden KI-Chats wird behauptet.

## Produkt- und Technikentscheidungen

- Aktives Ziel: **30 verschiedene 360°-Schauplätze** = 16 Produktionsstätten, 6 Handels-/Machtzentren, 8 historische Wendepunkte, ca. 1660–2023. **Bildstatus nach Review + Boston-Nachtrag 09.11.2026: 12 visuell akzeptiert, 5 neu zu machen, 13 offen. Kollege bearbeitet 18 Bild-To-dos; Projektleitung prüft alle 30.** Alte 60er- und 30/30-Pläne sind Archiv. Schwerpunkt ZuWi: *Von Handelskompanien zu Multinational Corporations*.
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

## AKTUELLER Bildstatus (Nutzerprüfung + E01-Nachtrag, 09.11.2026)

- **[Aktiver Gesamtplan: 30 Szenen](docs/SCENE_MASTERPLAN_30.md)** · [aktuelle Bildliste mit Dateinamen](docs/IMAGE_PRODUCTION_STATUS_30.md) · [JSON](docs/team/ACTIVE_SCENES_30.json) · [Gemini-Briefing für 18 offene Bilder](docs/team/GEMINI_IMAGE_HANDOFF_CURRENT.md) · [GitHub Issue #18](https://github.com/Matteo-Winter/FactoryGuessr/issues/18).
- **12 visuell akzeptiert:** `P01,P02,P03,P04,P05,P09,P10,P13,T01,T03,T04,E01`. E01 wurde im Folgechat mit „okay passt, nächstes bild“ visuell akzeptiert; **keinen technischen Kugel-PASS daraus folgern**.
- **5 explizit neu:** `T05,E03,E04,E05,E07`. **E03:** [3D-first Suez-Versuch und nicht bestandene Foto-Naht](docs/scene-research/E03_Suez_1869_REWORK_QA.md); neue Original-/3D-/QA-Binärdateien im Chat-ZIP, nicht automatisch im Repo. `suezkanal.png` weiter ersetzt werden müssen.
- **13 ohne aktuelles Prüfurteil:** `P06,P07,P08,P11,P12,P14,P15,P16,T02,T06,E02,E06,E08`. Vorhandene Kandidaten erst zur Prüfung einreichen, keine Ablehnung behaupten.
- Zusatzreview: `review-perlfluss-alternative.png` ist zweite akzeptierte T04-Variante, `review-venedig.webp` abgelehnte P02-Alternative. Marktplatz/Machu Picchu/Regenwald/Eisenbahn sind keine zusätzlichen aktiven Level.
- Keine Änderungen an `public/data/scenes.json` ohne separate historische/technische Browser-QA. `approved_panorama_count=0`, `target_scenes=30`. Kein eigenmächtiger Merge, Deploy oder bezahlter API-Aufruf.
- Jede neue Szene quellenbasiert, 3D-/360°-Rückseite, Ufer/Schiffe/Balken/Zenit/Nadir im echten perspektivischen Viewer prüfen. Zahl `0,0×` kann durch unnütze Spiegelung entstehen und ist kein visueller PASS.

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
