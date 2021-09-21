# -*- coding: utf-8 -*-
# @Time: 2021/9/13 18:29
# @Author: yuyinghao
# @FileName: get_redis_data.py
# @Software: PyCharm

import redis

def init_redis_pool(host, port, db, password='', decode_responses=True):
    pool = redis.ConnectionPool(host=host, port=port, db=db, password=password, decode_responses=decode_responses,
                                socket_connect_timeout=200)
    return redis.StrictRedis(connection_pool=pool)



