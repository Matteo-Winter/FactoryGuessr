# Arbeitsaufteilung — Made in Time (60 Szenen, 2 Personen)

> **ARCHIV – NICHT MEHR AKTUELL (09.11.2026).** Dieses Dokument beschreibt den früheren **60er- bzw. 30/30-Plan** und ist **keine Arbeitsanweisung** für neue Bilder. Aktueller Umfang: **30 Szenen, 16 Produktionsstätten (Nutzer) + 6 Handelsorte und 8 Wendepunkte (Kollege)**. Siehe [aktiver Masterplan](../SCENE_MASTERPLAN_30.md) und [aktueller Kollegen-Prompt](COLLEAGUE_MASTER_PROMPT_14.md). Alte Nummern bleiben nur als Referenz erhalten.


**Stand: 09.11.2026.** Quelle: [60-Szenen-Masterplan](../SCENE_MASTERPLAN_60.md). Verbindliche Aufteilung nach **Zieljahr aufsteigend** und bei Jahrgleichheit nach bestehender Master-Nummer. Es wird nicht nach der Tabellenposition aufgeteilt, denn diese war innerhalb einiger Epochen nicht streng chronologisch.

| Bereich | Verantwortung | Anzahl | Zeitspanne | Verbindliche Liste |
|---|---|---:|---|---|
| Ältere 30 | Projektleitung (du) | 30 | 1660–1925 | [OLDER_30_LEAD.md](OLDER_30_LEAD.md) |
| Neuere 30 | Kollege | 30 | 1925–2023 | [NEWER_30_COLLEAGUE.md](NEWER_30_COLLEAGUE.md) |

**Grenzfall:** 1925 wird über den Master-Index aufgeteilt: **Nr. 32 Paris 1925** gehört zu „alt“, **Nr. 34 Brasilien 1925** zu „neu“. Keine Doppelarbeit. Mit dieser Regel gilt **genau 30 + 30, alle ursprünglichen 60 Szenen einmal**.

Gemeinsames Produktionsprotokoll: [PRODUCTION_PLAYBOOK_360.md](PRODUCTION_PLAYBOOK_360.md).

## Koordinationsregeln

1. **Scene-Lock:** Nur der zugewiesene Verantwortliche erzeugt/revidiert Bilder für seine Master-Nummern. Andere können QA/Review kommentieren. Freie gegenseitige Bildbearbeitung nur nach expliziter Übergabe.
2. **Stabile Nummern:** Original-Master-Nr. `01`–`60` nicht ändern. Bestehende Pilotszenen-IDs (Großbritannien 1840, Guatemala 1910, China 2015) bleiben erhalten.
3. **Einheitlicher Stil:** fotorealistisch, historisch informiert, ein Hauptprodukt, zwei Standort- und zwei Zeitsignale, keine Textspoiler, fixer räumlich konsistenter 360°-Kamerastandpunkt.
4. **Kandidat ≠ fertig:** Quellen, Geometrie, Naht, Pole, historische Plausibilität, Rechte und Browserprüfung separat dokumentieren. Offizielle Metadaten `approved_panorama_count=0` bleiben unangetastet, bis ein Review wirklich abgeschlossen ist.
5. **Versionskontrolle:** Bildquelle, 3D-Szene und QA als eigenständiges Paket. GitHub-Änderungen auf Feature-Branches, PR zur Abnahme; keine parallelen Änderungen an `public/data/scenes.json` ohne Koordination.
6. **Kein unnötiges Stoppen:** Bei eindeutigem mechanischem/Nahtfehler selbst weiterarbeiten und mindestens einen konkret geprüften Reparaturversuch durchführen. Niemals weichgeglättete Pixelwerte als Geometriebeweis ausgeben; offen dokumentieren, wenn eine Variante grundsätzlich nicht reparierbar ist.

**Nächste Arbeitsstarter:** Alt: Nr. 05 (Dhaka 1720, Musselin), wenn Nr. 01–04 fachlich endgültig geklärt sind. Neu: Nr. 34 (Brasilien 1925, Kaffee), um Szenenverfahren und Qualitätsmaßstab mit einem gut erkennbaren Produkt zu testen.
