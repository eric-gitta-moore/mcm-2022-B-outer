import numpy as np

# 三维坐标初始化 ABCD 列表第一列为空值 验证
# 顺序  0 ABCD
# 自己设计一组 原始数据
x_lst = [0, 100*np.sqrt(3), 75*np.sqrt(3),75*np.sqrt(3), 50*np.sqrt(3), 50*np.sqrt(3), 50*np.sqrt(3), 25*np.sqrt(3), 25*np.sqrt(3), 25*np.sqrt(3), 25*np.sqrt(3),0,0,0,0,0]
y_lst = [0, 0,25,-25,50,0,-50,75,25,-25,-75,100,50,0,-50,-100]
z_lst = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(1,16):
    x_lst[i] += float(np.random.uniform(-1, 1, 1))
    y_lst[i] += float(np.random.uniform(-1, 1, 1))
    z_lst[i] += float(np.random.uniform(-1, 1, 1))


# 利用上述方法随机生成 接股票
x_lst =  [0, 172.5849703361308, 130.31053186487503, 129.8999963197148, 87.40951707533729, 86.73545784686141, 86.42219856743965, 43.238240083571775, 43.537671588762926, 42.907286891592236, 44.11251663622844, 0.9524770522945771, -0.1031730146858596, -0.5529740507383931, 0.9332149292996521, 0.5418555762004413]
y_lst = [0, 0.9743774126537483, 24.913086330612813, -25.876708996208606, 50.12316376755098, 0.9951782205496467, -49.52174747162192, 74.01871209180575, 24.16558240521679, -24.879408055333283, -74.73222042176403, 100.47725589932327, 49.4965680599237, -0.9345715613262222, -49.18974689256766, -100.58430167340168]
z_lst = [0, 0.11417707355129991, 0.49355928755122647, -0.14568634413313086, -0.07856198814204896, -0.8102178515140541, -0.7485911377795991, 0.7737870283715225, 0.7855557667588986, -0.22617781561841177, -0.5406072425582142, -0.5414806627246775, -0.2270074255766248, -0.15826725127853036, -0.0203398482543673, 0.7177759516825288]
'''
移动13 11_13_15_180
移动11 15_11_1_60 15_11_13_0
移动15 11_15_1_60 11_15_13_0
移动 12 13 14 p
    11_p_15_180
    11_p_1_theta
移动 3 6 10 p
移动 2 4 7 p
移动 8 8_120
移动 5 5_120
移动 9 9_120
'''
# 15个点调整

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


def mid(x, y, z):
    if x != max(x, y, z) and x != min(x, y, z):
        return x
    elif y != max(x, y, z) and y != min(x, y, z):
        return y
    else:
        return z



def f13(p):
    angle= calculate_angle_dimension_3(x_lst[13], y_lst[13], z_lst[13], x_lst[11], y_lst[11], z_lst[11], x_lst[15],
                                           y_lst[15], z_lst[15])
    angle_acc = angle
    objective_f = (angle - 180) ** 2
    objective_min_f = objective_f
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
                angle = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z, x_lst[11], y_lst[11], z_lst[11], x_lst[15],
                                           y_lst[15], z_lst[15])
                objective_tmpp = (angle - 180) ** 2
                if objective_tmpp < objective_min_f:
                    objective_min_f = objective_tmpp
                    j_min = j
                    i_min = i
                    k_min = k
                    angle_acc = angle
    x_lst[p] += 0.01 * (i_min - 10)
    y_lst[p] += 0.01 * (j_min - 10)
    z_lst[p] += 0.01 * (k_min - 10)
    print('f', p, angle_acc)

def f11(p):
    angle1 = calculate_angle_dimension_3(x_lst[p], y_lst[p], z_lst[p], x_lst[1], y_lst[1], z_lst[1], x_lst[15],
                                         y_lst[15], z_lst[15])
    angle2 = calculate_angle_dimension_3(x_lst[p], y_lst[p], z_lst[p], x_lst[13], y_lst[13], z_lst[13], x_lst[15],
                                         y_lst[15], z_lst[15])
    angle1_acc = angle1
    angle2_acc = angle2
    objective_f = (angle1-60) ** 2 +(angle2-0)**2
    objective_min_f = objective_f
    i_min = 10
    j_min = 10
    k_min = 10
    for i in range(0, 21):
        for j in range(0, 21):
            for k in range(0, 21):
                tmp_x = x_lst[p] + 0.01 * (i - 10)
                tmp_y = y_lst[p] + 0.01 * (j - 10)
                tmp_z = z_lst[p] + 0.01 * (k - 10)
                angle1 = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z, x_lst[1], y_lst[1], z_lst[1],
                                                     x_lst[15], y_lst[15], z_lst[15])
                angle2 = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z, x_lst[13], y_lst[13], z_lst[13],
                                                     x_lst[15],y_lst[15], z_lst[15])
                objective_tmpp = (angle1 - 60) ** 2 +(angle2-0)**2
                if objective_tmpp < objective_min_f:
                    objective_min_f = objective_tmpp
                    j_min = j
                    i_min = i
                    k_min = k
                    angle1_acc = angle1
                    angle2_acc = angle2
    x_lst[p] += 0.01 * (i_min - 10)
    y_lst[p] += 0.01 * (j_min - 10)
    z_lst[p] += 0.01 * (k_min - 10)
    print('f', p, angle1_acc,angle2_acc)


def f15(p):
    angle1 = calculate_angle_dimension_3(x_lst[p], y_lst[p], z_lst[p], x_lst[1], y_lst[1], z_lst[1], x_lst[11],
                                         y_lst[11], z_lst[11])
    angle2 = calculate_angle_dimension_3(x_lst[p], y_lst[p], z_lst[p], x_lst[13], y_lst[13], z_lst[13], x_lst[11],
                                         y_lst[11], z_lst[11])
    angle1_acc = angle1
    angle2_acc = angle2
    objective_f = (angle1-60) ** 2 +(angle2-0)**2
    objective_min_f = objective_f
    i_min = 10
    j_min = 10
    k_min = 10
    for i in range(0, 21):
        for j in range(0, 21):
            for k in range(0, 21):
                tmp_x = x_lst[p] + 0.01 * (i - 10)
                tmp_y = y_lst[p] + 0.01 * (j - 10)
                tmp_z = z_lst[p] + 0.01 * (k - 10)
                angle1 = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z, x_lst[1], y_lst[1], z_lst[1],
                                                     x_lst[11], y_lst[11], z_lst[11])
                angle2 = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z, x_lst[13], y_lst[13], z_lst[13],
                                                     x_lst[11],y_lst[11], z_lst[11])
                objective_tmpp = (angle1 - 60) ** 2 +(angle2-0)**2
                if objective_tmpp < objective_min_f:
                    objective_min_f = objective_tmpp
                    j_min = j
                    i_min = i
                    k_min = k
                    angle1_acc = angle1
                    angle2_acc = angle2
    x_lst[p] += 0.01 * (i_min - 10)
    y_lst[p] += 0.01 * (j_min - 10)
    z_lst[p] += 0.01 * (k_min - 10)
    print('f', p, angle1_acc,angle2_acc)


def f12_13_14(p):
    angle1 = calculate_angle_dimension_3(x_lst[p], y_lst[p], z_lst[p], x_lst[1], y_lst[1], z_lst[1], x_lst[11],
                                         y_lst[11], z_lst[11])
    angle2 = calculate_angle_dimension_3(x_lst[p], y_lst[p], z_lst[p], x_lst[15], y_lst[15], z_lst[15], x_lst[11],
                                         y_lst[11], z_lst[11])
    angle1_acc = angle1
    angle2_acc = angle2
    if p==13:
        objective_f = (angle1-90) ** 2 +(angle2-180)**2
    elif p==12:
        objective_f = (angle1 - 106.10211) ** 2 + (angle2 - 180) ** 2
    elif p==14:
        objective_f = (angle1 - 73.89789) ** 2 + (angle2 - 180) ** 2
    objective_min_f = objective_f
    i_min = 10
    j_min = 10
    k_min = 10
    for i in range(0, 21):
        for j in range(0, 21):
            for k in range(0, 21):
                tmp_x = x_lst[p] + 0.01 * (i - 10)
                tmp_y = y_lst[p] + 0.01 * (j - 10)
                tmp_z = z_lst[p] + 0.01 * (k - 10)
                angle1 = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z, x_lst[1], y_lst[1], z_lst[1],
                                                     x_lst[11], y_lst[11], z_lst[11])
                angle2 = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z, x_lst[15], y_lst[15], z_lst[15],
                                                     x_lst[11],y_lst[11], z_lst[11])
                if p == 13:
                    objective_tmpp = (angle1 - 90) ** 2 + (angle2 - 180) ** 2
                elif p == 12:
                    objective_tmpp = (angle1 - 106.10211) ** 2 + (angle2 - 180) ** 2
                elif p == 14:
                    objective_tmpp = (angle1 - 73.89789) ** 2 + (angle2 - 180) ** 2
                if objective_tmpp < objective_min_f:
                    objective_min_f = objective_tmpp
                    j_min = j
                    i_min = i
                    k_min = k
                    angle1_acc = angle1
                    angle2_acc = angle2
    x_lst[p] += 0.01 * (i_min - 10)
    y_lst[p] += 0.01 * (j_min - 10)
    z_lst[p] += 0.01 * (k_min - 10)
    print('f', p, angle1_acc,angle2_acc)

def f3_6_10(p):
    angle1 = calculate_angle_dimension_3(x_lst[p], y_lst[p], z_lst[p], x_lst[1], y_lst[1], z_lst[1], x_lst[11],
                                         y_lst[11], z_lst[11])
    angle2 = calculate_angle_dimension_3(x_lst[p], y_lst[p], z_lst[p], x_lst[1], y_lst[1], z_lst[1], x_lst[15],
                                         y_lst[15], z_lst[15])
    angle1_acc = angle1
    angle2_acc = angle2
    if p==6:
        objective_f = (angle1-90) ** 2 +(angle2-180)**2
    elif p==3:
        objective_f = (angle1 - 106.10211) ** 2 + (angle2 - 180) ** 2
    elif p==10:
        objective_f = (angle1 - 73.89789) ** 2 + (angle2 - 180) ** 2
    objective_min_f = objective_f
    i_min = 10
    j_min = 10
    k_min = 10
    for i in range(0, 21):
        for j in range(0, 21):
            for k in range(0, 21):
                tmp_x = x_lst[p] + 0.01 * (i - 10)
                tmp_y = y_lst[p] + 0.01 * (j - 10)
                tmp_z = z_lst[p] + 0.01 * (k - 10)
                angle1 = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z, x_lst[1], y_lst[1], z_lst[1],
                                                     x_lst[11], y_lst[11], z_lst[11])
                angle2 = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z, x_lst[15], y_lst[15], z_lst[15],
                                                     x_lst[1],y_lst[1], z_lst[1])
                if p == 6:
                    objective_tmpp = (angle1 - 90) ** 2 + (angle2 - 180) ** 2
                elif p == 3:
                    objective_tmpp = (angle1 - 106.10211) ** 2 + (angle2 - 180) ** 2
                elif p == 10:
                    objective_tmpp = (angle1 - 73.89789) ** 2 + (angle2 - 180) ** 2
                if objective_tmpp < objective_min_f:
                    objective_min_f = objective_tmpp
                    j_min = j
                    i_min = i
                    k_min = k
                    angle1_acc = angle1
                    angle2_acc = angle2
    x_lst[p] += 0.01 * (i_min - 10)
    y_lst[p] += 0.01 * (j_min - 10)
    z_lst[p] += 0.01 * (k_min - 10)
    print('f', p, angle1_acc,angle2_acc)



def f2_4_7(p):
    angle1 = calculate_angle_dimension_3(x_lst[p], y_lst[p], z_lst[p], x_lst[1], y_lst[1], z_lst[1], x_lst[15],
                                         y_lst[15], z_lst[15])
    angle2 = calculate_angle_dimension_3(x_lst[p], y_lst[p], z_lst[p], x_lst[1], y_lst[1], z_lst[1], x_lst[11],
                                         y_lst[11], z_lst[11])
    angle1_acc = angle1
    angle2_acc = angle2
    if p==4:
        objective_f = (angle1-90) ** 2 +(angle2-180)**2
    elif p==2:
        objective_f = (angle1 - 106.10211) ** 2 + (angle2 - 180) ** 2
    elif p==7:
        objective_f = (angle1 - 73.89789) ** 2 + (angle2 - 180) ** 2
    objective_min_f = objective_f
    i_min = 10
    j_min = 10
    k_min = 10
    for i in range(0, 21):
        for j in range(0, 21):
            for k in range(0, 21):
                tmp_x = x_lst[p] + 0.01 * (i - 10)
                tmp_y = y_lst[p] + 0.01 * (j - 10)
                tmp_z = z_lst[p] + 0.01 * (k - 10)
                angle1 = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z, x_lst[1], y_lst[1], z_lst[1],
                                                     x_lst[15], y_lst[15], z_lst[15])
                angle2 = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z, x_lst[1], y_lst[1], z_lst[1],
                                                     x_lst[11],y_lst[11], z_lst[11])
                if p == 4:
                    objective_tmpp = (angle1 - 90) ** 2 + (angle2 - 180) ** 2
                elif p == 2:
                    objective_tmpp = (angle1 - 106.10211) ** 2 + (angle2 - 180) ** 2
                elif p == 7:
                    objective_tmpp = (angle1 - 73.89789) ** 2 + (angle2 - 180) ** 2
                if objective_tmpp < objective_min_f:
                    objective_min_f = objective_tmpp
                    j_min = j
                    i_min = i
                    k_min = k
                    angle1_acc = angle1
                    angle2_acc = angle2
    x_lst[p] += 0.01 * (i_min - 10)
    y_lst[p] += 0.01 * (j_min - 10)
    z_lst[p] += 0.01 * (k_min - 10)
    print('f', p, angle1_acc,angle2_acc)



# 调整目标  三个 120度
def f8(p):
    angle1 = calculate_angle_dimension_3(x_lst[p], y_lst[p], z_lst[p], x_lst[11], y_lst[11], z_lst[11], x_lst[2],
                                           y_lst[2], z_lst[2])
    angle2 = calculate_angle_dimension_3(x_lst[p], y_lst[p], z_lst[p], x_lst[14], y_lst[14], z_lst[14], x_lst[2],
                                           y_lst[2], z_lst[2])
    angle3 = calculate_angle_dimension_3(x_lst[p], y_lst[p], z_lst[p], x_lst[11], y_lst[11], z_lst[11], x_lst[14],
                                           y_lst[14], z_lst[14])
    objective_f = (angle1 - 120) ** 2 + (angle2 - 120) ** 2 + (angle3 - 120) ** 2
    angle1_acc =angle1
    angle2_acc = angle2
    angle3_acc = angle3
    objective_min_f = objective_f
    i_min = 10
    j_min = 10
    k_min = 10
    for i in range(0, 21):
        for j in range(0, 21):
            for k in range(0, 21):
                tmp_x = x_lst[p] + 0.01 * (i - 10)
                tmp_y = y_lst[p] + 0.01 * (j - 10)
                tmp_z = z_lst[p] + 0.01 * (k - 10)
                angle1 = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z, x_lst[11], y_lst[11], z_lst[11],
                                                     x_lst[2],
                                                     y_lst[2], z_lst[2])
                angle2 = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z, x_lst[14], y_lst[14], z_lst[14],
                                                     x_lst[2],
                                                     y_lst[2], z_lst[2])
                angle3 = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z,  x_lst[11], y_lst[11], z_lst[11],
                                                     x_lst[14],
                                                     y_lst[14], z_lst[14])
                objective_tmpp = (angle1 - 120) ** 2 + (angle2 - 120) ** 2 + (angle3 - 120) ** 2
                if objective_tmpp < objective_min_f:
                    objective_min_f = objective_tmpp
                    j_min = j
                    i_min = i
                    k_min = k
                    angle1_acc = angle1
                    angle2_acc = angle2
                    angle3_acc = angle3
    x_lst[p] += 0.01 * (i_min - 10)
    y_lst[p] += 0.01 * (j_min - 10)
    z_lst[p] += 0.01 * (k_min - 10)
    print('f', p, angle1_acc,angle2_acc,angle3_acc)


def f5(p):
    angle1 = calculate_angle_dimension_3(x_lst[p], y_lst[p], z_lst[p], x_lst[1], y_lst[1], z_lst[1], x_lst[7],
                                           y_lst[7], z_lst[7])
    angle2 = calculate_angle_dimension_3(x_lst[p], y_lst[p], z_lst[p], x_lst[1], y_lst[1], z_lst[1], x_lst[10],
                                           y_lst[10], z_lst[10])
    angle3 = calculate_angle_dimension_3(x_lst[p], y_lst[p], z_lst[p], x_lst[7], y_lst[7], z_lst[7], x_lst[10],
                                           y_lst[10], z_lst[10])
    objective_f = (angle1 - 120) ** 2 + (angle2 - 120) ** 2 + (angle3 - 120) ** 2
    angle1_acc =angle1
    angle2_acc = angle2
    angle3_acc = angle3
    objective_min_f = objective_f
    i_min = 10
    j_min = 10
    k_min = 10
    for i in range(0, 21):
        for j in range(0, 21):
            for k in range(0, 21):
                tmp_x = x_lst[p] + 0.01 * (i - 10)
                tmp_y = y_lst[p] + 0.01 * (j - 10)
                tmp_z = z_lst[p] + 0.01 * (k - 10)
                angle1 = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z, x_lst[1], y_lst[1], z_lst[1],
                                                     x_lst[7],
                                                     y_lst[7], z_lst[7])
                angle2 = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z, x_lst[1], y_lst[1], z_lst[1],
                                                     x_lst[10],
                                                     y_lst[10], z_lst[10])
                angle3 = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z, x_lst[7], y_lst[7], z_lst[7],
                                                     x_lst[10],
                                                     y_lst[10], z_lst[10])
                objective_tmpp = (angle1 - 120) ** 2 + (angle2 - 120) ** 2 + (angle3 - 120) ** 2
                if objective_tmpp < objective_min_f:
                    objective_min_f = objective_tmpp
                    j_min = j
                    i_min = i
                    k_min = k
                    angle1_acc = angle1
                    angle2_acc = angle2
                    angle3_acc = angle3
    x_lst[p] += 0.01 * (i_min - 10)
    y_lst[p] += 0.01 * (j_min - 10)
    z_lst[p] += 0.01 * (k_min - 10)
    print('f', p, angle1_acc,angle2_acc,angle3_acc)

def f9(p):
    angle1 = calculate_angle_dimension_3(x_lst[p], y_lst[p], z_lst[p], x_lst[3], y_lst[3], z_lst[3], x_lst[12],
                                           y_lst[12], z_lst[12])
    angle2 = calculate_angle_dimension_3(x_lst[p], y_lst[p], z_lst[p], x_lst[15], y_lst[15], z_lst[15], x_lst[12],
                                           y_lst[12], z_lst[12])
    angle3 = calculate_angle_dimension_3(x_lst[p], y_lst[p], z_lst[p], x_lst[3], y_lst[3], z_lst[3], x_lst[15],
                                           y_lst[15], z_lst[15])
    objective_f = (angle1 - 120) ** 2 + (angle2 - 120) ** 2 + (angle3 - 120) ** 2
    angle1_acc = angle1
    angle2_acc = angle2
    angle3_acc = angle3
    objective_min_f = objective_f
    i_min = 10
    j_min = 10
    k_min = 10
    for i in range(0, 21):
        for j in range(0, 21):
            for k in range(0, 21):
                tmp_x = x_lst[p] + 0.01 * (i - 10)
                tmp_y = y_lst[p] + 0.01 * (j - 10)
                tmp_z = z_lst[p] + 0.01 * (k - 10)
                angle1 = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z, x_lst[3], y_lst[3], z_lst[3],
                                                     x_lst[12],
                                                     y_lst[12], z_lst[12])
                angle2 = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z, x_lst[15], y_lst[15], z_lst[15],
                                                     x_lst[12],
                                                     y_lst[12], z_lst[12])
                angle3 = calculate_angle_dimension_3(tmp_x,tmp_y,tmp_z, x_lst[3], y_lst[3], z_lst[3],
                                                     x_lst[15],
                                                     y_lst[15], z_lst[15])
                objective_tmpp = (angle1 - 120) ** 2 + (angle2 - 120) ** 2 + (angle3 - 120) ** 2
                if objective_tmpp < objective_min_f:
                    objective_min_f = objective_tmpp
                    j_min = j
                    i_min = i
                    k_min = k
                    angle1_acc = angle1
                    angle2_acc = angle2
                    angle3_acc = angle3
    x_lst[p] += 0.01 * (i_min - 10)
    y_lst[p] += 0.01 * (j_min - 10)
    z_lst[p] += 0.01 * (k_min - 10)
    print('f', p, angle1_acc,angle2_acc,angle3_acc)



def test():
    for test_num in range(50):
        f13(13)
    for test_num in range(50):
        f11(11)
    for test_num in range(50):
        f15(15)
    for test_num in range(50):
        f12_13_14(12)
        f12_13_14(13)
        f12_13_14(14)
    for test_num in range(50):
        f3_6_10(3)
        f3_6_10(6)
        f3_6_10(10)
    for test_num in range(50):
        f2_4_7(2)
        f2_4_7(4)
        f2_4_7(7)
    for test_num in range(50):
        f8(8)
        f5(5)
        f9(9)


test()

# 调整结束  模型 验证


print('调整后坐标x', x_lst)
print('调整后坐标y', y_lst)
print('调整后坐标z', z_lst)
