# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : mainController.py
# Time       ：2022/3/2 20:22
# Author     ：Lex
# email      : 2983997560@qq.com
# Description：
"""
import os.path
import sys
from public import path
from PyQt5.QtCore import QSettings
from Common.dmOperate import dm_register
from Unit.SignalUnit import signal
from Unit.ThreadOperateUnit import ThreadOperateUnit
from Common.publicFunction import showMsg, get_task
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog
from Application.View.mainView import MainView
from Application.Model.mainModel import MainModel


class MainController:
    def __init__(self):
        self.ini = path + "\\config.ini"  # 配置文件路径
        self.mainView = MainView()
        self.mainModel = MainModel
        self.load_settings()
        self.load_account()
        self.event_init()
        self.operate_show()

    def event_init(self):
        """ 事件初始化 """
        # 右键菜单
        self.mainView.tableWidget.customContextMenuRequested.connect(self.show_menu)
        self.mainView.pushButton_3.clicked.connect(self.load_file)
        self.mainView.pushButton_4.clicked.connect(self.load_file)
        self.mainView.pushButton.clicked.connect(self.save_settings)
        # 任务框
        self.mainView.pushButton_9.clicked.connect(self.select_task)
        self.mainView.pushButton_8.clicked.connect(lambda: self.up_down_task("up"))
        self.mainView.pushButton_7.clicked.connect(lambda: self.up_down_task("down"))
        self.mainView.pushButton_6.clicked.connect(lambda: self.del_task("all"))
        self.mainView.pushButton_5.clicked.connect(lambda: self.del_task("one"))

        # 线程更新界面
        signal.running_status.connect(self.display_status)
        signal.thread_id.connect(self.display_status)
        signal.log.connect(self.display_log)

    def operate_show(self):
        if dm_register():
            # 注册成功
            self.mainView.show()
        else:
            showMsg(self.mainView, "软件异常, 请联系作者, 错误码 -1")
            sys.exit()

    def show_menu(self, pos):
        """ 右键菜单 """
        # 0 时为第一行
        rowNum = -1
        for i in self.mainView.tableWidget.selectionModel().selection().indexes():
            rowNum = i.row()  # 当前选择行数 从0开始
        # 空白处为 -1
        if rowNum >= 0:
            action = self.mainView.menu.exec_(self.mainView.tableWidget.mapToGlobal(pos))
            if action == self.mainView.item1:
                self.start_game("one", rowNum)
            elif action == self.mainView.item2:
                self.pause_game("one", rowNum)
            elif action == self.mainView.item3:
                self.resume_game("one", rowNum)
            elif action == self.mainView.item4:
                self.stop_game("one", rowNum)
            elif action == self.mainView.item5:
                self.start_game("all", rowNum)
                self.mainView.item5.setEnabled(False)
            elif action == self.mainView.item6:
                self.pause_game("all", rowNum)
            elif action == self.mainView.item7:
                self.resume_game("all", rowNum)
            elif action == self.mainView.item8:
                self.stop_game("all", rowNum)
                self.mainView.item5.setEnabled(True)

    def load_file(self):
        """ 加载文件 """
        file_path, file_type = QFileDialog.getOpenFileName(self.mainView, "请选择文件", "E:/",
                                                           "All Files (*);;Text Files (*.txt)")
        if file_path:
            if "Text Files (*.txt)" == file_type:
                self.mainView.lineEdit_2.setText(file_path)
                self.load_account()
            else:
                self.mainView.lineEdit.setText(file_path)

    def load_account(self):
        """ 加载账密至列表中 """
        # 清空
        self.mainView.tableWidget.clearContents()

        # 获取账密路径
        account_path = self.mainView.lineEdit_2.text()
        # 文件路径存在
        if os.path.exists(account_path):
            # 打开账号文件, 读取并加载
            with open(account_path, "r", encoding="utf8") as f:
                lines = f.readlines()
                # 文件不为空
                if lines:
                    # 重设表格行数，防止没有数据的行修改时出错
                    self.mainView.tableWidget.setRowCount(len(lines))
                    for num, line in enumerate(lines):
                        line = line.strip('\n').split("|")
                        self.mainView.tableWidget.setItem(num, 2, QTableWidgetItem(line[0]))
                        self.mainView.tableWidget.setItem(num, 3, QTableWidgetItem(line[1]))
                        self.mainView.tableWidget.setItem(num, 4, QTableWidgetItem(line[2]))

    def save_settings(self):
        """ 保存界面配置 """
        settings = QSettings(self.ini, QSettings.IniFormat)
        app_path = self.mainView.lineEdit.text()
        account_path = self.mainView.lineEdit_2.text()
        max_num = self.mainView.lineEdit_3.text()
        start_delay = self.mainView.lineEdit_4.text()
        setting_dict = {
            "app_path": app_path,
            "account_path": account_path,
            "max_num": max_num,
            "start_delay": start_delay
        }
        for key, value in setting_dict.items():
            settings.setValue(key, value)

    def load_settings(self):
        """ 加载配置 """
        if os.path.exists(self.ini):
            # 路径存在
            settings = QSettings(self.ini, QSettings.IniFormat)
            settings.setIniCodec("UTF-8")
            program_path = settings.value("program_path")
            account_path = settings.value("account_path")
            max_num = settings.value("max_num")
            start_delay = settings.value("start_delay")
            self.mainView.lineEdit.setText(program_path)
            self.mainView.lineEdit_2.setText(account_path)
            self.mainView.lineEdit_3.setText(max_num)
            self.mainView.lineEdit_4.setText(start_delay)

    def select_task(self):
        """ 从 待选任务 => 已选任务"""
        index = self.mainView.listWidget.currentRow()
        # 获取当前行号, 注意判断 不选择为 -1
        if index > -1:
            row_text = self.mainView.listWidget.item(index).text()
            task_list = get_task(self.mainView)
            if row_text not in task_list:
                self.mainView.listWidget_2.addItem(row_text)

    def up_down_task(self, flag):
        index_old = self.mainView.listWidget_2.currentRow()
        value_count = self.mainView.listWidget_2.count()
        if flag == "down":
            index_new = index_old + 1
        else:
            index_new = index_old - 1
        if flag == "down" and index_new != value_count:  # 限制向下范围
            value_old = self.mainView.listWidget_2.item(index_old).text()
            self.mainView.listWidget_2.takeItem(index_old)  # 删除上方内容
            self.mainView.listWidget_2.insertItem(index_new, value_old)  # 指定位置添加内容
        elif flag == "up" and index_new >= 0:
            value_old = self.mainView.listWidget_2.item(index_new).text()
            self.mainView.listWidget_2.takeItem(index_new)
            self.mainView.listWidget_2.insertItem(index_old, value_old)

    def del_task(self, flag):
        if flag == "one":
            index = self.mainView.listWidget_2.currentRow()
            # 获取当前行号, 注意判断 不选择为 -1
            if index > -1:
                self.mainView.listWidget_2.takeItem(index)
        else:
            # 删除全部
            self.mainView.listWidget_2.clear()

    def start_game(self, flag, rowNum):
        # 获取任务信息, 传入, 启动总线程
        task_list = get_task(self.mainView)
        max_num = self.mainView.lineEdit_3.text()
        row_count = self.mainView.tableWidget.rowCount()
        start_delay = self.mainView.lineEdit_4.text()
        app_path = self.mainView.lineEdit.text()

        # 更新数据
        self.mainModel.update_total("app_path", app_path)
        self.mainModel.update_total("task_list", task_list)
        send_data = {
            "flag": flag,
            "max_num": min(int(max_num), int(row_count)),
            "row_num": rowNum,
            "start_delay": start_delay,
        }
        ThreadOperateUnit(**send_data).start_thread()

    def pause_game(self, flag, row_num):
        send_data = {
            "flag": flag,
            "row_num": row_num
        }
        ThreadOperateUnit(**send_data).pause_thread()

    def resume_game(self, flag, row_num):
        send_data = {
            "flag": flag,
            "row_num": row_num
        }
        ThreadOperateUnit(**send_data).resume_thread()

    def stop_game(self, flag, row_num):
        max_num = self.mainView.lineEdit_3.text()
        send_data = {
            "flag": flag,
            "max_num": max_num,
            "row_num": row_num
        }
        ThreadOperateUnit(**send_data).stop_thread()

    def display_status(self, row, column, content):
        """ 线程状态更新 """
        self.mainView.tableWidget.setItem(row, column, QTableWidgetItem(content))

    def display_log(self, content):
        """ 日志打印 """
        self.mainView.textBrowser.append(content)
        self.mainView.textBrowser.ensureCursorVisible()
