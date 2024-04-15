#————————————存储与绘制图案相关的代码————————————#

import pyautogui
from numpy import pi, sin, cos

def draw_line(start: list, end: list):
    '''绘制一个从起始点到终点的线'''
    pyautogui.moveTo(start[0], start[1])
    pyautogui.mouseDown()
    pyautogui.moveTo(end[0], end[1])
    pyautogui.mouseUp()

def draw_circle(center_point: list, radius: float, point_nums = 12):
    '''绘制圆形:
        center_point: 圆心
        radiu: 半径
        point_nums: 绘制的中间点个数，越大绘制图像越光滑'''
    draw_pie(center_point, radius, 0., 2 * pi, point_nums)

def draw_ellipse(center_point: list, a: float, b: float, point_nums = 12):
    '''绘制椭圆:
        center_point: 椭圆圆心
        a: x轴半径
        b: y轴半径
        point_nums: 绘制的中间点个数，越大绘制图像越光滑
    '''
    draw_pie(center_point, a, b, 0, 2 * pi, point_nums)

def draw_pie(center_point: list, a: float, b: float, start_theta: float, 
             end_theta: float, point_nums = 12):
    '''绘制扇形:
        center_point: 椭圆圆心
        a: x轴半径
        b: y轴半径
        start_theta: 起始角度
        end_theta: 结束角度
        point_nums: 绘制的中间点个数，越大绘制图像越光滑'''
    if start_theta > end_theta:
        start_theta, end_theta = end_theta, start_theta
    theta = start_theta
    theta_step = (end_theta - start_theta) / point_nums
    pyautogui.moveTo(center_point[0] + a * cos(theta), center_point[1] + b * sin(theta))
    pyautogui.mouseDown()
    for _ in range(int(point_nums)):
        theta += theta_step
        pyautogui.moveTo(center_point[0] + a * cos(theta), center_point[1] + b * sin(theta))
    pyautogui.mouseUp()