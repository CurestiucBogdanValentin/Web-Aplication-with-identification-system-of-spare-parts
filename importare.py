
from PIL import Image, ImageOps
import numpy as np
import os, os.path

imgs = []
path = "D:/proba/"
valid_images = [".jpg",".gif",".png",".tga"]
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    imgs.append(Image.open(os.path.join(path,f)))