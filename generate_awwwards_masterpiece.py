import os
import shutil
import json

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"

from generate_master_academy import COURSES_DATA

# Clean and structured JSON for embedded frontend script
courses_json = json.dumps(COURSES_DATA, ensure_ascii=False)

print("Preparing Awwwards-grade Minimal Luxury Masterpiece...")
