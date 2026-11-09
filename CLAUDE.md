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

- Aktives Ziel: **30 verschiedene 360°-Schauplätze** = 16 Produktionsstätten, 6 Handels-/Machtzentren, 8 historische Wendepunkte, ca. 1660–2023. **Bildproduktion: 4 Referenzen vom Nutzer visuell akzeptiert, 26 fehlen und werden vom Kollegen mit Gemini erstellt.** Projektleitung prüft alle 30. Alte 60er- und 30/30-Pläne sind Archiv. Schwerpunkt ZuWi: *Von Handelskompanien zu Multinational Corporations*.
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

## AKTUELLE Szene- und Bildplanung (09.11.2026)

- Historischer Inhalt weiterhin [**30 Szenen**](docs/SCENE_MASTERPLAN_30.md), aber Bildauswahl wurde **explizit durch Nutzer neu priorisiert**.
- **[VERBINDLICHE Bildliste: 4 akzeptiert, 26 zu erstellen](docs/IMAGE_PRODUCTION_STATUS_30.md)** und [JSON-Quelle](docs/team/ACTIVE_SCENES_30.json).
- **Visuell akzeptierte Referenzbilder:** `P02` Murano 1680, `P03` Jingdezhen 1700, `P05` GB Textilfabrik 1840, `P10` Detroit Autobau 1913. Achtung: Die vier Bilddateien wurden im Chat hochgeladen und sind **nicht automatisch über GitHub verfügbar**. Ihre echten Pixelgrößen stehen im Manifest. Sie sind noch **nicht** technisch/historisch `ready`.
- **Alle 26 anderen Bilder von Kollege/Gemini:** 12 P + 6 T + 8 E. **[Aufgabenbriefing](docs/team/GEMINI_IMAGE_HANDOFF_26.md)** und [Teamübergabe](docs/team/ACTIVE_SPLIT_30.md).
- Die alte Vorgabe **P01–P16 nur beim Nutzer** und `COLLEAGUE_MASTER_PROMPT_14.md` als vollständiger Arbeitsauftrag ist überholt. Der 14er-Prompt dient nur als ausführlicher *Anhang zu T/E-Historik und QA*, nicht als personelle Zuständigkeitsliste.
- Pro Szene institutionelle/archivarische Quellen, Jahr, Produkt oder historische Handlung, regional passende visuelle Hinweise und Anachronismen; 3D-/sphärische Bildgeometrie und echter Pannellum-QA-Check. **2:1 allein beweist keine gültige Kugel.**
- Bei Events mit Opfern/kolonialem Zwang **klar als KI-Rekonstruktion** kennzeichnen, keine falschen Augenzeugenfotos oder erfundenen Verletztenbilder.
- `target_scenes=30`, `approved_panorama_count=0`. Bestehende drei Piloteinträge in `public/data/scenes.json` sind keine vollständige Bildinventarliste und werden durch die 30er-Planung **nicht** stillschweigend überschrieben.
- Kein automatisches `ready`, Merge, Deployment oder kostenpflichtige API ohne ausdrückliche Freigabe.

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
