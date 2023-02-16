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



def img_crop(img, txt): #GT만큼 자르기


    img = Image.open(img)
    
    w,h  = img.size

    txt_data = txt_read(txt)

    txt_data = txt_data[0].split(" ")

    a= float(txt_data[1])   
    b= float(txt_data[2])   
    c= float(txt_data[3])   
    d= float(txt_data[4])   

    a= float(w*a)     #상대값 -> 절대값
    b= float(h*b)
    c= float(w*c)
    d= float(h*d)

    x1 = a - (c/2)
    y1 = b - (d/2)
    x2 = x1 + c
    y2 = y1 + d

    crop_img = img.crop((x1, y1, x2, y2))


    return crop_img



def mk_bg(img, txt, n): #배경 세밀화 과정(단색보다 더 디테일하도록)

    img_F = img_crop(img, txt)

    h, w = img_F.size

    img_B = img_F.crop((0, 0, 20, 20)) #(0,0)에서 (20,20)까지 추출
    
    padding_area = (100*h*w)/n

    #save_len = int(math.sqrt(h*w))
    padding_len = int(math.sqrt(padding_area)) #997


    img_B = img_B.resize((int(padding_len), int(padding_len)))


    return img_B



'''
def padding(img, txt, n):   #원본 이미지와 배경 이미지 결합
    
    img = img_crop(img, txt)
    
    h, w = img.size
    BG_img = mk_bg(img, txt, n)

    bh, bw = BG_img.size

    result_img = BG_img.paste(img, (int((bh-h)/2), int((bw-w)/2)))


    return result_img

'''

img = "img_old/black0613.JPG"
txt = "img_old/black0613.txt"

img_crop(img, txt).save("1step/black0613_crop.jpg")
mk_bg(img, txt, 1).save("1step/black0613_BG_1.jpg")
mk_bg(img, txt, 3).save("1step/black0613_BG_3.jpg")
mk_bg(img, txt, 5).save("1step/black0613_BG_5.jpg")
mk_bg(img, txt, 10).save("1step/black0613_BG_10.jpg")