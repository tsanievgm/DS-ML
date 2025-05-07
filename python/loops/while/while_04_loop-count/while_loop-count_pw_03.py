number = int(input('Введите число: '))
attempt_count = 0
while number != 7:
    if number < 7:
        print('Число меньше, чем нужно. Попробуйте еще раз!')
        number = int(input('Введите число: '))
    else:
        print('Число больше, чем нужно. Попробуйте еще раз!')
        number = int(input('Введите число: '))
    attempt_count += 1

print(f'Вы угадали! Число попыток: {attempt_count}')
