# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : publicFunction.py
# Time       ：2022/3/2 20:20
# Author     ：Lex
# email      : 2983997560@qq.com
# Description：公共函数
"""
from Unit.SignalUnit import signal
from PyQt5.QtWidgets import QMessageBox


def showMsg(widget, msg):
    QMessageBox.warning(widget, "温馨提示", msg, QMessageBox.Yes)


def get_task(widget):
    index = widget.listWidget_2.count()
    task_list = []
    for item in range(index):
        index_value = widget.listWidget_2.item(item).text()
        task_list.append(index_value)
    return task_list


def update_progress(row, content):
    signal.running_status.emit(row, 1, content)


def update_thread_id(row, context):
    signal.thread_id.emit(row, 0, context)


def update_log(content):
    signal.log.emit(content)
