import numpy as np

# 三维坐标初始化 ABCD 列表第一列为空值 验证
# 顺序  0 ABCD
# 自己设计一组 原始数据
x_lst = [0, 175/10-1, 0, 173/10, 174/10+1]
y_lst = [0, 99/10+1, 0, -100/10+1, 0]
z_lst = [0, 0.1, 0, 0.15, -0.15]


# 结果来自于"引理一可行性验证"代码运行结果
x_lst = [0, 16.519999999999996, 0, 17.3, 16.989999999999977]
y_lst = [0, 10.440000000000001, 0, -9.09, -1.29]
z_lst = [0, 0.1, 0, 0.15, 0.13]

#结果来自于“引理二可行性验证”代码运行结果
x_lst = [0, 16.519999999999996, 0, 17.3, 16.909999999999993]
y_lst = [0, 10.440000000000001, 0, -9.09, 0.6799999999999999]
z_lst = [0, 0.1, 0, 0.15, 0.12000000000000001]
## E 点数据 自行设计 用于检验引理三
x_lst.append(4.10)
y_lst.append(0.11)
z_lst.append(0.3)

x_lst_origin = tuple(x_lst)
y_lst_origin = tuple(y_lst)
z_lst_origin = tuple(z_lst)

print('原始坐标x', x_lst)
print('原始坐标y', y_lst)
print('原始坐标z',z_lst)

# 角度计算
def calculate_angle_dimension_3(x0, y0, z0, x1, y1, z1, x2, y2, z2):
    dis0 = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
    dis1 = (x2 - x0) ** 2 + (y2 - y0) ** 2 + (z2 - z0) ** 2
    dis2 = (x1 - x0) ** 2 + (y1 - y0) ** 2 + (z1 - z0) ** 2
    cos_angle = (dis2 + dis1 - dis0) / (2 * np.sqrt(dis1) * np.sqrt(dis2))
    angle = np.arccos(cos_angle)
    return angle / np.pi * 180


angleAEB = calculate_angle_dimension_3(x_lst[5], y_lst[5], z_lst[5], x_lst[1], y_lst[1], z_lst[1], x_lst[2],
                                     y_lst[2], z_lst[2])
angleBEC = calculate_angle_dimension_3(x_lst[5], y_lst[5], z_lst[5], x_lst[3], y_lst[3], z_lst[3], x_lst[2],
                                     y_lst[2], z_lst[2])
angleCEA = calculate_angle_dimension_3(x_lst[5], y_lst[5], z_lst[5], x_lst[1], y_lst[1], z_lst[1], x_lst[3],
                                     y_lst[3], z_lst[3])


def mid(x, y, z):
    if x != max(x, y, z) and x != min(x, y, z):
        return x
    elif y != max(x, y, z) and y != min(x, y, z):
        return y
    else:
        return z


# 原始角度
print('原始角度angleAEB,angleBEC,angleCEA', angleAEB,angleBEC,angleCEA)


# 调整E点 目标  三个 120度
def fE_120(p):
    angleAEB = calculate_angle_dimension_3(x_lst[5], y_lst[5], z_lst[5], x_lst[1], y_lst[1], z_lst[1], x_lst[2],
                                           y_lst[2], z_lst[2])
    angleBEC = calculate_angle_dimension_3(x_lst[5], y_lst[5], z_lst[5], x_lst[3], y_lst[3], z_lst[3], x_lst[2],
                                           y_lst[2], z_lst[2])
    angleCEA = calculate_angle_dimension_3(x_lst[5], y_lst[5], z_lst[5], x_lst[1], y_lst[1], z_lst[1], x_lst[3],
                                           y_lst[3], z_lst[3])
    objective_fE = (angleAEB - 120) ** 2 + (angleBEC - 120) ** 2 + (angleCEA - 120) ** 2
    objective_min_fE = objective_fE
    objective_fE_lst = []
    i_min = 10
    j_min = 10
    k_min = 10
    for i in range(0, 21):
        for j in range(0, 21):
            for k in range(0, 21):
                tmp_x = x_lst[p] + 0.01 * (i - 10)
                tmp_y = y_lst[p] + 0.01 * (j - 10)
                tmp_z = z_lst[p] + 0.01 * (k - 10)
                angleAEB = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z,x_lst[1], y_lst[1], z_lst[1],
                                                       x_lst[2],y_lst[2], z_lst[2])
                angleBEC = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z,x_lst[3], y_lst[3], z_lst[3],
                                                       x_lst[2], y_lst[2], z_lst[2])
                angleCEA = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z,x_lst[1], y_lst[1], z_lst[1],
                                                       x_lst[3],y_lst[3], z_lst[3])
                objective_tmpp = (angleAEB - 120) ** 2 + (angleBEC - 120) ** 2 + (angleCEA - 120) ** 2
                if objective_tmpp < objective_min_fE:
                    objective_min_fE = objective_tmpp
                    j_min = j
                    i_min = i
                    k_min = k
                    # angleD_acc = angleD
    x_lst[p] += 0.01 * (i_min - 10)
    y_lst[p] += 0.01 * (j_min - 10)
    z_lst[p] += 0.01 * (k_min - 10)
    # print('f', p, angleD_acc)



def test():
    for test_num in range(200):
        fE_120(5)

test()

# 调整结束  模型 验证

angleAEB = calculate_angle_dimension_3(x_lst[5], y_lst[5], z_lst[5], x_lst[1], y_lst[1], z_lst[1], x_lst[2],
                                     y_lst[2], z_lst[2])
angleBEC = calculate_angle_dimension_3(x_lst[5], y_lst[5], z_lst[5], x_lst[3], y_lst[3], z_lst[3], x_lst[2],
                                     y_lst[2], z_lst[2])
angleCEA = calculate_angle_dimension_3(x_lst[5], y_lst[5], z_lst[5], x_lst[1], y_lst[1], z_lst[1], x_lst[3],
                                     y_lst[3], z_lst[3])
print('调整后角度angleAEB,angleBEC,angleCEA', angleAEB,angleBEC,angleCEA)

print('调整后坐标x', x_lst)
print('调整后坐标y', y_lst)
print('调整后坐标z', z_lst)
