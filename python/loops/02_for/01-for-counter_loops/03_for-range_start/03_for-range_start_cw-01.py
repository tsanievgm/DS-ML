# Здесь мы практикуем функцию range() с добавлением аргумента `start`

begin_number = int(input('Введите начальное число: '))
end_number = int(input('Введите конечное число: '))
for number in range(begin_number, end_number + 1):
    print(number ** 2)