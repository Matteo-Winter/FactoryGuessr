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

- Aktives Ziel: **30 verschiedene 360°-Schauplätze** = 16 Produktionsstätten, 6 Handels-/Machtzentren, 8 historische Wendepunkte, ca. 1660–2023. **Bildstatus nach Review 09.11.2026: 11 visuell akzeptiert, 6 neu zu machen, 13 offen. Kollege bearbeitet 19 Bild-To-dos; Projektleitung prüft alle 30.** Alte 60er- und 30/30-Pläne sind Archiv. Schwerpunkt ZuWi: *Von Handelskompanien zu Multinational Corporations*.
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

## AKTUELLE Szene- und Bildplanung (Nutzerprüfung 09.11.2026)

- Historischer Umfang **30**: [Aktiver Masterplan](docs/SCENE_MASTERPLAN_30.md) mit 16 Produktionsstätten, 6 Handels-/Machtorten und 8 Wendepunkten.
- **[Verbindliche aktuelle Bildprüfung mit Dateinamen](docs/IMAGE_PRODUCTION_STATUS_30.md)** · [JSON-Quelle](docs/team/ACTIVE_SCENES_30.json) · [Aktueller Gemini-Prompt](docs/team/GEMINI_IMAGE_HANDOFF_CURRENT.md) · [Issue #18](https://github.com/Matteo-Winter/FactoryGuessr/issues/18).
- **11 Nutzerurteile „Passt“:** P01, P02, P03, P04, P05, P09, P10, P13, T01, T03, T04. **6 abgelehnte Dateien:** T05, E01, E03, E04, E05, E07. **13 aktive Szenen ohne Urteil im Review:** P06, P07, P08, P11, P12, P14, P15, P16, T02, T06, E02, E06, E08.
- **Arbeit des Kollegen mit Gemini:** genau **6 Remakes + 13 offene**; der alte Auftrag „26 Bilder komplett neu“ sowie die frühere 16/14-Bildzuweisung sind **überholt**. `COLLEAGUE_MASTER_PROMPT_14.md` dient nur noch als historisch-technischer Spezialanhang.
- Drei alte Pilot-IDs `gb-1840-textile-mill`, `gt-1910-banana-packing`, `cn-2015-electronics-assembly` entsprechen den aktiven P05, P09, P13, **nicht** drei zusätzlichen Leveln.
- Kanton/Perlfluss `review-perlfluss-alternative.png` ist eine zweite vom Nutzer als „Passt“ beurteilte **Variante von T04**, kein Level 31. Das abgelehnte Murano-Alternativbild ändert nichts an P02 „Passt“. Sonstige reviewed Extras außerhalb des 30er-Plans nicht neu als Level erstellen.
- **Nur Bildname und Reviewurteil sind bekannt.** Aktuelle Bildbytes sind durch GitHub-Notizen nicht übertragen; keine Dateihashes, Dateigrößen oder Bild-Uploads fingieren.
- **„Passt“ ist nur die visuelle Nutzerentscheidung**, kein vollständiger Kugelprojektion-/Historien-/Lizenz- oder Browser-PASS. `target_scenes=30`, `approved_panorama_count=0`. In `public/data/scenes.json` bestehende Piloten nicht stillschweigend überschreiben.
- Historische Recherche und Equirectangular-/Naht-/Zenit-/Nadir-/Perspektivprüfung pro Bild; sensible Ereignisse als KI-Rekonstruktion. Kein automatisches `ready`, Merge/Deployment oder kostenpflichtiger Aufruf.

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
