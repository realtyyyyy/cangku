import numpy as np

# 创建数据矩阵
data = np.array([[1, -1, 4],
                 [2, 1, 3],
                 [1, 3, -1]])

# 计算协方差矩阵
C = np.cov(data)

# 输出协方差矩阵
print("协方差矩阵 C:")
print(C)