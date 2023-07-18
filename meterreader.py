import time
import tkinter as tk
from PIL import Image, ImageTk
import os

local = 0
def meter_reader(file_path):
    '''这个函数用来读表，把数据读进txt，需要传入detect输出的地址，在detect中是save_dir'''
    txt_dict = {}  # 创建字典
    file_read = open(file_path)  # 打开需要读取的txt文件

    for line in file_read.readlines():  # 遍历txt文件的每一行
        line = str(line).replace("\n", "")
        # 注意，必须是双引号
        # 后面的【1】表示取出来分割后的第二个值，如果改成0则是取得第一个值
        a = line.split(',', 1)[1]
        b = line.split(',', 1)[0]
        txt_dict[b] = a
        # txt_dict[line.split(',',1)[0]] = line.split(' ',1)[1]
        # line.split 用来得到 key 和 value，后面的【1】表示取出来分割后的第二个值，如果改成0则是取得第一个值

    # 字符转换，将str 转换成 int 方便排序
    for i in list(txt_dict.keys()):
        b = int(i)
        txt_dict[b] = txt_dict.pop(i)
    # 进行排序，将字典按照keys的大小重新排列，并将value的值按照key的大小顺序排好
    c = []
    for i in sorted(txt_dict):
        c.append(txt_dict[i])

    c = ''.join(c)
    file_read.close()

    return c


# -------------------------------简单的UI界面显示------------------------------------
def show_ui(img_file_path):
    '''传入的img_file_path是图片所在的目录地址，在yolo中为save_dir'''

    fname = os.listdir("F:/meters-read-and-detect/yolov5-5.0-new" + "\\" + str(img_file_path))  # 获取文件目录下的所有文件名
    b = fname[0]  # 提取文件名
    file = open("./read result/read result.txt", "r")
    # 打开文件的位置是meter_reader中保存读数的txt的位置
    # 创建一个UI窗口
    win = tk.Tk()
    win.title("read meter")
    win.geometry('1200x1000')
    img = Image.open("F:/meters-read-and-detect/yolov5-5.0-new" + "\\" + str(img_file_path) + "\\" + b)  # 把图片地址传入
    #  这里注意传进来的img_file_path不是str类型，需要进行转换，否则会报错，所以在这里使用str（）进行转换
    img1 = img.resize((800, 600))  # 把图像等比缩放，保证都可以在UI界面正常显示
    photo = ImageTk.PhotoImage(img1)
    plc = tk.Label(image=photo)
    plc.pack()
    # 读取txt文件中的内容，并写在UI界面上
    a = file.read()
    label = tk.Label(win, text="%s" % a, font=("times", 20), fg="black")
    label.pack()
    win.mainloop()
#  -------------------------------------------------------------------------------------------------
#  ----------------------------------小数点解决方案----------------------------------------------
#  1、可以训练的时候加入对meter类型的识别，同时在算法中实现针对不同类型的meter，在读数时根据数据自动加入小数点
#  2、写多几个算法，每个类型的表用专用的算法读，同样根据读数加入小数点，这样做可以不增加额外的训练
#  下面是一个小数点的demo
# c = [4,5,6,7]
# class_meter = "pressure meter"
#
# c = [3,4,5,7,8,9]
# class_meter = "water meter"
#
# if class_meter == "pressure meter": 假如压力表读书保留3位小数，当读数数据大于4位的时候在第一位后面加小数点
# 如果读数小于4位，则在第三位前面加0和小数点
#     if len(c) >= 4:
#         c.insert(1,'.')
#     else:
#         c.insert(0,0)
#         c.insert(1,'.')
# elif class_meter == "water meter": 假如是水表，只有最后一位数是小数，则直接在读数的最后一位数前加入小数点即可
#     c.insert(-1,'.')
# for i in c:
#   print(i,end="")
#  -----------------------------------------------------------------------------------------------
