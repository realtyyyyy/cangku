import numpy as np

# 创建矩阵
matrix = np.array([[1, -1, 4],
                   [2, 1, 3],
                   [1, 3, -1]])

# 初始化一个随机向量作为初始估计的特征向量
v = np.random.rand(3)

# 设置迭代次数和收敛容限
max_iterations = 1000
tolerance = 1e-6

# 幂迭代法
for i in range(max_iterations):
    # 进行幂迭代
    Av = np.dot(matrix, v)

    # 更新估计的特征值
    eigenvalue = np.linalg.norm(Av)

    # 更新特征向量估计
    v = Av / eigenvalue

    # 计算收敛条件
    error = np.linalg.norm(Av - eigenvalue * v)

    # 如果满足收敛条件，退出循环
    if error < tolerance:
        break

# 输出特征值和特征向量
print("特征值:", eigenvalue)
print("特征向量:", v)