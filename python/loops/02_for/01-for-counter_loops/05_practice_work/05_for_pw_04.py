# Задача "Отрезок"

a = int(input('Начало отрезка: '))
b = int(input('Конец отрезка: '))
summ = 0
count = 0


print('Числа из отрезка, которвые деляется на 3: ')
for number in range(a, b + 1):
    if number % 3 == 0:
        print(number)
        summ += number
        count += 1

print(f'Среднее арифметическое этих чисел: {summ / count}')
