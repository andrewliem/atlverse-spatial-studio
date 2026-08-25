import os
from PIL import Image, ImageDraw, ImageFilter

gen_img_path = "/home/pandion/.gemini/antigravity/brain/fdc2fdd4-b2b0-4c6c-91ce-fd1f1a5be539/andrew_atlverse_lab_1787657333934.jpg"

if os.path.exists(gen_img_path):
    img = Image.open(gen_img_path)
    img_1080 = img.resize((1920, 1080), Image.Resampling.LANCZOS)
    img_1080.save("assets/studio.png", "PNG", optimize=True)
    img_1080.save("assets/studio.jpg", "JPEG", quality=95)
    img.save("assets/atlverse_studio_hd.png", "PNG")
    print("Saved custom Atlverse studio assets")

    W, H = 1920, 1080
    depth = Image.new("L", (W, H), 40) # Back wall depth
    ddraw = ImageDraw.Draw(depth)

    # 1. Window on Right (Skyline: 15 to 45)
    win_x1, win_y1, win_x2, win_y2 = int(W * 0.69), int(H * 0.10), W, int(H * 0.78)
    ddraw.rectangle([win_x1, win_y1, win_x2, win_y2], fill=20)
    # City buildings in window
    for bx in range(win_x1 + 30, win_x2, 80):
        ddraw.rectangle([bx, win_y2 - int(H * 0.45), bx + 60, win_y2], fill=40)

    # 2. Wall Frames (Depth: 60 - 75)
    # Andrew Portrait Frame (x: 29% to 41%, y: 10% to 42%)
    ddraw.rectangle([int(W * 0.29), int(H * 0.10), int(W * 0.41), int(H * 0.42)], fill=70)
    # Neural Net Architecture Poster (x: 44% to 63%, y: 13% to 41%)
    ddraw.rectangle([int(W * 0.44), int(H * 0.13), int(W * 0.63), int(H * 0.41)], fill=68)

    # 3. Left Bookshelf & Research Binders (Depth: 95 - 145)
    # Bookshelf structure (x: 0% to 28%, y: 3% to 68%)
    ddraw.rectangle([0, int(H * 0.03), int(W * 0.28), int(H * 0.68)], fill=115)
    # Hologram plates & diploma on shelf
    ddraw.rectangle([int(W * 0.03), int(H * 0.04), int(W * 0.16), int(H * 0.19)], fill=125) # UNKLAB Diploma
    ddraw.rectangle([int(W * 0.05), int(H * 0.53), int(W * 0.15), int(H * 0.67)], fill=135) # Certificate below

    # 4. Floor Gradient (Depth: 80 to 245)
    for y in range(int(H * 0.70), H):
        ratio = (y - H * 0.70) / (H * 0.30)
        val = int(80 + 165 * ratio)
        ddraw.line([(0, y), (W, y)], fill=val)

    # 5. Right Classroom Smart Blackboard (Depth: 130 - 180)
    # x: 83% to 100%, y: 28% to 88%
    ddraw.rectangle([int(W * 0.83), int(H * 0.28), W, int(H * 0.88)], fill=160)

    # 6. Reading Chair & AI Floating Bot (Depth: 140 - 185)
    ddraw.rectangle([int(W * 0.61), int(H * 0.58), int(W * 0.77), int(H * 0.85)], fill=145) # Chair
    ddraw.ellipse([int(W * 0.59), int(H * 0.45), int(W * 0.65), int(H * 0.59)], fill=180) # AI Bot

    # 7. Center Research Workstation & Monitors (Depth: 180 - 240)
    # Desk Surface & Structure
    desk_x1, desk_y1, desk_x2, desk_y2 = int(W * 0.12), int(H * 0.65), int(W * 0.61), int(H * 0.95)
    ddraw.rectangle([desk_x1, desk_y1, desk_x2, desk_y2], fill=210)
    ddraw.rectangle([desk_x1, desk_y1, desk_x2, desk_y1 + int(H * 0.08)], fill=230)
    # Dual Monitors (195)
    ddraw.rectangle([int(W * 0.26), int(H * 0.44), int(W * 0.53), int(H * 0.66)], fill=195)
    # Lamp & Robot head on desk
    ddraw.rectangle([int(W * 0.14), int(H * 0.57), int(W * 0.26), int(H * 0.72)], fill=220)

    # 8. Andrew sitting in chair (Fore-midground: 215 - 245)
    # x: 41% to 61%, y: 45% to 95%
    ddraw.rectangle([int(W * 0.41), int(H * 0.45), int(W * 0.60), int(H * 0.95)], fill=225)

    # 9. Foreground Plant & Floor Rug (240 - 255)
    ddraw.ellipse([0, int(H * 0.60), int(W * 0.10), H], fill=245) # Plant
    ddraw.rectangle([int(W * 0.12), int(H * 0.80), int(W * 0.24), int(H * 0.96)], fill=235) # Tower PC

    depth_smooth = depth.filter(ImageFilter.GaussianBlur(radius=6))
    depth_smooth.save("assets/depth.png", "PNG", optimize=True)
    print("Saved depth.png successfully")
