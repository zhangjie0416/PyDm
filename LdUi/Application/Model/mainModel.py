# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : mainModel.py
# Time       ：2022/3/2 20:22
# Author     ：Lex
# email      : 2983997560@qq.com
# Description：
"""
from public import *


class MainModel:
    @classmethod
    def update_one(cls, row_num, key, value, gl_data_type=0):
        """ 更新一行数据 """
        # 获取线程锁
        gl_thread_lock.acquire()
        # 更新数据
        if gl_data_type == 0:
            gl_data = gl_thread_data
        else:
            gl_data = gl_monitor_data
        gl_data[row_num][key] = value
        # 释放
        gl_thread_lock.release()

    @classmethod
    def get_thread(cls, row_num, key, gl_data_type=0):
        """ 获取一行数据 """
        if gl_data_type == 0:
            gl_data = gl_thread_data
        else:
            gl_data = gl_monitor_data
        re_data = gl_data[row_num][key]
        return re_data

    @classmethod
    def del_thread(cls, row_num, key, gl_data_type=0):
        """ 删除一行数据 """
        # 获取线程锁
        if gl_data_type == 0:
            gl_data = gl_thread_data
        else:
            gl_data = gl_monitor_data
        gl_thread_lock.acquire()
        gl_data[row_num][key] = None
        gl_thread_lock.release()

    @classmethod
    def get_total(cls, key):
        return gl_total_data[key]

    @classmethod
    def update_total(cls, key, val):
        """ 清空所有行 """
        gl_thread_lock.acquire()
        gl_total_data[key] = val
        gl_thread_lock.release()

    @classmethod
    def del_thread_all(cls, row_num, gl_data_type=0):
        """ 删除某一行的所有key数据 """
        if gl_data_type == 0:
            gl_data = gl_thread_data
        else:
            gl_data = gl_monitor_data
        for key, val in gl_data[row_num].items():
            gl_data[row_num][key] = None
