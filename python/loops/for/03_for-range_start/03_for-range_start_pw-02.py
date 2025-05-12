#  Задача: Сумма чисел

first_number = int(input('Введите первое положительное число: '))
second_number = int(input('Введите второе положтельное число: '))
total_summ = 0

for number in range(first_number, second_number + 1):
    total_summ += number

print(f'Сумма числе от {first_number} до {second_number} составит {total_summ}')
