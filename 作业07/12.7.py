import tensorflow as tf
from tensorflow.keras import layers, models

# 构建LeNet-5模型
model = models.Sequential()

# 第一层：卷积层1
model.add(layers.Conv2D(6, (5, 5), activation='relu', input_shape=(32, 32, 1)))
model.add(layers.MaxPooling2D((2, 2)))

# 第二层：卷积层2
model.add(layers.Conv2D(16, (5, 5), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

# 第三层：全连接层1
model.add(layers.Flatten())
model.add(layers.Dense(120, activation='relu'))

# 第四层：全连接层2
model.add(layers.Dense(84, activation='relu'))

# 输出层：全连接层3，对于分类问题通常使用softmax激活
model.add(layers.Dense(10, activation='softmax'))

# 打印模型结构
model.summary()