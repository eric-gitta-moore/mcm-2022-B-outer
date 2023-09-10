import numpy as np

# 三维坐标初始化 ABCD 列表第一列为空值 验证
# 顺序  0 ABCD
# 自己设计一组 原始数据
x_lst = [0, 175/10-1, 0, 173/10, 174/10+1]
y_lst = [0, 99/10+1, 0, -100/10+1, 0]
z_lst = [0, 0.1, 0, 0.15, -0.15]

x_lst_origin = tuple(x_lst)
y_lst_origin = tuple(y_lst)
z_lst_origin = tuple(z_lst)
print('原始坐标x',x_lst)
print('原始坐标y',y_lst)
print('原始坐标z',z_lst)

# 角度计算
def calculate_angle_dimension_3(x0, y0, z0, x1, y1, z1, x2, y2, z2):
    dis0 = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
    dis1 = (x2 - x0) ** 2 + (y2 - y0) ** 2 + (z2 - z0) ** 2
    dis2 = (x1 - x0) ** 2 + (y1 - y0) ** 2 + (z1 - z0) ** 2
    cos_angle = (dis2 + dis1 - dis0) / (2 * np.sqrt(dis1) * np.sqrt(dis2))
    angle = np.arccos(cos_angle)
    return angle / np.pi * 180


angle_BAC = calculate_angle_dimension_3(x_lst[1], y_lst[1], z_lst[1], x_lst[2], y_lst[2], z_lst[2], x_lst[3], y_lst[3],
                                        z_lst[3])
angle_BCA = calculate_angle_dimension_3(x_lst[3], y_lst[3], z_lst[3], x_lst[1], y_lst[1], z_lst[1], x_lst[2], y_lst[2],
                                        z_lst[2])
angleD = calculate_angle_dimension_3(x_lst[4], y_lst[4], z_lst[4], x_lst[1], y_lst[1], z_lst[1], x_lst[3],
                                     y_lst[3], z_lst[3])


def mid(x, y, z):
    if x != max(x, y, z) and x != min(x, y, z):
        return x
    elif y != max(x, y, z) and y != min(x, y, z):
        return y
    else:
        return z


# 原始角度
print('原始角度angle_BCA, angle_BAC, angleD',angle_BCA, angle_BAC, angleD)


# 调整D点 目标 角ADC=180
def fD_180(p):
    angleD = calculate_angle_dimension_3(x_lst[4], y_lst[4], z_lst[4], x_lst[1], y_lst[1], z_lst[1], x_lst[3],
                                         y_lst[3], z_lst[3])
    angleD_acc = angleD
    objective_fD = (angleD - 180) ** 2
    objective_min_fD = objective_fD
    objective_fD_lst = []
    i_min = 10
    j_min = 10
    k_min = 10
    for i in range(0, 21):
        for j in range(0, 21):
            for k in range(0, 21):
                tmp_x = x_lst[p] + 0.01 * (i - 10)
                tmp_y = y_lst[p] + 0.01 * (j - 10)
                tmp_z = z_lst[p] + 0.01 * (k - 10)
                angleD = calculate_angle_dimension_3(tmp_x, tmp_y, tmp_z, x_lst[1], y_lst[1], z_lst[1],
                                                     x_lst[3], y_lst[3], z_lst[3])
                objective_tmpp = (angleD - 180) ** 2
                if objective_tmpp < objective_min_fD:
                    objective_min_fD = objective_tmpp
                    j_min = j
                    i_min = i
                    k_min = k
                    angleD_acc = angleD
    x_lst[p] += 0.01 * (i_min - 10)
    y_lst[p] += 0.01 * (j_min - 10)
    z_lst[p] += 0.01 * (k_min - 10)
    # print('f', p, angleD_acc)



# 调整C点 目标 角BCA=60
def fC_60(p):
    angleC = calculate_angle_dimension_3(x_lst[3], y_lst[3], z_lst[3], x_lst[1], y_lst[1], z_lst[1], x_lst[2],
                                         y_lst[2], z_lst[2])
    angleDCA = calculate_angle_dimension_3(x_lst[3], y_lst[3], z_lst[3], x_lst[1], y_lst[1], z_lst[1], x_lst[4],
                                         y_lst[4], z_lst[4])
    angleC_acc = angleC
    objective_fC = (angleC - 60) ** 2 +(angleDCA-0)**2
    objective_min_fC = objective_fC
    objective_fC_lst = []
    i_min = 10
    j_min = 10
    k_min = 10
    for i in range(0, 21):
        for j in range(0, 21):
            for k in range(0, 21):
                tmp_x = x_lst[p] + 0.01 * (i - 10)
                tmp_y = y_lst[p] + 0.01 * (j - 10)
                tmp_z = z_lst[p] + 0.01 * (k - 10)
                angleC = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z, x_lst[1], y_lst[1], z_lst[1],
                                                     x_lst[2],
                                                     y_lst[2], z_lst[2])
                angleDCA = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z, x_lst[1], y_lst[1], z_lst[1],
                                                       x_lst[4],
                                                       y_lst[4], z_lst[4])
                objective_tmpp = (angleC - 60) ** 2 +(angleDCA-0)**2
                if objective_tmpp < objective_min_fC:
                    objective_min_fC = objective_tmpp
                    j_min = j
                    i_min = i
                    k_min = k
                    angleC_acc = angleC
    x_lst[p] += 0.01 * (i_min - 10)
    y_lst[p] += 0.01 * (j_min - 10)
    z_lst[p] += 0.01 * (k_min - 10)
    # print('f', p, angleC_acc)



# 调整C点 目标 角BAC=60 调用 p=1
def fA_60(p):
    angleA = calculate_angle_dimension_3(x_lst[p], y_lst[p], z_lst[p], x_lst[2], y_lst[2], z_lst[2], x_lst[3],
                                         y_lst[3], z_lst[3])
    angleDAC = calculate_angle_dimension_3(x_lst[p], y_lst[p], z_lst[p], x_lst[3], y_lst[3], z_lst[3], x_lst[4],
                                         y_lst[4], z_lst[4])
    angleA_acc = angleA
    objective_fA = (angleA - 60) ** 2 +(angleDAC-0)**2
    objective_min_fA = objective_fA
    objective_fA_lst = []
    i_min = 10
    j_min = 10
    k_min = 10
    for i in range(0, 21):
        for j in range(0, 21):
            for k in range(0, 21):
                tmp_x = x_lst[p] + 0.01 * (i - 10)
                tmp_y = y_lst[p] + 0.01 * (j - 10)
                tmp_z = z_lst[p] + 0.01 * (k - 10)
                angleA = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z, x_lst[2], y_lst[2], z_lst[2],
                                                     x_lst[3],
                                                     y_lst[3], z_lst[3])
                angleDAC = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z, x_lst[3], y_lst[3], z_lst[3],
                                                       x_lst[4],
                                                       y_lst[4], z_lst[4])
                objective_tmpp = (angleA - 60) ** 2 +(angleDAC-0)**2
                if objective_tmpp < objective_min_fA:
                    objective_min_fA = objective_tmpp
                    j_min = j
                    i_min = i
                    k_min = k
                    angleA_acc = angleA
    x_lst[p] += 0.01 * (i_min - 10)
    y_lst[p] += 0.01 * (j_min - 10)
    z_lst[p] += 0.01 * (k_min - 10)
    # print('f', p, angleA_acc)


def test():
    for test_num in range(30):
        fD_180(4)
    for test_num in range(30):
        fC_60(3)
    for test_num in range(30):
        fA_60(1)

test()

# 调整结束  模型 验证
angle_BAC = calculate_angle_dimension_3(x_lst[1], y_lst[1], z_lst[1], x_lst[2], y_lst[2], z_lst[2], x_lst[3], y_lst[3],
                                        z_lst[3])
angle_BCA = calculate_angle_dimension_3(x_lst[3], y_lst[3], z_lst[3], x_lst[1], y_lst[1], z_lst[1], x_lst[2], y_lst[2],
                                        z_lst[2])
angleD = calculate_angle_dimension_3(x_lst[4], y_lst[4], z_lst[4], x_lst[1], y_lst[1], z_lst[1], x_lst[3],
                                     y_lst[3], z_lst[3])
print('调整后角度angle_BCA, angle_BAC, angleD',angle_BCA, angle_BAC, angleD)

print('调整后坐标x',x_lst)
print('调整后坐标y',y_lst)
print('调整后坐标z',z_lst)

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin) * np.random.rand(n) + vmin


# np.random.rand(n)产生1*n数组，元素大小0-1

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')  # 可进行多图绘制

ax.scatter(list(x_lst_origin), list(y_lst_origin), list(z_lst_origin),c='orange')

from matplotlib.ticker import LinearLocator, FormatStrFormatter
ax.scatter(x_lst,y_lst,z_lst,c='purple')



ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
