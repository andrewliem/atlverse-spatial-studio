import os
from PIL import Image, ImageDraw, ImageFilter

gen_img_path = "/home/pandion/.gemini/antigravity/brain/fdc2fdd4-b2b0-4c6c-91ce-fd1f1a5be539/andrew_wide_futuristic_lab_1787658858191.jpg"

if os.path.exists(gen_img_path):
    img = Image.open(gen_img_path)
    img_1080 = img.resize((1920, 1080), Image.Resampling.LANCZOS)
    img_1080.save("assets/studio.png", "PNG", optimize=True)
    img_1080.save("assets/studio.jpg", "JPEG", quality=95)
    img.save("assets/atlverse_studio_hd.png", "PNG")
    print("Saved wide-angle clean futuristic studio assets")

    W, H = 1920, 1080
    depth = Image.new("L", (W, H), 50) # Back wall depth
    ddraw = ImageDraw.Draw(depth)

    # 1. Panoramic Sunset Window & City Skyline (Depth: 15 to 45)
    # Window region: x from 65% to 100%, y from 12% to 82%
    win_x1, win_y1, win_x2, win_y2 = int(W * 0.65), int(H * 0.12), W, int(H * 0.82)
    ddraw.rectangle([win_x1, win_y1, win_x2, win_y2], fill=20)
    # City skyscrapers in window
    for bx in range(win_x1 + 30, win_x2, 85):
        ddraw.rectangle([bx, win_y2 - int(H * 0.50), bx + 70, win_y2], fill=40)
    # Window frame mullions (Depth: 75)
    ddraw.line([(int(W * 0.77), win_y1), (int(W * 0.77), win_y2)], fill=75, width=14)
    ddraw.line([(int(W * 0.90), win_y1), (int(W * 0.90), win_y2)], fill=75, width=14)

    # 2. Wall Frames (Depth: 78 - 85)
    # Small Andrew Portrait Frame (x: 30% to 39%, y: 26% to 44%)
    ddraw.rectangle([int(W * 0.30), int(H * 0.26), int(W * 0.39), int(H * 0.44)], fill=82)
    # Neon Circuit Schematics Poster (x: 42% to 60%, y: 24% to 43%)
    ddraw.rectangle([int(W * 0.42), int(H * 0.24), int(W * 0.60), int(H * 0.43)], fill=80)

    # 3. Left Clean Futuristic Glass Bookshelf (Depth: 110 - 150)
    # Bookshelf structure (x: 2% to 27%, y: 13% to 89%)
    ddraw.rectangle([int(W * 0.02), int(H * 0.13), int(W * 0.27), int(H * 0.89)], fill=135)
    # Universitas Klabat Diploma inside shelf (x: 6% to 17%, y: 46% to 60%)
    ddraw.rectangle([int(W * 0.06), int(H * 0.46), int(W * 0.17), int(H * 0.60)], fill=145)

    # 4. Floor Gradient (Depth: 80 to 240)
    for y in range(int(H * 0.78), H):
        ratio = (y - H * 0.78) / (H * 0.22)
        val = int(80 + 160 * ratio)
        ddraw.line([(0, y), (W, y)], fill=val)

    # 5. Ergonomic Chair behind desk (Depth: 145)
    # x: 40% to 51%, y: 50% to 83%
    ddraw.rectangle([int(W * 0.40), int(H * 0.50), int(W * 0.51), int(H * 0.83)], fill=145)

    # 6. Floating AI Drone Companion (Depth: 160)
    # x: 63% to 70%, y: 40% to 50%
    ddraw.ellipse([int(W * 0.63), int(H * 0.40), int(W * 0.70), int(H * 0.50)], fill=165)

    # 7. Floating Holographic Classroom Board (Depth: 175)
    # x: 72% to 94%, y: 31% to 60%
    ddraw.rectangle([int(W * 0.72), int(H * 0.31), int(W * 0.94), int(H * 0.60)], fill=175)

    # 8. Floating Hologram Screens on Desk (Depth: 185)
    # x: 35% to 62%, y: 44% to 63%
    ddraw.rectangle([int(W * 0.35), int(H * 0.44), int(W * 0.62), int(H * 0.63)], fill=185)

    # 9. Curved Glass Floating Desk (Depth: 215 - 245)
    # x: 33% to 69%, y: 62% to 92%
    desk_x1, desk_y1, desk_x2, desk_y2 = int(W * 0.33), int(H * 0.62), int(W * 0.69), int(H * 0.92)
    ddraw.rectangle([desk_x1, desk_y1, desk_x2, desk_y2], fill=220)
    ddraw.rectangle([desk_x1, desk_y1, desk_x2, desk_y1 + int(H * 0.08)], fill=240)

    depth_smooth = depth.filter(ImageFilter.GaussianBlur(radius=6))
    depth_smooth.save("assets/depth.png", "PNG", optimize=True)
    print("Saved wide-angle depth.png successfully")
