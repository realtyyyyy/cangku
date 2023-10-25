import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# 加载鸢尾花数据集
iris = load_iris()
X, y = iris.data, iris.target

# 随机打乱数据
np.random.seed(42)  # 设置随机种子，以确保可重复性
indices = np.arange(len(X))
np.random.shuffle(indices)
X_shuffled = X[indices]
y_shuffled = y[indices]

# 划分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_shuffled, y_shuffled, test_size=0.3, random_state=42)

# 打印训练集和测试集的大小
print("训练集大小:", len(X_train))
print("测试集大小:", len(X_test))