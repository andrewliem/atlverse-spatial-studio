import os
from PIL import Image, ImageDraw, ImageFilter

gen_img_path = "/home/pandion/.gemini/antigravity/brain/fdc2fdd4-b2b0-4c6c-91ce-fd1f1a5be539/andrew_unified_futuristic_lab_1787658601322.jpg"

if os.path.exists(gen_img_path):
    img = Image.open(gen_img_path)
    img_1080 = img.resize((1920, 1080), Image.Resampling.LANCZOS)
    img_1080.save("assets/studio.png", "PNG", optimize=True)
    img_1080.save("assets/studio.jpg", "JPEG", quality=95)
    img.save("assets/atlverse_studio_hd.png", "PNG")
    print("Saved unified Atlverse studio assets")

    W, H = 1920, 1080
    depth = Image.new("L", (W, H), 50) # Back wall depth
    ddraw = ImageDraw.Draw(depth)

    # 1. Panoramic Sunset Window & City Skyline (Depth: 15 to 45)
    # Window region: x from 72% to 100%, y from 0% to 100%
    win_x1, win_y1, win_x2, win_y2 = int(W * 0.72), 0, W, H
    ddraw.rectangle([win_x1, win_y1, win_x2, win_y2], fill=20)
    # City buildings in window
    for bx in range(win_x1 + 30, win_x2, 70):
        ddraw.rectangle([bx, win_y2 - int(H * 0.55), bx + 55, win_y2], fill=40)
    # Window frame mullions (Depth: 75)
    ddraw.rectangle([int(W * 0.71), 0, int(W * 0.74), H], fill=75)
    ddraw.rectangle([int(W * 0.88), 0, int(W * 0.91), H], fill=75)

    # 2. Wall Portrait Frame (Andrew Tanny Liem) (Depth: 78 - 85)
    # x: 40% to 59%, y: 9% to 54%
    ddraw.rectangle([int(W * 0.40), int(H * 0.09), int(W * 0.59), int(H * 0.54)], fill=82)

    # 3. Left Illuminated Bookshelf & Diploma (Depth: 110 - 150)
    # Bookshelf structure (x: 0% to 27%, y: 5% to 80%)
    ddraw.rectangle([0, int(H * 0.05), int(W * 0.27), int(H * 0.80)], fill=130)
    # Universitas Klabat Diploma (x: 2% to 16%, y: 38% to 56%)
    ddraw.rectangle([int(W * 0.02), int(H * 0.38), int(W * 0.16), int(H * 0.56)], fill=145)

    # 4. Floor Gradient (Depth: 80 to 240)
    for y in range(int(H * 0.72), H):
        ratio = (y - H * 0.72) / (H * 0.28)
        val = int(80 + 160 * ratio)
        ddraw.line([(0, y), (W, y)], fill=val)

    # 5. Floating AI Drone Companion (Depth: 165)
    # x: 64% to 72%, y: 53% to 67%
    ddraw.ellipse([int(W * 0.64), int(H * 0.53), int(W * 0.72), int(H * 0.67)], fill=170)

    # 6. Floating Holographic Classroom Board (Depth: 175)
    # x: 70% to 84%, y: 35% to 53%
    ddraw.rectangle([int(W * 0.70), int(H * 0.35), int(W * 0.84), int(H * 0.53)], fill=175)

    # 7. Floating Hologram Screens on Desk (Depth: 185)
    # Left Hologram Screen (x: 23% to 39%, y: 55% to 80%)
    ddraw.rectangle([int(W * 0.23), int(H * 0.55), int(W * 0.39), int(H * 0.80)], fill=185)
    # Center Hologram Screen (x: 40% to 61%, y: 57% to 83%)
    ddraw.rectangle([int(W * 0.40), int(H * 0.57), int(W * 0.61), int(H * 0.83)], fill=185)

    # 8. Glass Workstation Desk (Depth: 215 - 245)
    # x: 17% to 83%, y: 73% to 92%
    desk_x1, desk_y1, desk_x2, desk_y2 = int(W * 0.17), int(H * 0.73), int(W * 0.83), int(H * 0.92)
    ddraw.rectangle([desk_x1, desk_y1, desk_x2, desk_y2], fill=220)
    ddraw.rectangle([desk_x1, desk_y1, desk_x2, desk_y1 + int(H * 0.06)], fill=240) # Glass surface
    # Desk legs
    ddraw.rectangle([desk_x1 + 40, desk_y1, desk_x1 + 65, H], fill=210)
    ddraw.rectangle([desk_x2 - 65, desk_y1, desk_x2 - 40, H], fill=210)

    depth_smooth = depth.filter(ImageFilter.GaussianBlur(radius=6))
    depth_smooth.save("assets/depth.png", "PNG", optimize=True)
    print("Saved unified depth.png successfully")
