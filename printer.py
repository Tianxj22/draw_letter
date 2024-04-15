#————————————————将相应文件的内容模拟键盘敲击出来————————————————#

#——————————————————————————————————————————————————————————#

import pyautogui
from time import sleep
from source_dealer import *
from numpy import pi, sin, cos
from Painter import *

# 符号大小
char_width = 60 * 0.618
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
    requires = get_file_value(ch)
    tl_point = pyautogui.position()
    for require in requires:
        if require[0] == 'e':
            draw_ellipse([tl_point[0] + char_width * require[1], tl_point[1] + char_height * require[2]], 
                         require[3] * char_width, require[4] * char_height, require[5])
        elif require[0] == 'l':
            draw_line([tl_point[0] + char_width * require[1], tl_point[1] + char_height * require[2]], 
                      [tl_point[0] + char_width * require[3], tl_point[1] + char_height * require[4]])
        elif require[0] == 'p':
            draw_pie([tl_point[0] + char_width * require[1], tl_point[1] + char_height * require[2]], 
                        require[3] * char_width, require[4] * char_height, require[5], require[6], require[7])
            

#——————————————————————————————————————————————————————————#

cnt_down(3)

# draw_single_char('2')

output_str = 'POCKETMON'
for ch in output_str:
    start_x, start_y = pyautogui.position()
    draw_single_char(ch)
    pyautogui.moveTo(start_x + 1.2 * char_width, start_y)