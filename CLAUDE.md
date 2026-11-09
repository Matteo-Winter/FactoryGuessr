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

- Aktives Ziel: **30 verschiedene 360°-Schauplätze** = 16 Produktionsstätten (Projektleitung), 6 Handels-/Machtzentren und 8 historische Wendepunkte (Kollege), ca. 1660–2023. Alte 60er- und 30/30-Pläne sind Archiv. Schwerpunkt ZuWi: *Von Handelskompanien zu Multinational Corporations*.
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

## AKTUELLER Motivplan und Produktionsfreigabe (09.11.2026)

- **[Aktiver Gesamtplan mit genau 30 Leveln](docs/SCENE_MASTERPLAN_30.md)**: 16 P + 6 T + 8 E. Die 60er-Liste und ältere 30/30-Teilung gelten **nicht** mehr als Produktionsaufträge.
- **[Arbeitsteilung 16/14](docs/team/ACTIVE_SPLIT_30.md)** · [Nutzer – 16 Produktionen](docs/team/USER_16_PRODUCTION.md) · [Kollege – 14 Handel-/Ereignisszenen](docs/team/COLLEAGUE_14_SCENES.md).
- **[Pflicht-Masterprompt für Kollegen](docs/team/COLLEAGUE_MASTER_PROMPT_14.md)**: historische Quellen, 3D-first, native sphärische 4K-Projektion, Bildrealismus, QA, event-sensible Rekonstruktion, Lieferschema.
- Nur die **zugewiesenen IDs** bearbeiten. T/E-Szenen nie mit dem alten „neuere 30 Produktionsstätten“-Auftrag verwechseln; P-Bilder bleiben bei Projektleitung.
- Pro Motiv institutionelle/archivarische Quellen, Ort und alte/historische Staatsform, produktive/historische Kernhandlung, mindestens zwei plausible Orte-/Zeitmerkmale, Anachronismen; dann echte 3D-Szene, Bilder, perspektivische QA und Browser-Review. **Kein 2:1-Foto als echten 360°-Raum ausgeben.**
- Für Ereignisse mit Opfern oder Konflikten keine scheinbar authentischen, erfundenen Augenzeugenbilder, Gewalt- oder Opferbilder; respektvolle **klar als KI-Rekonstruktion** gekennzeichnete historische Schauplätze.
- Die **drei existierenden Pilotszenen** `gb-1840-textile-mill`, `gt-1910-banana-packing`, `cn-2015-electronics-assembly` im Repo sind unverändert weiterzuverwenden, aber **nicht freigegeben**. Weitere vier P-Motive haben Bildkandidaten aus dem Chat (NL/Murano/Jingdezhen/Barbados); technische und historische Abnahme offen.
- `approved_panorama_count=0`; `target_scenes=30`. Weder `scene_status=ready` noch Deployment oder Merge ohne Review.
- Kollegen-Branchnamen `colleague/T01-...` bzw. `colleague/E01-...`, Claude-Code-Branchnamen `claude/...`. Keine parallele direkte Änderung an `public/data/scenes.json` ohne Koordination.

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
