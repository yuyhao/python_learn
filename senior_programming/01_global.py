# -*- coding: utf-8 -*-
# @Time: 2021/5/17 上午11:53
# @Author: yuyinghao
# @FileName: 01_global.py
# @Software: PyCharm


"""
global 作用: Python中定义函数时，若想在函数内部对函数外的变量进行操作，就需要在函数内部声明其为global
"""

x = 1
def modify_x():
    global x
    x = 3

def func_a():
    global x
    x += 1
    print(x)

func_a()