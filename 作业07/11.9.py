import numpy as np
from sklearn.datasets import load_iris


def kmeans(X, k, max_iters=100):
    # 1. 随机选择初始中心点
    indices = np.random.choice(X.shape[0], k, replace=False)
    centroids = X[indices]

    for _ in range(max_iters):
        # 2. 分配数据点到最近的中心点
        distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
        labels = np.argmin(distances, axis=1)

        # 3. 重新计算中心点
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])

        # 判断中心点是否发生变化
        if np.all(centroids == new_centroids):
            break

        centroids = new_centroids

    return labels, centroids


# 加载鸢尾花数据集
iris = load_iris()
X = iris.data

# 使用K-means进行聚类
k = 3
labels, centroids = kmeans(X, k)

# 打印结果
for i, centroid in enumerate(centroids):
    print(f"中心点 {i}: {centroid}")

for i, label in enumerate(labels):
    print(f"数据点 {i} 分配到中心点 {label}")