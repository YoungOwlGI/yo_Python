from skimage.io import imread
from skimage import color
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm  # 导入 tqdm
import time

# 记录开始时间
start_time = time.time()

# 读取图片并显示进度
print("正在读取图片...")
cimage = imread('image.png')
print("图片读取完成。")

# 如果图像是RGBA，则去掉A通道
if cimage.shape[2] == 4:
    cimage = cimage[:, :, :3]  # 保留前3个通道（R, G, B）

# 显示原图
fig, ax = plt.subplots(figsize=(20, 20))
ax.imshow(cimage)
ax.axis('off')
plt.show()  # 显示原图像

# RGB转为LAB
print("正在转换颜色空间为LAB...")
lab_img = color.rgb2lab(cimage)
x, y, _ = lab_img.shape

# 创建散点图数据
A_val = []
B_val = []
colors_map = cimage.reshape(-1, 3) / 256.0  # 归一化颜色

# 计算总像素数量
total_pixels = x * y

# 使用 tqdm 显示像素处理进度条
print("正在处理像素...")
with tqdm(total=total_pixels, desc="Processing Pixels") as pbar:
    for xi in range(x):
        for yi in range(y):
            A_val.append(lab_img[xi, yi][1])  # 提取 a* 通道
            B_val.append(lab_img[xi, yi][2])  # 提取 b* 通道
            pbar.update(1)  # 更新进度条，每处理一个像素更新一次

# 将提取的值转换为 numpy 数组
A_val = np.array(A_val)
B_val = np.array(B_val)

# 创建散点图
print("正在生成散点图...(时间可能较长，请耐心等待)")
plt.figure(figsize=(20, 20))
plt.scatter(A_val, B_val, c=colors_map, edgecolor='none')  # 添加边缘颜色
plt.xlabel("a* from green to red")
plt.ylabel("b* from blue to yellow")
plt.title('LAB Color Space Scatter Plot')
plt.axis('equal')  # 确保x轴与y轴比例相同
plt.show()

# 计算并显示总处理时间
end_time = time.time()
total_time = end_time - start_time
print(f"所有阶段完成，总花费时间: {total_time:.2f}秒")
