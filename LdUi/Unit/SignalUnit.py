# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : SignalUnit.py
# Time       ：22/3/6 11:33
# Author     ：Lex
# email      : 2983997560@qq.com
# Description：界面回写信号量
"""

from PyQt5.Qt import QObject, pyqtSignal


class SignalUnit(QObject):
    # 运行状态 行 列 内容
    running_status = pyqtSignal(int, int, str)

    # 线程id
    thread_id = pyqtSignal(int, int, str)

    # 调试日志
    log = pyqtSignal(str)


signal = SignalUnit()

