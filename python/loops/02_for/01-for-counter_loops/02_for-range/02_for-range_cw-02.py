total_months = int(input('Сколько месяцев будем копить? '))
summ = 0
for month in range(total_months):
    print(f'Месяц {month}')
    money = int(input('Сколько рублей откладываем? '))
    summ += money
print(f'За {total_months} месяцев ты накопишь {summ} рублей')