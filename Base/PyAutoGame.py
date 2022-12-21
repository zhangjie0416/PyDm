import time
from Base.DM import BaseDm
from public.Logger import Logger


class PyDm(BaseDm):
    logger = Logger()

    def reg(self, reg_code, ver_info):
        start_time = time.time()
        res = self.Reg(reg_code, ver_info)
        end_time = round(time.time()-start_time,2)
        if res == 1:
            self.logger.success(f"大漠插件注册成功,版本号:{self.Ver()},调用时间:{end_time}s")
        else:
            self.logger.error(f"大漠插件注册失败,注册码:{res}")
        return

    def free_dm(self, reg_code, ver_info):
        res = self.FreeReg(reg_code, ver_info)
        if res == 1:
            self.logger.success(f"大漠插件注册成功,版本号:{self.Ver()}")
        else:
            self.logger.error(f"大漠插件注册失败,注册码:{res}")
        return

    def round_num(self, num):
        return round(num, 3)

    def move_to_click(self, x, y, w=0, h=0, right=False, double=False, delay=100):
        # 移动鼠标点击
        self.logger.success(f"鼠标移动:[{x},{y}] 右键点击:{right} 双击:{double}")
        self.MoveToEx(x, y, w, h)
        if right:
            if double:
                self.RightDown()
                self.Delays(10, 30)
                self.RightUp()
                self.Delays(10, 30)
            self.RightDown()
            self.Delays(10, 30)
            self.RightUp()
        else:
            if double:
                self.LeftDown()
                self.Delays(10, 30)
                self.LeftUp()
                self.Delays(10, 30)
            self.LeftDown()
            self.Delays(10, 30)
            self.LeftUp()
            self.Delays(10, 30)
        self.Delay(delay)
        return

    def enum_window(self, parent, title, class_name, filter=1 + 4 + 8 + 16):
        # 枚举窗口
        hwnds = self.EnumWindow(parent, title, class_name, filter)
        if hwnds:
            hwnds = hwnds.split(',')
            self.logger.success(f"查找到窗口句柄:{hwnds}")
        else:
            hwnds = []
            self.logger.error("未枚举到窗口句柄")
        return hwnds

    def bind_windows_ex(self, hwnd, display, mouse, keypad, public, mode):
        res = self.BindWindowEx(hwnd, display, mouse, keypad, public, mode)
        if res == 1:
            self.logger.success(f"窗口句柄:[{hwnd}]绑定成功")
        else:
            self.logger.error(f"窗口句柄:[{hwnd}]绑定失败")
        return res

    def find_pic(self, args, find_time=1, click=False, right=False, double=False, delay=0):
        if len(args) != 7:
            args.append(0.9)
        start_time, count_num = time.time(), 1
        while True:
            res = self.FindPic(args[1], args[2], args[3], args[4], args[5], "000000", args[6], dir=0)
            if res[0] != -1:
                self.logger.success(
                    f"[图片识别]-- 名称:[{args[0]}],坐标:{res},范围:{args[1:5]}, 查找次数:{count_num},查找时间:{self.round_num(time.time() - start_time)}")
                if click:
                    self.move_to_click(res[1], res[2], right=right, double=double)
                break
            if time.time() - start_time >= find_time:
                self.logger.error(
                    f"[图片识别]-- 名称:[{args[0]}],坐标:{res},范围:{args[1:5]}, 查找次数:{count_num},查找时间:{find_time}")
                break
            self.Delays(10, 20)
            count_num += 1
        self.Delay(delay)
        return res[1:]

    def find_str(self, args, find_time=1, click=False, right=False, double=False, delay=0):
        if len(args) != 8:
            args.append(0.9)
        start_time, count_num = time.time(), 1
        while True:
            res = self.FindStr(args[1], args[2], args[3], args[4], args[5], args[6], args[7])
            if res[0] != -1:
                self.logger.success(
                    f"[文字识别]-- 名称:[{args[0]}],坐标:{res},范围:{args[1:5]}, 查找次数:{count_num},查找时间:{self.round_num(time.time() - start_time)}")
                if click:
                    self.move_to_click(res[1], res[2], right=right, double=double)
                break
            if time.time() - start_time >= find_time:
                self.logger.error(
                    f"[文字识别]-- 名称:[{args[0]}],坐标:{res},范围:{args[1:5]}, 查找次数:{count_num},查找时间:{self.round_num(time.time() - start_time)}")
                break
            self.Delays(10, 20)
            count_num += 1
        self.Delay(delay)
        return res[1:]

    def ocr(self, args, find_time=1, delay=0):
        if len(args) != 7:
            args.append(0.9)
        start_time, count_num = time.time(), 1
        while True:
            res = self.Ocr(args[1], args[2], args[3], args[4], args[5], args[6])
            if res:
                self.logger.success(
                    f"[Ocr]-- 名称:[{args[0]}],文字:{res},范围:{args[1:5]}, 查找次数:{count_num},查找时间:{self.round_num(time.time() - start_time)}")
                break
            if time.time() - start_time >= find_time:
                self.logger.error(
                    f"[文字识别]-- 名称:[{args[0]}],文字:{res},范围:{args[1:5]}, 查找次数:{count_num},查找时间:{find_time}")
                break
            self.Delays(10, 20)
            count_num += 1
        self.Delay(delay)
        return res

    def find_multi_color(self, args, find_time=1, click=False, right=False, double=False, delay=0):
        if len(args) != 8:
            args.append(0.9)
        start_time, count_num = time.time(), 1
        while True:
            res = self.FindMultiColor(args[1], args[2], args[3], args[4], args[5], args[6], args[7], 0)
            if res[0] != 0:
                self.logger.success(
                    f"|多点找色| -- 名称:[{args[0]}],坐标:{res},范围:{args[1:5]}, 查找次数:{count_num},查找时间:{self.round_num(time.time() - start_time)}")
                if click:
                    self.move_to_click(res[1], res[2], right=right, double=double)
                break
            if time.time() - start_time >= find_time:
                self.logger.error(
                    f"|多点找色| -- 名称:[{args[0]}],坐标:{res},范围:{args[1:5]}, 查找次数:{count_num},查找时间:{find_time}")
                break
            self.Delays(10, 20)
            count_num += 1
        self.Delay(delay)
        return res[1:]

    def sliding(self, start_index, stop_index, right=False, start_delay=100, stop_delay=100):
        self.Delay(start_delay)
        self.logger.success(f"|鼠标滑动| - 起始:{start_index},终点:{stop_index}")
        self.MoveTo(start_index[0], start_index[1])
        if right:
            self.RightDown()
        else:
            self.LeftDown()
        self.MoveTo(stop_index[0], stop_index[1])
        if right:
            self.RightUp()
        else:
            self.LeftUp()
        self.Delay(stop_delay)
        return


test = {
    "魔域": ["魔域", 241, 91, 463, 199, "f4c51f", "-15|-20|f4c51f,13|-20|f4c51f"]
}


def main():
    dm = PyDm()

    dm.reg("zj545768869285fc98bd0c1674b1eaf4268359ef244", "")
    # dm.bind_windows_ex(1578570, "gdi", "windows", "windows", "", 0)
    # dm.SetDict(0, "font.txt")
    # hwnds = dm.enum_window(0, "雷电模拟器", "")
    # hwnds2 = dm.enum_window(hwnds[0], "TheRender", "", filter=1 + 4 + 16)
    # dm.bind_windows_ex(hwnds2[0], "gdi", "windows", "windows", "", 0)

    # dm.find_pic(test["测试"], click=True)

    # dm.ocr(test["雷电1"])
    # dm.find_multi_color(test["魔域"])
    # dm.move_to_click(211, 191)


if __name__ == '__main__':
    main()
