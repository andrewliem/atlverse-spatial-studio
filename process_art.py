import os
from PIL import Image, ImageDraw, ImageFilter

gen_img_path = "/home/pandion/.gemini/antigravity/brain/fdc2fdd4-b2b0-4c6c-91ce-fd1f1a5be539/atlverse_studio_room_1787656801681.jpg"

if os.path.exists(gen_img_path):
    img = Image.open(gen_img_path)
    img = img.resize((1920, 1080), Image.Resampling.LANCZOS)
    img.save("assets/studio.png", "PNG", optimize=True)
    print("Saved high-res assets/studio.png")

    W, H = 1920, 1080
    depth = Image.new("L", (W, H), 35) # Back wall depth
    ddraw = ImageDraw.Draw(depth)

    # Window (Far)
    ddraw.rectangle([0, int(H * 0.08), int(W * 0.12), int(H * 0.72)], fill=10)

    # Wall posters (Mid-far: 60 - 75)
    # ATL VERSE Frame & side frames
    ddraw.rectangle([int(W * 0.44), int(H * 0.12), int(W * 0.58), int(H * 0.38)], fill=70) # Central ATL VERSE poster
    ddraw.rectangle([int(W * 0.36), int(H * 0.13), int(W * 0.43), int(H * 0.26)], fill=65) # Portrait
    ddraw.rectangle([int(W * 0.34), int(H * 0.28), int(W * 0.44), int(H * 0.39)], fill=65) # Diploma
    ddraw.rectangle([int(W * 0.60), int(H * 0.09), int(W * 0.69), int(H * 0.39)], fill=68) # City poster
    ddraw.rectangle([int(W * 0.71), int(H * 0.17), int(W * 0.84), int(H * 0.47)], fill=70) # 3D grid poster

    # Floor gradient (75 at wall to 240 at front)
    for y in range(int(H * 0.70), H):
        ratio = (y - H * 0.70) / (H * 0.30)
        val = int(80 + 160 * ratio)
        ddraw.line([(0, y), (W, y)], fill=val)

    # Bookshelf on left (110 - 145)
    ddraw.rectangle([int(W * 0.13), int(H * 0.16), int(W * 0.29), int(H * 0.92)], fill=125)
    # Hologram crystal on shelf
    ddraw.ellipse([int(W * 0.17), int(H * 0.43), int(W * 0.23), int(H * 0.55)], fill=155)

    # Desk & Workstation (165 - 210)
    ddraw.rectangle([int(W * 0.31), int(H * 0.63), int(W * 0.69), int(H * 0.95)], fill=180) # Desk body
    ddraw.rectangle([int(W * 0.31), int(H * 0.63), int(W * 0.69), int(H * 0.68)], fill=200) # Desk top

    # 3 Monitors (190)
    ddraw.rectangle([int(W * 0.30), int(H * 0.42), int(W * 0.69), int(H * 0.61)], fill=190)
    # Lamp & VR Headset on desk
    ddraw.rectangle([int(W * 0.34), int(H * 0.39), int(W * 0.42), int(H * 0.64)], fill=205) # Lamp
    ddraw.rectangle([int(W * 0.57), int(H * 0.59), int(W * 0.63), int(H * 0.65)], fill=215) # VR Headset

    # Right elements: Monstera plant, Electric Bass, Skateboard (140 - 230)
    ddraw.ellipse([int(W * 0.68), int(H * 0.62), int(W * 0.81), int(H * 0.92)], fill=160) # Monstera plant
    ddraw.rectangle([int(W * 0.78), int(H * 0.39), int(W * 0.88), int(H * 0.93)], fill=205) # Bass Guitar
    ddraw.rectangle([int(W * 0.89), int(H * 0.61), int(W * 0.96), int(H * 0.98)], fill=225) # Skateboard

    # Sleeping Cat on rug (Foreground: 250)
    ddraw.ellipse([int(W * 0.68), int(H * 0.88), int(W * 0.78), int(H * 0.97)], fill=248)

    depth_smooth = depth.filter(ImageFilter.GaussianBlur(radius=5))
    depth_smooth.save("assets/depth.png", "PNG", optimize=True)
    print("Saved high-res assets/depth.png")
