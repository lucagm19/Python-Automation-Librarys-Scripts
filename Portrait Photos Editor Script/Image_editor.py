from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os
path = './imgs'
pathOut = './editedmgs'
MAX_SIDE = 2500 

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    img = ImageOps.exif_transpose(img)

    img = img.convert('RGB')
    img.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
    img = img.filter(ImageFilter.UnsharpMask(radius=1.0, percent=140, threshold=3))
    blurred = img.filter(ImageFilter.GaussianBlur(radius=1.0))
    img = Image.blend(img, blurred, alpha=0.12)
    img = ImageEnhance.Contrast(img).enhance(1.08)   # 1.05-1.20
    img = ImageEnhance.Brightness(img).enhance(1.02) # 0.98-1.08
    img = ImageEnhance.Color(img).enhance(1.06)

    edit = img
    clean_name = os.path.splitext(filename)[0]

    edit.save(f'{pathOut}/{clean_name}_edited.jpg')