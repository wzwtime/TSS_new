# coding=utf
import operator

M = 1000

"""DAG的任务调度"""
dag = {
    1: {2: 18, 3: 12, 4: 9, 5: 11, 6: 14},
    2: {8: 19, 9: 16},
    3: {7: 23},
    4: {8: 27, 9: 23},
    5: {9: 13},
    6: {8: 15},
    7: {10: 17},
    8: {10: 11},
    9: {10: 13},
    10: {},
}
# print(dag[1].keys())

# task(1-10) P1 P2 P3
"""运行时间"""
computation_costs = [
    [14, 16, 9],
    [13, 19, 18],
    [11, 13, 19],
    [13, 8, 17],
    [12, 13, 10],
    [13, 16, 9],
    [7, 15, 11],
    [5, 11, 14],
    [18, 12, 20],
    [21, 7, 16],
]

# 各处理器上运行的任务
"""p1=[{job:1,start:0,end:9},{}]"""
p1 = []
p2 = []
p3 = []
make_span = 0
scheduler = []      # 记录各任务调度所在的处理器号
avg_costs = []      # 计算单个任务在不同处理器上调度的平均花销


def avg_cost():
    """计算单个任务在不同处理器上调度的平均花销"""
    for n in range(len(computation_costs)):
        cost = round(sum(computation_costs[n]), 2)  # 保留两位小数
        avg_costs.append(cost)
    return avg_costs


avg_cost()      # 调用执行
"""
avg_costs = []
for i in range(len(computation_costs)):
    avg_cost = round(sum(computation_costs[i]), 2)  # 保留两位小数
    avg_costs.append(avg_cost)
"""
rank_u = []


def rank__u():
    """计算优先级
    # 逆拓扑排序为10，9，8，7，6，5，4，3，2，1
    # 依次计算rank_u(n_i) = (w_i ) ̅ + max(n_j∈succ(n_i)⁡{c(i,j) ) ̅ + rank_u (n_j )}"""
    i = 10
    while i > 0:
        # print(dag[i])
        if len(dag[i]) == 0:  # 无后继节点
            rank_u.append([i, avg_costs[i - 1]])
        else:  # 有后继节点
            # 查找后继节点j
            max_nj = 0
            for j in dag[i].keys():
                cij = dag[i][j] * 3  # 边权<i,j>
                # 查找后继节点的rank_uj
                for k in range(len(rank_u)):
                    if j == rank_u[k][0]:
                        rank_uj = rank_u[k][1]
                        break
                if max_nj < cij + rank_uj:  # 取最大值
                    max_nj = cij + rank_uj
            rank_u.append([i, avg_costs[i - 1] + max_nj])
        i -= 1
    return rank_u


rank__u()

# 按rank_u降序排序
rank_u.sort(key=operator.itemgetter(1), reverse=True)
rank_u_copy = rank_u.copy()
# print('调度顺序：', rank_u)
# 调度顺序为：1 4 3 2 5 6 9 7 8 10
pred = []       # 前驱节点列表


def pred_list():
    """找出前驱节点"""
    for i in range(len(rank_u)):
        job = rank_u[i][0]
        temp = []
        for j in range(len(dag)):
            if job in dag[j + 1].keys():
                sub_pred = j + 1
                temp.append(sub_pred)
        pred.append([job, temp])
    return pred


pred_list()

# print("各节点前驱:", pred)
# print(pred[-1][1][0])

# 计算最早开始时间  EST(n_i,p_j ) = max{avail[j], max(n_m∈pred(n_i)){AFT(n_m ) + c_(m,i)}
# 计算最早结束时间  EFT(n_i,p_j)=w_(i,j) + EST(n_i,p_j)


def add_pi(pi):
    """加入任务到列表,将任务添加到调度列表中"""
    if pi == 1:
        p1.append({'job': job, 'start': est, 'end': eft})
        scheduler.append({job: 1})
    elif pi == 2:
        p2.append({'job': job, 'start': est, 'end': eft})
        scheduler.append({job: 2})
    else:
        p3.append({'job': job, 'start': est, 'end': eft})
        scheduler.append({job: 3})


def pred_max_nm():
    """前驱节点的最大时间"""
    max_nm = 0

    for j in range(len(job_pred)):
        # print(job_pred[j])
        # 查找前驱的完成时间 【1）查找前驱在哪个处理器 2）找到所在处理器索引位置 3）输出'end'对应的值 】
        for k in range(len(rank_u_copy)):  # rank_u_copy副本
            if job_pred[j] == rank_u_copy[k][0]:
                pred_pi = scheduler[k][job_pred[j]]
                aft = 0
                if pred_pi == 1:
                    for m in range(len(p1)):
                        if p1[m]['job'] == job_pred[j]:
                            aft = p1[m]['end']
                elif pred_pi == 2:
                    for m in range(len(p2)):

                        if p2[m]['job'] == job_pred[j]:
                            aft = p2[m]['end']
                else:
                    for m in range(len(p3)):
                        if p3[m]['job'] == job_pred[j]:
                            aft = p3[m]['end']
        # print(aft)
        # 计算cmi
        if pi == pred_pi:
            cmi = 0
        else:
            cmi = dag[job_pred[j]][job]
        # print(cmi)

        if max_nm < aft + cmi:
            max_nm = aft + cmi
            # print(max_nm)
    return max_nm


while len(rank_u) > 0:
    """每次选择列表中第一个任务调度"""
    job = rank_u.pop(0)[0]      # 作业号

    if len(rank_u) == 9:    # 首个任务
        est = 0
        # 查找任务job的最小花销处理器
        min_cost = computation_costs[job - 1][0]
        for i in range(3):
            if min_cost > computation_costs[job - 1][i]:
                min_cost = computation_costs[job - 1][i]
                pi = i+1      # 记录处理机号
        eft = computation_costs[job-1][pi-1]        # computation_costs[job-1][pi-1]=wij运行时间花销
        # print([est, eft])
        add_pi(pi)
        # 加入列表

    else:   # 其他任务
        """先计算max(n_m∈pred(n_i)){AFT(n_m ) + c_(m,i)}"""
        eft = M
        label = 0
        avail_pi = 0
        for pi in range(1, 4):  # 在不同的处理器上处理
            est = 0
            for i in range(len(pred)):
                if job == pred[i][0]:  # 找到前驱索引位置i
                    job_pred = pred[i][1]
                    # print(job_pred)
                    pred_max_nm()

            # 计算处理器可以处理任务job的最早时间
            if pi == 1 and len(p1) > 0:
                avail_pi = p1[-1]['end']
            elif pi == 2 and len(p2) > 0:
                avail_pi = p2[-1]['end']
            elif pi == 3 and len(p3) > 0:
                avail_pi = p3[-1]['end']

            max_nm = pred_max_nm()
            if est < max(avail_pi, max_nm):
                est = max(avail_pi, max_nm)

            if eft > est + computation_costs[job-1][pi-1]:
                eft = est + computation_costs[job-1][pi-1]
                label = pi
        # 更新est
        est = eft - computation_costs[job-1][label-1]
        # print([est, eft])

        # 加入pi列表
        add_pi(label)

print('scheduler:', scheduler)
print('p1:', p1)
print('p2:', p2)
print('p3:', p3)
print('make_span:', eft)

