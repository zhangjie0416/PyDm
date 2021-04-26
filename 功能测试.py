from main import DM
from Config_test import *

dm = DM(log_print=True, write_log=True)
hwnds = dm.EnumWindowByProcess("dnplayer.exe", "TheRender", "RenderWindow", filter=2 + 16)
dm.BindWindowEx(hwnds[0], "dx.graphic.opengl", "windows", "windows", "", 0)
# dm.FindPic(835,109,990,297, 'test.bmp', "000000",find_time=20)
# dm.FindMultiColor(491,102,624,234,"魔域图标", "d6a64e", "6|-2|dec66c,37|4|cb8027,40|4|e79936",click=True, find_time=20)
dm.SetDict(1, "map_name.txt")
# dm.FindStr(492, 187, 609, 214, "魔域", "ffffff-333333")
dm.OcrPara(ocr_conf["地图名称"])
#dm.FindStrPara(f_str_conf["测试"])
#dm.FindMultiColorPara(f_mucor_conf["测试"])
#dm.FindPicPara(pic["测试"])
dm.Capture(287, 143, 387, 252, "1.bmp")
