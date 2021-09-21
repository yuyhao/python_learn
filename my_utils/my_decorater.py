# -*- coding: utf-8 -*-
# @Time: 2021/9/14 8:59
# @Author: yuyinghao
# @FileName: my_decorater.py
# @Software: PyCharm

from functools import wraps
import time


def cost_time_second(unit='sec'):
    """
    计算程序执行时长
    :param unit: 时间单位(sec/min)
    :return: 原函数的结果 + 原函数运行的时间
    """
    def decorater(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()

            if unit == 'sec':
                print('function {} execute scuccess, cost time {} second'.format(
                    func.__name__, round((end_time - start_time), 6)))
            elif unit == 'min':
                print('function {} execute scuccess, cost time {} second'.format(
                    func.__name__, round((end_time - start_time) / 60, 6)))
            return result

        return wrapper

    return decorater


if __name__ == '__main__':

    # 0 记录执行时长
    @cost_time_second('sec')
    def cost_time_decorater_test():
        for i in range(100):
            time.sleep(0.05)
    cost_time_decorater_test()
