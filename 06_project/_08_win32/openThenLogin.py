#!/usr/bin/python

import os
import time
import win32gui
import win32api
import win32con
import pymouse, pykeyboard
from pymouse import *
from pykeyboard import PyKeyboard
from ctypes import *


def QQ(qq, pwd):
    # 运行QQ
    os.system("E:\\tengxun\Tencent\QQ\Bin\QQScLauncher.exe")
    time.sleep(2)  # 暂停2秒
    # 获取QQ的窗口句柄
    # 参数1是类名,参数2是QQ软件的标题
    a = win32gui.FindWindow(None, "QQ")

    # 获取QQ登录窗口的位置
    loginid = win32gui.GetWindowPlacement(a)
    print(999999999, loginid)
    print(loginid[4][0])
    print(loginid[4][1])

    # 定义一个键盘对象
    k = PyKeyboard()

    # 把鼠标放置到登陆框的输入处
    # windll.user32.SetCursorPos(loginid[4][2]+192,loginid[4][3]+112)
    # 用坐标工具获取
    windll.user32.SetCursorPos(950, 555)

    # 按下鼠标再释放
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # press mouse

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  # release mouse

    time.sleep(2)
    ###input username1234   1234

    print(qq)
    # 输入用户名
    k.type_string(qq)
    time.sleep(0.2)
    ##tab
    # 按下tab，切换到输入密码的地方
    win32api.keybd_event(9, 0, 0, 0)
    win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)
    # 按下tab用下面两行也行
    # k.press_key(k.tab_key)
    # k.release_key(k.tab_key)
    # 按下tab用下面一行也行
    # k.tap_key(k.tab_key)

    # 输入密码
    k.type_string(pwd)

    # 按下回车
    win32api.keybd_event(13, 0, 0, 0)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)


if __name__ == "__main__":
    # fn = "qq.txt"
    # F = open(fn,"r").readlines()
    # for i in F:
    # 	tx = i.split('----')
    # 	print (tx[0])#打印用户名
    # 	print (tx[1])#打印密码
    # 	QQ(tx[0],tx[1])
    QQ("1234", "1234")
