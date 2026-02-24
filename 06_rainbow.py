# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код

x = 50
y = 50
color_index = 0
for _ in range(7):
    start_point = sd.get_point(x, y)
    end_point = sd.get_point(x + 300, y + 400)
    color = rainbow_colors[color_index]
    sd.line(start_point=start_point, end_point=end_point, color=color, width=4)
    x += 5
    color_index += 1

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

point = sd.get_point(400, -20)
radius = 400
step = 18
color_index = 0
for _ in range(7):
    radius += step
    color = rainbow_colors[color_index]
    sd.circle(center_position=point, radius=radius, color=color, width=step)
    color_index += 1

sd.pause()
