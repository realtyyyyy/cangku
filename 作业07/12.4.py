import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# 加载鸢尾花数据集
iris = load_iris()
X, y = iris.data, iris.target

# 划分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 数据预处理：标准化
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 构建神经网络模型
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(4,)),  # 输入层
    tf.keras.layers.Dense(64, activation='relu'),  # 隐藏层1
    tf.keras.layers.Dense(32, activation='relu'),  # 隐藏层2
    tf.keras.layers.Dense(3, activation='softmax')  # 输出层，有3个类别
])

# 编译模型
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 训练模型
model.fit(X_train, y_train, epochs=100, verbose=2)

# 预测测试集
y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)

# 评估模型性能
accuracy = accuracy_score(y_test, y_pred_classes)
print("准确度:", accuracy)