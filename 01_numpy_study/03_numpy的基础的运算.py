# @Time : 2020/1/19 15:37 
# @Author : Fioman 
# @Phone : 13149920693
import numpy as np

a = np.array([10,20,30,40])
b = np.arange(4).reshape((2,2))
print(a,b)

d = a * b
print(d)

b_dot = np.dot(a,b)
print(b_dot)