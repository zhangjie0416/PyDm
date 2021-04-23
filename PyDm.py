# version=1.0
# update:20210423
import os
import time
import datetime
import win32com.client
from random import randint


class DM(object):
    def __init__(self, log_print=False, wirte_log=False):
        self.log_print = log_print
        self.write_log = wirte_log
        self.CheckDir()
        self.Register()
        self.dict_index = 0
        self.SetPath(r'F:\游戏脚本\大漠\resource')

    def SetDict(self, index, file):
        self.dm.SetDict(index, file)
        return

    def UseDict(self, index):
        if index != self.dict_index:
            self.dm.UseDict(index)
            self.dict_index = index
        return

    def CheckDir(self):
        if not os.path.exists('log'):
            os.mkdir("log")

    def LogPrint(self, info):
        if self.log_print:
            print("{}: {}".format(str(datetime.datetime.now()).split('.')[0].split(' ')[1], info))
        if self.write_log:
            with open("log/{}.txt".format(str(datetime.datetime.now()).split('.')[0].split(' ')[0]), "a") as log:
                log.write("{}: {}\n".format(str(datetime.datetime.now()).split('.')[0].split(' ')[1], info))
        return

    def Register(self):
        error_code = {'-1': '无法连接网络,(可能防火墙拦截,如果可以正常访问大漠插件网站，那就可以肯定是被防火墙拦截)',
                      '-2': '进程没有以管理员方式运行. (出现在win7 win8 vista 2008.建议关闭uac)', '0': '失败 (未知错误)', '1': '成功', '2': '余额不足',
                      '3': '绑定了本机器，但是账户余额不足50元.', '4': '注册码错误', '5': '你的机器或者IP在黑名单列表中或者不在白名单列表中.', '6': '非法使用插件. ',
                      '7': '你的帐号因为非法使用被封禁. （如果是在虚拟机中使用插件，必须使用Reg或者RegEx，不能使用RegNoMac或者RegExNoMac,否则可能会造成封号，或者封禁机器）',
                      '8': 'ver_info不在你设置的附加白名单中.', '-8': '版本附加信息长度超过了20', '-9': '版本附加信息里包含了非法字母.'}

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
            if str(dm_ret) in error_code.keys():
                self.LogPrint("收费注册失败,返回值:{},错误信息:{}".format(dm_ret, error_code[str(dm_ret)]))
            else:
                self.LogPrint("错误码:{},未找到对应错误信息".format(dm_ret))

        return

    def SetPath(self, path):
        self.dm.SetPath(path)
        return

    def GetLastError(self):
        error_info = str(self.dm.GetLastError())
        error_info_code = {'-1': ' 表示你使用了绑定里的收费功能，但是没注册，无法使用.',
                           '-2 ': ' 使用模式0 2 时出现，因为目标窗口有保护. 常见于win7以上系统.或者有安全软件拦截插件.解决办法',
                           '-3': ' 使用模式0 2 时出现，可能目标窗口有保护，也可能是异常错误. 可以尝试换绑定模式或许可以解决.', '-4 ': ' 使用模式101 103时出现，这是异常错误.',
                           '-5': ' 使用模式101 103时出现, 这个错误的解决办法就是关闭目标窗口，重新打开再绑定即可. 也可能是运行脚本的进程没有管理员权限. ',
                           '-6': ' 被安全软件拦截。典型的是金山.360等. 如果是360关闭即可。 如果是金山，必须卸载，关闭是没用的.',
                           '-7': ' 使用模式101 103时出现,异常错误. 还有可能是安全软件的问题，比如360等。尝试卸载360.',
                           '-9': ' 使用模式101 103时出现,异常错误. 还有可能是安全软件的问题，比如360等。尝试卸载360.',
                           '-8': ' 使用模式101 103时出现, 目标进程可能有保护,也可能是插件版本过老，试试新的或许可以解决. -8可以尝试使用DmGuard中的np2盾配合.',
                           '-10': ' 使用模式101 103时出现, 目标进程可能有保护,也可能是插件版本过老，试试新的或许可以解决. -8可以尝试使用DmGuard中的np2盾配合.',
                           '-11': ' 使用模式101 103时出现, 目标进程有保护. 告诉我解决。', '-12 ': ' 使用模式101 103时出现, 目标进程有保护. 告诉我解决。',
                           '-13': ' 使用模式101 103时出现, 目标进程有保护. 或者是因为上次的绑定没有解绑导致。 尝试在绑定前调用ForceUnBindWindow. ',
                           '-37': ' 使用模式101 103时出现, 目标进程有保护. 告诉我解决。',
                           '-14': ' 可能系统缺少部分DLL,尝试安装d3d. 或者是鼠标或者键盘使用了dx.mouse.api或者dx.keypad.api，但实际系统没有插鼠标和键盘. 也有可能是图色中有dx.graphic.3d之类的,但相应的图色被占用,比如全屏D3D程序.',
                           '-16': ' 可能使用了绑定模式 0 和 101，然后可能指定了一个子窗口.导致不支持.可以换模式2或者103来尝试. 另外也可以考虑使用父窗口或者顶级窗口.来避免这个错误。还有可能是目标窗口没有正常解绑然后再次绑定的时候.',
                           '-17': ' 模式101 103时出现. 这个是异常错误. 告诉我解决.', '-18 ': ' 句柄无效.',
                           '-19 ': ' 使用模式0 11 101时出现,这是异常错误,告诉我解决.',
                           '-20': ' 使用模式101 103 时出现,说明目标进程里没有解绑，并且子绑定达到了最大. 尝试在返回这个错误时，调用ForceUnBindWindow来强制解除绑定.',
                           '-21': ' 使用模式101 103 时出现,说明目标进程里没有解绑. 尝试在返回这个错误时，调用ForceUnBindWindow来强制解除绑定.',
                           '-22': ' 使用模式0 2,绑定64位进程窗口时出现,因为安全软件拦截插件释放的EXE文件导致.',
                           '-23': ' 使用模式0 2,绑定64位进程窗口时出现,因为安全软件拦截插件释放的DLL文件导致.',
                           '-24': ' 使用模式0 2,绑定64位进程窗口时出现,因为安全软件拦截插件运行释放的EXE.',
                           '-25 ': ' 使用模式0 2,绑定64位进程窗口时出现,因为安全软件拦截插件运行释放的EXE.',
                           '-26': ' 使用模式0 2,绑定64位进程窗口时出现, 因为目标窗口有保护. 常见于win7以上系统.或者有安全软件拦截插件.解决办法',
                           '-27': ' 绑定64位进程窗口时出现，因为使用了不支持的模式，目前暂时只支持模式0 2 11 13 101 103',
                           '-28': ' 绑定32位进程窗口时出现，因为使用了不支持的模式，目前暂时只支持模式0 2 11 13 101 103',
                           '-100 ': ' 调用读写内存函数后，发现无效的窗口句柄',
                           '-101': ' 读写内存函数失败', '-200 ': ' AsmCall失败'}
        if error_info in error_info_code.keys():
            self.LogPrint("错误码:{}|{}".format(error_info, error_info_code[error_info]))
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
            self.RandomDelay(10, 20)
            self.dm.LeftUp()
            self.RandomDelay(10, 20)
        self.dm.LeftDown()
        self.RandomDelay(10, 20)
        self.dm.LeftUp()
        self.RandomDelay(10, 20)
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

    def FindPic(self, x1, y1, x2, y2, pic_name, delta_color, sim=0.9, dir=0, click=True, find_time=1):
        start_time = time.time()
        count_num = 0
        while True:
            pic_index = self.dm.FindPic(x1, y1, x2, y2, pic_name, delta_color, sim, dir)
            count_num += 1
            if pic_index[0] != -1:
                self.LogPrint(
                    "找图成功,第{}次, {}坐标:{},{}, 找图范围:{},{},{},{}".format(count_num, pic_name, pic_name[1], pic_name[2], x1,
                                                                     y1, x2, y2))
                if click:
                    self.MoToClick(pic_index[1], pic_index[2])
                break
            if time.time() - start_time >= find_time:
                self.LogPrint("找图失败:{}, 共计:{}次, 找图范围:{},{},{},{}".format(pic_name, count_num, x1, y1, x2, y2))
                break
            self.RandomDelay(95, 96)
        return pic_index

    def FindMultiColor(self, x1, y1, x2, y2, first_color, offset_color, sim=0.9, dir=0, click=True, find_time=1):
        start_time = time.time()
        count_num = 0
        while True:
            colour_index = self.dm.FindMultiColor(x1, y1, x2, y2, first_color, offset_color, sim, dir)
            count_num += 1
            if colour_index[0]:
                self.LogPrint(
                    "多点找色成功,第{}次, {}坐标:{},{} 找色范围:{},{},{},{}".format(count_num, first_color, colour_index[1],
                                                                      colour_index[2], x1, y1, x2, y2))
                if click:
                    self.MoToClick(colour_index[1], colour_index[2])
                break
            else:
                if time.time() - start_time >= find_time:
                    self.LogPrint("多点找色失败:{}, 共计:{}次 找色范围:{},{},{},{}".format(first_color, count_num, x1, y1, x2, y2))
                    break
                self.RandomDelay(50, 51)
        return colour_index

    # 未测试
    def FindStr(self, x1, y1, x2, y2, string, color_format, sim=0.9, click=True, font_dict=0, find_time=1):
        self.UseDict(font_dict)
        start_time = time.time()
        count_num = 0
        while True:
            font_index = self.dm.FindStr(x1, y1, x2, y2, string, color_format, sim)
            count_num += 1
            if font_index[0] != -1:
                self.LogPrint(
                    "找字成功,第{}次, {}坐标:{},{} 找字范围:{},{},{},{}".format(count_num, string, font_index[1], font_index[2], x1,
                                                                    y1, x2, y2))
                if click:
                    self.MoToClick(font_index[1], font_index[2])
                break
            else:
                if time.time() - start_time >= find_time:
                    self.LogPrint("找字失败:{},共计:{}次 找字范围:{},{},{},{}".format(string, count_num, x1, y1, x2, y2))
                    break
                self.RandomDelay(50, 51)
        return

    def Ocr(self, x1, y1, x2, y2, color_format, sim=0.9, font_dict=0, find_time=1):
        self.UseDict(font_dict)
        start_time = time.time()
        count_num = 0
        while True:
            font = self.dm.Ocr(x1, y1, x2, y2, color_format, sim)
            count_num += 1
            if font:
                self.LogPrint("识别到字:{},第{}次识别到".format(font, count_num))
                break
            else:
                if time.time() - start_time >= find_time:
                    self.LogPrint("未识别到任何字,共计:{}次".format(count_num))
                    break
                self.RandomDelay(50, 51)
        return


if __name__ == '__main__':
    dm = DM(log_print=True, wirte_log=True)