# -*- coding: utf-8 -*-
# @Time: 2021/5/26 上午11:23
# @Author: yuyinghao
# @FileName: 04_ml.py
# @Software: PyCharm

from sklearn.datasets import load_iris
from pyspark.sql import SparkSession
from pyspark.ml import feature as fe
import pandas as pd
from pyspark.sql import functions as F

spark = SparkSession.builder.master('local').appName('test').getOrCreate()

# 获取数据
data = load_iris()
df = pd.DataFrame(data.data, columns = data.feature_names)
df['lable'] = data.target

# 数据转换
df = spark.createDataFrame(df)

# feature类
# Binarizer
binarizer = fe.Binarizer(threshold = 0.5, inputCol='petal width (cm)', outputCol='petal width (cm)_2')
df2 = binarizer.transform(df)


df = spark.createDataFrame([([1, 2, 3, 2],), ([4, 5, 5, 4],)], ['data'])
df.select(F.array_distinct(df.data)).collect()
