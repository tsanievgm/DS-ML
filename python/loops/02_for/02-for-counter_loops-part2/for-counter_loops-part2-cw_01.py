# Задача "Вывод куба числа"
n = int(input('Введите число: '))
for number in range(1, n // 2 + 1):
    number *= 2
    print(f'Число {number} ** 3 = {number ** 3}')
