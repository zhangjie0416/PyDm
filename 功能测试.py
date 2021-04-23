from PyDm import DM

dm = DM(log_print=True, wirte_log=True)

hwnds = dm.EnumWindowByProcess("dnplayer.exe", "TheRender", "RenderWindow", filter=2 + 16)
dm.BindWindowEx(hwnds[0], "gdi", "windows3", "windows", "", 0)
# dm.FindPic(0,0,1280,720, 'test.bmp', "000000",find_time=20)
dm.FindMultiColor(476, 88, 623, 244, "fffefd", "19|-18|00854a,-19|-15|00854a,27|-11|00854a",click=True, find_time=20)
