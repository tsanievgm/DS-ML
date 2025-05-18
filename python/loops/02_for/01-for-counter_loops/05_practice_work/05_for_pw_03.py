# Задача "Успеваемость в классе"

number = int(input('Сколько в классе учеников? '))
satisfactorily = 0
good = 0
excellent = 0

for performance in range(1,number + 1):
    grade = int(input('Введите оценку ученика: '))
    if grade == 3:
        satisfactorily += 1
    elif grade == 4:
        good += 1
    elif grade == 5:
        excellent += 1

if satisfactorily > good and satisfactorily > excellent:
    print('Сегодня больше троечников!')
elif good > satisfactorily and good > excellent:
    print('Сегодня больше хорошистов!')
elif excellent > satisfactorily and excellent > good:
    print('Сегодня больше отличников!')