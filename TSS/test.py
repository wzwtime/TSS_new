# coding=utf-8
import random
import os
import operator

"""
    waiting_queues = [
        # Pi：任务名,r1：CPU资源需求,r2：MEM资源需求,r3：IO资源需求,t：到达时间,T：任务完成时间,p：优先级
        ['P1', 0.3, 0.1, 0.2, 1, 2, 1, 1],
        ['P2', 0.2, 0.5, 0.5, 2, 4, 1, 1],
        ['P3', 0.4, 0.2, 0.5, 4, 1, 2, 1],
        ['P4', 0.5, 0.3, 0.3, 3, 2, 1, 1],
        ['P5', 0.4, 0.4, 0.3, 2, 3, 2, 1],
        ['P6', 0.4, 0.3, 0.1, 5, 3, 1, 1],
        ['P7', 0.3, 0.4, 0.3, 5, 2, 3, 1],
        ['P8', 0.2, 0.5, 0.3, 3, 1, 3, 1],
    ]
"""
"""
waiting_queues = {
    # 任务P1
    'P1': {
        'r1': 0.1,  # 需求的CPU资源
        'r2': 0.1,  # 需求的内存资源
        'r3': 0.1,  # 需求的I\O资源
        't': 1,     # 到达队列时刻
        'T': 1,     # 运行所需时间
    },
    # 任务P2
    'P2': {
        'r1': 0.2,
        'r2': 0.2,
        'r3': 0.2,
        't': 2,
        'T': 2,
    },
    # 任务P3
    'P3': {
        'r1': 0.3,
        'r2': 0.3,
        'r3': 0.3,
        't': 3,
        'T': 3,
    },
    # 任务P4
    'P4': {
        'r1': 0.3,
        'r2': 0.3,
        'r3': 0.3,
        't': 3,
        'T': 3,
    },
    # 任务P5
    'P5': {
        'r1': 0.2,
        'r2': 0.2,
        'r3': 0.2,
        't': 2,
        'T': 2,
    },
    # 任务P6
    'P6': {
        'r1': 0.1,
        'r2': 0.1,
        'r3': 0.1,
        't': 1,
        'T': 1,
    },
}

dic = sorted(waiting_queues.items(), key=lambda d: d[1]['t'], reverse=False)

print(dic)      # 变为元组

print("第一个任务：", dic[0])
print("第一个任务名称：", dic[0][0])
print("第一个任务资源需求：", dic[0][1])
print("第一个任务的第一个资源需求：", dic[0][1]['r1'])

for i in dic:
    print(i)


task_list = [
    ['P1', 0.1, 0.1, 0.1, 1, 1],
    ['P2', 0.2, 0.2, 0.3, 2, 2],
    ['P3', 0.3, 0.3, 0.3, 3, 3],
    ['P4', 0.4, 0.4, 0.2, 2, 4],
    ['P5', 0.5, 0.5, 0.5, 5, 5],
    ['P6', 0.6, 0.6, 0.6, 3, 6],
]


task_list.sort(key=operator.itemgetter(3, 4))
print(task_list)


# list.sort(reverse=True)         # 递减永久性排序
# print(list)
# print(list.index(['P1', 0.1, 0.1, 0.1, 1, 1]))
print("****************************")
print("task queues：")
for pi in range(len(task_list)):
    print(task_list[pi][0], ":", task_list[pi][1:6])

task_list.append(['P7'])
#task_list.pop(-1)
print(task_list)
task_list.remove(['P7'])    # 根据值删除元素

print(task_list)


list1 = []

for i in range(0, 6):
    pi = "P" + str(i+1)
    r1 = random.randint(1, 6) / 10
    r2 = random.randint(1, 6) / 10
    r3 = random.randint(1, 6) / 10
    t = random.randint(1, 6)
    T = random.randint(1, 6)

    list1.append([pi, r1, r2, r3, t, T])

print(list1)
for pi in range(len(list1)):
    print(list1[pi][0], ":", list1[pi][1:6])


# 查找P2 对应的r1,r2,r3,t,T
for pi in range(len(list1)):
    if list1[pi][0] == 'P1':
        print(list1[pi][4])
    

#del list1[0]

pi = 'P2'       #i=1


for i in range(len(list1)):
    if list1[i][0] == pi:
        del list1[i]
        break

print("%.2f" % (2/3))


filename = 'test.txt'
with open(filename, 'w') as file_object:
    file_object.write('Hello world.\n')     # 写入多行：加换行符
    file_object.write('Hello world.\n')

"""


def random_queues(n):  # cls 类方法的第一个参数，类似成员方法中的self
    """随机产生n个任务"""

    filename = 'waiting_queues.txt'
    os.remove(filename)     # 删除文件

    for i in range(0, n):
        pi = "P" + str(i + 1)
        r1 = random.randint(1, 5) / 10  # CPU资源需求：0.1-0.5
        r2 = random.randint(1, 5) / 10
        r3 = random.randint(1, 5) / 10
        t = random.randint(1, 5)  # 到达时刻: 1-5s
        T = random.randint(1, 5)  # 运行时间: 1-5s
        p = random.randint(1, 5)  # 优先级 1-5
        s = 1  # slowdown

        # 写文件
        with open(filename, 'a') as file_object:
            info = pi + " " + str(r1) + " " + str(r2) + " " + str(r3) + " " + str(t) + " " + str(T) + " " + str(
                p) + " " + str(s) + "\n"
            file_object.write(info)


# random_queues(int(input("请输入任务数 n:")))

# 读文件
wait_queue = []

file_name = 'waiting_queues.txt'
with open(file_name, 'r') as file_object:
    lines = file_object.readlines()
for line in lines:
    line_list = line.split()    # 默认以空格为分隔符对字符串进行切片
    pi = line_list[0]
    r1 = float(line_list[1])
    r2 = float(line_list[2])
    r3 = float(line_list[3])
    t = int(line_list[4])
    T = int(line_list[5])
    p = float(line_list[6])
    s = float(line_list[7])
    queue = [pi, r1, r2, r3, t, T, p, s]
    wait_queue.append(queue)
print(wait_queue)

"""
    双y轴显示
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()       # 次y轴
    ax1.set_ylim(0, max(Task.asd_act)+1)    # 刻度
    ax2.set_ylim(0, max(Task.asd_act)+1)
    ax1.set_ylabel("Average job slowdown", fontsize=10)
    ax2.set_ylabel("Average complete time(s)", fontsize=10)
    # plt.xticks([])  # 不显示x轴刻度
"""


