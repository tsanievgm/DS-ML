# Задача "Среднее арифметическое"

def average_func(a, b):
    summ = 0
    count = 0
    for number in range(a, b + 1):
        summ += number
        count += 1
    average = summ / count
    print(f'Среднее: {average}')
average_func(1,2)