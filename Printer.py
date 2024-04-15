#————————————————将相应文件的内容模拟键盘敲击出来————————————————#

#——————————————————————————————————————————————————————————#

import pyautogui
from time import sleep
from source_dealer import *
from numpy import pi, sin, cos
from Painter import *

#——————————————————————————————————————————————————————————#

class Printer():
    '''负责绘制整个文本的绘制器'''
    def __init__(self, char_height: float, char_width: float, width_limit: float, 
                 row_gap_rate: float, col_gap_rate: float,
                 lws_rate = 0.5) -> None:
        '''初始化绘制器：
            char_height: 单个字符高度, 
            char_width: 单个字符宽度,
            width_limit: 每行内容的最大宽度,
            row_gap_rate: 行间隔和字符高度的比例,
            col_gap_rate: 列间隔和字符高度的比例,
            lws_rate = 小写字符宽度相比于大写字符的缩放比例'''
        self.char_width, self.char_height = char_width, char_height
        self.width_limit = width_limit
        self.row_gap_rate, self.col_gap_rate = row_gap_rate, col_gap_rate
        self.lws_rate = lws_rate
        pass

    def draw_sentence(self, sentence: str):
        '''绘制整句话
            注意！当前鼠标位置会作为左上角'''
        start_x, start_y = pyautogui.position()
        dx, dy = 0., 0.
        for ch in sentence:
            if dx + self.get_width(ch) > self.width_limit:
                # 如果绘制的字符会超过宽度限制，则换一行
                dx = 0
                dy += (1 + self.row_gap_rate) * self.char_height
            pyautogui.moveTo(start_x + dx, start_y + dy)
            self.draw_single_char(ch)
            dx += (1 + self.col_gap_rate) * self.get_width(ch)

    def get_width(self, ch: str):
        '''计算ch的宽度'''
        rt = self.char_width
        if ch[0] >= 'a' and ch[0] <= 'z':
            rt *= self.lws_rate
        return rt

    def draw_single_char(self, ch: str):
        '''绘制单个字符'''
        requires = get_file_value(ch)
        tl_point = pyautogui.position()
        char_height, char_width = self.char_height, self.get_width(ch)
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