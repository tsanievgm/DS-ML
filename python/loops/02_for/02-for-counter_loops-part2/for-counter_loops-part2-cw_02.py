# Задача "Деление клетки"

total_hours = int(input('Введите количество часов: '))
cells = 1
for hour in range(1, total_hours // 3 + 1):
    cells *= 2
    print(f'Прошло часов: {hour * 3}')
    print(f'Количество клеток: {cells}')
    print(f'Осталось {total_hours - hour * 3} часов')
    print(' ')
print('Наблюдение завершено!')