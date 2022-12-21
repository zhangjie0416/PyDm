# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : processControl.py
# Time       ：22/3/5 18:44
# Author     ：Lex
# email      : 2983997560@qq.com
# Description：流程控制
"""
import time
from Application.Model.mainModel import MainModel
from Common.dmOperate import *
from Common.enterGame import enter_game
from Common.taskControl import taskControl
from Common.publicFunction import update_progress, update_log, update_thread_id


def ProcessControl(row_num):
    num = 0
    # 设置启动状态
    MainModel.update_one(row_num, "progress", "启动APP")
    while True:
        update_log("流程控制函数 %s 运行中 %d" % (str(row_num), num))
        num += 1
        time.sleep(1)

        # 获取指定行的数据
        progress = MainModel.get_thread(row_num, "progress")
        thread = MainModel.get_thread(row_num, "thread")
        update_thread_id(row_num, str(thread.handle))

        # 启动APP
        if progress == "启动APP":
            dm_runApp(row_num)

        time.sleep(1)

        # 查找没有绑定的窗口
        if progress == "查找窗口":
            dm_findWin(row_num)

        # 激活窗口并绑定
        if progress == "绑定窗口":
            dm_bindWin(row_num)

        # 进入游戏
        if progress == "进入游戏":
            enter_game(row_num)

        # 游戏操作
        if progress == "游戏操作":
            taskControl(row_num)

        # 任务完成
        if progress == "任务完成":
            update_progress(row_num, progress)
            break

        # 窗口失效
        if progress == "窗口失效":
            pass

        update_progress(row_num, progress)
        time.sleep(1)
