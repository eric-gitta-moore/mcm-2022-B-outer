import matplotlib.pyplot as plt
import numpy as np

#数据来自 局部调整代码运行的输出loss列表
loss2_lst = [0.09693063207098586, 1.9012285405187699e-06, 1.2369751065786411e-06, 8.361856303772742e-07, 7.2579039875979e-06, 5.960539409072659e-06, 5.960539409072659e-06, 5.960539409072659e-06, 5.960539409072659e-06, 5.960539409072659e-06, 5.960539409072659e-06, 5.960539409072659e-06, 5.960539409072659e-06, 5.960539409072659e-06, 5.960539409072659e-06, 5.960539409072659e-06, 5.960539409072659e-06, 5.960539409072659e-06, 5.960539409072659e-06, 5.960539409072659e-06, 5.960539409072659e-06]
loss3_lst = [0.09561901306702561, 0.05229697668268151, 0.044635081745983934, 0.030275505290341002, 0.025420145826290638, 0.01597830727868033, 0.0067486838166020595, 0.00087534624150675, 0.00017560159445929123, 5.34687889527174e-05, 1.560788549039343e-05, 1.918643508301866e-05, 9.592720259035705e-06, 1.0116030389218014e-05, 7.422980813541028e-06, 7.422980813541028e-06, 7.422980813541028e-06, 7.422980813541028e-06, 7.422980813541028e-06, 7.422980813541028e-06, 7.422980813541028e-06]
adjust_num_lst = list(range(21))
plt.rc('font', size=10)
# rc('text', usetex=True)
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.plot(adjust_num_lst, loss2_lst, linewidth=1, marker='o', markersize=4, label='每次选取圆周上两个无人机发射信号')
plt.plot(adjust_num_lst, loss3_lst, linewidth=1, marker='o', color='orange', markersize=4, label='每次选取圆周上三个无人机发射信号')
plt.xticks(adjust_num_lst)
plt.yticks(np.linspace(0, 0.1, 11, endpoint=True))
plt.xlabel('总循环次数')
plt.ylabel('全局检验误差值')
plt.legend()
plt.grid(axis='x', linestyle='-.', linewidth=1, color='black', alpha=0.3)
plt.grid(axis='y', linestyle='-.', linewidth=1, color='black', alpha=0.3)
plt.savefig('.\\两种模型对比.png', dpi=1000)
plt.show()
