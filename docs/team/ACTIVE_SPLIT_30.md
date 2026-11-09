# Aktive Teamaufteilung – 30 Szenen (Stand 09.11.2026)

**NEU: 16 Produktionsstätten (Nutzer) + 6 Handel-/Machtzentren (Kollege) + 8 historische Wendepunkte (Kollege) = 30.** Die frühere **30 ältere / 30 neuere** Aufteilung ist nicht mehr gültig.

| Zuständigkeit | Aktive IDs | Umfang | Liste |
|---|---|---:|---|
| Projektleitung / Nutzer | `P01–P16` | **16** | [USER_16_PRODUCTION.md](USER_16_PRODUCTION.md) |
| Kollege | `T01–T06` + `E01–E08` | **14** | [COLLEAGUE_14_SCENES.md](COLLEAGUE_14_SCENES.md) |

**Aktiver Gesamtplan:** [SCENE_MASTERPLAN_30.md](../SCENE_MASTERPLAN_30.md) · **Kollegen-Masterprompt:** [COLLEAGUE_MASTER_PROMPT_14.md](COLLEAGUE_MASTER_PROMPT_14.md) · **Manifest:** [ACTIVE_SCENES_30.json](ACTIVE_SCENES_30.json).

## Einfache parallele Zusammenarbeit

- Produktionsverantwortung ist nach **P/T/E-ID**, **nicht** nach Jahrgang verteilt.
- Jede Szene bekommt erst eine Quellen-Faktenkarte, dann eine geometrisch korrekte 3D-Umgebung, danach eine realistische 360°-Darstellung und QA.
- Stand: sieben bestehende Produktions-Bildkandidaten, **0/30 offizielle Freigaben**. Kein vorhandener 2:1-KI-Entwurf allein zählt als technisch fertige Kugel.
- **Projektleitung übernimmt fachliche Endabnahme und Merge**. Kollegenarbeiten auf `colleague/<ID>-...`-Branches, eigener PR mit QA-Bericht, keine eigenmächtigen Merges/Deployments. Szenen-JSON bleibt bis zum Review stabil.
- Urheber-/Lizenzstatus für historische Archivfotos und 3D-Assets prüfen. Keine tatsächlichen historischen Personen/Ereignisse als erfundene fotografische Aufnahmen ausgeben.
