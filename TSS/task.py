# coding=utf-8
import random
import os


class Task:
    """任务类"""
    # 类变量
    waiting_queues = []
    waiting_queues_copy = []    # 释放任务资源时用
    running_queues = {}
    complete_time = []          # 任务的完成时间
    average_complete_time = []  # 任务的平均完成时间
    slow_down = []              # 任务的减慢比
    average_slow_down = []      # 任务的平均减慢比
    asd_act = []        # 绘制直方图用
    act = []        # 绘制平均完成时间折线图用
    asd = []        # 绘制平均减慢比折线图用
    task_ct = []         # 绘制所有任务完成所用时间

    def __init__(self):
        """初始化属性"""

    @classmethod
    def read_file(cls):
        """读文件"""
        filename = 'waiting_queues.txt'
        with open(filename, 'r') as file_object:
            lines = file_object.readlines()
        for line in lines:
            line_list = line.split()  # 默认以空格为分隔符对字符串进行切片
            pi = line_list[0]
            r1 = float(line_list[1])
            r2 = float(line_list[2])
            r3 = float(line_list[3])
            t = int(line_list[4])
            T = int(line_list[5])
            p = float(line_list[6])
            s = float(line_list[7])
            queue = [pi, r1, r2, r3, t, T, p, s]
            Task.waiting_queues.append(queue)
            Task.waiting_queues_copy.append(queue)

    @classmethod            # 类方法
    def random_queues(cls, n):  # cls 类方法的第一个参数，类似成员方法中的self
        """随机产生n个任务"""
        filename = 'waiting_queues.txt'
        os.remove(filename)  # 删除文件
        for i in range(0, n):
            pi = "P" + str(i + 1)
            r1 = random.randint(1, 5) / 10  # CPU资源需求
            r2 = random.randint(1, 5) / 10
            r3 = random.randint(1, 5) / 10
            t = random.randint(1, n)  # 到达时刻
            T = random.randint(1, 10)  # 运行时间
            p = random.randint(1, 5)  # 优先级
            s = 1  # slowdown

            # 将任务写入文件
            # filename = 'waiting_queues.txt'
            with open(filename, 'a') as file_object:
                info = pi + " " + str(r1) + " " + str(r2) + " " + str(r3) + " " + str(t) + " " + str(T) + " " + str(
                    p) + " " + str(s) + "\n"
                file_object.write(info)

    @classmethod
    def add_running_pi(cls, pi, ti):    # 任务pi、系统时间ti
        """添加任务到运行队列"""
        p_i = Task.find_pi(Task.waiting_queues, pi)[0]
        i = Task.find_pi(Task.waiting_queues, pi)[1]
        Task.running_queues[p_i] = ti + Task.waiting_queues[i][5]       # 任务的完成时间

    @classmethod
    def find_pi(cls, queues, pi):
        """找到任务队列中pi,返回任务pi和pi的所在位置索引i"""
        for i in range(len(queues)):
            if queues[i][0] == pi:
                return pi, i

    @classmethod
    def del_waiting_pi(cls, pi):
        """从等待队列中剔除任务"""
        i = Task.find_pi(Task.waiting_queues, pi)[1]
        del Task.waiting_queues[i]

    @classmethod
    def del_running_pi(cls, pi):
        """从运行队列中剔除任务"""
        del Task.running_queues[pi]

    @classmethod
    def time_complete(cls, pi):
        """输出任务的完成时间"""
        return Task.running_queues[pi]

    @classmethod
    def len_waiting(cls):
        """输出等待队列中任务个数"""
        return len(Task.waiting_queues)

    @classmethod
    def len_running(cls):
        """输出运行队列中任务个数"""
        return len(Task.running_queues)

    @classmethod
    def is_complete(cls, pi, ti):  # 任务pi,系统时间ti
        """判断运行队列中是否有任务完成"""
        if Task.running_queues[pi] == ti:
            return True
        else:
            return False

    @classmethod
    def print_queue(cls):
        """打印任务队列"""
        print("task queues：")
        for pi in range(len(Task.waiting_queues)):
            print(Task.waiting_queues[pi][0], ":", Task.waiting_queues[pi][1:8])
        print("\n")


"""
task = Task()
task.random_queues(10
                   )
task.print_queue()

print(task.waiting_queues)

#task.print_queue()
#print(task.waiting_queues_copy)

task.add_running_pi('P3', 5)
print(task.running_queues)

task.del_waiting_pi('P3')
print(task.waiting_queues)

#task.del_running_pi('P3')
#print(task.running_queues)
"""







