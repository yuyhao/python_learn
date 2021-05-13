# -*- coding: utf-8 -*-
# @Time: 2021/5/13 下午5:09
# @Author: yuyinghao
# @FileName: 01_rdd.py
# @Software: PyCharm

from pyspark.sql import SparkSession
import os

os.environ['PYSPARK_PYTHON']='/usr/local/python36/bin/python3.6'
# 1 创建一个rdd

# 1.1 通过读取文本文件
spark = SparkSession.builder.master('local').appName('test').getOrCreate()
sc = spark.sparkContext

# 读取整个目录的内容
logs = sc.textFile('/media/yuyinghao/文档/0_工作/z_其他/2_参考书/')

# 读取单个文件
logs = sc.textFile('/media/yuyinghao/文档/0_工作/z_其他/2_参考书/[图灵程序设计丛书].深入学习mongodb.pdf')

# 使用通配符
logs = sc.textFile('/media/yuyinghao/文档/0_工作/z_其他/2_参考书/*java.pdf')

# 把整个目录加载为键值对
logs = sc.wholeTextFiles('/media/yuyinghao/文档/0_工作/z_其他/2_参考书/')
logs.count()
logs.name()

# 1.2 通过parallelize和range
rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7])
rdd.count()

rdd = sc.range(1, 8, 1, 4) # sc.range(start,end=None,step=1,numslices=None)，numslices指定所需分区数量

# 2 操作rdd
# collect 将rdd里面的元素以列表的形式返回
rdd= sc.parallelize([1,2,3,4,5,6,7])
print(rdd.collect())

# map 针对rdd里面的每一个元素执行操作
rdd2 = rdd.map(lambda x: x * 2)
rdd2.collect()

# reduce 递归 返回一个值
rdd3 = rdd.reduce(lambda x,y: x + y)
rdd3

# reduceByKey 返回rdd对象
rdd4 = sc.parallelize([[1, 2], [1, 10], [2, 3], [2, 4]])
rdd5 = rdd4.reduceByKey(lambda x, y: x + y)
rdd5.collect()

# reduceByKeyLocally # 返回值 字典格式
rdd6 = rdd4.reduceByKeyLocally(lambda x, y: x + y)
rdd6

# flatMap() 类似map

rdd7 = sc.parallelize([1, 2, 3, 4, 5, 6, 7])
rdd8 = rdd7.flatMap(lambda x: (x,x ** 2))
rdd8.collect()

#