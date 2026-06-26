"""
generate_favicons.py
Copies the generated logo PNG into the img/ folder as logo-icon.png,
then generates all favicon sizes from it.
"""
from PIL import Image
import os
import shutil

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR    = os.path.join(SCRIPT_DIR, "img")
SRC_PNG    = r"C:\Users\Shalani A\.gemini\antigravity-ide\brain\eedd3187-2268-4e69-b60b-142ce4f88113\logo_icon_raw_1782493062472.png"
LOGO_OUT   = os.path.join(IMG_DIR, "logo-icon.png")

os.makedirs(IMG_DIR, exist_ok=True)

# ── Step 1: Open the source image ────────────────────────────────────────────
img = Image.open(SRC_PNG).convert("RGBA")

# ── Step 2: Make white background transparent ─────────────────────────────────
pixels = img.getdata()
new_pixels = []
for px in pixels:
    r, g, b, a = px
    if r > 240 and g > 240 and b > 240:
        new_pixels.append((255, 255, 255, 0))
    else:
        new_pixels.append(px)
img.putdata(new_pixels)

# ── Step 3: Crop to bounding box ─────────────────────────────────────────────
bbox = img.getbbox()
if bbox:
    img = img.crop(bbox)

# ── Step 4: Pad into a square with 10% margin ─────────────────────────────────
max_dim  = max(img.width, img.height)
pad      = int(max_dim * 0.10)
canvas   = max_dim + pad * 2
square   = Image.new("RGBA", (canvas, canvas), (255, 255, 255, 0))
offset_x = (canvas - img.width)  // 2
offset_y = (canvas - img.height) // 2
square.paste(img, (offset_x, offset_y), img)

# ── Step 5: Save logo-icon.png (512×512 for Retina/PWA) ─────────────────────
logo_512 = square.resize((512, 512), Image.Resampling.LANCZOS)
logo_512.save(LOGO_OUT, "PNG")
print(f"Saved {LOGO_OUT}")

# ── Step 6: apple-touch-icon.png (180×180) ────────────────────────────────────
# White background for Apple (iOS does not support transparency here)
apple = Image.new("RGBA", (180, 180), (255, 255, 255, 255))
logo_180 = square.resize((152, 152), Image.Resampling.LANCZOS)
apple.paste(logo_180, (14, 14), logo_180)
apple.save(os.path.join(IMG_DIR, "apple-touch-icon.png"), "PNG")
print("Saved apple-touch-icon.png")

# ── Step 7: favicon-32x32.png ────────────────────────────────────────────────
fav32 = square.resize((32, 32), Image.Resampling.LANCZOS)
fav32.save(os.path.join(IMG_DIR, "favicon-32x32.png"), "PNG")
print("Saved favicon-32x32.png")

# ── Step 8: favicon-16x16.png ────────────────────────────────────────────────
fav16 = square.resize((16, 16), Image.Resampling.LANCZOS)
fav16.save(os.path.join(IMG_DIR, "favicon-16x16.png"), "PNG")
print("Saved favicon-16x16.png")

# ── Step 9: favicon.ico (multi-size: 16, 32, 48) ─────────────────────────────
ico_images = [
    square.resize((16, 16),  Image.Resampling.LANCZOS),
    square.resize((32, 32),  Image.Resampling.LANCZOS),
    square.resize((48, 48),  Image.Resampling.LANCZOS),
]
ico_images[0].save(
    os.path.join(IMG_DIR, "favicon.ico"),
    format="ICO",
    sizes=[(16, 16), (32, 32), (48, 48)],
    append_images=ico_images[1:],
)
print("Saved favicon.ico")

print("\nAll favicon assets generated successfully!")
