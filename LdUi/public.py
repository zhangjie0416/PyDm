# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : public.py
# Time       ：2022/3/2 21:19
# Author     ：Lex
# email      : 2983997560@qq.com
# Description：全局变量
"""
import copy
import os
import threading

# 路径设置
path = os.getcwd() + "\\Resource\\static\\"


# 数据结构
thread_data = {
    "dm": None,
    "thread": None,
    "hwnd": None,
    "account": None,
    "password": None,
    "progress": None
}

monitor_data = {
    "dm": None,
    "hwnd": None
}

# 全局数据
gl_total_data = {
    "thread_num": 0,
    'task_list': [],
    "app_path": None
}

gl_thread_lock = threading.Lock()       # 全局锁
gl_thread_data = []                     # 线程数据
gl_monitor_data = []                    # 监控数据
# 深浅拷贝
for item in range(100):
    thread_dict = copy.deepcopy(thread_data)
    monitor_dict = copy.deepcopy(monitor_data)
    gl_thread_data.append(thread_dict)
    gl_monitor_data.append(monitor_dict)

