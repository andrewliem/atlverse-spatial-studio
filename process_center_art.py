import os
from PIL import Image, ImageDraw, ImageFilter

gen_img_path = "/home/pandion/.gemini/antigravity/brain/fdc2fdd4-b2b0-4c6c-91ce-fd1f1a5be539/andrew_center_lab_1787657696627.jpg"

if os.path.exists(gen_img_path):
    img = Image.open(gen_img_path)
    img_1080 = img.resize((1920, 1080), Image.Resampling.LANCZOS)
    img_1080.save("assets/studio.png", "PNG", optimize=True)
    img_1080.save("assets/studio.jpg", "JPEG", quality=95)
    img.save("assets/atlverse_studio_hd.png", "PNG")
    print("Saved custom Atlverse studio assets from center.png likeness")

    W, H = 1920, 1080
    depth = Image.new("L", (W, H), 40) # Back wall depth
    ddraw = ImageDraw.Draw(depth)

    # 1. Window in Background (Skyline: 15 to 45)
    win_x1, win_y1, win_x2, win_y2 = int(W * 0.62), int(H * 0.08), int(W * 0.78), int(H * 0.74)
    ddraw.rectangle([win_x1, win_y1, win_x2, win_y2], fill=20)
    for bx in range(win_x1 + 20, win_x2, 60):
        ddraw.rectangle([bx, win_y2 - int(H * 0.40), bx + 45, win_y2], fill=42)

    # 2. Wall Portrait Frame (Andrew Tanny Liem from center.png) (Depth: 65 - 80)
    # x: 35% to 56%, y: 4% to 50%
    ddraw.rectangle([int(W * 0.35), int(H * 0.04), int(W * 0.56), int(H * 0.50)], fill=75)

    # 3. Left Bookshelf & Cabinet (Depth: 95 - 145)
    # Bookshelf upper levels (x: 0% to 26%, y: 3% to 68%)
    ddraw.rectangle([0, int(H * 0.03), int(W * 0.26), int(H * 0.68)], fill=115)
    # Diploma & Awards on shelf
    ddraw.rectangle([int(W * 0.04), int(H * 0.28), int(W * 0.18), int(H * 0.46)], fill=130)
    # Lower Cabinet (x: 0% to 26%, y: 68% to 100%)
    ddraw.rectangle([0, int(H * 0.68), int(W * 0.26), H], fill=165)

    # 4. Floor Gradient (Depth: 85 to 245)
    for y in range(int(H * 0.72), H):
        ratio = (y - H * 0.72) / (H * 0.28)
        val = int(85 + 160 * ratio)
        ddraw.line([(0, y), (W, y)], fill=val)

    # 5. Right Classroom Smart Blackboard (Depth: 135 - 175)
    # x: 78% to 100%, y: 24% to 92%
    ddraw.rectangle([int(W * 0.78), int(H * 0.24), W, int(H * 0.92)], fill=155)

    # 6. Reading Armchair (Depth: 190 - 225)
    # x: 81% to 99%, y: 65% to 98%
    ddraw.rectangle([int(W * 0.81), int(H * 0.65), int(W * 0.99), int(H * 0.98)], fill=210)

    # 7. AI Floating Bot (Depth: 170)
    ddraw.ellipse([int(W * 0.66), int(H * 0.55), int(W * 0.74), int(H * 0.69)], fill=175)

    # 8. Center Research Workstation & Desk (Depth: 180 - 240)
    desk_x1, desk_y1, desk_x2, desk_y2 = int(W * 0.26), int(H * 0.70), int(W * 0.70), int(H * 0.95)
    ddraw.rectangle([desk_x1, desk_y1, desk_x2, desk_y2], fill=215)
    ddraw.rectangle([desk_x1, desk_y1, desk_x2, desk_y1 + int(H * 0.08)], fill=235) # Desk top
    # Dual Monitors (Depth: 195)
    ddraw.rectangle([int(W * 0.36), int(H * 0.51), int(W * 0.64), int(H * 0.72)], fill=195)
    # Lamp on desk (Depth: 220)
    ddraw.rectangle([int(W * 0.27), int(H * 0.48), int(W * 0.37), int(H * 0.73)], fill=220)
    # PC Tower on floor (Depth: 230)
    ddraw.rectangle([int(W * 0.37), int(H * 0.78), int(W * 0.43), int(H * 0.96)], fill=230)

    depth_smooth = depth.filter(ImageFilter.GaussianBlur(radius=6))
    depth_smooth.save("assets/depth.png", "PNG", optimize=True)
    print("Saved precise depth.png successfully")
