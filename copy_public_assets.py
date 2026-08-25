import os
import shutil

src_dir = "assets"
dst_dir = "public/assets"
os.makedirs(dst_dir, exist_ok=True)

for item in os.listdir(src_dir):
    s = os.path.join(src_dir, item)
    d = os.path.join(dst_dir, item)
    if os.path.isfile(s):
        shutil.copy(s, d)
        print(f"Copied {s} -> {d}")

print("Assets copied to public/assets successfully")
