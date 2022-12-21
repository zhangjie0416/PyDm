# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : dmOperate.py
# Time       ：22/3/5 16:35
# Author     ：Lex
# email      : 2983997560@qq.com
# Description：大漠操作封装
"""
import os
import time
from PyGameAuto.Dm import RegDm
from Application.Model.mainModel import MainModel


def dm_register():
    """
     大漠注册
    :return: 成功 返回1, 失败或异常返回0
    """
    try:
        # 初始化大漠对象相关操作
        dm = RegDm.reg()
        dm_ret = dm.reg("ly901107042d26f3c35d6f239df9ad66ae403894", "lexgeeker6666")
        if dm_ret != 1:
            return 0
        return 1
    except Exception as e:
        return 0


def dm_create():
    """
    大漠对象创建
    :return: 成功 返回创建对象, 失败或异常返回0
    """
    try:
        return RegDm.CreateObj()
    except Exception as e:
        return


def dm_closeErr(dm):
    dm.SetShowErrorMsg(0)


def dm_setPath(dm):
    path = os.getcwd() + "\\Resource\\static"
    ret = dm.SetPath(path)
    return ret


def dm_setDict(dm):
    dm.SetDict(0, "font.txt")


def dm_unBind(dm):
    dm.UnBindWindow()


def dm_runApp(row_num):
    # 获取一行数据
    dm = MainModel.get_thread(row_num, "dm")
    app_path = MainModel.get_total("app_path")
    dm.RunApp(app_path, 1)

    # 回写状态
    MainModel.update_one(row_num, "progress", "查找窗口")


def dm_findWin(row_num):
    # 获取一行数据
    dm = MainModel.get_thread(row_num, "dm")
    hwnds = dm.EnumWindow(0, "记事本", "Notepad", 1+2)

    hwnd_list = []
    for num, hwnd in enumerate(hwnds.split(",")):
        # 获取第一个子窗口
        hwnd = dm.GetWindow(int(hwnd), 1)
        if dm.IsBind(int(hwnd)) == 1:
            continue
        # 没有绑定
        hwnd_list.append(hwnd)
    if hwnd_list:
        # 回写数据
        hwnd = hwnd_list[-1]
        MainModel.update_one(row_num, "hwnd", hwnd)
        MainModel.update_one(row_num, "progress", "绑定窗口")


def dm_bindWin(row_num):
    """ 绑定窗口 """
    # 获取一行数据
    dm = MainModel.get_thread(row_num, "dm")
    hwnd = MainModel.get_thread(row_num, "hwnd")
    ret = dm.BindWindow(int(hwnd), "gdi", "windows", "windows", 0)
    if ret != 1:
        # 绑定失败 回写
        MainModel.update_one(row_num, "progress", "窗口失效")
    else:
        # 激活窗口
        dm.SetWindowState(hwnd, 1)
        time.sleep(0.1)

        # # 创建监控大漠对象
        # mt_dm = dm_create()
        # if mt_dm:
        #     # 回写数据
        #     MainModel.update_one(row_num, "dm", mt_dm, gl_data_type=1)
        # else:
        #     pass
        # 移动窗口
        hwnd = dm.GetWindow(hwnd, 0)
        dm.MoveWindow(int(hwnd), row_num * 200, 0)
        # 回写数据
        MainModel.update_one(row_num, "progress", "进入游戏")


def dm_isAlive(row_num):
    pass
