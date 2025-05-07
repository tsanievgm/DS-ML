bags = int(input('Сколько нужно перетащить мешков? '))
total_weight = 0
bags_count = 0
while bags_count < bags:
    weight = int(input('Сколько весит мешок? '))
    total_weight += weight
    bags_count += 1
    print(f'Общий вес: {total_weight}')
    print(f'Перенесли мешков {bags_count} из {bags}')

print(f'Общий вес мешков составляет {total_weight}')
