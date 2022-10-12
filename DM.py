import os
import ctypes
import win32com.client
from comtypes.client import CreateObject


class DM(object):
    def __init__(self):
        self.dm = None

    def Ver(self):
        return self.dm.Ver()

    def Reg(self, reg_code, ver_info):
        self.dm = win32com.client.Dispatch('dm.dmsoft')
        return self.dm.Reg(reg_code, ver_info)

    def FreeReg(self, dm_path, reg_code, ver_info):
        dmreg = os.path.join(dm_path, 'DmReg.dll')
        location_dmreg = os.path.join(dm_path, 'dm.dll')
        dms = ctypes.windll.LoadLibrary(dmreg)
        dms.SetDllPathW(location_dmreg, 0)
        self.dm = CreateObject('dm.dmsoft')
        return self.dm.Reg(reg_code, ver_info)

    def CrackReg(self, dm_path):
        dmreg = os.path.join(dm_path, 'DmReg.dll')
        location_dmreg = os.path.join(dm_path, 'dm.dll')
        dms = ctypes.windll.LoadLibrary(dmreg)
        dms.SetDllPathW(location_dmreg, 0)
        self.dm = CreateObject('dm.dmsoft')
        return self.dm

    def SetDict(self, index, file):
        return self.dm.SetDict(index, file)

    def UseDict(self, index):
        return self.dm.UseDict(index)

    def SetPath(self, path):
        return self.dm.SetPath(path)

    def ClientToScreen(self, hwnd, x, y):
        return self.dm.ClientToScreen(hwnd, x, y)

    def EnumProcess(self, name):
        return self.dm.EnumProcess(name)

    def EnumWindow(self, parent, title, class_name, filter):
        return self.dm.EnumWindow(parent, title, class_name, filter)

    def EnumWindowByProcess(self, process_name, title, class_name, filter):
        return self.dm.EnumWindowByProcess(process_name, title, class_name, filter)

    def EnumWindowByProcessId(self, pid, title, class_name, filter):
        return self.dm.EnumWindowByProcessId(pid, title, class_name, filter)

    def EnumWindowSuper(self, spec1, flag1, type1, spec2, flag2, type2, sort):
        return self.dm.EnumWindowSuper(spec1, flag1, type1, spec2, flag2, type2, sort)

    def FindWindow(self, class_name, title):
        return self.dm.FindWindow(class_name, title)

    def FindWindowByProcess(self, process_name, class_name, title):
        return self.dm.FindWindowByProcess(process_name, class_name, title)

    def FindWindowByProcessId(self, process_id, class_name, title):
        return self.dm.FindWindowByProcessId(process_id, class_name, title)

    def FindWindowEx(self, parent, class_name, title):
        return self.dm.FindWindowEx(parent, class_name, title)

    def FindWindowSuper(self, spec1, flag1, type1, spec2, flag2, type2):
        return self.dm.FindWindowSuper(spec1, flag1, type1, spec2, flag2, type2)

    def GetClientRect(self, hwnd, x1, y1, x2, y2):
        return self.dm.GetClientRect(hwnd, x1, y1, x2, y2)

    def GetClientSize(self, hwnd, width, height):
        return self.dm.GetClientSize(hwnd, width, height)

    def GetForegroundFocus(self):
        return self.dm.GetForegroundFocus()

    def GetForegroundWindow(self):
        return self.dm.GetForegroundWindow()

    def GetMousePointWindow(self):
        return self.dm.GetMousePointWindow()

    def GetPointWindow(self, x, y):
        return self.dm.GetPointWindow(x, y)

    def GetProcessInfo(self, pid):
        return self.dm.GetProcessInfo(pid)

    def GetSpecialWindow(self, flag):
        return self.dm.GetSpecialWindow(flag)

    def GetWindow(self, hwnd, flag):
        return self.dm.GetWindow(hwnd, flag)

    def GetWindowClass(self, hwnd):
        return self.dm.GetWindowClass(hwnd)

    def GetWindowProcessId(self, hwnd):
        return self.dm.GetWindowProcessId(hwnd)

    def GetWindowProcessPath(self, hwnd):
        return self.dm.GetWindowProcessPath(hwnd)

    def GetWindowRect(self, hwnd, x1, y1, x2, y2):
        return self.dm.GetWindowRect(hwnd, x1, y1, x2, y2)

    def GetWindowState(self, hwnd, flag):
        return self.dm.GetWindowState(hwnd, flag)

    def GetWindowThreadId(self, hwnd):
        return self.dm.GetWindowThreadId(hwnd)

    def GetWindowTitle(self, hwnd):
        return self.dm.GetWindowTitle(hwnd)

    def MoveWindow(self, hwnd, x, y):
        return self.dm.MoveWindow(hwnd, x, y)

    def ScreenToClient(self, hwnd, x, y):
        return self.dm.ScreenToClient(hwnd, x, y)

    def SendPaste(self, hwnd):
        return self.dm.SendPaste(hwnd)

    def SendString(self, hwnd, str):
        return self.dm.SendString(hwnd, str)

    def SendString2(self, hwnd, str):
        return self.dm.SendString2(hwnd, str)

    def SendStringIme(self, str):
        return self.dm.SendStringIme(str)

    def SendStringIme2(self, hwnd, str, mode):
        return self.dm.SendStringIme2(hwnd, str, mode)

    def SetClientSize(self, hwnd, width, height):
        return self.dm.SetClientSize(hwnd, width, height)

    def SetWindowSize(self, hwnd, width, height):
        return self.dm.SetWindowSize(hwnd, width, height)

    def SetWindowState(self, hwnd, flag):
        return self.dm.SetWindowState(hwnd, flag)

    def SetWindowText(self, hwnd, title):
        return self.dm.SetWindowText(hwnd, title)

    def SetWindowTransparent(self, hwnd, trans):
        return self.dm.SetWindowTransparent(hwnd, trans)

    def BindWindow(self, hwnd, display, mouse, keypad, mode):
        return self.dm.BindWindow(hwnd, display, mouse, keypad, mode)

    def BindWindowEx(self, hwnd, display, mouse, keypad, public, mode):
        return self.dm.BindWindowEx(hwnd, display, mouse, keypad, public, mode)

    def DownCpu(self, type, rate):
        return self.dm.DownCpu(type, rate)

    def EnableBind(self, enable):
        return self.dm.EnableBind(enable)

    def EnableFakeActive(self, enable):
        return self.dm.EnableFakeActive(enable)

    def EnableIme(self, enable):
        return self.dm.EnableIme(enable)

    def EnableKeypadMsg(self, enable):
        return self.dm.EnableKeypadMsg(enable)

    def EnableKeypadPatch(self, enable):
        return self.dm.EnableKeypadPatch(enable)

    def EnableKeypadSync(self, enable, time_out):
        return self.dm.EnableKeypadSync(enable, time_out)

    def EnableMouseMsg(self, enable):
        return self.dm.EnableMouseMsg(enable)

    def EnableMouseSync(self, enable, time_out):
        return self.dm.EnableMouseSync(enable, time_out)

    def EnableRealKeypad(self, enable):
        return self.dm.EnableRealKeypad(enable)

    def EnableRealMouse(self, enable, mousedelay, mousestep):
        return self.dm.EnableRealMouse(enable, mousedelay, mousestep)

    def EnableSpeedDx(self, enable):
        return self.dm.EnableSpeedDx(enable)

    def ForceUnBindWindow(self, hwnd):
        return self.dm.ForceUnBindWindow(hwnd)

    def GetBindWindow(self):
        return self.dm.GetBindWindow()

    def GetFps(self):
        return self.dm.GetFps()

    def HackSpeed(self, rate):
        return self.dm.HackSpeed(rate)

    def IsBind(self, hwnd):
        return self.dm.IsBind(hwnd)

    def LockDisplay(self, lock):
        return self.dm.LockDisplay(lock)

    def LockInput(self, lock):
        return self.dm.LockInput(lock)

    def LockMouseRect(self, x1, y1, x2, y2):
        return self.dm.LockMouseRect(x1, y1, x2, y2)

    def SetAero(self, enable):
        return self.dm.SetAero(enable)

    def SetDisplayDelay(self, time):
        return self.dm.SetDisplayDelay(time)

    def SetDisplayRefreshDelay(self, time):
        return self.dm.SetDisplayRefreshDelay(time)

    def SetInputDm(self, dm_id, rx, ry):
        return self.dm.SetInputDm(dm_id, rx, ry)

    def SwitchBindWindow(self, hwnd):
        return self.dm.SwitchBindWindow(hwnd)

    def UnBindWindow(self):
        return self.dm.UnBindWindow()

    def EnableMouseAccuracy(self, enable):
        return self.dm.EnableMouseAccuracy(enable)

    def GetCursorPos(self, x, y):
        return self.dm.GetCursorPos(x, y)

    def GetCursorShape(self):
        return self.dm.GetCursorShape()

    def GetCursorShapeEx(self, int_, type_):
        return self.dm.GetCursorShapeEx(int_, type_)

    def GetCursorSpot(self):
        return self.dm.GetCursorSpot()

    def GetKeyState(self, vk_code):
        return self.dm.GetKeyState(vk_code)

    def GetMouseSpeed(self):
        return self.dm.GetMouseSpeed()

    def KeyDown(self, vk_code):
        return self.dm.KeyDown(vk_code)

    def KeyDownChar(self, key_str):
        return self.dm.KeyDownChar(key_str)

    def KeyPress(self, vk_code):
        return self.dm.KeyPress(vk_code)

    def KeyPressChar(self, key_str):
        return self.dm.KeyPressChar(key_str)

    def KeyPressStr(self, key_str, delay):
        return self.dm.KeyPressStr(key_str, delay)

    def KeyUp(self, vk_code):
        return self.dm.KeyUp(vk_code)

    def KeyUpChar(self, key_str):
        return self.dm.KeyUpChar(key_str)

    def LeftClick(self):
        return self.dm.LeftClick()

    def LeftDoubleClick(self):
        return self.dm.LeftDoubleClick()

    def LeftDown(self):
        return self.dm.LeftDown()

    def LeftUp(self):
        return self.dm.LeftUp()

    def MiddleClick(self):
        return self.dm.MiddleClick()

    def MiddleDown(self):
        return self.dm.MiddleDown()

    def MiddleUp(self):
        return self.dm.MiddleUp()

    def MoveR(self, rx, ry):
        return self.dm.MoveR(rx, ry)

    def MoveTo(self, x, y):
        return self.dm.MoveTo(x, y)

    def MoveToEx(self, x, y, w, h):
        return self.dm.MoveToEx(x, y, w, h)

    def RightClick(self):
        return self.dm.RightClick()

    def RightDown(self):
        return self.dm.RightDown()

    def RightUp(self):
        return self.dm.RightUp()

    def SetKeypadDelay(self, type, delay):
        return self.dm.SetKeypadDelay(type, delay)

    def SetMouseDelay(self, type, delay):
        return self.dm.SetMouseDelay(type, delay)

    def SetMouseSpeed(self, speed):
        return self.dm.SetMouseSpeed(speed)

    def SetSimMode(self, mode):
        return self.dm.SetSimMode(mode)

    def WaitKey(self, vk_code, time_out):
        return self.dm.WaitKey(vk_code, time_out)

    def WheelDown(self):
        return self.dm.WheelDown()

    def WheelUp(self):
        return self.dm.WheelUp()

    def AppendPicAddr(self, pic_info, addr, size):
        return self.dm.AppendPicAddr(pic_info, addr, size)

    def BGR2RGB(self, bgr_color):
        return self.dm.BGR2RGB(bgr_color)

    def Capture(self, x1, y1, x2, y2, file):
        return self.dm.Capture(x1, y1, x2, y2, file)

    def CaptureGif(self, x1, y1, x2, y2, file, delay, time):
        return self.dm.CaptureGif(x1, y1, x2, y2, file, delay, time)

    def CaptureJpg(self, x1, y1, x2, y2, file, quality):
        return self.dm.CaptureJpg(x1, y1, x2, y2, file, quality)

    def CapturePng(self, x1, y1, x2, y2, file):
        return self.dm.CapturePng(x1, y1, x2, y2, file)

    def CmpColor(self, x, y, color, sim):
        return self.dm.CmpColor(x, y, color, sim)

    def EnableDisplayDebug(self, enable_debug):
        return self.dm.EnableDisplayDebug(enable_debug)

    def EnableFindPicMultithread(self, enable):
        return self.dm.EnableFindPicMultithread(enable)

    def EnableGetColorByCapture(self, enable):
        return self.dm.EnableGetColorByCapture(enable)

    def FindColor(self, x1, y1, x2, y2, color, sim, dir):
        return self.dm.FindColor(x1, y1, x2, y2, color, sim, dir)

    def FindColorBlock(self, x1, y1, x2, y2, color, sim, count, width, height):
        return self.dm.FindColorBlock(x1, y1, x2, y2, color, sim, count, width, height)

    def FindColorBlockEx(self, x1, y1, x2, y2, color, sim, count, width, height):
        return self.dm.FindColorBlockEx(x1, y1, x2, y2, color, sim, count, width, height)

    def FindColorE(self, x1, y1, x2, y2, color, sim, dir):
        return self.dm.FindColorE(x1, y1, x2, y2, color, sim, dir)

    def FindColorEx(self, x1, y1, x2, y2, color, sim, dir):
        return self.dm.FindColorEx(x1, y1, x2, y2, color, sim, dir)

    def FindMulColor(self, x1, y1, x2, y2, color, sim):
        return self.dm.FindMulColor(x1, y1, x2, y2, color, sim)

    def FindMultiColor(self, x1, y1, x2, y2, first_color, offset_color, sim, dir):
        return self.dm.FindMultiColor(x1, y1, x2, y2, first_color, offset_color, sim, dir)

    def FindMultiColorE(self, x1, y1, x2, y2, first_color, offset_color, sim, dir):
        return self.dm.FindMultiColorE(x1, y1, x2, y2, first_color, offset_color, sim, dir)

    def FindMultiColorEx(self, x1, y1, x2, y2, first_color, offset_color, sim, dir):
        return self.dm.FindMultiColorEx(x1, y1, x2, y2, first_color, offset_color, sim, dir)

    def FindPic(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir):
        return self.dm.FindPic(x1, y1, x2, y2, pic_name, delta_color, sim, dir)

    def FindPicE(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir):
        return self.dm.FindPicE(x1, y1, x2, y2, pic_name, delta_color, sim, dir)

    def FindPicEx(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir):
        return self.dm.FindPicEx(x1, y1, x2, y2, pic_name, delta_color, sim, dir)

    def FindPicExS(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir):
        return self.dm.FindPicExS(x1, y1, x2, y2, pic_name, delta_color, sim, dir)

    def FindPicMem(self, x1, y1, x2, y2, pic_info, delta_color, sim, dir):
        return self.dm.FindPicMem(x1, y1, x2, y2, pic_info, delta_color, sim, dir)

    def FindPicMemE(self, x1, y1, x2, y2, pic_info, delta_color, sim, dir):
        return self.dm.FindPicMemE(x1, y1, x2, y2, pic_info, delta_color, sim, dir)

    def FindPicMemEx(self, x1, y1, x2, y2, pic_info, delta_color, sim, dir):
        return self.dm.FindPicMemEx(x1, y1, x2, y2, pic_info, delta_color, sim, dir)

    def FindPicS(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir):
        return self.dm.FindPicS(x1, y1, x2, y2, pic_name, delta_color, sim, dir)

    def FindPicSim(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir):
        return self.dm.FindPicSim(x1, y1, x2, y2, pic_name, delta_color, sim, dir)

    def FindPicSimE(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir):
        return self.dm.FindPicSimE(x1, y1, x2, y2, pic_name, delta_color, sim, dir)

    def FindPicSimEx(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir):
        return self.dm.FindPicSimEx(x1, y1, x2, y2, pic_name, delta_color, sim, dir)

    def FindPicSimMem(self, x1, y1, x2, y2, pic_info, delta_color, sim, dir):
        return self.dm.FindPicSimMem(x1, y1, x2, y2, pic_info, delta_color, sim, dir)

    def FindPicSimMemE(self, x1, y1, x2, y2, pic_info, delta_color, sim, dir):
        return self.dm.FindPicSimMemE(x1, y1, x2, y2, pic_info, delta_color, sim, dir)

    def FindPicSimMemEx(self, x1, y1, x2, y2, pic_info, delta_color, sim, dir):
        return self.dm.FindPicSimMemEx(x1, y1, x2, y2, pic_info, delta_color, sim, dir)

    def FindShape(self, x1, y1, x2, y2, offset_color, sim, dir):
        return self.dm.FindShape(x1, y1, x2, y2, offset_color, sim, dir)

    def FindShapeE(self, x1, y1, x2, y2, offset_color, sim, dir):
        return self.dm.FindShapeE(x1, y1, x2, y2, offset_color, sim, dir)

    def FindShapeEx(self, x1, y1, x2, y2, offset_color, sim, dir):
        return self.dm.FindShapeEx(x1, y1, x2, y2, offset_color, sim, dir)

    def FreePic(self, pic_name):
        return self.dm.FreePic(pic_name)

    def GetAveHSV(self, x1, y1, x2, y2):
        return self.dm.GetAveHSV(x1, y1, x2, y2)

    def GetAveRGB(self, x1, y1, x2, y2):
        return self.dm.GetAveRGB(x1, y1, x2, y2)

    def GetColor(self, x, y):
        return self.dm.GetColor(x, y)

    def GetColorBGR(self, x, y):
        return self.dm.GetColorBGR(x, y)

    def GetColorHSV(self, x, y):
        return self.dm.GetColorHSV(x, y)

    def GetColorNum(self, x1, y1, x2, y2, color, sim):
        return self.dm.GetColorNum(x1, y1, x2, y2, color, sim)

    def GetPicSize(self, pic_name):
        return self.dm.GetPicSize(pic_name)

    def GetScreenData(self, x1, y1, x2, y2):
        return self.dm.GetScreenData(x1, y1, x2, y2)

    def GetScreenDataBmp(self, x1, y1, x2, y2, data, size):
        return self.dm.GetScreenDataBmp(x1, y1, x2, y2, data, size)

    def ImageToBmp(self, pic_name, bmp_name):
        return self.dm.ImageToBmp(pic_name, bmp_name)

    def IsDisplayDead(self, x1, y1, x2, y2, t):
        return self.dm.IsDisplayDead(x1, y1, x2, y2, t)

    def LoadPic(self, pic_name):
        return self.dm.LoadPic(pic_name)

    def LoadPicByte(self, addr, size, pic_name):
        return self.dm.LoadPicByte(addr, size, pic_name)

    def MatchPicName(self, pic_name):
        return self.dm.MatchPicName(pic_name)

    def RGB2BGR(self, rgb_color):
        return self.dm.RGB2BGR(rgb_color)

    def SetExcludeRegion(self, mode, info):
        return self.dm.SetExcludeRegion(mode, info)

    def SetFindPicMultithreadCount(self, count):
        return self.dm.SetFindPicMultithreadCount(count)

    def SetPicPwd(self, pwd):
        return self.dm.SetPicPwd(pwd)

    def AddDict(self, index, dict_info):
        return self.dm.AddDict(index, dict_info)

    def ClearDict(self, index):
        return self.dm.ClearDict(index)

    def EnableShareDict(self, enable):
        return self.dm.EnableShareDict(enable)

    def FetchWord(self, x1, y1, x2, y2, color, word):
        return self.dm.FetchWord(x1, y1, x2, y2, color, word)

    def FindStr(self, x1, y1, x2, y2, string, color_format, sim):
        return self.dm.FindStr(x1, y1, x2, y2, string, color_format, sim)

    def FindStrE(self, x1, y1, x2, y2, string, color_format, sim):
        return self.dm.FindStrE(x1, y1, x2, y2, string, color_format, sim)

    def FindStrEx(self, x1, y1, x2, y2, string, color_format, sim):
        return self.dm.FindStrEx(x1, y1, x2, y2, string, color_format, sim)

    def FindStrExS(self, x1, y1, x2, y2, string, color_format, sim):
        return self.dm.FindStrExS(x1, y1, x2, y2, string, color_format, sim)

    def FindStrFast(self, x1, y1, x2, y2, string, color_format, sim):
        return self.dm.FindStrFast(x1, y1, x2, y2, string, color_format, sim)

    def FindStrFastE(self, x1, y1, x2, y2, string, color_format, sim):
        return self.dm.FindStrFastE(x1, y1, x2, y2, string, color_format, sim)

    def FindStrFastEx(self, x1, y1, x2, y2, string, color_format, sim):
        return self.dm.FindStrFastEx(x1, y1, x2, y2, string, color_format, sim)

    def FindStrFastExS(self, x1, y1, x2, y2, string, color_format, sim):
        return self.dm.FindStrFastExS(x1, y1, x2, y2, string, color_format, sim)

    def FindStrFastS(self, x1, y1, x2, y2, string, color_format, sim):
        return self.dm.FindStrFastS(x1, y1, x2, y2, string, color_format, sim)

    def FindStrS(self, x1, y1, x2, y2, string, color_format, sim):
        return self.dm.FindStrS(x1, y1, x2, y2, string, color_format, sim)

    def FindStrWithFont(self, x1, y1, x2, y2, string, color_format, sim, font_name, font_size, flag):
        return self.dm.FindStrWithFont(x1, y1, x2, y2, string, color_format, sim, font_name, font_size, flag)

    def FindStrWithFontE(self, x1, y1, x2, y2, string, color_format, sim, font_name, font_size, flag):
        return self.dm.FindStrWithFontE(x1, y1, x2, y2, string, color_format, sim, font_name, font_size, flag)

    def FindStrWithFontEx(self, x1, y1, x2, y2, string, color_format, sim, font_name, font_size, flag):
        return self.dm.FindStrWithFontEx(x1, y1, x2, y2, string, color_format, sim, font_name, font_size, flag)

    def GetDict(self, index, font_index):
        return self.dm.GetDict(index, font_index)

    def GetDictCount(self, index):
        return self.dm.GetDictCount(index)

    def GetDictInfo(self, str, font_name, font_size, flag):
        return self.dm.GetDictInfo(str, font_name, font_size, flag)

    def GetNowDict(self):
        return self.dm.GetNowDict()

    def GetResultCount(self, ret):
        return self.dm.GetResultCount(ret)

    def GetResultPos(self, ret, index):
        return self.dm.GetResultPos(ret, index)

    def GetWordResultCount(self, str):
        return self.dm.GetWordResultCount(str)

    def GetWordResultPos(self, str, index):
        return self.dm.GetWordResultPos(str, index)

    def GetWordResultStr(self, str, index):
        return self.dm.GetWordResultStr(str, index)

    def GetWords(self, x1, y1, x2, y2, color, sim):
        return self.dm.GetWords(x1, y1, x2, y2, color, sim)

    def GetWordsNoDict(self, x1, y1, x2, y2, color):
        return self.dm.GetWordsNoDict(x1, y1, x2, y2, color)

    def Ocr(self, x1, y1, x2, y2, color_format, sim):
        return self.dm.Ocr(x1, y1, x2, y2, color_format, sim)

    def OcrEx(self, x1, y1, x2, y2, color_format, sim):
        return self.dm.OcrEx(x1, y1, x2, y2, color_format, sim)

    def OcrExOne(self, x1, y1, x2, y2, color_format, sim):
        return self.dm.OcrExOne(x1, y1, x2, y2, color_format, sim)

    def OcrInFile(self, x1, y1, x2, y2, pic_name, color_format, sim):
        return self.dm.OcrInFile(x1, y1, x2, y2, pic_name, color_format, sim)

    def SaveDict(self, index, file):
        return self.dm.SaveDict(index, file)

    def SetColGapNoDict(self, col_gap):
        return self.dm.SetColGapNoDict(col_gap)

    def SetDictMem(self, index, addr, size):
        return self.dm.SetDictMem(index, addr, size)

    def SetDictPwd(self, pwd):
        return self.dm.SetDictPwd(pwd)

    def SetExactOcr(self, exact_ocr):
        return self.dm.SetExactOcr(exact_ocr)

    def SetMinColGap(self, min_col_gap):
        return self.dm.SetMinColGap(min_col_gap)

    def SetMinRowGap(self, min_row_gap):
        return self.dm.SetMinRowGap(min_row_gap)

    def SetRowGapNoDict(self, row_gap):
        return self.dm.SetRowGapNoDict(row_gap)

    def SetWordGap(self, word_gap):
        return self.dm.SetWordGap(word_gap)

    def SetWordGapNoDict(self, word_gap):
        return self.dm.SetWordGapNoDict(word_gap)

    def SetWordLineHeight(self, line_height):
        return self.dm.SetWordLineHeight(line_height)

    def SetWordLineHeightNoDict(self, line_height):
        return self.dm.SetWordLineHeightNoDict(line_height)

    def DmGuard(self, enable, type):
        return self.dm.DmGuard(enable, type)

    def DmGuardExtract(self, type, path):
        return self.dm.DmGuardExtract(type, path)

    def DmGuardLoadCustom(self, type, path):
        return self.dm.DmGuardLoadCustom(type, path)

    def DmGuardParams(self, cmd, subcmd, param):
        return self.dm.DmGuardParams(cmd, subcmd, param)

    def UnLoadDriver(self):
        return self.dm.UnLoadDriver()

    def AsmAdd(self, asm_ins):
        return self.dm.AsmAdd(asm_ins)

    def AsmCall(self, hwnd, mode):
        return self.dm.AsmCall(hwnd, mode)

    def AsmCallEx(self, hwnd, mode, base_addr):
        return self.dm.AsmCallEx(hwnd, mode, base_addr)

    def AsmClear(self):
        return self.dm.AsmClear()

    def AsmSetTimeout(self, time_out, param):
        return self.dm.AsmSetTimeout(time_out, param)

    def Assemble(self, base_addr, is_64bit):
        return self.dm.Assemble(base_addr, is_64bit)

    def DisAssemble(self, asm_code, base_addr, is_64bit):
        return self.dm.DisAssemble(asm_code, base_addr, is_64bit)

    def SetShowAsmErrorMsg(self, show):
        return self.dm.SetShowAsmErrorMsg(show)

    def FaqCancel(self):
        return self.dm.FaqCancel()

    def FaqCapture(self, x1, y1, x2, y2, quality, delay, time):
        return self.dm.FaqCapture(x1, y1, x2, y2, quality, delay, time)

    def FaqCaptureFromFile(self, x1, y1, x2, y2, file, quality):
        return self.dm.FaqCaptureFromFile(x1, y1, x2, y2, file, quality)

    def FaqCaptureString(self, str):
        return self.dm.FaqCaptureString(str)

    def FaqFetch(self):
        return self.dm.FaqFetch()

    def FaqGetSize(self, handle):
        return self.dm.FaqGetSize(handle)

    def FaqIsPosted(self):
        return self.dm.FaqIsPosted()

    def FaqPost(self, server, handle, request_type, time_out):
        return self.dm.FaqPost(server, handle, request_type, time_out)

    def FaqSend(self, server, handle, request_type, time_out):
        return self.dm.FaqSend(server, handle, request_type, time_out)

    def EnablePicCache(self, enable):
        return self.dm.EnablePicCache(enable)

    def GetBasePath(self):
        return self.dm.GetBasePath()

    def GetDmCount(self):
        return self.dm.GetDmCount()

    def GetID(self):
        return self.dm.GetID()

    def GetLastError(self):
        return self.dm.GetLastError()

    def GetPath(self):
        return self.dm.GetPath()

    def RegEx(self, reg_code, ver_info, ip):
        return self.dm.RegEx(reg_code, ver_info, ip)

    def RegExNoMac(self, reg_code, ver_info, ip):
        return self.dm.RegExNoMac(reg_code, ver_info, ip)

    def RegNoMac(self, reg_code, ver_info):
        return self.dm.RegNoMac(reg_code, ver_info)

    def SetDisplayInput(self, mode):
        return self.dm.SetDisplayInput(mode)

    def SetEnumWindowDelay(self, delay):
        return self.dm.SetEnumWindowDelay(delay)

    def SetShowErrorMsg(self, show):
        return self.dm.SetShowErrorMsg(show)

    def SpeedNormalGraphic(self, enable):
        return self.dm.SpeedNormalGraphic(enable)

    def CopyFile(self, src_file, dst_file, over):
        return self.dm.CopyFile(src_file, dst_file, over)

    def CreateFolder(self, folder):
        return self.dm.CreateFolder(folder)

    def DecodeFile(self, file, pwd):
        return self.dm.DecodeFile(file, pwd)

    def DeleteFile(self, file):
        return self.dm.DeleteFile(file)

    def DeleteFolder(self, folder):
        return self.dm.DeleteFolder(folder)

    def DeleteIni(self, section, key, file):
        return self.dm.DeleteIni(section, key, file)

    def DeleteIniPwd(self, section, key, file, pwd):
        return self.dm.DeleteIniPwd(section, key, file, pwd)

    def DownloadFile(self, url, save_file, timeout):
        return self.dm.DownloadFile(url, save_file, timeout)

    def EncodeFile(self, file, pwd):
        return self.dm.EncodeFile(file, pwd)

    def EnumIniKey(self, section, file):
        return self.dm.EnumIniKey(section, file)

    def EnumIniKeyPwd(self, section, file, pwd):
        return self.dm.EnumIniKeyPwd(section, file, pwd)

    def EnumIniSection(self, file):
        return self.dm.EnumIniSection(file)

    def EnumIniSectionPwd(self, file, pwd):
        return self.dm.EnumIniSectionPwd(file, pwd)

    def GetFileLength(self, file):
        return self.dm.GetFileLength(file)

    def GetRealPath(self, path):
        return self.dm.GetRealPath(path)

    def IsFileExist(self, file):
        return self.dm.IsFileExist(file)

    def IsFolderExist(self, folder):
        return self.dm.IsFolderExist(folder)

    def MoveFile(self, src_file, dst_file):
        return self.dm.MoveFile(src_file, dst_file)

    def ReadFile(self, file):
        return self.dm.ReadFile(file)

    def ReadIni(self, section, key, file):
        return self.dm.ReadIni(section, key, file)

    def ReadIniPwd(self, section, key, file, pwd):
        return self.dm.ReadIniPwd(section, key, file, pwd)

    def SelectDirectory(self):
        return self.dm.SelectDirectory()

    def SelectFile(self):
        return self.dm.SelectFile()

    def WriteFile(self, file, content):
        return self.dm.WriteFile(file, content)

    def WriteIni(self, section, key, value, file):
        return self.dm.WriteIni(section, key, value, file)

    def WriteIniPwd(self, section, key, value, file, pwd):
        return self.dm.WriteIniPwd(section, key, value, file, pwd)

    def Beep(self, f, duration):
        return self.dm.Beep(f, duration)

    def CheckFontSmooth(self):
        return self.dm.CheckFontSmooth()

    def CheckUAC(self):
        return self.dm.CheckUAC()

    def Delay(self, mis):
        return self.dm.Delay(mis)

    def Delays(self, mis_min, mis_max):
        return self.dm.Delays(mis_min, mis_max)

    def DisableCloseDisplayAndSleep(self):
        return self.dm.DisableCloseDisplayAndSleep()

    def DisableFontSmooth(self):
        return self.dm.DisableFontSmooth()

    def DisablePowerSave(self):
        return self.dm.DisablePowerSave()

    def DisableScreenSave(self):
        return self.dm.DisableScreenSave()

    def EnableFontSmooth(self):
        return self.dm.EnableFontSmooth()

    def ExitOs(self, type):
        return self.dm.ExitOs(type)

    def GetClipboard(self):
        return self.dm.GetClipboard()

    def GetCpuType(self):
        return self.dm.GetCpuType()

    def GetCpuUsage(self):
        return self.dm.GetCpuUsage()

    def GetDir(self, type):
        return self.dm.GetDir(type)

    def GetDiskModel(self, index):
        return self.dm.GetDiskModel(index)

    def GetDiskReversion(self, index):
        return self.dm.GetDiskReversion(index)

    def GetDiskSerial(self, index):
        return self.dm.GetDiskSerial(index)

    def GetDisplayInfo(self):
        return self.dm.GetDisplayInfo()

    def GetDPI(self):
        return self.dm.GetDPI()

    def GetLocale(self):
        return self.dm.GetLocale()

    def GetMachineCode(self):
        return self.dm.GetMachineCode()

    def GetMachineCodeNoMac(self):
        return self.dm.GetMachineCodeNoMac()

    def GetMemoryUsage(self):
        return self.dm.GetMemoryUsage()

    def GetNetTime(self):
        return self.dm.GetNetTime()

    def GetNetTimeByIp(self, ip):
        return self.dm.GetNetTimeByIp(ip)

    def GetOsBuildNumber(self):
        return self.dm.GetOsBuildNumber()

    def GetOsType(self):
        return self.dm.GetOsType()

    def GetScreenDepth(self):
        return self.dm.GetScreenDepth()

    def GetScreenHeight(self):
        return self.dm.GetScreenHeight()

    def GetScreenWidth(self):
        return self.dm.GetScreenWidth()

    def GetSystemInfo(self, type, method):
        return self.dm.GetSystemInfo(type, method)

    def GetTime(self):
        return self.dm.GetTime()

    def Is64Bit(self):
        return self.dm.Is64Bit()

    def IsSurrpotVt(self):
        return self.dm.IsSurrpotVt()

    def Play(self, media_file):
        return self.dm.Play(media_file)

    def RunApp(self, app_path, mode):
        return self.dm.RunApp(app_path, mode)

    def SetClipboard(self, value):
        return self.dm.SetClipboard(value)

    def SetDisplayAcceler(self, level):
        return self.dm.SetDisplayAcceler(level)

    def SetLocale(self):
        return self.dm.SetLocale()

    def SetScreen(self, width, height, depth):
        return self.dm.SetScreen(width, height, depth)

    def SetUAC(self, enable):
        return self.dm.SetUAC(enable)

    def ShowTaskBarIcon(self, hwnd, is_show):
        return self.dm.ShowTaskBarIcon(hwnd, is_show)

    def Stop(self, id):
        return self.dm.Stop(id)

    def ActiveInputMethod(self, hwnd, input_method):
        return self.dm.ActiveInputMethod(hwnd, input_method)

    def CheckInputMethod(self, hwnd, input_method):
        return self.dm.CheckInputMethod(hwnd, input_method)

    def EnterCri(self):
        return self.dm.EnterCri()

    def ExecuteCmd(self, cmd, current_dir, time_out):
        return self.dm.ExecuteCmd(cmd, current_dir, time_out)

    def FindInputMethod(self, input_method):
        return self.dm.FindInputMethod(input_method)

    def InitCri(self):
        return self.dm.InitCri()

    def LeaveCri(self):
        return self.dm.LeaveCri()

    def ReleaseRef(self):
        return self.dm.ReleaseRef()

    def SetExitThread(self, enable):
        return self.dm.SetExitThread(enable)
