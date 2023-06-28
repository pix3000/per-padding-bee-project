import numpy as np
import PIL
from PIL import Image
import os

Image.MAX_IMAGE_PIXELS = None

def add(img, n):

    dir_F = "img_old/"
    dir_B = f"1step/BG/{n}/"

    img_name  = img.split(".")[0] +'.jpg'

    img = Image.open(dir_F + img)    #apis0000.jpeg
    BG_img = Image.open(dir_B + img_name) #apis0000.jpg, 배경 이미지는 무조건 jpg로 고정

        
    h, w = img.size
    bh, bw = BG_img.size

    BG_img.paste(img, (int((bh-h)/2), int((bw-w)/2)))

    BG_img.save(f'2step/{n}/{img_name})





file_list = os.listdir('img_old')

file_list_2 = []

for file_name in file_list:
    if file_name[-3:] != "txt":
        file_list_2.append(file_name)



for file_name in file_list_2:
    add(file_name, 1)
    add(file_name, 3)
    add(file_name, 5)
    add(file_name, 10)
