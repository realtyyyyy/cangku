import numpy as np

# 定义矩阵
matrix = np.array([[2, 1],
                   [4, 5]])

# 计算特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# 输出特征值和特征向量
print("特征值:")
print(eigenvalues)
print("\n特征向量:")
print(eigenvectors)