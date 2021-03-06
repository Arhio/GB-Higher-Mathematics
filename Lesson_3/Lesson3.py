import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import math

# Урок 3
# Задание 1.2
# Напишите код на Python, реализующий расчет длины вектора, заданного его координатами. (в программе)


# def LineLengthXY(x1, y1, x2, y2):
#     return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
#
#
# def LineLengthXYZ(x1, x2, y1, y2, z1, z2):
#     return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
#
#
# print('Длина вектора составит: ' + str(LineLengthXY(
#     int(input('Введите x1 вектора:')),
#     int(input('Введите у1 вектора:')),
#     int(input('Введите x2 вектора:')),
#     int(input('Введите у2 вектора:'))
#     )))


# Задание 2
# Почему прямые не кажутся перпендикулярными? (см.ролик)
# fig, ax_f = plt.subplots()
#
# x = np.linspace(-5, 5, 30)
# k = 6
# y1 = (k * x) + 1
# y2 = (-1/k) * x + 1
#
# ax_f.plot(x, y1)
# ax_f.plot(x, y2)
# n = 5 + x * 0
# ax_f.plot(x, n)
# ax_f.plot(x, -n)
# ax_f.plot(n, x)
# ax_f.plot(-n, x)
# ax_f.set_xlim(-15, 15)
# ax_f.set_ylim(-15, 15)
# ax_f.set_title('Задание 2.')
#
# plt.show()

# Задание 3.1
# Напишите код на Python, реализующий построения окружности

# fig, ax_f = plt.subplots()
#
# x = np.linspace(-5, 5, 100)
# r = 5
# y = (r ** 2 - x ** 2) ** (1/2)
# n = 5 + x * 0
#
# ax_f.plot(x, y)
# ax_f.plot(x, -y)
# ax_f.plot(x, n)
# ax_f.plot(x, -n)
# ax_f.plot(n, x)
# ax_f.plot(-n, x)
# ax_f.set_xlim(-15, 15)
# ax_f.set_ylim(-15, 15)
# ax_f.set_title('Задание 3.1.')
#
# plt.show()

# Задание 3.2
# Напишите код на Python, реализующий построения эллипса
# fig, ax_f = plt.subplots()
#
# x = np.linspace(-5, 5, 100)
# r = 5
# b = 3
# y = (b/r) * (r ** 2 - x ** 2) ** (1/2)
#
# ax_f.plot(x, y)
# ax_f.plot(x, -y)
# n = 5 + x * 0
# ax_f.plot(x, n)
# ax_f.plot(x, -n)
# ax_f.plot(n, x)
# ax_f.plot(-n, x)
# ax_f.set_xlim(-15, 15)
# ax_f.set_ylim(-15, 15)
# ax_f.set_title('Задание 3.2.')
#
# plt.show()

# Задание 3.3
# Напишите код на Python, реализующий построения гиперболы
# fig, ax_f = plt.subplots()
#
# x = np.linspace(-10, 10, 100)
# r = 5
# b = 5
# y = (r ** 2 + x ** 2) ** (1/2)
#
# ax_f.plot(x, y)
# ax_f.plot(x, -y)
# ax_f.set_xlim(-15, 15)
# ax_f.set_ylim(-15, 15)
# ax_f.set_title('Задание 3.3.')
#
# plt.show()

# Задание 5.1
# Нарисуйте трехмерный график двух параллельных плоскостей.

# fig = figure()
# ax = Axes3D(fig)
# X = np.arange(-5, 5, 0.5)
# Y = np.arange(-5, 5, 0.5)
# X, Y = np.meshgrid(X, Y)
# Z = 2*X + 5*Y
# ax.plot_wireframe(X, Y, Z)
# ax.plot_wireframe(X + 1, Y + 1, Z + 1)
# ax.scatter(0, 0, 0, 'z', 50, 'red')
# show()

# Задание 5.2
# Нарисуйте трехмерный график двух любых поверхностей второго порядка.

# fig = figure()
# ax = Axes3D(fig)
# X = np.arange(-3, 3, 0.5)
# Y = np.arange(-7, 7, 0.5)
# a = 2
# b = 4
# X, Y = np.meshgrid(X, Y)
# Z = (X ** 2/a ** 2) - (Y ** 2/b ** 2)
# ax.plot_wireframe(X, Y, Z)
# ax.scatter(0, 0, 0, 'z', 50, 'red')
# show()


# Задание 1
# Нарисуйте график функции: y(x) = k∙cos(x – a) + b
# fig, ax_f = plt.subplots()
#
# x = np.linspace(-5, 5, 100)
# y1 = 1 * np.cos(x - 2) + 3
# y2 = 3 * np.cos(x - 2) + 1
# y3 = 2 * np.cos(x - 4) + 2
#
# ax_f.plot(x, y1)
# ax_f.plot(x, y2)
# ax_f.plot(x, y3)
# ax_f.set_xlim(-15, 15)
# ax_f.set_ylim(-15, 15)
# ax_f.set_title('Задание 1.')
#
# plt.show()


# Задание 3
# Напишите код, который будет переводить полярные координаты в декартовы.
# r = 5
# a = 1 #угол в радианах
# x = r * math.cos(a)
# y = r * math.sin(a)
# print("x = " + str(x))
# print("y = " + str(y))

# Напишите код, который будет рисовать график окружности в полярных координатах.
# a = np.linspace(0, 2*math.pi, 50)
# r = 10
# x = r * np.cos(a)
# y = r * np.sin(a)
#
# plt.plot(x, y)
# plt.show()
#
# #Напишите код, который будет рисовать график отрезка прямой линии в полярных координатах.#
# x = np.linspace(0, 10, 50)
# a = math.pi / 4
# y = x * np.sin(a)
#
# plt.plot(x, y)
# plt.show()

# Задание 4
# 4.1 Решите систему уравнений:
# x = np.linspace(-10, 10, 50)
#
# y1 = x ** 2 - 1
# y2 = (np.exp(x) + x)/-x
#
#
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.show()

# 4.2 Решите систему уравнений:
# x1 = np.linspace(-500, 500, 300)
# y1 = x1 ** 2 - 1
# xy = [[_x, (np.exp(_x) + _x) / - _x] for _x, _y in zip(x1, x1) if math.exp(_x) + _x * (_x - (math.exp(_x) + _x)/-_x) > 1]
# x2 = [x for x, y in xy]
# y2 = [y for x, y in xy]
#
# plt.plot(x1, y1)
# plt.plot(x2, y2)
#
# plt.show()