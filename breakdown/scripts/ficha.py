"""Ficha técnica del set (PNG 1920x1080) para el breakdown."""
import os
from PIL import Image, ImageDraw, ImageFont

F = os.environ.get("FONT_DIR", "/usr/share/fonts/opentype/inter/")  # en Mac: carpeta con las .otf de Inter
f_h1 = ImageFont.truetype(F + "InterDisplay-Bold.otf", 52)
f_h2 = ImageFont.truetype(F + "Inter-SemiBold.otf", 26)
f_row = ImageFont.truetype(F + "Inter-Medium.otf", 25)
f_sm = ImageFont.truetype(F + "Inter-Regular.otf", 21)

W, H = 1920, 1080
im = Image.new("RGB", (W, H), (12, 14, 16))
d = ImageDraw.Draw(im)
x0 = 90
d.text((x0, 70), "VANESA MARTÍN · FICHA DE LUZ", font=f_h1, fill="white")
d.text((x0, 140), "Reconstrucción en KaveLight · plató negro con charca de 5 cm · Radical Sonora (Madrid)",
       font=f_sm, fill=(150, 156, 162))

cols = [x0, x0 + 90, x0 + 470, x0 + 1100, x0 + 1420]
heads = ["#", "CAPA", "APARATO · MODIFICADOR", "POSICIÓN", "SALIDA · K"]
y = 220
for c, h in zip(cols, heads):
    d.text((c, y), h, font=f_h2, fill=(120, 190, 210))
y += 50
d.line([(x0, y), (W - x0, y)], fill=(50, 55, 60), width=2)
rows = [
    ("01", "Contra", "Aputure LS 600d Pro · viseras F10 · ¼ CTB", "Parrilla 4,6 m · detrás", "84 % · 5600 K"),
    ("02", "Spot balconcillo", "Aputure F22c", "Balconcillo 4,5 m · izq.", "5600 K"),
    ("03", "Rebote (efecto aguas)", "Aputure LS 600d Pro · Spotlight Mount II 19°", "Rasante 0,4 m · izq.", "7 % · 5600 K"),
    ("04", "Panel cenital", "LiteGear LiteMat 2 · SnapGrid 40°", "4,7 m sobre la isla", "43 % · 5600 K"),
    ("05", "Astera A", "Astera Titan Tube · SnapBag", "Entre flores 0,4 m", "73 % · 5600 K"),
    ("06", "Astera B", "Astera Titan Tube · SnapBag", "1.er término 0,8 m", "17 % · 5600 K"),
    ("—", "Humo", "Haze", "Todo el plató", "17 %"),
]
y += 22
for r in rows:
    for c, t in zip(cols, r):
        d.text((c, y), t, font=f_row, fill=(230, 233, 236) if c != cols[0] else (120, 190, 210))
    y += 58
d.line([(x0, y), (W - x0, y)], fill=(50, 55, 60), width=2)
y += 40
d.text((x0, y), "CÁMARA", font=f_h2, fill=(120, 190, 210))
d.text((x0 + 200, y), "Blackmagic Pocket 6K · 20 mm · T2.0 · ISO 800 · ND 3.0 · 4300 K · 25 fps · a 30 cm del agua",
       font=f_row, fill=(230, 233, 236))
y += 55
d.text((x0, y), "GRIP", font=f_h2, fill=(120, 190, 210))
d.text((x0 + 200, y), "2 × marco de difusión 18×24 · cortinas negras alrededor de la charca · parrilla a 5 m",
       font=f_row, fill=(230, 233, 236))
y += 55
d.text((x0, y), "SET", font=f_h2, fill=(120, 190, 210))
d.text((x0 + 200, y), "Plató 7,8 × 19,3 m · charca negra 4 × 5 m con 5 cm de agua · balconcillo a 3 m",
       font=f_row, fill=(230, 233, 236))
d.text((x0, H - 70), "El efecto aguas real lo hace el rebote del spot en el agua; en KaveLight se simula con un foco rasante.",
       font=f_sm, fill=(130, 136, 142))
im.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "03_metadatos", "ficha_tecnica_luces.png"))
print("ok")
