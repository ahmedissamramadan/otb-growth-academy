import os, glob

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
from build_entire_enterprise_system import get_header

html_files = [
    "sprint.html", "masterclass.html", "prompts.html", 
    "case-studies.html", "quiz.html", "sops.html", "downloads.html"
]

for fname in html_files:
    fpath = os.path.join(BASE_DIR, fname)
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace header block
        import re
        new_hdr = get_header(fname).strip()
        # replace between <header class="navbar"> and </div class="podcast-strip"> (or equivalent)
        pat = r'<header class="navbar">.*?</audio>\s*</div>\s*</div>'
        updated = re.sub(pat, new_hdr, content, flags=re.DOTALL)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(updated)
        print(f"Updated header in {fname}")

# Sync to Downloads
import shutil
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"
if os.path.exists(DOWNLOADS_DIR):
    shutil.rmtree(DOWNLOADS_DIR)
shutil.copytree(BASE_DIR, DOWNLOADS_DIR)
print("Synchronized all updated files to Downloads!")
