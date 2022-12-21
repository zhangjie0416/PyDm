# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : taskControl.py
# Time       ：22/3/6 8:01
# Author     ：Lex
# email      : 2983997560@qq.com
# Description：游戏操作
"""
import time

from Application.Model.mainModel import MainModel
from Common.publicFunction import update_log


def taskControl(row_num):
    dm = MainModel.get_thread(row_num, "dm")
    hwnd = MainModel.get_thread(row_num, "hwnd")
    task_list = MainModel.get_total("task_list")
    for index in range(len(task_list)):
        # 主线任务
        if task_list[index] == "主线任务":
            # 执行主线任务
            for item in range(20):
                dm.SendString(hwnd, "窗口 %s 执行主线任务 %d\n" % (str(row_num), item))
                time.sleep(1)
                update_log("窗口 %s 执行主线任务 %d" % (str(row_num), item))

        # 副本任务
        elif task_list[index] == "副本任务":
            for item in range(20):
                dm.SendString(hwnd, "窗口 %s 执行副本任务 %d\n" % (str(row_num), item))
                time.sleep(1)
                update_log("窗口 %s 执行副本任务 %d" % (str(row_num), item))

        # 跑图任务
        elif task_list[index] == "跑图任务":
            for item in range(20):
                dm.SendString(hwnd, "窗口 %s 执行跑图任务 %d\n" % (str(row_num), item))
                time.sleep(1)
                update_log("窗口 %s 执行跑图任务 %d" % (str(row_num), item))

    # 回写数据
    MainModel.update_one(row_num, "progress", "任务完成")
