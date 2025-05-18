total_cards = int(input('Введите количество карточек: '))
total_summ = 0
for card in range(1,total_cards + 1):
    total_summ += card
for card in range(total_cards - 1):
    remaining_card = int(input('Номер оставшейся карты: '))
    total_summ -= remaining_card
print(f'Номер потерявшейся карточки: {total_summ}')