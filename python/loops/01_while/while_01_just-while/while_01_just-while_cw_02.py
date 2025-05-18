balance = int(input('Сколько денег пришло? '))
while balance >= 5000:
    product_cost = int(input('Введите стоимость товара: '))
    balance -= product_cost
    print(f'Текущий баланс: {balance}')
    
print('Внимание! На карте осталось мало денег')
print(f'Баланс счета: {balance}')