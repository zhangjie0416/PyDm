#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author      : topsec
# @Time        : 2022/12/14 10:26
# @File        : Logger.py
# @ScriptName  :

from datetime import datetime


class Logger(object):
    def __init__(self, debug=True):
        self.debug = debug

    def now(self):
        return str(datetime.now()).split('.')[0]

    def success(self, text):
        if self.debug:
            print(f"\033[1;32m{self.now()}\033[0m\033[1;31m - \033[0m\033[1;32m{text}\033[0m")

    def error(self, text):
        if self.debug:
            print(f"\033[1;31m{self.now()}\033[0m\033[1;31m - \033[0m\033[1;31m{text}\033[0m")

    def game_log(self, text):
        print(f"\033[1;33m{self.now()}\033[0m\033[1;31m - \033[0m\033[1;33m{text}\033[0m")


logger = Logger()
