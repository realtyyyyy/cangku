from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 加载鸢尾花数据集
iris = load_iris()
X = iris.data  # 特征数据
y = iris.target  # 类别标签

# 使用train_test_split方法划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 参数说明：
# X：特征数据
# y：类别标签
# test_size：指定测试集的大小，这里为0.2，表示20%的数据作为测试集
# random_state：可选参数，设置随机种子以确保可重复性

# 打印训练集和测试集的大小
print("训练集大小:", X_train.shape)
print("测试集大小:", X_test.shape)
# 创建KNN分类器
knn = KNeighborsClassifier(n_neighbors=3)  # 选择K值，这里设置为3

# 训练KNN模型
knn.fit(X_train, y_train)

# 在训练集上进行预测
y_train_pred = knn.predict(X_train)
train_accuracy = accuracy_score(y_train, y_train_pred)

# 在测试集上进行预测
y_test_pred = knn.predict(X_test)
test_accuracy = accuracy_score(y_test, y_test_pred)

# 打印训练集和测试集的准确度
print("训练集准确度:", train_accuracy)
print("测试集准确度:", test_accuracy)