# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : mainView.py
# Time       ：2022/3/2 19:54
# Author     ：Lex
# email      : 2983997560@qq.com
# Description：主界面View
"""
from Resource.ui.main import MainUI
from PyQt5.QtWidgets import QWidget, QMenu, QFileDialog
from PyQt5.QtCore import Qt


class MainView(MainUI, QWidget):

    def __init__(self):
        super(MainView, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.menu = QMenu()
        self.ui_init()

    def ui_init(self):
        """ 自定义初始化 """
        # 第0行和标题间横杠
        self.tableWidget.horizontalHeader().setStyleSheet(
            "border-bottom-width: 0.5px;border-style: outset;border-color: rgb(229,229,229);"
        )
        # 右键产生子菜单
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.item1 = self.menu.addAction(u"启动选中")
        self.item2 = self.menu.addAction(u"暂停选中")
        self.item3 = self.menu.addAction(u"恢复选中")
        self.item4 = self.menu.addAction(u"停止选中")
        self.item5 = self.menu.addAction(u"启动所有")
        self.item6 = self.menu.addAction(u"暂停所有")
        self.item7 = self.menu.addAction(u"恢复所有")
        self.item8 = self.menu.addAction(u"停止所有")
