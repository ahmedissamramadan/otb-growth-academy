import os
import glob
import re
import shutil

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"

# 1. Update style.css with dedicated phone & LTR isolation rules
css_path = os.path.join(BASE_DIR, "style.css")
if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        css_content = f.read()
    
    phone_css_rule = """
/* RTL PHONE NUMBER & NUMERIC ISOLATION (W3C / Unicode BiDi Best Practice) */
.phone-number,
.phone-link,
a[href^="tel:"],
bdi[dir="ltr"],
.ltr-text {
  direction: ltr !important;
  unicode-bidi: isolate !important;
  display: inline-block;
  text-align: left;
  font-family: var(--font-mono), var(--font-ar), sans-serif;
  letter-spacing: 0.5px;
}
"""
    if "RTL PHONE NUMBER" not in css_content:
        css_content += phone_css_rule
        with open(css_path, "w", encoding="utf-8") as f:
            f.write(css_content)
        print("Added RTL phone isolation rules to style.css")

# 2. Update all HTML files in BASE_DIR
html_files = glob.glob(os.path.join(BASE_DIR, "*.html"))
for hf in html_files:
    with open(hf, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Pattern to match raw tel links like <a href="tel:+201008080295">+20 100 808 0295</a>
    # Replace with <bdi dir="ltr"><a href="tel:+201008080295" class="phone-link">&lrm;+20 100 808 0295</a></bdi>
    pattern = r'<a href="tel:(\+?[0-9]+)">([^<]+)</a>'
    
    def repl(m):
        raw_num = m.group(1)
        display_num = m.group(2).replace('&lrm;', '').strip()
        return f'<bdi dir="ltr"><a href="tel:{raw_num}" class="phone-link">&lrm;{display_num}</a></bdi>'
    
    # Also handle if already partially wrapped
    content = re.sub(r'<bdi dir="ltr"><bdi dir="ltr">', '<bdi dir="ltr">', content)
    content = re.sub(r'</bdi></bdi>', '</bdi>', content)
    
    updated_content = re.sub(pattern, repl, content)
    
    with open(hf, "w", encoding="utf-8") as f:
        f.write(updated_content)
    print(f"Fixed phone numbers in {os.path.basename(hf)}")

# 3. Update build_awwwards_platform.py so future runs preserve this
awwwards_gen = os.path.join(BASE_DIR, "build_awwwards_platform.py")
if os.path.exists(awwwards_gen):
    with open(awwwards_gen, "r", encoding="utf-8") as f:
        gen_content = f.read()
    gen_content = gen_content.replace(
        '<a href="tel:+201008080295">+20 100 808 0295</a>',
        '<bdi dir="ltr"><a href="tel:+201008080295" class="phone-link">&lrm;+20 100 808 0295</a></bdi>'
    )
    with open(awwwards_gen, "w", encoding="utf-8") as f:
        f.write(gen_content)
    print("Updated build_awwwards_platform.py")

# 4. Synchronize to Downloads
if os.path.exists(DOWNLOADS_DIR):
    shutil.rmtree(DOWNLOADS_DIR)
shutil.copytree(BASE_DIR, DOWNLOADS_DIR)
print("Synchronized all files to Downloads!")
