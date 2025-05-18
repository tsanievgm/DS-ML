# Задача "Космический корабль"

total_count = 0

for number in range(1,11):
    iden = int(input('Введите номер человека: '))
    if iden > 0 and iden % 2 == 0:
        total_count += 1
print(f'Количество корректных номеров (четных и положительных): {total_count}')