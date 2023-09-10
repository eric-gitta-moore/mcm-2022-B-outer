import matplotlib.pyplot as plt
import numpy as np

# 半径基准 R=100
R = 100
r = [100] * 10
# 原始极坐标参数
theta_origin = [0, 0, 40.10, 80.21, 119.75, 159.86, 199.96, 240.07, 280.17, 320.28]
radii_origin = [0, 100, 98, 112, 105, 98, 112, 105, 98, 112]
# 调整后最终极坐标参数(待更新)
theta_final = [0]*10
radii_final = [0]*10
# 这里 radii_new结果来自于预处理后运行的结果,见代码“T1-3局部调整.py”的运行结果！
radii_new = [0,100, 99.93632293390803, 99.69178293027487, 100.75479540910527, 101.38545566398636, 99.60404550052611, 100.21153524192636, 100.24852533523602, 100.17667460519363]

# 直角坐标数组 所有局部调整处理均在直角坐标下进行，但最终模型的验证需要转换回极坐标,调整过程中变化的是x_lst,y_lst数组
x_lst = [0]*10
y_lst = [0]*10
# 下标 对应
for i in range(1, 10):
    x_lst[i] = radii_new[i] * np.cos(theta_origin[i]/180*np.pi)
    y_lst[i] = radii_new[i] * np.sin(theta_origin[i] / 180 * np.pi)
print(x_lst, y_lst)


def calculate_angle(x0,y0,x1,y1,x2,y2):
    dis0 = (x1 - x2)**2+(y1 - y2)**2
    dis1 = (x2-x0) ** 2+(y2-y0)**2
    dis2 = (x1 - x0)**2+(y1-y0)**2
    cos_angle = (dis2+dis1-dis0)/(2*np.sqrt(dis1)*np.sqrt(dis2))
    angle = np.arccos(cos_angle)
    return angle/np.pi*180

def mid(x,y,z):
    if x!=max(x,y,z) and x!=min(x,y,z):
        return x
    elif y!=max(x,y,z) and y!=min(x,y,z):
        return y
    else:
        return z



# 以27为发射点，点p作为接收点的调整策略，调整策略仅依据2个接收角
def f27_p(p):
    # 局部调整一个点（以27为发射点调整接收点 除了1以外的其他接收点均需要调整）
    # 一次调整的过程
    # 三个接收角度
    angle0p2 = calculate_angle(x_lst[p],y_lst[p],x_lst[0],y_lst[0],x_lst[2],y_lst[2])
    angle0p7 = calculate_angle(x_lst[p],y_lst[p],x_lst[0],y_lst[0],x_lst[7],y_lst[7])
    angle0p2_acc = angle0p2
    angle0p7_acc = angle0p7
    if p==3 or p==6:
        objective_fp= (max(angle0p2,angle0p7)-70)**2+(min(angle0p2,angle0p7)-10)**2
    elif p==1 or p==8:
        objective_fp= (max(angle0p2,angle0p7)-70)**2+(min(angle0p2,angle0p7)-30)**2
    elif p==4 or p==5:
        objective_fp= (max(angle0p2,angle0p7)-50)**2+(min(angle0p2,angle0p7)-30)**2
    else:
        objective_fp= (max(angle0p2,angle0p7)-50)**2+(min(angle0p2,angle0p7)-50)**2
    objective_min_fp = objective_fp
    objective_fp_lst=[]
    i_min=10
    j_min=10
    for i in range(0,21):
        for j in range(0,21):
            tmp_x = x_lst[p]+0.01*(i-10)
            tmp_y = y_lst[p]+0.01*(j-10)
            angle0p2 = calculate_angle(tmp_x, tmp_y, x_lst[0], y_lst[0], x_lst[2], y_lst[2])
            angle0p7 = calculate_angle(tmp_x, tmp_y, x_lst[0], y_lst[0], x_lst[7], y_lst[7])
            if p==3 or p==6:
                objective_tmpp= (max(angle0p2,angle0p7)-70)**2+(min(angle0p2,angle0p7)-10)**2
            elif p==1 or p==8:
                objective_tmpp= (max(angle0p2,angle0p7)-70)**2+(min(angle0p2,angle0p7)-30)**2
            elif p==4 or p==5:
                objective_tmpp= (max(angle0p2,angle0p7)-50)**2+(min(angle0p2,angle0p7)-30)**2
            else:
                objective_tmpp= (max(angle0p2,angle0p7)-50)**2+(min(angle0p2,angle0p7)-50)**2
            if objective_tmpp < objective_min_fp:
                objective_min_fp = objective_tmpp
                j_min = j
                i_min = i
                angle0p2_acc = angle0p2
                angle0p7_acc = angle0p7

    x_lst[p] += 0.01*(i_min-10)
    y_lst[p] += 0.01*(j_min-10)
    print('f',p,angle0p2_acc, angle0p7_acc, objective_fp, objective_min_fp)


# 以38为发射点，点p作为接收点的调整策略，调整策略仅依据2个接收角
def g38_p(p):
    # 局部调整一个点（以27为发射点调整接收点 除了1以外的其他接收点均需要调整）
    # 一次调整的过程
    # 三个接收角度
    angle0p3 = calculate_angle(x_lst[p],y_lst[p],x_lst[0],y_lst[0],x_lst[3],y_lst[3])
    angle0p8 = calculate_angle(x_lst[p],y_lst[p],x_lst[0],y_lst[0],x_lst[8],y_lst[8])
    angle0p3_acc = angle0p3
    angle0p8_acc = angle0p8
    if p==2 or p==9:
        objective_gp= (max(angle0p3,angle0p8)-70)**2+(min(angle0p3,angle0p8)-30)**2
    elif p==4 or p==7:
        objective_gp= (max(angle0p3,angle0p8)-70)**2+(min(angle0p3,angle0p8)-10)**2
    elif p==5 or p==6:
        objective_gp= (max(angle0p3,angle0p8)-50)**2+(min(angle0p3,angle0p8)-30)**2
    objective_min_gp = objective_gp
    objective_gp_lst=[]
    i_min=10
    j_min=10
    for i in range(0,21):
        for j in range(0,21):
            tmp_x = x_lst[p]+0.01*(i-10)
            tmp_y = y_lst[p]+0.01*(j-10)
            angle0p3 = calculate_angle(tmp_x, tmp_y, x_lst[0], y_lst[0], x_lst[3], y_lst[3])
            angle0p8 = calculate_angle(tmp_x, tmp_y, x_lst[0], y_lst[0], x_lst[8], y_lst[8])
            if p == 2 or p == 9:
                objective_tmpp = (max(angle0p3, angle0p8) - 70) ** 2 + (min(angle0p3, angle0p8) - 30) ** 2
            elif p == 4 or p == 7:
                objective_tmpp = (max(angle0p3, angle0p8) - 70) ** 2 + (min(angle0p3, angle0p8) - 10) ** 2
            elif p == 5 or p == 6:
                objective_tmpp = (max(angle0p3, angle0p8) - 50) ** 2 + (min(angle0p3, angle0p8) - 30) ** 2
            if objective_tmpp < objective_min_gp:
                objective_min_gp = objective_tmpp
                j_min = j
                i_min = i
                angle0p3_acc = angle0p3
                angle0p8_acc = angle0p8

    x_lst[p] += 0.01*(i_min-10)
    y_lst[p] += 0.01*(j_min-10)
    print('g',p,angle0p3_acc, angle0p8_acc, objective_gp, objective_min_gp)


# 以49为发射点，点p作为接收点的调整策略，调整策略仅依据2个接收角
def h49_p(p):
    # 局部调整一个点（以49为发射点调整接收点 除了1以外的其他接收点均需要调整）
    # 一次调整的过程
    # 三个接收角度
    angle0p4 = calculate_angle(x_lst[p],y_lst[p],x_lst[0],y_lst[0],x_lst[4],y_lst[4])
    angle0p9 = calculate_angle(x_lst[p],y_lst[p],x_lst[0],y_lst[0],x_lst[9],y_lst[9])
    angle0p4_acc = angle0p4
    angle0p9_acc = angle0p9
    if p==2:
        objective_hp= (max(angle0p4,angle0p9)-50)**2+(min(angle0p4,angle0p9)-50)**2
    elif p==5 or p==8:
        objective_hp= (max(angle0p4,angle0p9)-70)**2+(min(angle0p4,angle0p9)-10)**2
    elif p==6 or p==7:
        objective_hp= (max(angle0p4,angle0p9)-50)**2+(min(angle0p4,angle0p9)-30)**2
    elif p==3:
        objective_hp= (max(angle0p4,angle0p9)-70)**2+(min(angle0p4,angle0p9)-30)**2
    objective_min_hp = objective_hp
    objective_fp_lst=[]
    i_min=10
    j_min=10
    for i in range(0,21):
        for j in range(0,21):
            tmp_x = x_lst[p]+0.01*(i-10)
            tmp_y = y_lst[p]+0.01*(j-10)
            angle0p4 = calculate_angle(tmp_x, tmp_y, x_lst[0], y_lst[0], x_lst[4], y_lst[4])
            angle0p9 = calculate_angle(tmp_x, tmp_y, x_lst[0], y_lst[0], x_lst[9], y_lst[9])
            if p == 2:
                objective_tmpp = (max(angle0p4, angle0p9) - 50) ** 2 + (min(angle0p4, angle0p9) - 50) ** 2
            elif p == 5 or p == 8:
                objective_tmpp = (max(angle0p4, angle0p9) - 70) ** 2 + (min(angle0p4, angle0p9) - 10) ** 2
            elif p == 6 or p == 7:
                objective_tmpp = (max(angle0p4, angle0p9) - 50) ** 2 + (min(angle0p4, angle0p9) - 30) ** 2
            elif p == 3:
                objective_tmpp = (max(angle0p4, angle0p9) - 70) ** 2 + (min(angle0p4, angle0p9) - 30) ** 2
            if objective_tmpp < objective_min_hp:
                objective_min_hp = objective_tmpp
                j_min = j
                i_min = i
                angle0p4_acc = angle0p4
                angle0p9_acc = angle0p9

    x_lst[p] += 0.01*(i_min-10)
    y_lst[p] += 0.01*(j_min-10)
    print('h',p,angle0p4_acc, angle0p9_acc, objective_hp, objective_min_hp)


# 以15为发射点，点p作为接收点的调整策略，调整策略仅依据2个接收角
def u15_p(p):
    # 局部调整一个点（以15为发射点调整接收点 除了1以外的其他接收点均需要调整）
    # 一次调整的过程
    # 三个接收角度
    angle0p1 = calculate_angle(x_lst[p],y_lst[p],x_lst[0],y_lst[0],x_lst[1],y_lst[1])
    angle0p5 = calculate_angle(x_lst[p],y_lst[p],x_lst[0],y_lst[0],x_lst[5],y_lst[5])
    angle0p1_acc = angle0p1
    angle0p5_acc = angle0p5
    if p==2 or p==4:
        objective_up= (max(angle0p1,angle0p5)-70)**2+(min(angle0p1,angle0p5)-30)**2
    elif p==6 or p==9:
        objective_up= (max(angle0p1,angle0p5)-70)**2+(min(angle0p1,angle0p5)-10)**2
    elif p==7 or p==8:
        objective_up= (max(angle0p1,angle0p5)-50)**2+(min(angle0p1,angle0p5)-30)**2
    elif p==3:
        objective_up= (max(angle0p1,angle0p5)-50)**2+(min(angle0p1,angle0p5)-50)**2
    objective_min_up = objective_up
    objective_up_lst=[]
    i_min=10
    j_min=10
    for i in range(0,21):
        for j in range(0,21):
            tmp_x = x_lst[p]+0.01*(i-10)
            tmp_y = y_lst[p]+0.01*(j-10)
            angle0p1 = calculate_angle(tmp_x, tmp_y, x_lst[0], y_lst[0], x_lst[1], y_lst[1])
            angle0p5 = calculate_angle(tmp_x, tmp_y, x_lst[0], y_lst[0], x_lst[5], y_lst[5])
            if p == 2 or p == 4:
                objective_tmpp = (max(angle0p1, angle0p5) - 70) ** 2 + (min(angle0p1, angle0p5) - 30) ** 2
            elif p == 6 or p == 9:
                objective_tmpp = (max(angle0p1, angle0p5) - 70) ** 2 + (min(angle0p1, angle0p5) - 10) ** 2
            elif p == 7 or p == 8:
                objective_tmpp = (max(angle0p1, angle0p5) - 50) ** 2 + (min(angle0p1, angle0p5) - 30) ** 2
            elif p == 3:
                objective_tmpp = (max(angle0p1, angle0p5) - 50) ** 2 + (min(angle0p1, angle0p5) - 50) ** 2
            if objective_tmpp < objective_min_up:
                objective_min_up = objective_tmpp
                j_min = j
                i_min = i
                angle0p1_acc = angle0p1
                angle0p5_acc = angle0p5

    x_lst[p] += 0.01*(i_min-10)
    y_lst[p] += 0.01*(j_min-10)
    print('u',p,angle0p1_acc, angle0p5_acc, objective_up, objective_min_up)



# 以16为发射点，点p作为接收点的调整策略，调整策略仅依据2个接收角
def v16_p(p):
    # 局部调整一个点（以16为发射点调整接收点 除了1以外的其他接收点均需要调整）
    # 一次调整的过程
    # 三个接收角度
    angle0p1 = calculate_angle(x_lst[p],y_lst[p],x_lst[0],y_lst[0],x_lst[1],y_lst[1])
    angle0p6 = calculate_angle(x_lst[p],y_lst[p],x_lst[0],y_lst[0],x_lst[6],y_lst[6])
    angle0p1_acc = angle0p1
    angle0p6_acc = angle0p6
    if p==2 or p==5:
        objective_vp= (max(angle0p1,angle0p6)-70)**2+(min(angle0p1,angle0p6)-10)**2
    elif p==7 or p==9:
        objective_vp= (max(angle0p1,angle0p6)-70)**2+(min(angle0p1,angle0p6)-30)**2
    elif p==3 or p==4:
        objective_vp= (max(angle0p1,angle0p6)-50)**2+(min(angle0p1,angle0p6)-30)**2
    elif p==8:
        objective_vp= (max(angle0p1,angle0p6)-50)**2+(min(angle0p1,angle0p6)-50)**2
    objective_min_vp = objective_vp
    objective_vp_lst=[]
    i_min=10
    j_min=10
    for i in range(0,21):
        for j in range(0,21):
            tmp_x = x_lst[p]+0.01*(i-10)
            tmp_y = y_lst[p]+0.01*(j-10)
            angle0p1 = calculate_angle(tmp_x, tmp_y, x_lst[0], y_lst[0], x_lst[1], y_lst[1])
            angle0p6 = calculate_angle(tmp_x, tmp_y, x_lst[0], y_lst[0], x_lst[6], y_lst[6])
            if p == 2 or p == 5:
                objective_tmpp = (max(angle0p1, angle0p6) - 70) ** 2 + (min(angle0p1, angle0p6) - 10) ** 2
            elif p == 7 or p == 9:
                objective_tmpp = (max(angle0p1, angle0p6) - 70) ** 2 + (min(angle0p1, angle0p6) - 30) ** 2
            elif p == 3 or p == 4:
                objective_tmpp = (max(angle0p1, angle0p6) - 50) ** 2 + (min(angle0p1, angle0p6) - 30) ** 2
            elif p == 8:
                objective_tmpp = (max(angle0p1, angle0p6) - 50) ** 2 + (min(angle0p1, angle0p6) - 50) ** 2
            if objective_tmpp < objective_min_vp:
                objective_min_vp = objective_tmpp
                j_min = j
                i_min = i
                angle0p1_acc = angle0p1
                angle0p6_acc = angle0p6

    x_lst[p] += 0.01*(i_min-10)
    y_lst[p] += 0.01*(j_min-10)
    print('v',p,angle0p1_acc, angle0p6_acc, objective_vp, objective_min_vp)


# 一轮调整（每次取三架飞机作为发射站）该函数为一次调整
def adjust_2_group():
    # 三基准-分别调整其余各个点（除点0-1以外的点）
    f27_p(3)
    f27_p(4)
    f27_p(5)
    f27_p(6)
    f27_p(8)
    f27_p(9)

    g38_p(2)
    g38_p(4)
    g38_p(5)
    g38_p(6)
    g38_p(7)
    g38_p(9)

    h49_p(2)
    h49_p(3)
    h49_p(5)
    h49_p(6)
    h49_p(7)
    h49_p(8)

    u15_p(2)
    u15_p(3)
    u15_p(4)
    u15_p(6)
    u15_p(7)
    u15_p(8)
    u15_p(9)

    v16_p(2)
    v16_p(3)
    v16_p(4)
    v16_p(5)
    v16_p(7)
    v16_p(8)
    v16_p(9)


loss_lst = []
for adjust_num in range(21):
    loss = 0
    for p in range(1,10):
        loss = 0
        if p!=6 and p!=1:
            angle0p1 = calculate_angle(x_lst[p],y_lst[p],x_lst[0],y_lst[0],x_lst[1],y_lst[1])
            angle0p6 = calculate_angle(x_lst[p],y_lst[p],x_lst[0],y_lst[0],x_lst[6],y_lst[6])
            objective_tmpp = 0
            if p == 2 or p == 5:
                objective_tmpp = (max(angle0p1, angle0p6) - 70) ** 2 + (min(angle0p1, angle0p6) - 10) ** 2
            elif p == 7 or p == 9:
                objective_tmpp = (max(angle0p1, angle0p6) - 70) ** 2 + (min(angle0p1, angle0p6) - 30) ** 2
            elif p == 3 or p == 4:
                objective_tmpp = (max(angle0p1, angle0p6) - 50) ** 2 + (min(angle0p1, angle0p6) - 30) ** 2
            elif p == 8:
                objective_tmpp = (max(angle0p1, angle0p6) - 50) ** 2 + (min(angle0p1, angle0p6) - 50) ** 2
            loss+=objective_tmpp
        else:
            angle0p1 = calculate_angle(x_lst[p],y_lst[p], x_lst[0], y_lst[0], x_lst[1], y_lst[1])
            angle0p5 = calculate_angle(x_lst[p],y_lst[p], x_lst[0], y_lst[0], x_lst[5], y_lst[5])
            objective_tmpp = 0
            if p == 2 or p == 4:
                objective_tmpp = (max(angle0p1, angle0p5) - 70) ** 2 + (min(angle0p1, angle0p5) - 30) ** 2
            elif p == 6 or p == 9:
                objective_tmpp = (max(angle0p1, angle0p5) - 70) ** 2 + (min(angle0p1, angle0p5) - 10) ** 2
            elif p == 7 or p == 8:
                objective_tmpp = (max(angle0p1, angle0p5) - 50) ** 2 + (min(angle0p1, angle0p5) - 30) ** 2
            elif p == 3:
                objective_tmpp = (max(angle0p1, angle0p5) - 50) ** 2 + (min(angle0p1, angle0p5) - 50) ** 2
            loss += objective_tmpp

    loss_lst.append(1.5*loss)
    # print(adjust_num, loss)
    # 一轮调整 包含5小轮调整 每次分别进行6，6，6，7，7架无人机的调整
    adjust_2_group()


#结束方案二的调整，下面验证模型
print('loss_lst',loss_lst)
# 误差函数随着迭代次数的变化曲线
# print('loss_lst',loss_lst)

x_lst_final = x_lst
y_lst_final = y_lst
theta_final = [0]*10
radii_final = [0]*10

#将最终结果反变换为极坐标形式
for i in range(1, 10):
    radii_final[i] = np.sqrt(x_lst_final[i]**2+y_lst_final[i]**2)
    if y_lst_final[i] > 0 and x_lst_final[i]>0:
        theta_final[i] = np.arctan(y_lst_final[i] / x_lst_final[i])/np.pi*180
    elif y_lst_final[i] > 0 and x_lst_final[i] < 0:
        theta_final[i] = 180 - np.arctan(- y_lst_final[i] / x_lst_final[i])/np.pi*180
    elif y_lst_final[i] < 0 and x_lst_final[i] < 0:
        theta_final[i] = np.arctan(y_lst_final[i] / x_lst_final[i])/np.pi*180+180
    elif y_lst_final[i] < 0 and x_lst_final[i] > 0:
        theta_final[i] = 360 - np.arctan(- y_lst_final[i] / x_lst_final[i]) / np.pi * 180


adjust_num_lst = list(range(0,21))
plt.rc('font', size=10)
# rc('text', usetex=True)
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.plot(adjust_num_lst, loss_lst[:], linewidth=1, marker='o', markersize=4, label='每次选取圆周上两个无人机发射信号')
plt.xticks(adjust_num_lst, rotation=-45)
plt.yticks(np.linspace(0, 0.1, 11, endpoint=True))
plt.xlabel('总循环次数')
plt.ylabel('全局检验误差值')
plt.legend()
plt.grid(axis='x', linestyle='-.', linewidth=1, color='black', alpha=0.3)
plt.grid(axis='y', linestyle='-.', linewidth=1, color='black', alpha=0.3)
plt.savefig('.\\每次选取圆周上两个无人机发射信号.png', dpi=1000)
plt.show()
print('调整后所有点的笛卡尔坐标',x_lst, y_lst)
print('转换完毕后所有点的极坐标',theta_final,radii_final)