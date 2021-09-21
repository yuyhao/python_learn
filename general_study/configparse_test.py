# -*- coding: utf-8 -*-
# @Time: 2021/9/13 10:28
# @Author: yuyinghao
# @FileName: configparse_test.py
# @Software: PyCharm

import configparser

property_path = '/properties.ini'

config = configparser.ConfigParser()  # config初始化
config.read(property_path, encoding='utf-8')  # 读入配置文件

# 常用配置
config.sections()  # 0 读取所有的section

config.options('my_property')  # 读取指定section的option键

if config.has_option('my_property', 'my_name'):
    config.get('my_property', 'my_name')  # 读取指定section 指定key的值

config.items('my_property')  # 读取指定section的全部内容, 返回[元组]  [('my_name', 'yuyinghao'), ('my_age', '29'), ('my_sexy', 'male')]

config.set('my_property', 'my_name', 'yuyh2')
config.write(open(property_path, 'w'))  # 修改配置

config.has_section("my")  # 检查option是否存在
config.has_option("my_property", 'my_name')  # 检查option是否存在

config.add_section('my_property2')

config.remove_option('my_property', 'my_name')
config.write(open(property_path, 'w'))



