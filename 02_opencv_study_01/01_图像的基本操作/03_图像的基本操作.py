# @Time : 2020/1/19 15:37 
# @Author : Fioman 
# @Phone : 13149920693
import cv2
import numpy as np

image = cv2.imread('pic/cat.jpg') # default 默认是彩色图片
cv2.imshow('Default',image)
cv2.waitKey(0)

# 截取部分图像,比如截取猫的两只眼睛.
eye = image[128:148,50:150]
cv2.imshow('Eye',eye)
cv2.waitKey(0)

# 颜色通道提取
B,G,R = cv2.split(image) # 提取之后降低维度了,全部变成灰度图了.
cv2.imshow('B',B)
cv2.imshow('G',G)
cv2.imshow('R',R)
cv2.waitKey(0)
print(B.shape,G.shape,R.shape) # (414, 500) (414, 500) (414, 500)

# 通道合并,如果只想显示单独的颜色,红,绿,蓝单独的显示出来,则可以用合并通道的方式,将另外的两个通道全部用0来代替就可以
zeros = np.zeros(image.shape[:2],dtype='uint8') # 这里的数据类型一定要指定,默认是float64
print(zeros.shape)

B1 = cv2.merge((B,zeros,zeros)) # 合并通道的时候是一个元组的形式
G1 = cv2.merge((zeros,G,zeros))
R1 = cv2.merge((zeros,zeros,R))

cv2.imshow('B1',B1)
cv2.imshow('G1',G1)
cv2.imshow('R1',R1)
cv2.waitKey(0)

# 合并为原图
original = cv2.merge((B,G,R))
cv2.imshow('Original',original)
cv2.waitKey(0)

# 同时也可以使用numpy,数组的操作方式进行分割
image_copy = image.copy()
image_copy[:,:,1] = 0
image_copy[:,:,2] = 0
cv2.imshow('B2',image_copy)
image_copy = image.copy()
image_copy[:,:,0] = 0
image_copy[:,:,2] = 0
cv2.imshow("G2",image_copy)
image_copy = image.copy()
image_copy[:,:,0] = 0
image_copy[:,:,1] = 0
cv2.imshow('R2',image_copy)
cv2.waitKey(0)

