# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код

def draw_ellipse(start_x, start_y, end_x, end_y, color):
        left_bottom = sd.get_point(start_x, start_y)
        right_top = sd.get_point(start_x + end_x, start_y + end_y)
        sd.ellipse(left_bottom=left_bottom, right_top=right_top, color=color, width=1)
      
def draw_smile(x, y, color):
    draw_ellipse(x, y, 100, 80, color)

    draw_ellipse(x + 30, y + 40, 10, 15, color)
    draw_ellipse(x + 60, y + 40, 10, 15, color)

    sd.line(start_point=sd.get_point(x + 35, y + 20), end_point=sd.get_point(x + 60, y + 20), color=color)
    sd.line(start_point=sd.get_point(x + 20, y + 30), end_point=sd.get_point(x + 35, y + 20), color=color)
    sd.line(start_point=sd.get_point(x + 60, y + 20), end_point=sd.get_point(x + 75, y + 30), color=color)
    
for _ in range(10):
      x = sd.random_number(0, 500)
      y = sd.random_number(0, 500)
      color = sd.random_color()
      draw_smile(x, y, color)

sd.pause()
