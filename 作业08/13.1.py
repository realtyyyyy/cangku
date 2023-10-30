import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
# 加载鸢尾花数据集
iris = datasets.load_iris()
# 获取数据和标签
X = iris.data  # 特征数据
y = iris.target  # 类别标签
# 选择前两个特征进行可视化
feature1 = 0  # 花萼长度
feature2 = 1  # 花萼宽度

# 获取不同类别的索引
for target in np.unique(y):
    plt.scatter(X[y == target, feature1], X[y == target, feature2], label=iris.target_names[target])

plt.xlabel(iris.feature_names[feature1])
plt.ylabel(iris.feature_names[feature2])
plt.legend()
plt.title('Iris Dataset - 2D Feature Visualization')
plt.show()