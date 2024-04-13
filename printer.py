#————————————————将相应文件的内容模拟键盘敲击出来————————————————#

#——————————————————————————————————————————————————————————#

import pyautogui
from time import sleep
from source_dealer import *

# 符号大小
char_width = 30
char_height = 60

#——————————————————————————————————————————————————————————#

def cnt_down(sec: int):
    '''脚本开始前倒计时'''
    print(f'脚本将在{sec}秒钟后运行，请提前移动到需要的位置，现在开始倒数：')
    while sec > 0:
        print(sec)
        sleep(1.)
        sec -= 1

def draw_single_char(ch: str):
    '''绘制单个字符'''
    points = get_file_value(ch)
    pyautogui.moveRel(points[0][0] * char_width, points[0][1] * char_height)
    cur_pos = points[0]
    pyautogui.mouseDown()
    for point in points[1:]:
        pyautogui.moveRel((point[0] - cur_pos[0]) * char_width, (point[1] - cur_pos[1]) * char_height)
        cur_pos = point
    pyautogui.mouseUp()

#——————————————————————————————————————————————————————————#

cnt_down(5)

output_str = '0123456789'
for ch in output_str:
    start_x, start_y = pyautogui.position()
    draw_single_char(ch)
    pyautogui.moveTo(start_x + 1.2 * char_width, start_y)