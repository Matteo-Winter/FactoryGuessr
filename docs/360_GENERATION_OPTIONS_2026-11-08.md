# 360°-Panoramen: Anbieterentscheidung und Validierungsplan

Stand: **08.11.2026**. Status: **Research / 0 von 60 Freigaben**. Dies ist keine Bestätigung, dass ein Anbieter für unsere Szenen bereits erfolgreich getestet wurde.

## Ausgangslage

Der bestehende Viewer ist funktionsfähig; PR #2 ist auf `main` gemergt. Die drei KI-JPGs sind jeweils 1774×887 px, **keine** korrekt nachgewiesenen equirectangularen Panoramen. Sichtbare Farb-/Geometriesprünge an der L/R-Naht und problematische Pole.

Eigener reproduzierter Baseline-Befund mit `scripts/check_panorama.py` (Werte sind MAE der RGB-Kanäle, nicht semantische Bildqualität; 5 % der Bildhöhe oben/unten aus Nahtwert ausgeschlossen):

| Szene | Bildgröße | Naht/gewöhnliche Nachbarspalten | Ergebnis |
| --- | --- | ---: | --- |
| Großbritannien 1840 | 1774×887 | 2.937× | Nahtwarnung, unter 4K |
| Guatemala 1910 | 1774×887 | 2.367× | Nahtwarnung, unter 4K |
| China 2015 | 1774×887 | 1.844× | Nahtwarnung, unter 4K |

**Vorsicht:** Ein niedriger Messwert beweist keine korrekte Panorama-Projektion, insbesondere nicht am Zenit/Nadir. Die aktuelle QA markiert niemals Bilder automatisch als freigegeben.

## Kandidaten (Fakten laut Anbieter- und Projektquellen)

### 0 — PanoPulse (kostenloser Vorabtest vor einem Abo)

**Neu geprüft am 08.11.2026.** PanoPulse wirbt mit Text-/Bild-zu-360° und equirectangularem Export sowie *25 kostenlosen Generierungen bei Registrierung, ohne Kreditkarte oder Wasserzeichen*. Die Generatoroberfläche zeigt jedoch **3 Credits pro Aufruf**, während die FAQ von 25 **Generierungen** spricht: Wie diese beiden Angaben zusammenpassen, ist **nicht verifiziert**. Die Tarifseite nennt Basic **$14.90/Monat mit 4K und 1000 Credits**, aber eine **4K-Exportberechtigung im Gratis-Konto ist nicht klar belegt**. Keine Aussage über einen kostenlosen 4K-Export treffen, bevor er tatsächlich heruntergeladen und gemessen wurde.

Der Dienst ist jünger, mit wenig belastbarer unabhängiger QA. Seine AGB garantieren ausdrücklich **weder Bildqualität noch nahtlose Projektion**, und Uploads/Ergebnisse können durch externe Dienstleister verarbeitet werden. Deshalb: nur einen **nicht vertraulichen Textprompt** testen, keine historischen Fremdbilder/privaten Daten hochladen. Ohne Nutzungsbedingungen/Ausgaberechte und 4K-Datei bleibt der Test **unveröffentlicht und ungeprüft**. Claude erstellt keine Accounts ohne direkte Nutzeraktion und autorisiert **keine Zahlung**.

Vorgeschalteter No-Cost-Test: im öffentlichen Generator prüfen, ob Registrierung notwendig ist; bei Zugang genau **eine** britische Textilmühle aus dem bestehenden Briefing als Text-to-360 generieren und, falls kostenlos erlaubt, als Original-equirectangular JPG/PNG exportieren. Falls kostenlos **kein** Export möglich ist: stoppen und Skybox Standard als bevorzugte bezahlte Alternative empfehlen. Das Design-/Qualitätsgate bleibt unverändert.

Quellen:
- https://panopulse.com/
- https://panopulse.com/panorama
- https://panopulse.com/panorama/pricing
- https://panopulse.com/terms

### A — Skybox AI, Blockade Labs (bevorzugter **bezahlter** Praxisversuch)

- **Modell 4:** nativer 360°-Skybox-Export **4096×2048**, Standard = **3 Credits** pro Bild, Enhanced = **6 Credits**; nur Standard- oder Business-Abo. Modell 4 unterstützt 1K/2K/4K-Exporte, **keinen nativen 8K-Export**. Modell-3-Ausgabe dagegen **8192×4096**, **1 Credit** pro Bild. *Mehr Pixel = nicht automatisch bessere Bildgestaltung.*
- **Image2Pano:** Seit **13.10.2026** in aktueller **Staging-Dokumentation** erwähnt; Model 4, 3 Credits, Eingabe `image_to_pano_init_image`; `variant_id` darf dabei nicht mitgegeben werden. Produktwebsite bewirbt Image2Pano als verfügbar. **Vor API-Nutzung in Live-Konto/API verifizieren**, ob Feature und Parameter in Production tatsächlich freigeschaltet sind; Produktions-Changelog kann nachhinken.
- **API:** `POST https://backend.blockadelabs.com/api/v1/skybox` mit `skybox_style_id`, `prompt`, optional `negative_text`; Bild über `file_url` nach `complete`. Style und `max-char` müssen über `GET .../skybox/styles?model_version=4` abgefragt werden; keine Style-ID blind festschreiben. API-Key als `x-api-key` nur lokal/serverseitig, niemals als URL oder ins Repo.
- **Veröffentlichte Monatspläne:** Essential $24 / 100 Credits, Standard $60 / 300 Credits, Business $140 / 500 Credits (bei monatlicher Abrechnung; Anbieter zeigt daneben jährliche Preise, $48 Standard monatliches Äquivalent bei Jahreszahlung). **5 kostenlose Credits sind nur für Vorschau und erlauben keinen Export**; Model 4 ist auf Free/Essential nicht verfügbar. Alle Preise USD ohne Steuer/Wechselkurs; vor Kauf erneut prüfen.
- **Rechenbeispiel für genau 60 Szenen:** 60 × 3 = **180 Credits**, falls jede Model-4-Standard-Generierung im ersten Versuch nutzbar ist; bei 2 Versuchen/Szene **360 Credits**, bei 3 Versuchen **540 Credits**. *Es gibt keine belastbare Aussage, wie viele Versuche für einen qualitativ guten Raum nötig sein werden.* 300 Credits reichen also nur für 100 Standard-Versuche, nicht für unbegrenzte Überarbeitungen. Monatspauschale und mögliche Ablauffristen/Steuern separat beachten.
- Planseite verspricht kommerzielle Rechte; Anbieterbedingungen und eventuelle Rechte Dritter/Referenzbilder müssen dennoch geprüft werden. Kein automatisches Veröffentlichen einer wissenschaftlichen Vergleichsstudie zu Anbietern, ohne deren Bedingungen zu beachten.

Quellen:
- https://docs.blockadelabs.com/api/skybox.html
- https://docs.blockadelabs.com/api/skybox-exports.html
- https://docs-staging.blockadelabs.com/api/changelog.html
- https://docs-staging.blockadelabs.com/api/skybox.html
- https://www.blockadelabs.com/model-4
- https://skybox.blockadelabs.com/plans
- https://www.blendbox.ai/terms-of-service

### B — PanFusion (offener Forschungsweg)

- CVPR 2024: *Taming Stable Diffusion for Text to 360° Panorama Image Generation*, eigens für 360° und verzerrungsbewusst entwickelte Diffusionsarchitektur, inklusive Room-Layout-Constraints.
- GitHub: Code unter **MIT-Lizenz**. Conda/PyTorch-Setup mit Checkpoints und Forschungs-Abhängigkeiten. Gewichte, Trainingsdaten und deren Nutzungsbedingungen gesondert vor praktischer Anwendung prüfen.
- Für einen zeitkritischen WU-Prototyp ist Reproduzierbarkeit auf einem durchschnittlichen MacBook Air **noch nicht belegt**. Keine Behauptung, dass das Modell mit vorhandener Mac-GPU/Arbeitsspeicher in vernünftiger Zeit läuft. Aufwand für Setup und Qualitätstuning kann größer sein als ein kleiner kommerzieller Pilot.

Quellen:
- https://github.com/chengzhag/PanFusion
- https://github.com/chengzhag/PanFusion/blob/main/LICENSE
- https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Taming_Stable_Diffusion_for_Text_to_360_Panorama_Image_Generation_CVPR_2024_paper.html

### C — MVDiffusion (offenes Image-to-Panorama-Outpainting)

- NeurIPS 2023: Multi-View-Generation; Repo beschreibt ausdrücklich das Outpainting eines **einzelnen Perspektivbildes** zur 360°-Panoramaansicht. Code laut Projekt-README MIT.
- Eher Forschungs-Baseline für die Frage, wie eine existierende Fabrikansicht räumlich erweitert werden kann. Nicht als verlässlich laufende Plug-and-Play-App auf unserem Mac bestätigt; Setup, Gewichte, Ressourcen und Lizenzbedingungen prüfen.

Quelle: https://github.com/Tangshitao/MVDiffusion

## Vorgeschlagene Versuchsanordnung

1. **Ohne Zahlung vorprüfen:** PanoPulse-Selbstaussagen zu Gratis-Generierung, Export und Auflösung praktisch bestätigen; nur wenn eine echte herunterladbare 4K-Datei vorliegt, mit unserem QA-Gate bewerten. Ansonsten **keinen Schein-PASS** aus einem Browser-Preview ableiten.
2. **Bezahlte Alternative bei ungenügendem Gratis-Test und nach ausdrücklicher Budgetfreigabe:** `gb-1840-textile-mill` als Text-to-360 über Skybox Model 4 Standard (nicht die alten fehlerhaften 2:1-Panoramen als vermeintlich korrekte `init_image` benutzen).
3. Optional ein Model-3-Panorama desselben Briefings als günstigere 8K-Baseline (nur wenn im Account erlaubt und nach Kostenfreigabe).
4. Optional **Image2Pano** aus einem *gewöhnlichen perspektivischen Foto* (nicht dem alten 2:1-Weitwinkelbild) testen, wenn historische Referenztreue wichtiger als reine sphärische Qualität ist. Vorher verfügbare Produktionsfunktion prüfen.
5. **Echte heruntergeladene Bilddatei** unabhängig prüfen:
   - Pixelgröße, equirectangular 2:1.
   - `python3 -m pip install -r requirements-qa.txt` und `python3 scripts/check_panorama.py <pfad> --json`.
   - Pannellum-Rundblick **360°**, Naht bei `±180°`, Zenit `+90°`, Nadir `-90°`, vier Queransichten, Maschinen-/Arbeiterverzerrungen und historischen Realismus *manuell* kontrollieren.
   - Ergebnisdatei, Prompt, Modell/Style, Seed, Ausgabedatum, Ausgaben/Credits, Nutzungsrechte und 6 Screenshots als Nachweis in privater Arbeitsdokumentation speichern.
6. Nur nach **visuell bestätigter Qualitätsprüfung** Status `ready`; bis dahin `approved_panorama_count=0`.

### Historisches Text-zu-360-Briefing, Pilot Großbritannien ca. 1840

**Prompt (unter 1000 englische Zeichen, vor Nutzung in Style-Template-Limit prüfen):**

```text
Historically plausible reconstruction of a cotton textile mill in industrial Britain circa 1840, viewed at adult eye height from the center of a long factory floor. Coherent continuous 360-degree indoor environment: massive brick mill walls, tall multi-pane windows, cast iron columns, overhead line shafts and leather transmission belts driving period-correct cotton spinning and power-loom machinery. Rows of wooden and iron machines, working women and men in practical 1840s clothing, cotton dust in shafts of muted daylight, worn plank floors. Authentic industrial scale and believable geometry from every direction. A single camera position in a real enclosed room, continuous ceiling and floor. Natural realism, not fantasy or steampunk.
```

**Negative prompt:**

```text
modern electricity, electric motors, fluorescent lamps, plastic, computers, robots, forklifts, safety posters, legible signs, dates, flags, company logos, futuristic architecture, impossible machines, multiple horizons, cut-open building, discontinuous seam, warped floor, fisheye collage
```

*Beide Prompts sind eine Ausgangshypothese; das später gewählte Style-Template kann andere maximale Zeichenlängen haben.*

## Nicht-Ziele

- Keine direkte Lizenz-/Preisfreigabe, kein API-Token im Repo, **keine kostenpflichtige Generierung ohne Nutzerentscheidung**.
- Kein Fake-"Street-View-Gehen" aus einer einzelnen 360°-Textur: echte Ortswechsel erfordern mehrere durch Hotspots verbundene Panoramen oder ein geometrisch konsistentes 3D-Modell.
- Nicht 60 halbgare Bilder erzeugen; ein bestandenes Qualitätsgate vor Skalierung.
