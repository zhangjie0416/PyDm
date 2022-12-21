# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : ThreadOperateUnit.py
# Time       ：22/3/5 19:44
# Author     ：Lex
# email      : 2983997560@qq.com
# Description：线程操作
"""
import threading
import time
from Common.publicFunction import update_log, update_thread_id
from Application.Model.mainModel import MainModel
from Common.winControl import winControl
from PyGameAuto.Thread.MyThread import MyThread
from Common.dmOperate import dm_create


def pause_one_thread(row_num):
    # 查询对应 row_num 是否在启动过
    thread = MainModel.get_thread(row_num, "thread")
    if thread:
        # 启动过, 进行判断, 是否存活
        if thread.is_alive:
            update_log("暂停线程 %s" % str(row_num))
            thread.thread_pause()


def resume_one_thread(row_num):
    # 查询对应 row_num 是否在启动过
    thread = MainModel.get_thread(row_num, "thread")
    if thread:
        # 启动过, 进行判断, 是否存活
        if thread.is_alive:
            update_log("恢复线程 %s" % str(row_num))
            thread.thread_resume()


def stop_one_thread(row_num):
    # 查询对应 row_num 是否在启动过
    thread = MainModel.get_thread(row_num, "thread")
    if thread:
        # 启动过, 进行判断, 是否存活
        if thread.is_alive:
            update_log("停止线程 %s" % str(row_num))
            thread.thread_stop()
            MainModel.del_thread_all(row_num)


def count_row():
    """ 获取库中线程 row_num """
    thread_num = MainModel.get_total("thread_num")
    return thread_num


class ThreadOperateUnit:
    def __init__(self, **kwargs):
        super(ThreadOperateUnit, self).__init__()
        self.task_list = kwargs.get("task_list", None)
        self.flag = kwargs.get("flag", None)
        self.row_num = kwargs.get("row_num", None)
        self.max_num = kwargs.get("max_num", None)
        self.start_delay = kwargs.get("start_delay", None)
        self.app_path = kwargs.get("app_path", None)

    def __start_one_thread(self):
        # 查询对应 row_num 是否在启动过
        thread = MainModel.get_thread(self.row_num, "thread")
        thread_num = MainModel.get_total("thread_num")
        if thread:
            # 启动过, 进行判断, 是否存活
            if thread.is_alive:
                update_log("线程 %s 已在运行...." % int(self.row_num))
        else:
            # 创建大漠对象
            dm = dm_create()
            if not dm:
                return
            # 回写线程数据
            MainModel.update_one(self.row_num, "dm", dm)

            thread = MyThread(winControl, args=(self.row_num,))
            thread.start()
            update_log("启动线程 %s" % str(self.row_num))
            thread_num += 1
            # 回写数据
            MainModel.update_one(self.row_num, "thread", thread)
            MainModel.update_total("thread_num", thread_num)

    def __start_all_thread(self):
        MyThread().init_com()
        # 启动所有
        for item in range(int(self.max_num)):
            self.row_num = item
            self.__start_one_thread()
            time.sleep(int(self.start_delay))
        MyThread().uninstall_com()

    def start_thread(self):
        if self.flag == "one":
            self.__start_one_thread()
        else:
            thread = MyThread(target=self.__start_all_thread)
            thread.start()

    def pause_thread(self):
        if self.flag == "one":
            pause_one_thread(self.row_num)
        else:
            # max 停止应该是取库中线程数
            for item in range(count_row()):
                self.row_num = item
                pause_one_thread(item)

    def resume_thread(self):
        if self.flag == "one":
            resume_one_thread(self.row_num)
        else:
            # max 停止应该是取库中线程数
            # 恢复所有
            for item in range(count_row()):
                self.row_num = item
                resume_one_thread(item)

    def stop_thread(self):
        if self.flag == "one":
            stop_one_thread(self.row_num)
        else:
            # max 停止应该是取库中线程数
            for item in range(count_row()):
                self.row_num = item
                stop_one_thread(item)
