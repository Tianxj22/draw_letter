#————————————————————————运行绘制函数的主程序————————————————————#

#————————————————————————————头文件————————————————————————————#

from Printer import *
from time import sleep


#————————————————————————————全局变量——————————————————————————#

char_height, char_width = 60, 30
char_width_limit = 600
row_gap_rate, col_gap_rate = 0.2, 0.2
output_str = 'A benchmark corpus of 100 English novels, covering the 19th and the beginning of the 20th century.It contains novels by 33 authors!#$%'

#————————————————————————————函数—————————————————————————————#

def cnt_time(time_limit: int, event: str):
    '''时间倒计时'''
    print(f"{time_limit}秒后将{event}")
    cnt = time_limit
    while cnt > 0:
        print(cnt)
        cnt -= 1
        sleep(1)

#——————————————————————————程序主体————————————————————————————#

printer = Printer(char_height=char_height, char_width=char_width, 
                  width_limit=char_width_limit, row_gap_rate=row_gap_rate, col_gap_rate=col_gap_rate)


cnt_time(5, '运行程序')
printer.draw_sentence(output_str)