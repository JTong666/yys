import win32api, win32con, win32gui
import time
from ctypes import *


def clickLeftCur():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def moveCurPos(x,y):
    windll.user32.SetCursorPos(x, y)

def getCurPos():
    return win32gui.GetCursorPos()


def getPos():
    while True:
        time.sleep(0.2)
        getCurPos()
        pos = getCurPos()
        s = windll.user32.GetForegroundWindow()
        print(s, pos)



def main():
    getPos()


if __name__=="__main__":
    main()