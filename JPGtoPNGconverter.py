import sys
from pathlib import Path
from PIL import Image
import os

folder_with_jpg = sys.argv[1]
folder_with_png = sys.argv[2]
Path(folder_with_png).mkdir(parents=True, exist_ok=True)
for file in os.listdir(folder_with_jpg):
    im = Image.open(f"{folder_with_jpg }/{file}")
    im.save(f"{folder_with_png}/{file.split('.')[0]}.png", "png")
