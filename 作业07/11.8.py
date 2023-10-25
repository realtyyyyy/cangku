import numpy as np
from sklearn.datasets import load_iris

# 加载鸢尾花数据集
iris = load_iris()
X, y = iris.data, iris.target

# 获取唯一的标签类别
unique_labels = np.unique(y)

# 初始化中心点列表
centroids = []

# 计算每个标签类别的中心点
for label in unique_labels:
    # 选择属于当前标签类别的数据点
    data_points = X[y == label]

    # 计算均值，即中心点
    centroid = np.mean(data_points, axis=0)
    centroids.append(centroid)

# 打印中心点
for i, centroid in enumerate(centroids):
    print(f"中心点 {i} (标签 {unique_labels[i]}): {centroid}")

# 计算每个数据点到中心点的欧氏距离
distances_to_centroids = [np.linalg.norm(x - centroids[y[i]]) for i, x in enumerate(X)]

# 打印数据点到中心点的欧氏距离
for i, distance in enumerate(distances_to_centroids):
    print(f"数据点 {i} 到中心点 {y[i]} 的欧氏距离: {distance}")