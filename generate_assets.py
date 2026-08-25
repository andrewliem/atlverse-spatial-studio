import math
import os
from PIL import Image, ImageDraw, ImageFilter

os.makedirs("assets", exist_ok=True)

WIDTH = 1920
HEIGHT = 1080

# -------------------------------------------------------------
# 1. GENERATE STUDIO COLOR IMAGE (studio.png)
# -------------------------------------------------------------
img = Image.new("RGBA", (WIDTH, HEIGHT), (22, 22, 30, 255))
draw = ImageDraw.Draw(img)

# --- A. Wall & Room Background ---
# Warm interior gradient
for y in range(HEIGHT):
    # Gradient from soft warm dusk at top to studio floor
    ratio = y / HEIGHT
    if y < int(HEIGHT * 0.72): # Wall
        r = int(32 + 25 * (1 - ratio))
        g = int(34 + 20 * (1 - ratio))
        b = int(48 + 25 * (1 - ratio))
    else: # Wooden Floor with warm tones
        f_ratio = (y - HEIGHT * 0.72) / (HEIGHT * 0.28)
        r = int(55 + 30 * f_ratio)
        g = int(35 + 20 * f_ratio)
        b = int(28 + 15 * f_ratio)
    draw.line([(0, y), (WIDTH, y)], fill=(r, g, b, 255))

# Floor baseboard / trim
draw.rectangle([0, int(HEIGHT * 0.70), WIDTH, int(HEIGHT * 0.72)], fill=(20, 20, 28, 255))
draw.line([(0, int(HEIGHT * 0.70)), (WIDTH, int(HEIGHT * 0.70))], fill=(60, 60, 80, 255), width=2)

# Wooden floor planks
for x in range(0, WIDTH, 120):
    draw.line([(x, int(HEIGHT * 0.72)), (x - 60, HEIGHT)], fill=(30, 20, 15, 180), width=2)

# Rug under the desk
rug_x1, rug_y1, rug_x2, rug_y2 = 360, int(HEIGHT * 0.75), 1560, int(HEIGHT * 0.96)
draw.rectangle([rug_x1, rug_y1, rug_x2, rug_y2], fill=(85, 30, 45, 255))
# Rug border pattern
draw.rectangle([rug_x1 + 12, rug_y1 + 10, rug_x2 - 12, rug_y2 - 10], outline=(200, 140, 70, 255), width=4)
# Rug fringe
for x in range(rug_x1, rug_x2, 8):
    draw.line([(x, rug_y2), (x, rug_y2 + 8)], fill=(220, 200, 160, 255), width=2)

# --- B. Window on Left & Sunlight Shaft ---
win_x1, win_y1, win_x2, win_y2 = 40, int(HEIGHT * 0.12), 260, int(HEIGHT * 0.68)
# Window frame & sky
draw.rectangle([win_x1, win_y1, win_x2, win_y2], fill=(255, 200, 120, 255)) # Sunset / golden hour sky
# Distant city buildings in window
draw.rectangle([win_x1 + 20, win_y2 - 120, win_x1 + 70, win_y2], fill=(210, 150, 100, 255))
draw.rectangle([win_x1 + 80, win_y2 - 160, win_x1 + 140, win_y2], fill=(190, 130, 90, 255))
draw.rectangle([win_x1 + 150, win_y2 - 90, win_x1 + 200, win_y2], fill=(220, 160, 110, 255))
# Window grid panes
draw.rectangle([win_x1, win_y1, win_x2, win_y2], outline=(50, 45, 55, 255), width=10)
draw.line([(win_x1 + (win_x2-win_x1)//2, win_y1), (win_x1 + (win_x2-win_x1)//2, win_y2)], fill=(50, 45, 55, 255), width=6)
for wy in range(win_y1 + 100, win_y2, 110):
    draw.line([(win_x1, wy), (win_x2, wy)], fill=(50, 45, 55, 255), width=6)

# Sunlight ray overlay (polygonal warm light beam across the room)
sun_overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
sun_draw = ImageDraw.Draw(sun_overlay)
sun_draw.polygon([
    (win_x1 + 10, win_y1 + 10),
    (win_x2, win_y2),
    (1450, HEIGHT),
    (400, HEIGHT)
], fill=(255, 220, 150, 45))
img = Image.alpha_composite(img, sun_overlay)
draw = ImageDraw.Draw(img)

# --- C. Left Bookshelf (x: 280 to 520) ---
bs_x1, bs_y1, bs_x2, bs_y2 = 290, int(HEIGHT * 0.16), 510, int(HEIGHT * 0.88)
# Wooden shelf uprights
draw.rectangle([bs_x1, bs_y1, bs_x1 + 22, bs_y2], fill=(130, 80, 50, 255))
draw.rectangle([bs_x2 - 22, bs_y1, bs_x2, bs_y2], fill=(110, 68, 42, 255))
# Shelf levels
shelves = [int(HEIGHT * 0.26), int(HEIGHT * 0.42), int(HEIGHT * 0.58), int(HEIGHT * 0.74)]
for sy in shelves:
    draw.rectangle([bs_x1 - 5, sy, bs_x2 + 5, sy + 18], fill=(155, 95, 60, 255))
    draw.rectangle([bs_x1 - 5, sy + 14, bs_x2 + 5, sy + 18], fill=(95, 55, 35, 255))

# Items on Shelf 1 (Top): Trophy & Holographic Orb
# Golden Trophy
trophy_x = bs_x1 + 50
draw.polygon([(trophy_x, shelves[0]), (trophy_x + 35, shelves[0]), (trophy_x + 25, shelves[0] - 40), (trophy_x + 10, shelves[0] - 40)], fill=(240, 190, 40, 255))
draw.rectangle([trophy_x + 12, shelves[0] - 55, trophy_x + 23, shelves[0] - 40], fill=(210, 160, 30, 255))
draw.ellipse([trophy_x + 5, shelves[0] - 80, trophy_x + 30, shelves[0] - 50], fill=(255, 215, 60, 255))
# Hologram Crystal / Orb
orb_cx, orb_cy = bs_x1 + 140, shelves[0] - 35
draw.ellipse([orb_cx - 20, orb_cy - 20, orb_cx + 20, orb_cy + 20], fill=(0, 220, 255, 220), outline=(255, 255, 255, 255), width=2)
# Stand under orb
draw.rectangle([orb_cx - 15, shelves[0] - 10, orb_cx + 15, shelves[0]], fill=(50, 50, 65, 255))

# Items on Shelf 2: Colorful Books & Tech Gadget
book_colors = [(220, 60, 60), (45, 140, 220), (230, 180, 40), (80, 190, 100), (160, 80, 210), (220, 100, 50)]
bx = bs_x1 + 25
for col in book_colors:
    bw = 14
    bh = 70 + (bx % 25)
    draw.rectangle([bx, shelves[1] - bh, bx + bw, shelves[1]], fill=col)
    draw.rectangle([bx, shelves[1] - bh, bx + bw, shelves[1] - bh + 4], fill=(255, 255, 255, 120))
    bx += bw + 3

# Items on Shelf 3: More books & Small Plant
draw.rectangle([bs_x1 + 130, shelves[2] - 25, bs_x1 + 165, shelves[2]], fill=(180, 90, 50, 255)) # Pot
draw.ellipse([bs_x1 + 125, shelves[2] - 60, bs_x1 + 170, shelves[2] - 20], fill=(50, 170, 80, 255)) # Foliage

# Items on Shelf 4 (Bottom): Storage boxes & manuals
draw.rectangle([bs_x1 + 25, shelves[3] - 50, bs_x1 + 95, shelves[3]], fill=(80, 90, 110, 255))
draw.rectangle([bs_x1 + 105, shelves[3] - 60, bs_x1 + 185, shelves[3]], fill=(140, 110, 80, 255))

# --- D. Wall Frames & Art ---
# Large Central Frame: "ATL VERSE" Poster
pf_x1, pf_y1, pf_x2, pf_y2 = 880, int(HEIGHT * 0.12), 1160, int(HEIGHT * 0.38)
draw.rectangle([pf_x1, pf_y1, pf_x2, pf_y2], fill=(15, 18, 25, 255), outline=(190, 170, 130, 255), width=8)
# Poster artwork: Neon grid & typography
draw.rectangle([pf_x1 + 15, pf_y1 + 15, pf_x2 - 15, pf_y2 - 15], fill=(240, 235, 225, 255))
# Stylized logo / text block inside poster
draw.rectangle([pf_x1 + 40, pf_y1 + 50, pf_x2 - 40, pf_y1 + 90], fill=(20, 25, 35, 255))
draw.polygon([(pf_x1 + 60, pf_y2 - 60), (pf_x1 + 140, pf_y2 - 130), (pf_x2 - 60, pf_y2 - 60)], fill=(0, 200, 220, 255))

# Left Wall Frame (Metaverse Map / Portrait)
f2_x1, f2_y1, f2_x2, f2_y2 = 720, int(HEIGHT * 0.14), 840, int(HEIGHT * 0.26)
draw.rectangle([f2_x1, f2_y1, f2_x2, f2_y2], fill=(245, 240, 230, 255), outline=(140, 100, 70, 255), width=6)
draw.ellipse([f2_x1 + 25, f2_y1 + 20, f2_x2 - 25, f2_y2 - 30], fill=(210, 130, 90, 255))

# Certificate frame below it
f3_x1, f3_y1, f3_x2, f3_y2 = 700, int(HEIGHT * 0.29), 855, int(HEIGHT * 0.39)
draw.rectangle([f3_x1, f3_y1, f3_x2, f3_y2], fill=(240, 238, 225, 255), outline=(140, 100, 70, 255), width=5)
draw.rectangle([f3_x1 + 20, f3_y1 + 20, f3_x2 - 20, f3_y1 + 28], fill=(160, 140, 100, 255))

# Right Wall Frame (World / Berlin / Spatial Map)
f4_x1, f4_y1, f4_x2, f4_y2 = 1420, int(HEIGHT * 0.16), 1640, int(HEIGHT * 0.48)
draw.rectangle([f4_x1, f4_y1, f4_x2, f4_y2], fill=(230, 240, 235, 255), outline=(80, 60, 45, 255), width=8)
# Map graphics
draw.polygon([(f4_x1 + 40, f4_y1 + 80), (f4_x2 - 50, f4_y1 + 100), (f4_x1 + 90, f4_y2 - 60)], fill=(70, 160, 130, 255))
draw.rectangle([f4_x1 + 30, f4_y2 - 45, f4_x2 - 30, f4_y2 - 20], fill=(40, 40, 50, 255))

# Neon sticky notes on wall
notes = [(1680, int(HEIGHT * 0.22), (255, 240, 80)), (1730, int(HEIGHT * 0.26), (255, 120, 180)), (1690, int(HEIGHT * 0.35), (100, 240, 200))]
for nx, ny, ncol in notes:
    draw.rectangle([nx, ny, nx + 40, ny + 45], fill=ncol)

# --- E. Main Workstation Desk (x: 580 to 1400) ---
desk_x1, desk_y1, desk_x2, desk_y2 = 580, int(HEIGHT * 0.62), 1380, int(HEIGHT * 0.94)
# Desk Top Surface
draw.rectangle([desk_x1, desk_y1, desk_x2, desk_y1 + 36], fill=(185, 120, 75, 255)) # Rich oak top
draw.rectangle([desk_x1, desk_y1 + 30, desk_x2, desk_y1 + 36], fill=(120, 70, 40, 255)) # Bevel shadow
# Glowing cyan underglow strip
draw.rectangle([desk_x1 + 20, desk_y1 + 36, desk_x2 - 20, desk_y1 + 42], fill=(0, 230, 255, 240))
# Desk Legs
leg_w = 26
draw.rectangle([desk_x1 + 40, desk_y1 + 36, desk_x1 + 40 + leg_w, desk_y2], fill=(140, 85, 50, 255))
draw.rectangle([desk_x2 - 40 - leg_w, desk_y1 + 36, desk_x2 - 40, desk_y2], fill=(130, 75, 45, 255))
# Crossbar
draw.rectangle([desk_x1 + 40, desk_y1 + 180, desk_x2 - 40, desk_y1 + 195], fill=(110, 65, 38, 255))

# --- F. Computer Monitor & Peripherals (on desk) ---
# Monitor Stand
mon_cx = 960
draw.rectangle([mon_cx - 50, desk_y1 - 10, mon_cx + 50, desk_y1], fill=(180, 185, 195, 255))
draw.rectangle([mon_cx - 12, desk_y1 - 70, mon_cx + 12, desk_y1 - 10], fill=(150, 155, 165, 255))

# Monitor Screen (Large Ultrawide / Studio Display)
mon_w = 420
mon_h = 240
mon_x1 = mon_cx - mon_w // 2
mon_y1 = desk_y1 - 70 - mon_h
mon_x2 = mon_x1 + mon_w
mon_y2 = mon_y1 + mon_h
# Outer Bezel
draw.rectangle([mon_x1, mon_y1, mon_x2, mon_y2], fill=(25, 28, 38, 255), outline=(80, 85, 100, 255), width=6)
# Display Area (IDE Code & 3D Spatial Canvas glowing)
disp_x1, disp_y1, disp_x2, disp_y2 = mon_x1 + 10, mon_y1 + 10, mon_x2 - 10, mon_y2 - 10
draw.rectangle([disp_x1, disp_y1, disp_x2, disp_y2], fill=(18, 22, 32, 255))
# Simulated code lines & UI
draw.rectangle([disp_x1, disp_y1, disp_x1 + 60, disp_y2], fill=(12, 15, 22, 255)) # Sidebar
code_cols = [(240, 100, 100), (100, 200, 255), (120, 240, 140), (255, 215, 80), (180, 140, 240)]
for ly in range(disp_y1 + 25, disp_y2 - 20, 14):
    indent = 80 + (ly % 40)
    lw = 60 + (ly * 7) % 180
    col = code_cols[(ly // 14) % len(code_cols)]
    draw.line([(disp_x1 + indent, ly), (disp_x1 + indent + lw, ly)], fill=col, width=3)

# Desk Lamp (Left of Monitor)
lamp_base_x = 680
draw.rectangle([lamp_base_x - 20, desk_y1 - 8, lamp_base_x + 20, desk_y1], fill=(45, 50, 60, 255))
draw.line([(lamp_base_x, desk_y1 - 8), (lamp_base_x + 30, desk_y1 - 100)], fill=(70, 75, 90, 255), width=6)
draw.line([(lamp_base_x + 30, desk_y1 - 100), (lamp_base_x + 80, desk_y1 - 85)], fill=(70, 75, 90, 255), width=6)
draw.polygon([(lamp_base_x + 75, desk_y1 - 95), (lamp_base_x + 115, desk_y1 - 70), (lamp_base_x + 95, desk_y1 - 55)], fill=(45, 50, 60, 255))
# Lamp light glow
lamp_glow = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
lamp_gdraw = ImageDraw.Draw(lamp_glow)
lamp_gdraw.polygon([(lamp_base_x + 105, desk_y1 - 65), (lamp_base_x + 60, desk_y1), (lamp_base_x + 220, desk_y1)], fill=(255, 240, 180, 65))
img = Image.alpha_composite(img, lamp_glow)
draw = ImageDraw.Draw(img)

# Keyboard & Mouse on Desk
draw.rectangle([mon_cx - 110, desk_y1 + 6, mon_cx + 40, desk_y1 + 22], fill=(40, 45, 55, 255), outline=(70, 75, 90, 255))
draw.ellipse([mon_cx + 70, desk_y1 + 8, mon_cx + 95, desk_y1 + 20], fill=(220, 225, 235, 255)) # White mouse

# Coffee Mug & Pencil Cup (Right of Monitor)
draw.rectangle([1210, desk_y1 - 35, 1235, desk_y1], fill=(240, 235, 220, 255)) # Coffee mug
draw.rectangle([1255, desk_y1 - 50, 1285, desk_y1], fill=(40, 60, 80, 255)) # Pen holder
draw.line([(1265, desk_y1 - 50), (1260, desk_y1 - 75)], fill=(240, 60, 60, 255), width=3)
draw.line([(1275, desk_y1 - 50), (1280, desk_y1 - 70)], fill=(60, 180, 240, 255), width=3)

# VR Headset / Spatial Device on desk
vr_x = 1130
draw.rounded_rectangle([vr_x, desk_y1 - 28, vr_x + 65, desk_y1], radius=8, fill=(35, 38, 48, 255), outline=(90, 95, 115, 255))
draw.ellipse([vr_x + 12, desk_y1 - 20, vr_x + 28, desk_y1 - 8], fill=(15, 200, 255, 220)) # Sensor lens
draw.ellipse([vr_x + 38, desk_y1 - 20, vr_x + 54, desk_y1 - 8], fill=(15, 200, 255, 220))

# --- G. Right Tech/Music Wall (Electric Guitar, Cyber Synth, Skateboard) ---
# Monstera Plant in corner
plant_x, plant_y = 1430, int(HEIGHT * 0.72)
draw.rectangle([plant_x - 30, plant_y, plant_x + 30, plant_y + 80], fill=(190, 100, 60, 255)) # Terracotta Pot
draw.ellipse([plant_x - 70, plant_y - 120, plant_x + 10, plant_y - 20], fill=(40, 150, 80, 255))
draw.ellipse([plant_x, plant_y - 150, plant_x + 80, plant_y - 50], fill=(30, 130, 70, 255))
draw.ellipse([plant_x - 30, plant_y - 180, plant_x + 50, plant_y - 90], fill=(50, 170, 90, 255))

# Electric Bass / Cyber Guitar on Stand
gt_x = 1620
# Guitar Body (Seafoam Green / Cyan modern aesthetic)
draw.ellipse([gt_x - 45, int(HEIGHT * 0.65), gt_x + 45, int(HEIGHT * 0.88)], fill=(120, 210, 190, 255), outline=(50, 80, 75, 255), width=4)
draw.rectangle([gt_x - 20, int(HEIGHT * 0.70), gt_x + 20, int(HEIGHT * 0.82)], fill=(245, 245, 245, 255)) # Pickguard
# Neck & Headstock
draw.rectangle([gt_x - 8, int(HEIGHT * 0.38), gt_x + 8, int(HEIGHT * 0.68)], fill=(210, 170, 120, 255))
draw.polygon([(gt_x - 10, int(HEIGHT * 0.38)), (gt_x + 15, int(HEIGHT * 0.34)), (gt_x - 5, int(HEIGHT * 0.34))], fill=(210, 170, 120, 255))
# Strings
for so in [-4, -1, 2, 5]:
    draw.line([(gt_x + so, int(HEIGHT * 0.36)), (gt_x + so, int(HEIGHT * 0.84))], fill=(240, 240, 240, 255), width=1)

# Skateboard leaning on wall
sk_x1, sk_y1 = 1760, int(HEIGHT * 0.55)
draw.polygon([(sk_x1, sk_y1), (sk_x1 + 45, sk_y1 + 10), (sk_x1 + 90, int(HEIGHT * 0.94)), (sk_x1 + 45, int(HEIGHT * 0.96))], fill=(200, 150, 90, 255), outline=(40, 40, 50, 255), width=3)
# Wheels
draw.ellipse([sk_x1 + 35, int(HEIGHT * 0.90), sk_x1 + 55, int(HEIGHT * 0.95)], fill=(220, 80, 80, 255))
draw.ellipse([sk_x1 + 75, int(HEIGHT * 0.87), sk_x1 + 95, int(HEIGHT * 0.92)], fill=(220, 80, 80, 255))

# --- H. Cyber Cat Companion on the Rug (Foreground) ---
cat_x, cat_y = 1380, int(HEIGHT * 0.84)
# Body
draw.ellipse([cat_x, cat_y, cat_x + 70, cat_y + 45], fill=(245, 240, 230, 255)) # Cream cat
# Head & Ears
draw.ellipse([cat_x - 20, cat_y - 10, cat_x + 25, cat_y + 30], fill=(245, 240, 230, 255))
draw.polygon([(cat_x - 15, cat_y + 5), (cat_x - 10, cat_y - 25), (cat_x + 5, cat_y)], fill=(230, 180, 160, 255))
draw.polygon([(cat_x + 5, cat_y + 5), (cat_x + 18, cat_y - 22), (cat_x + 25, cat_y + 5)], fill=(230, 180, 160, 255))
# Glowing Cyber Collar (Teal)
draw.arc([cat_x - 5, cat_y + 12, cat_x + 15, cat_y + 28], start=30, end=150, fill=(0, 240, 255, 255), width=3)
# Tail
draw.arc([cat_x + 50, cat_y - 15, cat_x + 85, cat_y + 35], start=200, end=350, fill=(230, 225, 215, 255), width=8)

img.save("assets/studio.png", format="PNG", optimize=True)
print("Saved assets/studio.png")


# -------------------------------------------------------------
# 2. GENERATE MATCHING DEPTH MAP (depth.png)
# -------------------------------------------------------------
# 0 = far background / infinite, 255 = nearest foreground
depth = Image.new("L", (WIDTH, HEIGHT), 30) # Default back wall depth
ddraw = ImageDraw.Draw(depth)

# Window sky (Furthest away)
ddraw.rectangle([win_x1, win_y1, win_x2, win_y2], fill=10)
# Window frame
ddraw.rectangle([win_x1, win_y1, win_x2, win_y2], outline=45, width=10)

# Wall Frames & Posters (Slightly in front of back wall)
ddraw.rectangle([pf_x1, pf_y1, pf_x2, pf_y2], fill=65)
ddraw.rectangle([f2_x1, f2_y1, f2_x2, f2_y2], fill=60)
ddraw.rectangle([f3_x1, f3_y1, f3_x2, f3_y2], fill=60)
ddraw.rectangle([f4_x1, f4_y1, f4_x2, f4_y2], fill=65)

# Floor Gradient (Gradient from 70 at wall to 230 at near camera)
for y in range(int(HEIGHT * 0.70), HEIGHT):
    ratio = (y - HEIGHT * 0.70) / (HEIGHT * 0.30)
    val = int(75 + 160 * ratio)
    ddraw.line([(0, y), (WIDTH, y)], fill=val)

# Bookshelf (Left midground: 80 - 130)
ddraw.rectangle([bs_x1, bs_y1, bs_x2, bs_y2], fill=110)
for sy in shelves:
    ddraw.rectangle([bs_x1 - 5, sy, bs_x2 + 5, sy + 18], fill=135)
# Books and shelf items
ddraw.rectangle([bs_x1 + 20, shelves[1] - 80, bs_x1 + 180, shelves[1]], fill=145)
ddraw.ellipse([orb_cx - 25, orb_cy - 25, orb_cx + 25, orb_cy + 25], fill=150) # Hologram orb

# Main Desk (Fore-midground: 160 - 210)
ddraw.rectangle([desk_x1, desk_y1, desk_x2, desk_y2], fill=175)
ddraw.rectangle([desk_x1, desk_y1, desk_x2, desk_y1 + 40], fill=195) # Desk top

# Computer Monitor (185 - 205)
ddraw.rectangle([mon_x1, mon_y1, mon_x2, mon_y2], fill=185)
ddraw.rectangle([mon_cx - 15, desk_y1 - 70, mon_cx + 15, desk_y1], fill=175)

# Lamp & Desk Objects (190 - 215)
ddraw.rectangle([lamp_base_x - 20, desk_y1 - 100, lamp_base_x + 120, desk_y1], fill=200)
ddraw.rectangle([mon_cx - 120, desk_y1, mon_cx + 100, desk_y1 + 25], fill=215) # Keyboard / mouse
ddraw.rounded_rectangle([vr_x, desk_y1 - 30, vr_x + 70, desk_y1], radius=8, fill=220) # VR headset

# Right elements: Plant, Guitar, Skateboard (140 - 230)
ddraw.ellipse([plant_x - 80, plant_y - 180, plant_x + 80, plant_y + 80], fill=150) # Plant
ddraw.rectangle([gt_x - 50, int(HEIGHT * 0.34), gt_x + 50, int(HEIGHT * 0.90)], fill=190) # Guitar
ddraw.polygon([(sk_x1, sk_y1), (sk_x1 + 45, sk_y1 + 10), (sk_x1 + 90, int(HEIGHT * 0.94)), (sk_x1 + 45, int(HEIGHT * 0.96))], fill=220) # Skateboard

# Cat on floor (Nearest foreground: 245)
ddraw.ellipse([cat_x - 25, cat_y - 25, cat_x + 85, cat_y + 50], fill=245)

# Smooth blur depth map slightly for natural gradient transitions
depth_blurred = depth.filter(ImageFilter.GaussianBlur(radius=4))
depth_blurred.save("assets/depth.png", format="PNG", optimize=True)
print("Saved assets/depth.png")
