# @Time : 2020/1/19 15:37 
# @Author : Fioman 
# @Phone : 13149920693
"""
cv2.VideoCapture 可以捕获摄像头,用数字来控制不同的设备,比如0,1
如果是视频文件,直接指定文件路径即可.

类似文件流,检查是否打开,可以使用isOpened()
然后再使用read()函数读取.视频读取完成,返回的frame为None的时候表示读取完成.
如果ret返回False,表示读取失败 0xFF 表示一个8位的2进制数,8个1
"""
import cv2

vc = cv2.VideoCapture("pic/test.mp4")

# 检查是否打开
open = vc.read() if vc.isOpened() else False

while open:
    ret, frame = vc.read()
    if frame is None:
        break
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('result', gray)

        if cv2.waitKey(100) & 0XFF == ord('q'):
            break

vc.release()
cv2.destroyAllWindows()
