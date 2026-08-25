import os
import shutil
from PIL import Image

src_gen = "/home/pandion/.gemini/antigravity/brain/fdc2fdd4-b2b0-4c6c-91ce-fd1f1a5be539/atlverse_original_studio_1787656933483.jpg"
target_dir = "/home/pandion/Documents/antigravity/lucid-bose/assets"
os.makedirs(target_dir, exist_ok=True)

if os.path.exists(src_gen):
    # 1. Save original full-resolution JPG
    shutil.copy(src_gen, os.path.join(target_dir, "atlverse_studio_original.jpg"))
    
    # 2. Save high-quality PNG
    img = Image.open(src_gen)
    img.save(os.path.join(target_dir, "atlverse_studio_hd.png"), "PNG")
    
    # 3. Save standard studio.png used by web app
    img_1080 = img.resize((1920, 1080), Image.Resampling.LANCZOS)
    img_1080.save(os.path.join(target_dir, "studio.png"), "PNG")
    img_1080.save(os.path.join(target_dir, "studio.jpg"), "JPEG", quality=95)

    print("All image formats saved successfully into assets/")
