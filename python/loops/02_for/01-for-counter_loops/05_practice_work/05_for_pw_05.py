print('Замечательные числа в диапазоне двухзначных: ')
for number in range(10, 100):
    temp = number
    digit_product = 1
    while temp > 0:
        digit_product *= temp % 10
        temp //= 10
    if number == digit_product * 3:
        print(number)