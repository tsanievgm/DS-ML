deposit = int(input('Вклад в банке: '))
interest_rate = int(input('Проценты: '))
target = int(input('Порог вклада: '))
total_amount = 0
year_count = 1

while deposit < target:
    total_amount = deposit + int((deposit * interest_rate) / 100)
    print(f'{year_count} год. {deposit} + {interest_rate}% = {total_amount}')
    deposit = total_amount
    year_count += 1
print(f'Количество лет для достижения порога: {year_count}')