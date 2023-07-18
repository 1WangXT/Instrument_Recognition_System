# coding=utf-8
# 进行增强之前先跑一轮这个算法，把透明度丢掉，否则会报错
# 第一步先重命名，随后labelimg标注，完了以后跑这个算法，最后再进行数据增强
# 多次测试发现，对于读表任务来说，不增强的效果反而比较好
import os  # 打开文件时需要
from PIL import Image


class convert2RGB():
    def __init__(self, path):
        # 图片文件夹路径
        self.path = "../VOCdevkit/VOC2007/JPEGImages"  # 图片文件夹路径

    def convert(self):
        filelist = os.listdir(self.path)
        for item in filelist:
            if item.endswith('.jpg') or item.endswith('.png'):
                print(item)
                file = self.path + '/' + item
                im = Image.open(file)
                length = len(im.split())
                if length == 4:
                    r, g, b, a = im.split()
                    # im = img.convert('RGB')
                    im = Image.merge("RGB", (r, g, b))
                    os.remove(file)
                    im.save(file[:-4] + ".jpg")


if __name__ == '__main__':
    # 定义自己的路径
    imgPath = 'AUGimg'
    demo = convert2RGB(imgPath)
    demo.convert()
