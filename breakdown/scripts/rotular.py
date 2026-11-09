"""Rotula las capas del breakdown de Vanesa Martín (lower third + ficha técnica)."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "01_capas_camara")
RAW = os.path.join(BASE, "raw")
OUT = os.path.join(BASE, "rotuladas")
os.makedirs(OUT, exist_ok=True)

F = os.environ.get("FONT_DIR", "/usr/share/fonts/opentype/inter/")  # en Mac: carpeta con las .otf de Inter
f_tag = ImageFont.truetype(F + "Inter-SemiBold.otf", 22)
f_title = ImageFont.truetype(F + "InterDisplay-Bold.otf", 54)
f_line = ImageFont.truetype(F + "Inter-Medium.otf", 28)
f_small = ImageFont.truetype(F + "Inter-Regular.otf", 22)

CAM = "Cámara: Blackmagic Pocket 6K · 20 mm · T2.0 · ISO 800 · ND 3.0 · 4300 K · 25 fps"
TAG = "RECONSTRUCCIÓN EN KAVELIGHT"

L = {
    "contra": ("CONTRA", "Aputure LS 600d Pro · viseras F10 · ¼ CTB · 84 % · 5600 K",
               "Colgado de la parrilla a 4,6 m, detrás de Vanesa · recorta pelo y hombros, marca el haz con humo"),
    "spot": ("SPOT BALCONCILLO", "Aputure F22c · 5600 K",
             "Desde el balconcillo a 4,5 m, izquierda de cámara · dibuja el óvalo en el agua delante de la isla"),
    "rebote": ("REBOTE · EFECTO AGUAS (simulado)", "Aputure LS 600d Pro · Spotlight Mount II 19° · 7 % · 5600 K",
               "Rasante a 0,4 m, delante a la izquierda · hace de la luz que sube del agua a Vanesa"),
    "panel": ("PANEL CENITAL", "LiteGear LiteMat 2 · SnapGrid 40° · 43 % · 5600 K",
              "A 4,7 m sobre la isla · sube el nivel general de forma suave"),
    "asteraA": ("ASTERA A", "Astera Titan Tube · SnapBag · 73 % · 5600 K",
                "Escondida entre las flores a 0,4 m · baña el bodegón"),
    "asteraB": ("ASTERA B", "Astera Titan Tube · SnapBag · 17 % · 5600 K",
                "Primer término izquierda a 0,8 m · separa las plantas del negro"),
    "humo": ("HUMO", "Haze al 17 %", "Hace visible el haz de la contra y une todas las capas"),
}

JOBS = [
    # archivo raw, salida, etiqueta capa, clave, realce EV
    ("00_frame_final.jpg", "00_frame_final.jpg", "FRAME FINAL", None, 0),
    ("01_contra_solo.jpg", "01_contra_solo.jpg", "LUZ 1 SOLA", "contra", 0),
    ("02_spot_balconcillo_solo.jpg", "02_spot_balconcillo_solo.jpg", "LUZ 2 SOLA", "spot", 0),
    ("03_rebote_solo.jpg", "03_rebote_solo.jpg", "LUZ 3 SOLA", "rebote", 0),
    ("04_panel_cenital_solo.jpg", "04_panel_cenital_solo.jpg", "LUZ 4 SOLA", "panel", 0),
    ("05_astera_A_solo.jpg", "05_astera_A_solo.jpg", "LUZ 5 SOLA", "asteraA", 0),
    ("05_astera_A_solo.jpg", "05b_astera_A_solo_realce+2EV.jpg", "LUZ 5 SOLA · REALCE +2 EV", "asteraA", 2),
    ("06_astera_B_solo.jpg", "06_astera_B_solo.jpg", "LUZ 6 SOLA", "asteraB", 0),
    ("06_astera_B_solo.jpg", "06b_astera_B_solo_realce+3EV.jpg", "LUZ 6 SOLA · REALCE +3 EV", "asteraB", 3),
    ("B1_contra.jpg", "B1_capa1_contra.jpg", "CAPA 1", "contra", 0),
    ("B2_contra+spot.jpg", "B2_capa2_+spot.jpg", "CAPA 2 · +", "spot", 0),
    ("B3_contra+spot+rebote.jpg", "B3_capa3_+rebote.jpg", "CAPA 3 · +", "rebote", 0),
    ("B4_+panel_cenital.jpg", "B4_capa4_+panel.jpg", "CAPA 4 · +", "panel", 0),
    ("B5_+asteras_todas_sin_humo.jpg", "B5_capa5_+asteras.jpg", "CAPA 5 · +", "asteraA", 0),
    ("B6_+humo_frame_final.jpg", "B6_capa6_+humo_frame_final.jpg", "CAPA 6 · +", "humo", 0),
]


def render(src, dst, tag, key, ev):
    im = Image.open(os.path.join(RAW, src)).convert("RGB")
    if ev:
        im = ImageEnhance.Brightness(im).enhance(2 ** ev)
    W, H = im.size
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    # banda inferior degradada
    band = 190
    for i in range(band):
        a = int(200 * (i / band) ** 1.4)
        d.line([(0, H - band + i), (W, H - band + i)], fill=(0, 0, 0, a))
    im = Image.alpha_composite(im.convert("RGBA"), ov)
    d = ImageDraw.Draw(im)
    x = 70
    if key is None:
        l1 = "Contra · spot balconcillo · rebote · panel cenital · 2 × Astera · humo"
    else:
        name, l1, l2 = L[key]
        if key == "asteraA" and tag.startswith("CAPA 5"):
            l1 = "2 × Astera Titan Tube · SnapBag · 73 % y 17 % · 5600 K"
    d.text((x, H - 112), l1, font=f_line, fill=(235, 238, 242))
    d.text((x, H - 62), CAM, font=f_small, fill=(165, 170, 175))
    im.convert("RGB").save(os.path.join(OUT, dst), quality=95)


for j in JOBS:
    if os.path.exists(os.path.join(RAW, j[0])):
        render(*j)
        print("ok", j[1])
    else:
        print("falta", j[0])
