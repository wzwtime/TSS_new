# coding=utf-8
import matplotlib.pyplot as plt
from algorithm import Algorithm     # 导入算法模块
from task import Task
from resource import Resource

news_waiting_queues = Task.waiting_queues_copy


def print_ti(ti):
    """打印系统时间"""
    if ti == 1:
        print("First second:")
    elif ti == 2:
        print("Second second:")
    elif ti == 3:
        print("The third second:")
    else:
        print("The " + str(ti) + "th second:")


def release_task_res(pi):
    """查找任务pi,并释放其分配的系统资源"""
    for i in range(len(news_waiting_queues)):
        if news_waiting_queues[i][0] == pi:
            r_cpu = news_waiting_queues[i][1]  # 查看原始信息
            r_mem = news_waiting_queues[i][2]
            r_io = news_waiting_queues[i][3]

            Resource.release_res(r_cpu, r_mem, r_io)  # 释放资源

            break


def task_complete(ti):
    """判断是否有任务完成"""
    new_running_queues = Task.running_queues.copy()
    for pi in new_running_queues.keys():
        if Task.is_complete(pi, ti):
            t1 = new_running_queues[pi]     # 完成时刻
            i = Task.find_pi(news_waiting_queues, pi)[1]
            t = news_waiting_queues[i][4]       # 到达时刻

            Task.complete_time.append(t1 - t)   # 加入任务完成时间列表
            average_complete_time = round(sum(Task.complete_time)/len(Task.complete_time), 2)   # 计算平均完成时间
            Task.average_complete_time.append(average_complete_time)    # 加入列表

            print("Task " + str(pi) + " running completed，complete time C" + str(i + 1) + " is " + str(t1 - t) + " s.")

            Task.del_running_pi(pi)  # 剔除任务

            release_task_res(pi)    # 释放资源


def scheduling_pi(ti):
    """调度任务，可调度多个任务"""
    # 对每个任务计算响应比
    Algorithm.response_ratio(ti)

    # 对任务队列排序,高响应比优先
    if name == "HRRF":
        Algorithm.hrrf()
    Task.print_queue()

    # 调度任务
    new_waiting_queues = Task.waiting_queues.copy()
    for i in range(len(new_waiting_queues)):  # 遍历队列
        pi = new_waiting_queues[i][0]
        j = Task.find_pi(new_waiting_queues, pi)[1]
        t = new_waiting_queues[j][4]

        Algorithm.scheduling(pi, t, ti)  # 调度单个任务


def print_task_numbers():
    """打印队列剩余任务数量"""
    if Task.len_running() in [0, 1]:
        print("The running queues have " + str(Task.len_running()) + " task.")
    else:
        print("The running queues have " + str(Task.len_running()) + " tasks.")

    if Task.len_waiting() in [0, 1]:
        print("The waiting queues have " + str(Task.len_waiting()) + " task.\n")
    else:
        print("The waiting queues have " + str(Task.len_waiting()) + " tasks.\n")


def drawing_act():
    """绘制ACT折线图"""
    length = len(Task.act[0])
    input_values = [i for i in range(1, (int(length) + 1))]   # 任务数量
    plt.title("Average complete time of different scheduling algorithms.")
    plt.xlabel("The number of scheduled tasks", fontsize=12)
    plt.ylabel("Average Complete Time(s)", fontsize=12)
    my_x_ticks = range(0, int(length) + 1, 2)
    plt.xticks(my_x_ticks)
    # 提供输入输出，改变x轴第一个输出，"x-":节点标识
    plt.plot(input_values, Task.act[0], "s-", label="FCFS")
    plt.plot(input_values, Task.act[1], "^-", label="SJF")
    plt.plot(input_values, Task.act[2], "8-", label="HRRF")

    plt.grid(True)         # 显示网格
    plt.legend(loc='upper left')           # 显示图例
    plt.savefig('act.png', bbox_inches='tight')
    plt.close()
    # plt.show()


def drawing_asd():
    """绘制ASD折线图"""
    length = len(Task.asd[0])
    input_values = [i for i in range(1, (int(length) + 1))]   # 任务数量
    plt.title("Average Job Slowdown of different scheduling algorithms.")
    plt.xlabel("The number of scheduled tasks", fontsize=11)
    plt.ylabel("Average Job Slowdown", fontsize=11)
    my_x_ticks = range(0, int(length) + 1, 2)
    plt.xticks(my_x_ticks)

    plt.xlim(0, int(length) + 1)
    plt.plot(input_values, Task.asd[0], "s-", label="FCFS")
    plt.plot(input_values, Task.asd[1], "^-", label="SJF")
    plt.plot(input_values, Task.asd[2], "8-", label="HRRF")

    plt.grid(True)         # 显示网格
    plt.legend(loc='upper right')           # 显示图例
    plt.savefig('asd.png', bbox_inches='tight')
    plt.close()
    # plt.show()


def autolabel_1(rects, x, y):       # rect:矩形
    """显示直方图数值"""
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / x, height + y, '%s' % float(height))        # 水平显示
        # plt.text(rect.get_x() + rect.get_width() / 3, height + 0.5, '%s' % float(height), rotation=90)     # 垂直显示


def asd_bar():
    """绘制不同算法平均完成时间和平均减慢比直方图"""
    plt.title('Average job slowdown of different scheduling algorithms.', fontsize=12)
    plt.ylabel("Average job slowdown", fontsize=12)
    plt.ylim(0, max(Task.asd_act[0], Task.asd_act[2], Task.asd_act[4]) * 1.2)
    plt.xticks([])
    rect1 = plt.bar(left=0, height=Task.asd_act[0], color=(0, 0, 0), edgecolor='w', hatch="//",
                    label='FCFS', width=0.1, yerr=0.000001)
    rect2 = plt.bar(left=0.1, height=Task.asd_act[2], color=(1, 1, 1), edgecolor='black', hatch="\\\\",
                    label='SJF', width=0.1, yerr=0.000001)
    rect3 = plt.bar(left=0.2, height=Task.asd_act[4], color=(0.5, 0.5, 0.5), edgecolor='w', hatch="||",
                    label='HRRF', width=0.1, yerr=0.000001)
    plt.legend(loc='best')  # 显示图例

    autolabel_1(rect1, 3, 0.01)    # 显示数值
    autolabel_1(rect2, 3, 0.01)
    autolabel_1(rect3, 3, 0.01)

    # plt.xticks((0, 0.1, 0.2), ('FCFS', 'SJF', 'HRRF'))
    plt.savefig('asd_bar.png', bbox_inches='tight')
    plt.close()


def act_bar():
    """绘制不同算法平均完成时间和平均减慢比直方图"""
    plt.title('Average complete time of different scheduling algorithms.', fontsize=12)
    plt.ylim(0, max(Task.asd_act[1], Task.asd_act[3], Task.asd_act[5]) * 1.2)
    plt.ylabel("Average complete time(s)", fontsize=12)
    plt.xticks([])  # 不显示x坐标轴数值
    rect1 = plt.bar(left=0, height=Task.asd_act[1], color=(0, 0, 0), edgecolor='w', hatch="//",
                    label='FCFS', width=0.1, yerr=0.000001)
    rect2 = plt.bar(left=0.1, height=Task.asd_act[3], color=(1, 1, 1), edgecolor='black', hatch="\\\\",
                    label='SJF', width=0.1, yerr=0.000001)
    rect3 = plt.bar(left=0.2, height=Task.asd_act[5], color=(0.5, 0.5, 0.5), edgecolor='w', hatch="||",
                    label='HRRF', width=0.1, yerr=0.000001)
    plt.legend(loc='best')  # 显示图例

    autolabel_1(rect1, 3, 0.4)  # 显示数值
    autolabel_1(rect2, 3, 0.4)
    autolabel_1(rect3, 3, 0.4)
    # plt.xticks((0, 0.1, 0.2), ('FCFS', 'SJF', 'HRRF'))
    plt.savefig('act_bar.png', bbox_inches='tight')
    plt.close()


def autolabel_2(rects):       # rect:矩形
    """显示直方图数值"""
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.5, height + 1, '%s' % int(height))        # 水平显示


def task_ct_bar():
    """绘制不同算法所有任务完成所用时间直方图"""
    plt.title('The time spent on running all tasks of different scheduling algorithms', fontsize=10)
    plt.xticks([])
    # plt.yticks(range(1, max(Task.task_ct) + 5, 2))
    plt.ylim(0, max(Task.task_ct) * 1.25)
    plt.ylabel("The time spent on running all tasks(s)", fontsize=10)
    plt.xticks([])
    rect1 = plt.bar(left=0, height=Task.task_ct[0], color=(0, 0, 0), edgecolor='w', hatch="//",
                    label='FCFS', width=0.1, yerr=0.000001)
    rect2 = plt.bar(left=0.1, height=Task.task_ct[1], color=(1, 1, 1), edgecolor='black', hatch="\\\\",
                    label='SJF', width=0.1, yerr=0.000001)
    rect3 = plt.bar(left=0.2, height=Task.task_ct[2], color=(0.5, 0.5, 0.5), edgecolor='w', hatch="||",
                    label='HRRF', width=0.1, yerr=0.000001)
    plt.legend(loc='best')  # 显示图例

    autolabel_2(rect1)  # 显示数值
    autolabel_2(rect2)
    autolabel_2(rect3)
    # plt.xticks((0, 0.2, 0.4), ('FCFS', 'SJF', 'HRRF'))
    plt.savefig('time_spent.png', bbox_inches='tight')
    plt.close()
    # plt.show()


def execute():
    """模拟执行任务"""
    try:
        ti = 1
        while True:
            # 打印系统时间
            print_ti(ti)

            # 判断是否有任务完成
            task_complete(ti)

            if Task.len_waiting() > 0:
                # 调度任务
                scheduling_pi(ti)

            elif Task.len_running() == 0:
                Task.asd.append(Task.average_slow_down.copy())
                Task.act.append(Task.average_complete_time.copy())

                asd = Task.average_slow_down.pop(-1)
                Task.asd_act.append(asd)
                act = Task.average_complete_time.pop(-1)
                Task.asd_act.append(act)

                Task.slow_down = []
                Task.complete_time = []
                Task.average_slow_down = []
                Task.average_complete_time = []
                print("The queues of running and waiting is empty, the end.")
                Task.task_ct.append(int(ti))
                print("All tasks completed time is : " + str(ti) + " s")
                print("********************************************************")
                break
            # 打印队列剩余任务数量
            print_task_numbers()
            ti += 1
    except RuntimeError:
        print("Error！")


# FCFS
Algorithm.fcfs()
name = 'FCFS'
# Task.print_queue()  # 打印任务队列
execute()
# SJF
Algorithm.sjf()
name = 'SJF'
# Task.print_queue()  # 打印任务队列
execute()

# PSA
# Algorithm.psa()

# HRRF
Task.read_file()
Algorithm.hrrf()
# Task.print_queue()  # 打印任务队列
name = 'HRRF'
execute()

print(Task.act)
print(Task.asd)

drawing_asd()
drawing_act()
asd_bar()       # 绘制直方图
act_bar()
task_ct_bar()


