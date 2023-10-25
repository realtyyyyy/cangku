import cv2
import numpy as np

# 读取图片
image = cv2.imread("your_image.jpg")

# 将图片转换为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 指定调整后的大小
new_size = (100, 100)  # 这里指定为100x100像素

# 调整图像大小
resized_image = cv2.resize(gray_image, new_size)

# 保存结果
cv2.imwrite("output_image.jpg", resized_image)

# 显示原始图像和处理后的图像
cv2.imshow("Original Image", image)
cv2.imshow("Resized Gray Image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()