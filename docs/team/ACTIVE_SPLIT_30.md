# Aktuelle Bildproduktion – 11 akzeptiert, 6 neu, 13 offen

**Stand: Bildprüfung des Nutzers vom 09.11.2026.** Der historische Umfang bleibt **30 Level = 16 Produktionsorte, 6 Handelsorte, 8 Wendepunkte**.

| Bildstatus | Anzahl | Aufgabe |
|---|---:|---|
| **Passt** (visuelle Auswahl) | **11** | Originaldatei sichern; separater 360°-/Historien-/Browser-QA noch offen |
| **Neu machen** | **6** | Diese sechs Bildversionen neu erzeugen; Szenen/IDs unverändert |
| **Kein Urteil im aktuellen Review** | **13** | Vorhandenes Bild zur Prüfung geben oder neues mit Gemini erzeugen |
| **Formal im Spiel freigegeben** | **0** | Keine stillschweigende `ready`-Markierung |

**Der Kollege mit Gemini bearbeitet die **19 offenen aktiven Punkte**: sechs Remakes plus 13 unbeurteilte Szenen.** Projektleitung/Nutzer wählt und beurteilt Ergebnisse für alle 30. Kein neuer 16/14-Aufgabensplit für die Bildgenerierung.

**[Aktuelle 30er-Bildliste mit exakten Dateinamen](../IMAGE_PRODUCTION_STATUS_30.md)** · **[Gemini-Auftrag](GEMINI_IMAGE_HANDOFF_CURRENT.md)** · **[Szenenstatus als JSON](ACTIVE_SCENES_30.json)** · **[GitHub Issue #18](https://github.com/Matteo-Winter/FactoryGuessr/issues/18)**.

- Die drei bereits vorhandenen technischen Pilot-IDs `gb-1840-textile-mill`, `gt-1910-banana-packing`, `cn-2015-electronics-assembly` gehören zu P05/P09/P13 und werden nicht doppelt gezählt.
- Kanton `review-perlfluss-alternative.png` ist die zweite akzeptierte Variante **desselben Levels T04**, kein zusätzliches Level. Die abgelehnte Murano-Kollegenfassung ändert nicht die positive P02-Hauptversion.
- Sonstige bewertete Motive außerhalb des aktiven 30er-Plans **nicht** als neue Szenen anlegen.
- **"Passt" = Nutzerurteil zur Bildwirkung**, nicht formaler Geometrie-/Quellen-/Lizenz-PASS. Die hier genannten Dateinamen sind nicht automatisch als Originalbilder in GitHub verfügbar.
- Feature-Branch/PR für Integration; kein eigenständiger Merge/Deployment; `public/data/scenes.json` bleibt `approved_panorama_count=0` bis Abnahme.
