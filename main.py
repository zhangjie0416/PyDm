# version=1.0
# update:20210423
import os
import time
import datetime
import win32com.client
from random import randint
from Config import *


class DM(object):
    def __init__(self, log_print=False, write_log=False):
        self.log_print = log_print
        self.write_log = write_log
        self.CheckDir()
        self.Register()
        self.dict_index = 0
        self.SetPath(r'{}\resource'.format(os.getcwd()))

    def SetDict(self, index, file):
        self.dm.SetDict(index, file)
        return

    def UseDict(self, index):
        if index != self.dict_index:
            self.dm.UseDict(index)
            self.dict_index = index
        return

    def Capture(self, x1, y1, x2, y2, file):
        save_path = r'{}\screen\{}'.format(os.getcwd(), file)
        self.LogPrint(log_info["Capture"][0].format(x1, y1, x2, y2, save_path))
        return self.dm.Capture(x1, y1, x2, y2, save_path)

    def CheckDir(self):
        if not os.path.exists('log'):
            os.mkdir("log")
        if not os.path.exists('resource'):
            os.mkdir("resource")
        if not os.path.exists('screen'):
            os.mkdir("screen")

    def LogPrint(self, info):
        if self.log_print:
            print("{}: {}".format(str(datetime.datetime.now()).split('.')[0].split(' ')[1], info))
        if self.write_log:
            with open("log/{}.txt".format(str(datetime.datetime.now()).split('.')[0].split(' ')[0]), "a") as log:
                log.write("{}: {}\n".format(str(datetime.datetime.now()).split('.')[0].split(' ')[1], info))
        return

    def Register(self):
        try:
            old_time = time.time()
            self.dm = win32com.client.Dispatch('dm.dmsoft')
            delta_T = round(time.time() - old_time, 3)
            self.LogPrint(f"调用大漠插件成功,版本号【{self.dm.Ver()}】调用时间:{delta_T}")
        except Exception as e:
            self.LogPrint("调用大漠插件失败:{}".format(e))
        dm_ret = self.dm.Reg("zj545768869285fc98bd0c1674b1eaf4268359ef244", "")
        if dm_ret == 1:
            self.LogPrint("大漠插件收费注册成功")

        else:
            if str(dm_ret) in register_error_code.keys():
                self.LogPrint("收费注册失败,返回值:{},错误信息:{}".format(dm_ret, register_error_code[str(dm_ret)]))
            else:
                self.LogPrint("错误码:{},未找到对应错误信息".format(dm_ret))

        return

    def SetPath(self, path):
        self.dm.SetPath(path)
        return

    def GetLastError(self):
        error_info = str(self.dm.GetLastError())
        if error_info in last_error_code.keys():
            self.LogPrint("错误码:{}|{}".format(error_info, last_error_code[error_info]))
        return error_info

    def RandomDelay(self, start, stop):
        self.dm.Delay(randint(start, stop))
        return

    def EnumWindowByProcess(self, process_name, title, class_name, filter=1 + 2 + 8 + 16):
        hwnds = self.dm.EnumWindowByProcess(process_name, title, class_name, filter)
        if hwnds:
            hwnd_list = [int(hwnd) for hwnd in hwnds.split(",")]
        else:
            hwnd_list = []
        self.LogPrint("找到窗口句柄{}个: {}".format(len(hwnd_list), hwnd_list))
        return hwnd_list

    def BindWindowEx(self, hwnd, display, mouse, keypad, public, mode):
        bind_info = self.dm.BindWindowEx(hwnd, display, mouse, keypad, public, mode)
        if bind_info != 1:
            self.LogPrint("窗口绑定失败,即将调用错误码示例...")
            self.GetLastError()
        else:
            self.LogPrint("窗口绑定成功,句柄: {}".format(hwnd))
        return bind_info

    def RandomLeftClick(self, double=False):
        if double:
            self.dm.LeftDown()
            self.RandomDelay(5, 10)
            self.dm.LeftUp()
            self.RandomDelay(5, 10)
        self.dm.LeftDown()
        self.RandomDelay(5, 10)
        self.dm.LeftUp()
        self.RandomDelay(5, 10)
        return

    def RandomRightClick(self, double=False):
        if double:
            self.dm.RightDown()
            self.RandomDelay(10, 20)
            self.dm.RightUp()
            self.RandomDelay(10, 20)
        self.dm.RightDown()
        self.RandomDelay(10, 20)
        self.dm.RightUp()
        self.RandomDelay(10, 20)
        return

    def MoToClick(self, x, y, w=5, h=5, left=True, double=False, offset=True):
        if offset:
            self.dm.MoveToEx(x, y, w, h)
        else:
            self.dm.MoveTo(x, y)
        self.RandomDelay(30, 50)
        if left:
            if double:
                self.RandomLeftClick(double=True)
            else:
                self.RandomLeftClick()
        else:
            if double:
                self.RandomRightClick(double=True)
            else:
                self.RandomRightClick()
        return

    def FindPic(self, x1, y1, x2, y2, pic_name, delta_color, sim, click, find_time):
        self.LogPrint(log_info["FindPic"][0].format(x1, y1, x2, y2, pic_name, delta_color, sim, click, find_time))
        start_time, count_num = time.time(), 0
        while True:
            pic_index = self.dm.FindPic(x1, y1, x2, y2, pic_name, delta_color, sim, 0)
            count_num += 1
            if pic_index[0] != -1:
                if click == 1:
                    self.MoToClick(pic_index[1], pic_index[2])
                break
            if time.time() - start_time >= find_time:
                break
            self.RandomDelay(95, 96)
        elapsed_time = round((time.time() - start_time) * 1000, 2)
        self.LogPrint(log_info["FindPic"][1].format(pic_index, count_num, elapsed_time))
        return pic_index

    def FindPicPara(self, args):
        x1, y1, x2, y2, pic_name, delta_color = args[0], args[1], args[2], args[3], args[4], args[5]
        sim, click, find_time = 0.9, 1, 1
        if len(args) == 7:
            if args[6].get("sim"): sim = args[6]["sim"]
            if args[6].get("click"): click = args[6]["click"]
            if args[6].get("find_time"): find_time = args[6]["find_time"]
        self.FindPic(x1, y1, x2, y2, pic_name, delta_color, sim, click, find_time)
        return

    def FindMultiColor(self, x1, y1, x2, y2, first_color, offset_color, sim, click, find_time):
        self.LogPrint(
            log_info["FindMultiColor"][0].format(x1, y1, x2, y2, first_color, offset_color, sim, click, find_time))
        start_time, count_num = time.time(), 0
        while True:
            colour_index = self.dm.FindMultiColor(x1, y1, x2, y2, first_color, offset_color, sim, 0)
            count_num += 1
            if colour_index[0]:
                if click == 1:
                    self.MoToClick(colour_index[1], colour_index[2])
                break
            else:
                if time.time() - start_time >= find_time:
                    break
                self.RandomDelay(50, 51)
        elapsed_time = round((time.time() - start_time) * 1000, 2)
        self.LogPrint(log_info["FindMultiColor"][1].format(colour_index, count_num, elapsed_time))
        return colour_index

    def FindMultiColorPara(self, args):
        x1, y1, x2, y2, = args[0], args[1], args[2], args[3],
        color_name, first_color, offset_color = args[4], args[5], args[6]
        sim, click, find_time = 0.9, 1, 1
        if len(args) == 8:
            if args[7].get("sim"): sim = args[7]["sim"]
            if args[7].get("click"): click = args[7]["click"]
            if args[7].get("find_time"): find_time = args[7]["find_time"]
        self.FindMultiColor(x1, y1, x2, y2, first_color, offset_color, sim, click, find_time)
        return

    def FindStr(self, x1, y1, x2, y2, string, color_format, sim, font_dict, click, find_time):
        self.LogPrint(log_info["FindStr"][0].format(x1, y1, x2, y2, string, color_format,
                                                    sim, font_dict, click, find_time))
        self.UseDict(font_dict)
        start_time,count_num = time.time(),0
        while True:
            font_index = self.dm.FindStr(x1, y1, x2, y2, string, color_format, sim)
            count_num += 1
            if font_index[0] != -1:
                if click == 1:
                    self.MoToClick(font_index[1], font_index[2])
                break
            else:
                if time.time() - start_time >= find_time:
                    break
                self.RandomDelay(50, 51)
        elapsed_time = round((time.time() - start_time) * 1000, 2)
        self.LogPrint(log_info["FindStr"][1].format(font_index, count_num, elapsed_time))
        return

    def FindStrPara(self, args):
        x1, y1, x2, y2, string, color_format = args[0], args[1], args[2], args[3], args[4], args[5]
        sim, click, font_dict, find_time = 0.9, 1, 1, 1
        if len(args) == 7:
            if args[6].get("sim"): sim = args[6]["sim"]
            if args[6].get("click"): click = args[6]["click"]
            if args[6].get("font_dict"): font_dict = args[6]["font_dict"]
            if args[6].get("find_time"): find_time = args[6]["find_time"]
        self.FindStr(x1, y1, x2, y2, string, color_format, sim, font_dict, click, find_time)
        return

    def Ocr(self, x1, y1, x2, y2, color_format, sim, font_dict, find_time):
        self.LogPrint(log_info["Ocr"][0].format(x1, y1, x2, y2, color_format, sim, font_dict, find_time))
        self.UseDict(font_dict)
        start_time,count_num = time.time(),0
        while True:
            font = self.dm.Ocr(x1, y1, x2, y2, color_format, sim)
            count_num += 1
            if font:
                break
            else:
                if time.time() - start_time >= find_time:
                    break
                self.RandomDelay(50, 51)
        elapsed_time = round((time.time() - start_time) * 1000, 2)
        self.LogPrint(log_info["Ocr"][1].format(font, count_num, elapsed_time))
        return

    def OcrPara(self, args):
        x1, y1, x2, y2, color_format = args[0], args[1], args[2], args[3], args[4],
        sim, font_dict, find_time = 0.9, 1, 1
        if len(args) == 6:
            if args[5].get("sim"): sim = args[5]["sim"]
            if args[5].get("font_dict"): font_dict = args[5]["font_dict"]
            if args[5].get("find_time"): find_time = args[5]["find_time"]
        self.Ocr(x1, y1, x2, y2, color_format, sim, font_dict, find_time)
        return


if __name__ == '__main__':
    dm = DM(log_print=True, write_log=True)
