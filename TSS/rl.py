# coding=utf

"""
                                基于强化学习的任务调度

1、调度目标：Minimize average job slowdown.
2、调度动作(Action)：动作集合{0，1，….，M},等待队列中只排M个任务，后续所有任务用总个数 n_future 表示
    1）0表示不调度
    2）1 <= a <= M，a表示调度第a个任务，t时刻可调度多个任务
3、调度奖励(Reward)：Average job slowdown.

"""






