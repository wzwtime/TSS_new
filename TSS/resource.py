# coding=utf-8


class Resource:
    """系统资源类"""
    resources = {      # 类变量
        'R_CPU': 1.0,  # CPU资源
        'R_MEM': 1.0,  # 内存资源
        'R_I/O': 1.0,  # I/O资源
    }

    def __init__(self):
        """初始化属性"""

    @classmethod
    def allocate_res(cls, r_cpu, r_mem, r_io):
        """分配系统资源"""
        Resource.resources['R_CPU'] -= r_cpu
        Resource.resources['R_MEM'] -= r_mem
        Resource.resources['R_I/O'] -= r_io

    @classmethod
    def release_res(cls, r_cpu, r_mem, r_io):
        """释放系统资源"""
        Resource.resources['R_CPU'] += r_cpu
        Resource.resources['R_MEM'] += r_mem
        Resource.resources['R_I/O'] += r_io

    @classmethod
    def get_res(cls):
        """获取系统资源"""
        r_cpu = Resource.resources['R_CPU']
        r_mem = Resource.resources['R_MEM']
        r_io = Resource.resources['R_I/O']
        return r_cpu, r_mem, r_io

