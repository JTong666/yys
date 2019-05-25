import win32gui
import sys

import win32con

hwnd_title = dict()
hd =1

def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


win32gui.EnumWindows(get_all_hwnd, 0)

list = [];
q=0
win32gui.EnumWindows(get_all_hwnd, 0)
for h, t in hwnd_title.items():
    if t is not "":
        if t == '阴阳师-网易游戏':
            list.append(h)
            q=h
print(list)
#
# title = win32gui.GetWindowText(q)
# clsname = win32gui.GetClassName(q)
#
# print(title)
# print(clsname)

#print("脚本名：", sys.argv[1])

className = "阴阳师-网易游戏"

hwnd = win32gui.FindWindow(None, className)

print(hwnd)

rect = win32gui.GetWindowRect(hwnd)


print(rect[0], rect[1])

rect = (383, 183, 1537, 869);

win32gui.SetWindowPos(hwnd, win32con.HWND_BOTTOM, 384, 189, 1154, 713, win32con.SWP_NOSIZE)



