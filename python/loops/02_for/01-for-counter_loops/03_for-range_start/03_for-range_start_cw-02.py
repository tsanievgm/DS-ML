# Задача "Здоровый сон"

wakeup = int(input('Во сколько проснулся? '))
awake_hours = 0
calories_sum = 0
for hour in range(wakeup, 23):
    print(f'Сейчас {hour} часов')
    calories = int(input('Сколько съел за час? '))
    calories_sum += calories
    awake_hours += 1
    if calories_sum > 2000:
        print('Хорошо поел. Можно и поспать.')
        break
    awake_hours += 1
print(f'Съедено калорий за день - {calories_sum}')
print(f'Не спал {awake_hours} часов')