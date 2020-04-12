# @Time : 2020/1/19 15:37 
# @Author : Fioman 
# @Phone : 13149920693
"""
图片的读取常用的有两种方式:
cv2.IMREAD_COLOR: 彩色图 3通道 默认是彩色图
cv2.IMREAD_GRAYSCALE: 灰度图 2通道
注意opencv读取图片的格式是BGR的格式,和RGB的顺序刚好是颠倒的
图片的写入
图片的显示
"""

import cv2
import numpy as np

image = cv2.imread('pic/cat.jpg')  # 默认是彩色图,image的格式是ndarray,数据类型是uint8
print(image)
print(image.shape, image.ndim, image.size, type(image), image.dtype)

# 显示图片
cv2.imshow('Color-Default',image)
cv2.waitKey(0)

# 读取灰度图
gray = cv2.imread('pic/cat.jpg',cv2.IMREAD_GRAYSCALE)
print(gray.shape,gray.ndim,gray.size,type(gray),gray.dtype)
print(gray)

# 显示图片
cv2.imshow('Gray',gray)
cv2.waitKey(0)
# shape 表示的是行数,列数,通道数. 也就是高,宽,以及通道数.

# 将两个图片相加,然后再显示和写入.

image_and = image - 20
cv2.imwrite("pic/mycat.png",image_and)
cv2.imshow("Add",image_and)
cv2.waitKey(0)

