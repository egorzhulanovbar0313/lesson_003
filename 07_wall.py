# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код

x_start = -100
y_start = -50
brick_width = 100
brick_height = 50
rows = 15
cols = 10

for row in range(rows):
    x_offset = 0 
    if row % 2 == 1:
      x_offset = brick_width // 2

    for col in range(cols):
        x = x_offset + col * brick_width
        y = y_start + row * brick_height
        left_bottom = sd.get_point(x, y)
        right_top = sd.get_point(x + brick_width, y + brick_height)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=1, color=sd.COLOR_ORANGE)

sd.pause()
