# -*- coding: utf-8 -*-
# @Time: 2021/9/10 22:41
# @Author: yuyinghao
# @FileName: new_style_class.py
# @Software: PyCharm

class A:
    def __init__(self, age):
        self.age = age
        print('执行init方法')


x = A(age='nae')
x(1)


class B:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print(self.name)

    @classmethod
    def get_age(cls):
        print('this is cls method')

    @staticmethod
    def get_other():
        print('static method')

    def get_test3(self):
        self.get_other()

b = B('yyh', 29)
b.get_test3()
