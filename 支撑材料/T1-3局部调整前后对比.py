import matplotlib.pyplot as plt
import numpy as np
theta_origin = [0, 40.1 / 180 * np.pi, 80.21 / 180 * np.pi, 119.75 / 180 * np.pi, 159.86 / 180 * np.pi,
                199.96 / 180 * np.pi, 240.07 / 180 * np.pi, 280.17 / 180 * np.pi, 320.28 / 180 * np.pi, 0]
radii_origin = [100, 98, 112, 105, 98, 112, 105, 98, 112, 100]
# 预处理之后 局部调整之前结果
theta_new = [ 0, 40.10/ 180 * np.pi, 80.21/ 180 * np.pi, 119.75/ 180 * np.pi, 159.86/ 180 * np.pi, 199.96/ 180 * np.pi, 240.07/ 180 * np.pi, 280.17/ 180 * np.pi, 320.28/ 180 * np.pi]
radii_new = [100, 99.93632293390803, 99.69178293027487, 100.75479540910527, 101.38545566398636, 99.60404550052611, 100.21153524192636, 100.24852533523602, 100.17667460519363]

# 局部调整完毕后的最终结果
theta_final_3 = [ 0, 40.00519109590449/ 180 * np.pi, 80.00752953377022/ 180 * np.pi, 120.00517736973678/ 180 * np.pi, 160.00125255454452/ 180 * np.pi, 200.0065961204145/ 180 * np.pi, 240.00635516989564/ 180 * np.pi, 280.00312223116225/ 180 * np.pi, 320.0043287618317/ 180 * np.pi]
radii_final_3 = [ 100.0, 99.99322691422431, 99.99692731511092, 99.99673434899272, 99.99589372790767, 99.99534161143691, 99.99861497102681, 100.00366684622732, 100.00554390657751]
theta_final_2 = [ 0, 40.001507829210176/ 180 * np.pi, 80.00188679482879/ 180 * np.pi, 119.99735046206672/ 180 * np.pi, 159.99586843265078/ 180 * np.pi, 199.99925214978813/ 180 * np.pi, 240.00139307145201/ 180 * np.pi, 279.99747986150595/ 180 * np.pi, 320.0006461137713/ 180 * np.pi]
radii_final_2 = [ 100.0, 100.00088698287816, 99.99866298763807, 100.00039430169991, 99.9993141654332, 100.00131768208384, 100.00361438544694, 100.00193031270435, 99.9978831830899]
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.figure(figsize=(15.0, 10.0))

plt.polar(theta_origin, radii_origin, marker='d', ms=0.6, ls=':')
plt.fill(theta_origin, radii_origin, color='yellow', alpha=0.2, label='原始位置')

plt.polar(theta_new, radii_new, marker='d', ms=0.6, ls=':')
plt.fill(theta_new, radii_new, color='blue', alpha=0.1, label='预处理后局部调整前位置')

plt.polar(theta_final_3, radii_final_3,marker='o', ms=0.6, ls=':',)
plt.fill(theta_final_3, radii_final_3, color='blue', alpha=0.3,label='每次选3个点局部调整')

plt.polar(theta_final_2, radii_final_2,marker='o', ms=0.6, ls=':',)
plt.fill(theta_final_2, radii_final_2, color='blue', alpha=0.3,label='每次选2个点局部调整')

plt.title('局部调整前后无人机位置变化示意图', pad=25, fontsize=15)
plt.legend(loc='upper right')
plt.savefig('.\\局部调整前后无人机位置变化示意图.png', dpi=1000)


plt.show()