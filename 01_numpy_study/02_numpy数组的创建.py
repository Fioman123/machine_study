# @Time : 2020/1/19 15:37 
# @Author : Fioman 
# @Phone : 13149920693
import numpy as np

a = np.array([2,23,4],dtype=np.float32) # 定义一维的array
print(a.dtype)

# 定义二维的array
a2 = np.array([[1,2,3],
               [4,5,6]])

# 生成一个全部是0的矩阵
a_zeros = np.zeros((3,4))
print(a_zeros,"dtype = {}".format(a_zeros.dtype)) # 默认的dtype是float64

# 使用arange生成数组.
a_range = np.arange(0,12,2)
print(a_range,'维度 = {},形状 = {}'.format(a_range.ndim,a_range.shape))

# 使用arange生成3行4列的矩阵
a_34 = np.arange(12).reshape((3,4))
print(a_34,'维度 = {},形状 = {}'.format(a_34.ndim,a_34.shape))

# 可以生成线断的一个数组.给出一个起点和终点,还有就是给出要生成多少段(也就是多少个数),就可以生成一个数组.
linspace = np.linspace(1,10,5)
print(linspace,type(linspace),linspace.dtype,linspace.shape)

linspace2 = np.linspace(2,20,3)
print(linspace2,type(linspace2),linspace2.dtype,linspace2.shape)

linspace3 = np.linspace(1,20,8).reshape((4,2)) # reshape的两个数的乘积一定要等于段数.
# 也就是说reshape之后的形状必须满足(a,b) a*b = 前面的linspace的段数8
print(linspace3,linspace3.ndim,linspace3.shape)

# 定义一个矩阵
a = np.array([[1,3,4],
              [2,5,6]])
print(a.dtype) # 默认创建的是 int32,如果全部是整数
b = np.array([[1,2,3],[2.1,3,4]]) # 如果 有一个是浮点类型,则创建的就是float的类型
print(b.dtype) # float64

zero_b = np.zeros((3,4))  # zeros 和 ones 创建的默认数据类型都是float
print(zero_b.shape,zero_b.dtype) # shape 3行4列.  dtype默认是float64

