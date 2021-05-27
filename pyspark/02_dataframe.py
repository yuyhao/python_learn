


from pyspark.sql import SparkSession
spark=SparkSession.builder.master("local").appName("test").getOrCreate()
sc=spark.sparkContext

# 创建dataframe

# 通过rdd
rdd= sc.parallelize([('John',30),('Mary',78)])
dataframe=spark.createDataFrame(rdd,['name','age'])
print(dataframe.collect())

# 通过python
data=[('John',30),('Mary',78)]
dataframe=spark.createDataFrame(data,['name','age'])
print(dataframe.collect())

# 通过pandas转换
import pandas as pd
data = pd.DataFrame({'name': ['John', 'Mary'], 'age': [30, 78]})
data = spark.createDataFrame(data)
data.collect()

# 读取外部数据
spark.read.csv(

)

spark.read.json(

)

# 操作dataframe

# columns 返回列表
data.columns

# dtypes 返回列表
data.dtypes

# take 返回前n行数据
data.take(2)

# show 打印结果
z = data.show()

# 筛选 列
data.select(['name'])

# 筛选 行
data.filter()

# drop # 不能删除列表
data.drop('name')

# head()
data.head()

# count
data.count()

# describe
data.describe()

###################################
import numpy as np
data = pd.DataFrame({'A': [1, 2, 3, 4, np.nan], 'B':['a', 'b', 'c', 'd', 'e']})

df = spark.createDataFrame(data)

# printSchema
df.printSchema()

# 去重 distinct
df.select('A').distinct().show()

# 随机抽样
df.sample()

# 选择一列或者多列
df.select(['A', 'B'])
df.select('A')
df.select(df.A, df.B)

# where
df.where(df.A == 1).show()
df.where('A = 1').show()

# 排序 orderBy
df.orderBy(df['A']).show()
df.orderBy(df['A'].desc()).show()

# 按条件筛选 when between
from pyspark.sql import functions as F
df.select(df['A'], F.when(df['A'] > 2, 1).otherwise(0)).show()

# 新增列 withColumn
df.withColumn('C', F.lit(9)).show()

# isin
df.where(df['A'].isin([1, 2]))

#########################################
# 数据合并 union join
data2 = data
df2 = spark.createDataFrame(data2)

# union
df.union(df2).show()

# join


###########################################
# 统计
df.crosstab(df['A'], df['B'])

# 分组 groupBy

# apply
df.rdd.ma
