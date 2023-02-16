import numpy as np
import PIL
from PIL import Image


img1 = "1step/black0613.JPG"
img2 = "1step/black0613_BG_10.jpg"


img = Image.open(img1)
BG_img = Image.open(img2)

    
h, w = img.size
bh, bw = BG_img.size

BG_img.paste(img, (int((bh-h)/2), int((bw-w)/2)))

print(BG_img.size)

BG_img.save("2step/0613_result_10.jpg")