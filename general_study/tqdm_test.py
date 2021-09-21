# -*- coding: utf-8 -*-
# @Time: 2021/9/13 9:11
# @Author: yuyinghao
# @FileName: tqdm_test.py
# @Software: PyCharm

from tqdm import tqdm, trange
import time

for i in trange(100):
    time.sleep(0.1)