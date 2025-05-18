# Задача "Простые числа"

def is_prime(n):
    is_prime_flag = True

    if n < 2:
        is_prime_flag = False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime_flag = False
            print('Данное число является составным')
            break

    print('Данное число является простым')

is_prime(3)