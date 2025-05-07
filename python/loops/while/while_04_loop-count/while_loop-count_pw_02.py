deposit = int(input('Вклад в банке: '))
rate_number = int(input('Проценты: '))
interest_amount = 0
target_deposit = int(input('Порог вклада: '))
year_count = 0

while interest_amount < target_deposit:
    year_count += 1
    interest_amount = deposit + int((deposit * rate_number) / 100)
    deposit = interest_amount
    print(f'{year_count} год. {deposit} + {rate_number}% = {interest_amount}')

print(f'Количество лет для достижения порога: {year_count}')


