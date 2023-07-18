#  这个算法是用来进行自动化图像处理的，可以对一个文件夹中的图像进行处理
#  具体效果是可以自动判断图像的亮暗，然后调用不同的算法对图像进行处理，让图像更清晰，方便后续的读数
import os
import cv2


def pic_process(read_path, save_path):
    """需要传入读取图片的路径和保存图片的路径"""
    # read_path = "/VOCdevkit/VOC2007/JPEGImages"  # 读取图片的路径
    # save_path = "F:/DEEPLEARNING/yolov5-5.0/VOCdevkit/VOC2007/1"  # 保存图片的路径
    for i in os.listdir(read_path):  # 批量读取 批量保存
        img = cv2.imread(read_path+"/"+i, 0)  # 读取顺便灰度化
        r, c = img.shape[:2]
        dark_sum = 0  # 偏暗的像素 初始化为0个
        dark_prop = 0  # 偏暗像素所占比例初始化为0
        piexs_sum = r * c  # 整个弧度图的像素个数为r*c
        for row in img:
            for colum in row:
                if colum < 40:  # 人为设置的超参数,表示0~39的灰度值为暗
                    dark_sum += 1
        dark_prop = dark_sum / piexs_sum
        if dark_prop >= 0.30:  # 人为设置的超参数:表示若偏暗像素所占比例超过0.30,调整这个参数 来调整判断图像亮暗的尺度
            print(" is dark!")  # 暗的图像
            equa = cv2.equalizeHist(img)
            result1 = cv2.GaussianBlur(equa, (3, 3), 3)
            cv2.imwrite(save_path+"/"+"%s" %i, result1)
            #  对于比较暗的图像，调用图像均衡化算法进行图片增强和高斯滤波去噪
        else:
            print(" is bright!")
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))  # 创建CLAHE对象
            dst = clahe.apply(img)  # 限制对比度的自适应阈值均衡化
            result = cv2.GaussianBlur(dst, (3, 3), 3)
            cv2.imwrite(save_path+"/"+"%s" %i, result)
            # 对于比较亮的图像 调用CLAHE 限制对比度的直方图均衡化进行图像处理，并采用高斯滤波去噪


pic_process(read_path="", save_path="")
# read_path = "/VOCdevkit/VOC2007/JPEGImages"  # 读取图片的路径
# save_path = "F:/DEEPLEARNING/yolov5-5.0/VOCdevkit/VOC2007/1"  # 保存图片的路径