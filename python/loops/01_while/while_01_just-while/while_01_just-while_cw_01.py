passwd = int(input('Введите пароль: '))
while passwd != 235:
    print('Неверный пароль!')
    passwd = int(input('Попробуйте еще раз: '))
print('Пароль верный. Добро пожаловать.')