# -*- codeing = utf-8 -*-
# @Time : 2021/08/21 21:12
# @Author : 217703 ZHANG WENXUAN
# @File : main.py
# @Software : PyCharm
import win32con
import win32gui
import cv2
import torch
from cs_model import load_model
from grabscreen import grab_screen

#detect.py
device='cuda' if torch.cuda.is_available() else 'cpu'
half = device != 'cpu'

x, y = (2560, 1440)  # プログラムウィンドウのサイズ
re_x, re_y = (2560, 1440)  # スクリーンのサイズ

model=load_model()

while True:
    img0 = grab_screen(region=(0, 0, x, y))  # 左上の角から右下の角

    cv2.namedWindow('detect', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('detect', re_x // 3, re_y // 3)  # ウィンドウのサイズ 1/3
    cv2.imshow('detect', img0)

    hwnd = win32gui.FindWindow(None, 'detect')  # ウィンドウを探す
    CVRECT = cv2.getWindowImageRect('detect')
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    # ウィンドウを常に最前面にする  、０が左上隅（すみ）に固まる 、[win32con.SWP_NOMOVE | win32con.SWP_NOSIZE]-->移動可能

    if cv2.waitKey(1) & 0xFF == ord('p'):  # キーボードの「p」ボタン押しと、ウィンドウをしまう///ショートカットキー
        cv2.destroyAllWindows()
        break
