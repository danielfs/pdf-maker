import cv2, numpy as np, os, pathlib
from PIL import Image

files = os.listdir('.')
images = sorted([f for f in files if f.endswith('.jpg')])

pathlib.Path('output').mkdir(parents=True, exist_ok=True)

images_list = []

for i in images:
    img = cv2.imread(i)
    res = cv2.resize(img, dsize=(1080, 1440), interpolation=cv2.INTER_CUBIC)

    output_image_path = f"output/{i}"

    cv2.imwrite(output_image_path, res)

    images_list.append(Image.open(output_image_path).convert('RGB'))

images_list[0].save(f"output/Daniel Fernandes Silva.pdf", save_all=True, append_images=images_list[1:])
