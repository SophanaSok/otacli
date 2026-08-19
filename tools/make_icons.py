from PIL import Image, ImageDraw

S = 1024          # supersample, downscaled at the end for smooth edges
BG      = (18, 22, 28, 255)
BAR     = (28, 34, 42, 255)
TEAL    = (79, 209, 197, 255)
TEXT    = (230, 237, 243, 255)
DOTS    = [(255, 95, 86, 255), (255, 189, 46, 255), (39, 201, 63, 255)]

img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(img)

R = int(S * 0.19)
d.rounded_rectangle([0, 0, S - 1, S - 1], radius=R, fill=BG)

# terminal title bar
bar_h = int(S * 0.19)
d.rounded_rectangle([0, 0, S - 1, bar_h + R], radius=R, fill=BAR)
d.rectangle([0, bar_h, S - 1, bar_h + R], fill=BG)

r = int(S * 0.028)
for i, c in enumerate(DOTS):
    cx = int(S * 0.10) + i * int(S * 0.085)
    d.ellipse([cx - r, bar_h // 2 - r, cx + r, bar_h // 2 + r], fill=c)

# prompt chevron
w = int(S * 0.055)
d.line([(int(S * 0.20), int(S * 0.42)), (int(S * 0.36), int(S * 0.60)),
        (int(S * 0.20), int(S * 0.78))], fill=TEAL, width=w, joint="curve")
for pt in [(0.20, 0.42), (0.36, 0.60), (0.20, 0.78)]:
    cx, cy = int(S * pt[0]), int(S * pt[1])
    d.ellipse([cx - w // 2, cy - w // 2, cx + w // 2, cy + w // 2], fill=TEAL)

# cursor block
d.rectangle([int(S * 0.46), int(S * 0.70), int(S * 0.80), int(S * 0.78)], fill=TEXT)

png = img.resize((512, 512), Image.LANCZOS)
png.save("icon_1.png")
img.resize((256, 256), Image.LANCZOS).save(
    "icon.ico", sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
print("wrote icon_1.png (512px) and icon.ico")
