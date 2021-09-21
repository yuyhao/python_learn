# -*- coding: utf-8 -*-
# @Time: 2021/9/13 19:43
# @Author: yuyinghao
# @FileName: decorater_test.py
# @Software: PyCharm

from functools import wraps
import time


def cost_time_second(unit='sec'):
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


@cost_time_second('sec')
def cost_time_decorater_test():
    for i in range(100):
        time.sleep(0.05)


if __name__ == '__main__':
    cost_time_decorater_test()
