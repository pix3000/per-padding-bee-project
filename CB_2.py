import numpy as np
import PIL
from PIL import Image
import os
import platform
import math





def txt_read(txtname):  #text 값 읽어오기
    f = open(txtname, "r")
    lines = f.readlines()

    return lines


def img_crop(img):
    dir = "/home/hj/apple/apple_data/ver2/mix/val/"
    tr =  img.split(".")[0] + ".txt"
    
    global crop_img
    img = Image.open(dir + img)
    tr = txt_read(dir + tr)
    
    w,h  = img.size
    
    for i, txt_data in enumerate(tr):
        txt_data = txt_data.split(" ")
        
        try:
            a = float(txt_data[1])
            b = float(txt_data[2])
            c = float(txt_data[3])
            d = float(txt_data[4])
        except ValueError:
            print(f"Invalid data in {tr} -> \"{txt_data}\". Skipping this line.")
            continue

        a = float(w*a)
        b = float(h*b)
        c = float(w*c)
        d = float(h*d)

        x1 = a - (c/2)
        y1 = b - (d/2)
        x2 = x1 + c
        y2 = y1 + d

        crop_img = img.crop((x1, y1, x2, y2))
    
    return crop_img




def mk_bg(img, n): #배경 세밀화 과정(단색보다 더 디테일하도록)
    
    img_F = img_crop(img)

    h, w = img_F.size

    img_B = img_F.crop((0, 0, 10, 10)) #(0,0)에서 (20,20)까지 추출
    
    padding_area = (100*h*w)/n

    #save_len = int(math.sqrt(h*w))
    padding_len = int(math.sqrt(padding_area)) #997


    img_B = img_B.resize((int(padding_len), int(padding_len)))

    img_name =  img.split(".")[0]
    img_B = img_B.convert("RGB")
    #img_B.save(f'1step/BG/{n}/{img}_{n}.jpg')
    img_B.save(f'/home/hj/apple/apple_data/ver2/mix/BG/{img_name}.jpg')
    #img_F.save(f'1step/crop/{img}')

    

#file_list = os.listdir('img_old')
file_list = os.listdir('/home/hj/apple/apple_data/ver2/mix/val')

file_list_2 = []

for file_name in file_list:
    if file_name[-3:] != "txt":
        file_list_2.append(file_name)



for file_name in file_list_2:
    mk_bg(file_name, 0.3)
