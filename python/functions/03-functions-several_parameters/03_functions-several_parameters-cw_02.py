# Задача "Навигатор"
import math

def my_distance(func_x, func_y):
    distance = math.sqrt(func_x ** 2 + func_y ** 2)
    print(distance)

def between_distance(func_x_1, func_y_1, func_x_2, func_y_2):
    distance = math.sqrt((func_x_2 - func_x_1) ** 2 + (func_y_2 - func_y_1) ** 2)
    print(distance)

choise = int(input('1 - расстояние до точки, 2 - расстояние между двумя точками: '))

if choise == 1:
    x = float(input('Введите координату x: '))
    y = float(input('Введите координату y: '))
    my_distance(x, y)
elif choise == 2:
    x_1 = float(input('Введите координату x первой точки: '))
    y_1 = float(input('Введите координату y первой точки: '))
    x_2 = float(input('Введите координату x второй точки: '))
    y_2 = float(input('Введите координату y второй точки: '))
    between_distance(x_1, y_1, x_2, y_2)
else:
    print('Ошибка ввода')