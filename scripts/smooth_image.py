from envtest import smooth_image

from skimage import data
import matplotlib.pyplot as plt


image = data.camera()   # 从 skimage 库里获取一张测试用的图片（相机拍摄的照片）
sigma = 5              # 定义平滑的强度参数 sigma，数字越大，图像越模糊

smoothed_image = smooth_image(image, sigma)  # 调用我们之前写的 smooth_image 函数，对图片进行高斯模糊

f = plt.figure()       # 创建一个新的图形窗口
f.add_subplot(1, 2, 1) # 在图形窗口创建一个1行2列的子图，激活第1个子图
plt.imshow(image)      # 显示原始图片
f.add_subplot(1, 2, 2) # 激活第2个子图
plt.imshow(smoothed_image) # 显示平滑处理后的图片
plt.show(block=True)   # 显示这个图形窗口，阻止程序继续执行直到关闭窗口
