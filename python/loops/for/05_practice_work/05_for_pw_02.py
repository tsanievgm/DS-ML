total_salary = 0
for money in range(1, 13):
    salary = int(input('Введите зарплату сотрудника: '))
    total_salary += salary

print(f'Средняя зарплата за год: {total_salary / 12}')