import matplotlib.pyplot as plt
import numpy as np

R = 100
r = [100] * 8
theta = [40.10, 80.21, 119.75, 159.86, 199.96, 240.07, 280.17, 320.28]
theta_positive = theta[0:4]
alpha_positive = [70, 50, 30, 10]
beta_positive = [0] * 4
theta_negative = theta[4:]
alpha_negative = [10, 30, 50, 70]
beta_negative = [0] * 4
for i in range(4):
    beta_positive[i] = 180 - alpha_positive[i] - theta_positive[i]
    r[i] = R * np.sin(beta_positive[i] / 180 * np.pi) / np.sin(alpha_positive[i] / 180 * np.pi)
    beta_negative[i] = -alpha_negative[i] - 180 + theta_negative[i]
    r[i + 4] = R * np.sin(beta_negative[i] / 180 * np.pi) / np.sin(alpha_negative[i] / 180 * np.pi)
print(r)

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.figure(figsize=(10.0, 8.0))
theta_origin = [0, 40.1 / 180 * np.pi, 80.21 / 180 * np.pi, 119.75 / 180 * np.pi, 159.86 / 180 * np.pi,
                199.96 / 180 * np.pi, 240.07 / 180 * np.pi, 280.17 / 180 * np.pi, 320.28 / 180 * np.pi, 0]
radii_origin = [100, 98, 112, 105, 98, 112, 105, 98, 112, 100]

theta_new=[0]
for item in theta_origin:
    theta_new.append(item)
theta_new.append(0)
theta_new = theta_origin
radii_new = [100]
for item in r:
    radii_new.append(item)
radii_new.append(100)
print(radii_new)

# 绘制第一个极坐标图
plt.polar(theta_new, radii_new, marker='d', ms=6, ls=':')
plt.fill(theta_new, radii_new, color='blue', alpha=0.2, label='预处理调整后位置')
plt.polar(theta_origin, radii_origin,marker='o', ms=8, ls=':',)
plt.fill(theta_origin, radii_origin, color='yellow', alpha=0.1,label='给定初始位置')

colors = 8 * np.random.rand(1)
c = plt.scatter([0], [0], c=colors, s=100, cmap='hsv', alpha=0.75)

plt.title('预处理前后无人机位置变化示意图', pad=25, fontsize=15)
plt.legend(bbox_to_anchor=(1.3, 1))

plt.show()
