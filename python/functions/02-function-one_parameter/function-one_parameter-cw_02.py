# Задача "Функция"
import math

def func(x):
    if -5 <= x <= 5:
        print(f'x = {x}, y = {math.exp(x)}' )
    elif x < -5:
        print(f'x = {x}, y = {2 * abs(x) - 1}')
    else:
        print(f'x = {x}. y = {2 * x}')

for x in range(-10, 11):
    func(x)