import numpy as np
import PIL
from PIL import Image
import os
import platform
import math

Image.MAX_IMAGE_PIXELS = None

def txt_read(txtname):  #text 값 읽어오기
    f = open(txtname, "r")
    lines = f.readlines()

    return lines



def n_txt(img, n):

    img1 = Image.open("/home/hj/apple/apple_data/ver2/mix/train/" + img) #원본 이미지
    img_name = img.split(".")[0]
    img2 = Image.open(f'/home/hj/apple/apple_data/ver2/mix/0.3/{img_name}.jpg')
    tr =  img.split(".")[0] + ".txt"
    tr = txt_read("/home/hj/apple/apple_data/ver2/mix/train/" + tr)
    
    if len(tr) == 0:
        return None
    
    w1, h1 = img1.size
    w2, h2 = img2.size

    new_txt_data = []
    
    for txt_data in tr:
        txt_data = txt_data.split(" ")
        a= float(txt_data[1])   
        b= float(txt_data[2])   
        c= float(txt_data[3])   
        d= float(txt_data[4])   

        cx = ((a * w1) + (w2-w1)/2)/w2
        cy = ((b * h1) + (h2-h1)/2)/h2
        w = ((c * w1)/w2)
        h = ((d * h1)/h2)
        
        new_txt_data.append(f"{txt_data[0]} {cx:.5f} {cy:.5f} {w:.5f} {h:.5f}")
    
    with open(f'/home/hj/apple/apple_data/ver2/mix/0.3/{img_name}.txt', "w") as File:
        File.write("\n".join(new_txt_data))
    File.close


all_list = os.listdir('/home/hj/apple/apple_data/ver2/mix/train')
img_list = [i for i in all_list if "txt" not in i]

for i in img_list:
    n_txt(i, 0.3)
