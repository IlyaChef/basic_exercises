# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
print(*names, sep='\n')



# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4

names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in range(len(names)):
    print(f'{names[name]}: {len(names[name])}')


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']

for name in names:
    if is_male[name]:
        print(f'{name}: пол мужской')
    else:
        print(f'{name}: пол женский')
    




# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

groups = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]
print(f'Всего {len(groups)} группы.')
print(f'Группа 1: {len(groups[0])} ученика.')
print(f'Группа 2: {len(groups[1])} ученика.')
print(f'Группа 3: {len(groups[2])} ученика.')

# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]
print(f'Группа 1: {(groups[0][0])}, {(groups[0][1])}')
print(f'Группа 2: {(groups[1][0])}, {(groups[1][1])}, {(groups[1][2])}')
print(f'Группа 3: {(groups[2][0])}, {(groups[2][1])}, {(groups[2][2])}, {(groups[2][3])}')