# Задача "Почта 2"

def delivery_data(surname, name, country, city, street, number_house, number_apartment,):
    print(f'Фамилия: {surname}')
    print(f'Имя: {name}')
    print(f'Страна проживания: {country}')
    print(f'Город: {city}')
    print(f'Улица: {street}')
    print(f'Номер дома: {number_house}')
    print(f'Номер квартиры: {number_apartment}')
    print(' ')

delivery_data('Иванов',
              'Иван',
              'Россия',
              'Москва',
              'Гамидова',
              23,
              44)