# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : enterGame.py
# Time       ：22/3/6 11:15
# Author     ：Lex
# email      : 2983997560@qq.com
# Description：进入游戏
"""
import time
from Common.publicFunction import update_progress
from Application.Model.mainModel import MainModel


def enter_game(row_num):
    # 获取一行数据
    dm = MainModel.get_thread(row_num, "dm")
    # 进入游戏操作
    time.sleep(3)
    # 进入成功

    # 回写数据
    MainModel.update_one(row_num, "progress", "游戏操作")
