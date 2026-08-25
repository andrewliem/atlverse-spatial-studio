import os
from PIL import Image, ImageDraw, ImageFilter

gen_img_path = "/home/pandion/.gemini/antigravity/brain/fdc2fdd4-b2b0-4c6c-91ce-fd1f1a5be539/andrew_futuristic_lab_1787657843003.jpg"

if os.path.exists(gen_img_path):
    img = Image.open(gen_img_path)
    img_1080 = img.resize((1920, 1080), Image.Resampling.LANCZOS)
    img_1080.save("assets/studio.png", "PNG", optimize=True)
    img_1080.save("assets/studio.jpg", "JPEG", quality=95)
    img.save("assets/atlverse_studio_hd.png", "PNG")
    print("Saved ultra-futuristic studio assets")

    W, H = 1920, 1080
    depth = Image.new("L", (W, H), 50) # Back wall depth
    ddraw = ImageDraw.Draw(depth)

    # 1. Panoramic Window & Distant City Skyline (Depth: 15 to 45)
    # Window region: x from 52% to 100%, y from 8% to 80%
    win_x1, win_y1, win_x2, win_y2 = int(W * 0.52), int(H * 0.08), W, int(H * 0.80)
    ddraw.rectangle([win_x1, win_y1, win_x2, win_y2], fill=20)
    # City buildings in window
    for bx in range(win_x1 + 30, win_x2, 80):
        ddraw.rectangle([bx, win_y2 - int(H * 0.45), bx + 65, win_y2], fill=40)
    # Window frame mullions (Mid-back: 75)
    ddraw.line([(int(W * 0.68), win_y1), (int(W * 0.68), win_y2)], fill=75, width=14)
    ddraw.line([(int(W * 0.87), win_y1), (int(W * 0.87), win_y2)], fill=75, width=14)

    # 2. Wall Frames (Depth: 75 - 85)
    # Small Andrew Portrait Frame (x: 28% to 36%, y: 20% to 41%)
    ddraw.rectangle([int(W * 0.28), int(H * 0.20), int(W * 0.36), int(H * 0.41)], fill=82)
    # Neon Circuit Architecture Poster (x: 38% to 51%, y: 23% to 41%)
    ddraw.rectangle([int(W * 0.38), int(H * 0.23), int(W * 0.51), int(H * 0.41)], fill=80)

    # 3. Left Futuristic Holographic Bookshelf & UNKLAB Diploma (Depth: 110 - 150)
    # UNKLAB Diploma at top (x: 10% to 20%, y: 7% to 22%)
    ddraw.rectangle([int(W * 0.10), int(H * 0.07), int(W * 0.20), int(H * 0.22)], fill=125)
    # Bookshelf structure (x: 3% to 25%, y: 20% to 88%)
    ddraw.rectangle([int(W * 0.03), int(H * 0.20), int(W * 0.25), int(H * 0.88)], fill=135)

    # 4. Floor Gradient (Depth: 80 to 240)
    for y in range(int(H * 0.76), H):
        ratio = (y - H * 0.76) / (H * 0.24)
        val = int(80 + 160 * ratio)
        ddraw.line([(0, y), (W, y)], fill=val)

    # 5. Floating AI Drone Companion (Depth: 160)
    # x: 28% to 35%, y: 44% to 56%
    ddraw.ellipse([int(W * 0.28), int(H * 0.44), int(W * 0.35), int(H * 0.56)], fill=165)

    # 6. Floating Holographic Classroom HUD (Depth: 175)
    # x: 77% to 97%, y: 35% to 60%
    ddraw.rectangle([int(W * 0.77), int(H * 0.35), int(W * 0.97), int(H * 0.60)], fill=175)

    # 7. Ergonomic Chair behind desk (Depth: 145)
    ddraw.rectangle([int(W * 0.38), int(H * 0.50), int(W * 0.49), int(H * 0.76)], fill=145)

    # 8. Floating Hologram Screens on Desk (Depth: 180)
    # x: 38% to 68%, y: 44% to 64%
    ddraw.rectangle([int(W * 0.38), int(H * 0.44), int(W * 0.68), int(H * 0.64)], fill=180)

    # 9. Curved Glass & Carbon-Fiber Floating Desk (Depth: 215 - 245)
    # x: 30% to 75%, y: 61% to 87%
    desk_x1, desk_y1, desk_x2, desk_y2 = int(W * 0.30), int(H * 0.61), int(W * 0.75), int(H * 0.87)
    ddraw.rectangle([desk_x1, desk_y1, desk_x2, desk_y2], fill=220)
    ddraw.rectangle([desk_x1, desk_y1, desk_x2, desk_y1 + int(H * 0.08)], fill=240)

    depth_smooth = depth.filter(ImageFilter.GaussianBlur(radius=6))
    depth_smooth.save("assets/depth.png", "PNG", optimize=True)
    print("Saved ultra-futuristic depth.png successfully")
