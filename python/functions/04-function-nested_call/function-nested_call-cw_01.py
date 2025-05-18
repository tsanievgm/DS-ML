
def main_menu():
    print('1. Сделать что-то хорошее')
    print('2. Сделать что-то хорошее')
    choice = int(input('Введите номер действия: '))
    if choice == 1:
        good()
    elif choice == 2:
        bad()
    else:
        print('Ошибка ввода. Нужно ввести 1 или 2')
        main_menu()

def good():
    print('Все хорошо')
    input('Нажмите любую кнопку, чтобы вернуться в меню')
    main_menu()

def bad():
    print('Все плохо')

main_menu()