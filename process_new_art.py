import os
from PIL import Image, ImageDraw, ImageFilter

gen_img_path = "/home/pandion/.gemini/antigravity/brain/fdc2fdd4-b2b0-4c6c-91ce-fd1f1a5be539/atlverse_original_studio_1787656933483.jpg"

if os.path.exists(gen_img_path):
    img = Image.open(gen_img_path)
    img = img.resize((1920, 1080), Image.Resampling.LANCZOS)
    img.save("assets/studio.png", "PNG", optimize=True)
    print("Saved fresh assets/studio.png")

    W, H = 1920, 1080
    depth = Image.new("L", (W, H), 50) # Back wall depth
    ddraw = ImageDraw.Draw(depth)

    # 1. Panoramic Window & Distant City Skyline (Far: 15 to 45)
    # Window region: x from 42% to 100%, y from 12% to 78%
    win_x1, win_y1, win_x2, win_y2 = int(W * 0.42), int(H * 0.10), W, int(H * 0.78)
    ddraw.rectangle([win_x1, win_y1, win_x2, win_y2], fill=20)
    # City buildings in window
    for bx in range(win_x1 + 30, win_x2 - 40, 100):
        bw = 70
        bh = int(H * 0.40) + (bx % 120)
        ddraw.rectangle([bx, win_y2 - bh, bx + bw, win_y2], fill=40)
    # Window grid mullions / frame (Mid-back: 75)
    for wy in range(win_y1, win_y2, int(H * 0.33)):
        ddraw.line([(win_x1, wy), (win_x2, wy)], fill=75, width=12)
    for wx in range(win_x1, win_x2, int(W * 0.18)):
        ddraw.line([(wx, win_y1), (wx, win_y2)], fill=75, width=12)

    # 2. Floor Gradient (Gradient from 70 at wall to 240 in near foreground)
    for y in range(int(H * 0.68), H):
        ratio = (y - H * 0.68) / (H * 0.32)
        val = int(75 + 165 * ratio)
        ddraw.line([(0, y), (W, y)], fill=val)

    # 3. Left Side Quantum Server Rack & Synth (Midground: 110 - 150)
    # Synth Keyboard & Audio waveform (x: 0% to 17%, y: 40% to 78%)
    ddraw.rectangle([0, int(H * 0.48), int(W * 0.17), int(H * 0.78)], fill=130)
    # Server Rack (x: 17% to 29%, y: 32% to 76%)
    ddraw.rectangle([int(W * 0.17), int(H * 0.32), int(W * 0.29), int(H * 0.76)], fill=125)
    # Hologram ATL VERSE Orb (x: 10% to 22%, y: 38% to 58%)
    ddraw.ellipse([int(W * 0.11), int(H * 0.38), int(W * 0.21), int(H * 0.58)], fill=145)

    # 4. Ergonomic Chair behind desk (Midground: 135)
    ddraw.rectangle([int(W * 0.56), int(H * 0.48), int(W * 0.66), int(H * 0.82)], fill=140)

    # 5. Floating Companion Robot (Mid-foreground: 175)
    # x: 65% to 73%, y: 46% to 58%
    ddraw.ellipse([int(W * 0.65), int(H * 0.45), int(W * 0.73), int(H * 0.58)], fill=180)

    # 6. Floating Hologram Screens (Fore-midground: 170)
    # Center holographic terminal screens (x: 33% to 62%, y: 32% to 64%)
    ddraw.rectangle([int(W * 0.34), int(H * 0.32), int(W * 0.62), int(H * 0.64)], fill=165)

    # 7. Curved Glass Desk & Workstation (Foreground: 200 - 245)
    # x: 32% to 73%, y: 64% to 92%
    desk_x1, desk_y1, desk_x2, desk_y2 = int(W * 0.32), int(H * 0.64), int(W * 0.73), int(H * 0.94)
    ddraw.rectangle([desk_x1, desk_y1, desk_x2, desk_y2], fill=215)
    ddraw.rectangle([desk_x1, desk_y1, desk_x2, desk_y1 + int(H * 0.08)], fill=235) # Desk surface
    # Keyboard, mouse, cup on desk (245)
    ddraw.rectangle([int(W * 0.47), int(H * 0.64), int(W * 0.60), int(H * 0.70)], fill=245)

    # 8. Floor Cables (Foreground: 235 - 255)
    ddraw.line([(0, int(H * 0.92)), (int(W * 0.45), int(H * 0.85))], fill=240, width=18)
    ddraw.line([(int(W * 0.75), int(H * 0.96)), (W, int(H * 0.82))], fill=250, width=22)

    depth_smooth = depth.filter(ImageFilter.GaussianBlur(radius=6))
    depth_smooth.save("assets/depth.png", "PNG", optimize=True)
    print("Saved fresh assets/depth.png")
