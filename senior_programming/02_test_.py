# -*- coding: utf-8 -*-
# @Time: 2021/5/28 上午9:32
# @Author: yuyinghao
# @FileName: 02_test_.py
# @Software: PyCharm

class Test:
   def __init__(self):
       self.foo = 11
       self._bar = 23
       self.__baz = 23


test_1 = Test()
dir(test_1)
test_1.foo
test_1._bar
test_1.__baz