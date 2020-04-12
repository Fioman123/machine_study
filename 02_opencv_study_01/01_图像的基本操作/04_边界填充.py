# @Time : 2020/1/19 15:37 
# @Author : Fioman 
# @Phone : 13149920693
"""
cv2.copyMakeBorder(image,top_size,bottom_size,left_size,right_size,boderType)
边界填充的时候,需要指定上下左右,需要填充的像素大小,也就是你要填充多少个像素.
也就是图像的放大的量化值,然后borderType就是你要使用的填充的方式,有如下几种:
复制法: BORDER_REPLICATE,复制最边缘像素
反射法: BORDER_REFLECT,对感兴趣的图像中的像素在两边进行复制例如：fedcba|abcdefgh|hgfedcb
排除边界的反射法法: BORDER_REFLECT_101: 也就是以最边缘像素为轴，对称，gfedcb|abcdefgh|gfedcba
外包装法: BORDER_WRAP: 外包装法cdefgh|abcdefgh|abcdefg
常量法: 指定一个value常数进行填充
"""
import cv2
from matplotlib import pyplot as plt

image = cv2.imread('pic/cat.jpg')

top_size, bottom_size, left_size, right_size = (50, 50, 50, 50)
replicate = cv2.copyMakeBorder(image,top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(image,top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(image,top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(image,top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(image,top_size, bottom_size, left_size, right_size,borderType=cv2.BORDER_CONSTANT,value=0)

# subplot() 就是这个意思 231 就是整个窗口分成2行3列,当前图像的位置在1
# 232 意思一样
plt.subplot(231),plt.imshow(image,'gray'),plt.title("ORIGINAL") # 整个图像窗口分成2行三列,当前图像位置为1
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title("REPLICATE") # 整个图像窗口分成2行三列,当前图像位置为2
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title("REFLECT")
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()





