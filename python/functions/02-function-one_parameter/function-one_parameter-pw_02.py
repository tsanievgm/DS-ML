# Задача "Вот это объемы 2"
import math

def sphere_area (R):
    print(f'Площадь сферы: {4 * math.pi * (R ** 2)}')

def sphere_volume(R):
    print(f'Объем сферы: {4 / 3 * math.pi * (R ** 3)}')

sphere_area(2)

sphere_volume(2)
