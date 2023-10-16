import numpy as np
import matplotlib.pyplot as plt

# 生成100个服从标准正态分布的随机样本
samples = np.random.randn(100)

# 绘制直方图
plt.hist(samples, bins=10, density=True, alpha=0.6, color='g')
plt.title('标准正态分布样本直方图')
plt.xlabel('值')
plt.ylabel('频率')
plt.grid(True)

# 显示图形
plt.show()