# Recap para seguir en local: breakdown de Vanesa Martín en KaveLight

Este archivo recoge todo lo hecho en la sesión en la nube (2–9 nov 2026), para que una sesión de Claude Code **en el Mac** siga sin perder nada.

Repositorio: `soniathatsmyname-coder/claude`, rama `claude/sharp-euler-667ao9`, PR en borrador [soniathatsmyname-coder/claude#1](https://github.com/soniathatsmyname-coder/claude/pull/1). La carpeta `breakdown/` de esa rama es la que va a `/Volumes/A004/kave light/breakdown`.

---

## 1. Cómo arrancar la sesión local

1. Copia la carpeta `breakdown/` de la rama a `/Volumes/A004/kave light/breakdown`, o clona el repositorio en ese disco.
2. Abre el Terminal:
   ```bash
   cd "/Volumes/A004/kave light" && claude
   ```
3. Conecta en esa sesión el **mismo conector de KaveLight** que en la nube (`https://mcp.kavelight.com/mcp`). En la app: KaveLight abierto, con la misma cuenta y Controls ▸ AI Assistants activado.
4. Pide al empezar: *"Lee breakdown/RECAP_SESION_LOCAL.md y seguimos desde ahí."*
5. Para grabar la pantalla: Ajustes del Sistema ▸ Privacidad y seguridad ▸ Grabación de pantalla ▸ permitir el Terminal o la app de Claude.
   - Captura: `screencapture -x archivo.png`
   - Vídeo: `screencapture -v archivo.mov`
6. Opcional, para simular gestos de ratón: `brew install cliclick`. No está probado si KaveLight responde a arrastres simulados en el visor 3D.
7. Los scripts de `breakdown/scripts/` usan Python con Pillow (`pip3 install pillow`) y ffmpeg (`brew install ffmpeg`). Las fuentes son Inter: si no está en `/usr/share/fonts/...`, usa `FONT_DIR=/ruta/a/inter/ python3 scripts/rotular.py`.

---

## 2. El encargo (memoria de Sonia, resumida)

- **Entregables:** para KaveLight, 1 reel "previs vs final" y 2 stories.
  - El reel va en español con subtítulos en inglés.
  - KaveLight quiere también la versión en inglés para sus canales.
- **Es una reconstrucción y se dice así.** El plano se rodó sin KaveLight; nunca se presenta como previs hecha antes del rodaje.
- **Referencia:** "VANESA MARTIN 60S", minuto 01:29 (Vimeo de Sonia). 16:9, ProRes HQ 1080p25.
- **Plano:** Vanesa centrada de cuerpo entero, mono azul claro, manos en los bolsillos, sobre una isla de anthurium, gramíneas y rocas porosas.
  - El agua ocupa el tercio inferior y refleja las rocas.
  - Fondo negro, humo, cono desde arriba a la izquierda por detrás de la cabeza.
  - Tono frío cian, viñeta y grano. Bodegón de producto tipo Loewe.
- **Set real:** Radical Sonora (Madrid).
  - Plató de 19,3 × 7,8 m, con un ciclorama blanco de 6 m que no se usó.
  - Piscina negra de 4 × 5 m con 5 cm de agua, rodeada de cortinas negras.
  - Balconcillo a media altura, encima del catering.
  - Parrilla a unos 5 m; techo de unos 6 m (sin confirmar).
- **Cámara real:** casi a ras del agua (unos 30 cm), en el borde de la piscina opuesto al ciclorama. Cuerpo y óptica sin confirmar.
- **Luz real por capas:**
  1. **Contra:** spot colgado de la parrilla, por detrás de ella. Con humo marca el haz.
  2. **Spot desde el balconcillo:** apunta al agua delante de la isla. El óvalo rebota y le sube de frente con el temblor del agua: el **efecto aguas**. El óvalo se esconde tras un montículo de flores.
  3. **Fill pequeño a 45º:** sin confirmar.
  4. **Astera(s):** entre las flores.
- **Guion del reel** (borrador de Sonia, unos 60 s). Gancho: *"Así iluminamos a Vanesa Martín como si fuera un bodegón de producto"*.
  - El código de descuento va en el post y en una story, no en el reel.
  - Se publica con la etiqueta de colaboración pagada.
- **Pendientes del encargo:**
  - OK de derechos de la productora y del equipo de Vanesa.
  - Código de descuento y duración de la prueba con KaveLight.
  - Datos técnicos reales.
  - Versión en inglés.
- **Backstage (en el PC):** `Downloads/Fotos en iCloud.zip`.
  - IMG_5519 e IMG_5524: la contra.
  - IMG_5521 e IMG_5525: el haz del balconcillo y el óvalo.
  - IMG_5505 e IMG_5507: reflejo de la contra en el agua.
- **Planta aproximada:** `Documents/sonia-marca/kave/planta_luces_vanesa_aprox.html`

---

## 3. Estado actual de la escena en KaveLight

Proyecto **"Vanesa Martin test"**, archivo `/Volumes/A004/kave light/Vanesa Martin test.cineviz`, escena "1 INT. STAGE - NIGHT".

Convenciones de KaveLight: metros, +Y arriba, suelo y = 0. Cámara a +Z mirando a −Z; izquierda de cuadro = −X. La superficie del agua está en y ≈ 0,10.

### Cámara (id `FC9665A7-7B14-4068-B970-5F9E87969045`)
- Blackmagic Pocket Cinema Camera 6K, 6K 16:9, **20 mm**, T2.0, ISO 800, 180°, **25 fps**, ND 3.0, balance 4300 K, exposición manual.
- Posición **(0, 0,43, 4,04)**, apuntando al punto **(0, 0,976, −0,118)**. Foco: sigue a la Actriz.
- **Encuadre del plano.** Para volver a él: `move_node` a esa posición, `aim_at` a ese punto y `set_camera` con 20 mm, T2.0, ND 3.0 y `focus_on` la Actriz.

### Luces

| Capa | Nombre en KaveLight | id | Aparato real o rótulo | Posición | Ajuste |
|---|---|---|---|---|---|
| 01 Contra | Aputure LS 600d Pro (LED) | `296057D7-30AD-448F-8290-F6A6B63C296C` | Aputure 600d Pro + viseras F10 + ¼ CTB + marco de difusión LEE 250 | (−0,82, 4,58, −3,33), colgado de la parrilla | 84 %, 5600 K, haz 45° |
| 02 Spot del balconcillo | amaran 300c | `34C0DDF9-36B5-4BF7-B10F-CAAC7C701CBB` | **Rótulo: Aputure F22c** (por la lista de gaffer de Sonia) | (−3,30, 4,51, 4,70), en el balconcillo | 6 %, 5600 K, Spotlight Mount 19° |
| 03 Rebote (efecto aguas simulado) | Aputure LS 600d Pro (LED) | `3AA0D846-22BF-403D-A1E1-89243E39207F` | 600d + Spotlight Mount II 19° + marco de difusión LEE 216 | (−2,25, 0,41, 2,00), rasante delante a la izquierda | 7 %, 5600 K |
| 04 Panel cenital | TOPLIGHT (tipo Aputure F22) LiteMat 2 | `91BF418A-DD91-41AA-936E-B54AFFD372F3` | LiteGear LiteMat 2 + SnapGrid 40° | (−1,61, 4,66, 0,80) | 43 %, 5600 K |
| 05 Astera A | Raseo plantas Titan | `00B8DA91-4C85-4614-AE61-4053899CCD28` | Astera Titan + SnapBag | (−2,45, 0,43, 1,39) | 73 % |
| 06 Astera B | Raseo plantas Titan | `99A05384-3971-456B-AA7A-F845842A4331` | Astera Titan + SnapBag | (−1,95, 0,83, 3,21) | 17 % |
| Humo | (atmósfera) | — | Haze | — | densidad 0,17, anisotropía 0,46 |

Lecturas del fotómetro en la cara, cada luz sola:

| Luz | Lux en la cara |
|---|---|
| Contra | 3373 |
| Rebote | 1229 |
| Panel | 100 |
| Astera A | 19 |
| Astera B | 2,8 |
| Spot | 0 directos (va al agua) |

### Set (lo que no es arte)
- **Suelo:** `0C27BE05…`, 7,8 × 19,3 m.
- **Paredes:** "Fondo negro" `065C1173…` (es el ciclorama, pintado blanco #f4f4f2), "Lateral izq negro" `2AC96829…`, "Lateral dcha negro" `63C4D0C2…`.
- **Cortina negra del fondo:** `239EDF0E…`, tapa el ciclorama.
- **Ocultos por Sonia:** pared frontal `2768A95A…`, cortinas laterales `BCC2080E…` y `4CB28F22…`, techo `E02D92B5…`.
- **Balconcillo:** prop construido `DBD37CE8…`, a 3 m de altura, pared izquierda.
- **Parrilla:** prop construido `59B0B768…`, a unos 5 m.

### Arte y figura
- **Charca 5 cm:** `FF6F05CA…`, de 4 × 5 m, estirada a 5,6 m en z por Sonia.
  - Liner negro y agua "Pool Water" con tinte #05080a.
  - Encima, tres discos de **ondas** modeladas (perfil lathe, 2–3 mm de alto): A `16FA842B…`, B `3393BCC5…` y C `3303112C…`. El generador está en `scripts/ripples.py`.
- **Practicable bajo la figura:** `E32091CE…`.
- **Rocas:** `C5374F77…`, `507086CC…`, `0296DA6B…`, `F4C7C340…`.
- **Plantas:** `46EA1766…`, `40DD8812…`, `988D6A5B…`, `31A911DD…`, `52C00073…`, `F84BB74E…`, `91B85439…`, `5ADF614D…`, `16048344…`.
- **Actriz:** `3C54F509-B6BF-4DC3-B1BA-8E94B566D043`.
  - Personaje Margot, pose "Hands in Pockets", mirando hacia abajo a la izquierda.
  - Sudadera y vaquero en chambray #aebdc8, botas marrones, pelo castaño oscuro. No hay mono en el vestuario y el moño no se puede cambiar.

---

## 4. Lo que ya está hecho (en `breakdown/`)

| Carpeta | Contenido |
|---|---|
| `01_capas_camara/raw/` | Desde la cámara del plano, 1920×1080 path-traced, todas con la **misma exposición**: `00_frame_final`; cada luz sola, **sin humo** (`01`–`06`); capas sumándose **sin humo** (`B1`–`B5`) y `B6` = + humo = frame final. |
| `01_capas_camara/rotuladas/` | Lo mismo con rótulo mínimo, como pidió Sonia: **solo la línea del aparato y la de cámara**. Las Astera llevan además versiones con realce (+2 y +3 EV). |
| `02_angulos_set/` | A general de producción · B 3/4 desde el balconcillo · C contraplano hacia el balconcillo · D cenital desde la parrilla · E lateral a ras de agua · F detalle de la contra en la parrilla · G detalle del 600d de rebote con la Astera · I agua de cerca. Exposición T5.6 sin ND, equivalente a la del plano. |
| `03_metadatos/` | `ficha_tecnica_luces.png` y `planta_cenital_kavelight.png`. La planta es **solo luces, cámara y cotas**: el arte y Vanesa se ocultaron solo para sacarla. |
| `04_clips/` | `clip4_capas_encendiendose` (limpio y rotulado, fundidos) · `clip2_travelling_rasante_hasta_el_plano` (12 renders + interpolación de movimiento con ffmpeg, acaba en el frame final HQ). |
| `scripts/` | `rotular.py` (rótulos), `ficha.py` (ficha técnica), `capas_clip.sh` (clip de fundidos), `ripples.py` (perfil de ondas), `cells.py` (gobo de celdas; descartado). |

En los Frames de KaveLight solo está guardado **"BRK 00 Frame final (todas + humo)"**, en borrador (se termina con Frames ▸ Refine).

---

## 5. Decisiones y aprendizajes (para no repetir pruebas)

- **El efecto aguas real no se puede simular en KaveLight.** Se probaron tres cosas, sin efecto visible en Vanesa:
  - el spot rebotando en el agua: el path tracer no saca cáusticas;
  - un parche de acero o blanco en el agua;
  - un gobo de celdas (`cells.py`): la sombra sale demasiado difusa.
  
  **Decisión:** en KaveLight se enseña la geometría (spot del balconcillo → óvalo → rebote) y el nivel con el 600d rasante. El temblor se cuenta con el plano real, o con CC Caustics en After Effects sobre el render, marcado como simulado.
- **Ondas:** las ondas modeladas sí rompen el reflejo de forma realista (discos lathe sobre el agua negra). "Sea Water" sale azul de mar; se descartó.
- **Rótulos:** el amaran 300c se rotula como **Aputure F22c** (lista de gaffer). El panel cenital se rotula "LiteGear LiteMat 2", sin mencionar el F22.
- **Humo:** en las capas va apagado y se enciende solo en el último paso, por decisión de Sonia.
- **Óptica:** con la Pocket 6K (APS-C) y la cámara en el borde de la piscina hacen falta unos 18–20 mm para que Vanesa entre entera y el agua ocupe el tercio inferior.
- **Límites de las herramientas de KaveLight:**
  - `render_monitor` llega como máximo a 1920 px y unas 256 muestras.
  - A veces devuelve el render anterior en caché: repetir la llamada.
  - Hubo errores 502 temporales: esperar unos 60 s.
  - No hay herramienta para la falsa color, ni para animar la cámara, ni para elegir marcas de ópticas.
  - `add_grip` no deja elegir el dibujo del cookie.
- **Sonia edita la escena en paralelo.** Releer siempre con `get_scene` antes de tocar nada y no pisar sus cambios. Si un frame guardado está en previsualización en Frames, KaveLight bloquea las ediciones.

---

## 6. Pendiente: lo que la sesión local tiene que hacer

### A. Grabaciones de pantalla "orgánicas" de la interfaz (lo que pidió Sonia)
Grabar con `screencapture -v`. Claude cambia la escena con las herramientas de KaveLight; Sonia, o `cliclick` si funciona, hace los gestos de ratón. Guardar en `breakdown/05_pantalla/`.

1. **Moverse por el set:** órbita lenta del visor 3D alrededor de la isla, el balconcillo y la parrilla.
2. **Luces una a una:** todo apagado y, una a una, contra → spot → rebote → panel → Astera A y B → humo. Antes de encender cada luz, `select_nodes` para que se abra su panel.
3. **Tocar una luz:** con la contra seleccionada, subir y bajar la salida, la temperatura y la apertura del haz, y quitar y poner el ¼ CTB. Al final, devolver los valores de la tabla de arriba.
4. **Cámara:** cambiar la óptica de 20 a 35 mm y volver, cambiar el T-stop, poner la guía 2.39 (`set_camera frame_guide`) y quitarla. Enseñar el selector de cuerpos.
5. **Falsa color y fotómetro:** solo desde la interfaz (Monitor). Lo activa Sonia, o `cliclick`.
6. **Planta:** vista Overhead y zoom a las luces.
7. *(Opcional)* **"Montamos el set desde cero":** escena nueva "BUILD FROM 0" en el mismo proyecto, añadiendo pieza a pieza mientras se graba, sin tocar la escena base.

### B. Otros pendientes
- Guardar el proyecto (⌘S).
- Terminar con Refine el frame "BRK 00".
- Si se quieren, añadir a Frames las capas como "BRK 01…06".
- Rotular la planta con los nombres de la lista de gaffer (F22c en el spot), si Sonia lo pide.
- Clips que quedaron sin hacer: órbita (render a render) y grúa desde la parrilla. Probablemente los sustituyen las grabaciones de pantalla.
- Fill a 45º de la memoria: no está montado porque faltan datos.
- PR #1: está en borrador; se sigue actualizando en la misma rama.

---

## 7. Mensaje para pegar al abrir la sesión local

> Estamos en "/Volumes/A004/kave light". Lee `breakdown/RECAP_SESION_LOCAL.md`: es el traspaso de una sesión anterior en la nube sobre el breakdown de Vanesa Martín en KaveLight (proyecto "Vanesa Martin test"). Comprueba primero que el conector de KaveLight responde (`list_projects`) y relee la escena con `get_scene` sin cambiar nada. Después vamos con el punto 6A: grabaciones de pantalla de la interfaz, toma a toma. Yo te digo "siguiente". Guarda todo en `breakdown/05_pantalla/`.
