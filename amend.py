import os

def txt_read(txt): 
    f = open(txt, "r")
    lines = f.readlines()

    return lines


# 미완성
def amend(txt):
    
    dir = "new_file/"

    txt_name = txt.split(".")[0]
    txt = txt_read(dir + txt)

    n = int(len(txt)) #줄 개수
    

    for i in range(0, n-1):

        
        txt = txt[0].split(" ")

        ncls =int(txt[0]) + 1


        File = open(f"{txt_name}_new.txt", "w")
        print(f"{ncls} {txt[1]} {txt[2]} {txt[3]} {txt[4]}", file = File)
        
        File.close



def amend(txt):
    
    txt_name = txt.split(".")[0]
    txt = txt_read(txt)

    result_txt = ""


    n = int(len(txt)) #줄 개수
    
    for i in range(0, n):

        
        txt_ = txt[i].split(" ")

        ncls =int(txt_[0]) + 1
        result_txt += f"{ncls} {txt_[1]} {txt_[2]} {txt_[3]} {txt_[4]}"

    File = open(f"{txt_name}_new.txt", "w")
    print(result_txt, file=File)
    File.close



# 파이토닉하게 재작성한 함수
def amend2(txt):
    txt_name = txt.split(".")[0]

    dir = "img/"
    txt = txt_read(dir + txt)
    result_txt = ""

    for text_line in txt:
        result_txt += f"1{text_line[1:-1]}\n"

    #File = open(f"{txt_name}_new2.txt", "w")
    File = open(f"result/{txt_name}.txt", "w")
    print(result_txt, file=File)
    File.close




all_list = os.listdir('new_file')
txt_list = [i for i in all_list] 

for i in txt_list:
    amend2(i)