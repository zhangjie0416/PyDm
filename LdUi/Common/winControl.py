# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : winControl.py
# Time       ：22/3/5 18:26
# Author     ：Lex
# email      : 2983997560@qq.com
# Description：窗口线程流程操作
"""
import time

from Application.Model.mainModel import MainModel
from Common.dmOperate import *
from PyGameAuto.Thread.MyThread import MyThread

from Common.processControl import ProcessControl


def winControl(row_num):
    """ 根据行号 获取大漠对象, 并进行前期设置 """
    # 初始化com
    MyThread().init_com()

    # 获取一行数据
    dm = MainModel.get_thread(row_num, "dm")
    time.sleep(3)
    # 关闭错误开关
    dm_closeErr(dm)

    # 设置路径
    dm_setPath(dm)

    # 设置字库
    dm_setDict(dm)

    # 流程函数
    ProcessControl(row_num)

    # 解绑
    dm_unBind(dm)

    # 停止线程
    thread = MainModel.get_thread(row_num, "thread")
    thread.thread_stop()

    # 释放
    MyThread().uninstall_com()
