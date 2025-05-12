#  Задача: Разминка для здоровья

start_work = int(input('Во сколько часов начало рабочего дня? '))
end_of_day = 20
training_minutes = 0
work_count = 0

total_time_training = 0

for hour in range(start_work, end_of_day + 1):
    work_count += 1
    training = int(input('Dремя разминки. Сколько минут посвятил ей? '))
    training_minutes += training

    if training_minutes >= 45:
        break

print(f'Алексей сегодня тренировался {training_minutes} минут')
print(f'Также сегодня он работал {work_count} часов')

if training_minutes >= 45:
    print('Алексей достиг своей цели в 45 минут активности в течении рабочего дня')
else:
    print('К сожалению, Алексей сегодня не добился своей цели')


