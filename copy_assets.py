import os
import shutil

src_dir = "/Users/ahmedissamramadan/Documents/Unified_Ecosystem/05_Strategy/OTB_Agency/04_Assets_&_Media"
dst_dir = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy/assets"
os.makedirs(dst_dir, exist_ok=True)

for item in os.listdir(src_dir):
    if item.endswith(".jpg") or item.endswith(".png"):
        s = os.path.join(src_dir, item)
        d = os.path.join(dst_dir, item)
        shutil.copy2(s, d)
        print(f"Copied {item}")
