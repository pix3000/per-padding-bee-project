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


    img1 = Image.open("img_old/" + img) #원본 이미지

    img_name = img.split(".")[0]

    img2 = Image.open(f"2step/{n}/{img_name}.jpg") #패딩한 이미지
    
    tr =  img.split(".")[0] + ".txt"

    tr = txt_read("img_old/" + tr)
    if len(tr) == 0:
        return None
        
    w1, h1 = img1.size
    w2, h2 = img2.size


    # for i, txt_data in enumerate(tr):
    txt_data = tr[0].split(" ")
    #txt_data = txt_data.split(" ")

    #try, except

    a= float(txt_data[1])   
    b= float(txt_data[2])   
    c= float(txt_data[3])   
    d= float(txt_data[4])   

    cx = (a * w1)/w2 + (w2-w1)/2
    cy = (b * h1)/h2 + (h2-h1)/2
    w = (c * w1)/w2
    h = (d * h1)/h2

    File = open(f"2step/{n}/{img_name}.txt", "w")
    print(f"{txt_data[0]} {cx} {cy} {w} {h}", file = File)
    File.close


#다시 상대값으로 바꾸자아아아

'''
    if cx < 0:
        print(txt_data[0], cx, cy, w, h)
        print(img)
        exit()

    File = open(f"2step/{n}/{img_name}.txt", "w")
    print(txt_data[0], cx, cy, w, h)
    File.close
'''

all_list = os.listdir('img_old')
img_list = [i for i in all_list if "txt" not in i] #리스트 컨프리헨션


# for i in os.listdir('img_old'):
for i in img_list:
    n_txt(i, 1)
    n_txt(i, 3)
    n_txt(i, 5)
    n_txt(i, 10)