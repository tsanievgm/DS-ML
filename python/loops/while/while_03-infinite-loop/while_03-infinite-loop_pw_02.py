workflow = False
while True:
    work = int(input("Продолжаем работать? 1/0: "))
    if work == 0:
        workflow = False
        print('Приложение закрывается')
        break
print('Работа завершена')