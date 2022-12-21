# -*- coding: utf-8 -*-
# @Author      : topsec
# @Time        : 2022/12/14 10:10
# @File        : PyLd.py
# @ScriptName  : 雷电模拟器方法

import os
import shutil
import time
from public.Logger import logger


class PyLd(object):

    def __init__(self, console_path):
        # 请根据自己电脑配置
        self.console = os.path.join(console_path, "dnconsole.exe")
        self.ld = os.path.join(console_path, 'ld.exe')
        self.share_path = os.path.join(console_path, 'share')

    def run_command(self, command, index=0, command_type=0):
        if command_type == 0:
            result = os.popen(f"{self.console} {command}").read()
        elif command_type == 1:
            result = os.popen(f'{self.ld} -s {index} {command}').read()
        else:
            result = ""
        return result

    def get_list(self):
        """
        获取模拟器列表
        每个模拟器列表包含：索引，标题，顶层窗口句柄，绑定窗口句柄，是否进入android，进程PID，VBox进程PID
        """
        result = self.run_command("list2").split('\n')
        simulator_list = []
        for simulator in result:
            if "99999" in simulator or not simulator: continue
            simulator_info = simulator.split(',')
            simulator_dict = {
                "索引": simulator_info[0],
                "标题": simulator_info[1],
                "顶层窗口句柄": simulator_info[2],
                "绑定窗口句柄": simulator_info[3],
                "是否进入android": simulator_info[4],
                "进程PID": simulator_info[5],
                "VBox进程PID": simulator_info[6],
            }
            simulator_list.append(simulator_dict)
        return simulator_list

    def list_running(self):
        """
        获取正在运行的模拟器列表
        """
        running_list = []
        for simulator in self.get_list():
            if simulator["是否进入android"] == "1":
                running_list.append(simulator)
        return running_list

    def install(self, index: int, path: str):
        logger.success(f"模拟器:{index} 安装APP:{path}")
        shutil.copy(path, self.share_path + str(index) + '/update.apk')
        time.sleep(1)
        self.run_command('pm install /sdcard/Pictures/update.apk', command_type=1, index=index)
        return

    def uninstall(self, index: int, package: str):
        logger.success(f"模拟器:{index} 卸载APP:{package}")
        result = self.run_command(f'uninstallapp --index {index} --packagename {package}')
        logger.success(result)
        return result

    def start_app(self, index: int, package: str):
        logger.success(f"模拟器:{index} 启动APP:{package}")
        result = self.run_command(f'runapp --index {index} --packagename {package}')
        return result

    def stop_app(self, index: int, package: str):
        logger.success(f"模拟器:{index} 停止APP:{package}")
        result = self.run_command(f'killapp --index {index} --packagename {package}')
        return result

    # 获取安装包列表
    def get_package_list(self, index):
        package_list = self.run_command('pm list packages -3', command_type=1, index=index).split('\n\n')
        return [package for package in package_list if package]

    def has_install(self, index: int, package: str):
        # 检测是否安装指定的应用
        logger.success(f"模拟器:{index} 检测是否安装:{package}")
        if package in self.get_package_list(index):
            status = True
        else:
            status = False
        return status

    def launch(self, index):
        # 启动模拟器
        result = self.run_command(f'launch --index {index}')
        return result

    def quit(self, index):
        # 关闭模拟器
        result = self.run_command(f'quit --index {index}')
        return result

    # 添加模拟器
    def add(self, name: str):
        logger.success(f"添加模拟器:{name}")
        result = self.run_command(f"add --name {name}")
        return result


if __name__ == '__main__':
    ld = PyLd("D:\SoftWare\leidian\LDPlayer4")
    print(ld.list_running())
    print(ld.get_package_list('0'))
