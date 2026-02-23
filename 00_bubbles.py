# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)
sd.background_color = (0, 0, 0)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код

point = sd.get_point(500, 500)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, width=2, color=(0, 255, 0))

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код

def bubble(point, step, color=(255, 255, 0)):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2, color=color )

point = sd.get_point(350, 350)
bubble(point=point, step=10, color=(0, 255, 255))

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

for x in range(100, 1100, 100):
    point = sd.get_point(x, 100)
    bubble(point=point, step=5)

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

for y in range(200, 500, 100):
    for x in range(200, 1200, 100):
        point = sd.get_point(x, y)
        bubble(point=point, step=10, color=(255, 0, 0))

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

for _ in range(100):
    point = sd.random_point()
    bubble(point=point, step=5, color=sd.random_color())

sd.pause()


