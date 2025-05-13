# colors = ['#E6BBC1', '#D8DEBA', '#CBBAC5', '#C1CACA', '#D8B1BF', '#98C793']

# import random as r
#
# r_string = 'desfygujklpolkijuhgbfvcesdfcgvbrtrdecfEDSXC787878!'
# lst = list(r_string)
# r.shuffle(lst)
# print(lst)
#
# temp = lst[:0]
# if '!' in temp:
#     print(*temp, sep='')
# else:
#     temp.append('!')
#     print(*temp, sep='')

# print(*lst[:8], sep='') #срез списка  * -вначале переменной передача списка, при условии что это список

# value = r.choice(colors) #сгенирировать случайное число
# print(value)

# index = r.randint(0, len(colors) - 1)
# print(colors[index])

# for _ in range(10):
#     index = r.randint(0, len(colors))
#     print(index)

# кортеж, к кортежу обращение идет быстрее, занимает меньше памяти, есть взаимное присвоение, кортеж - неизменяемый, кортеж можно сразнивать

# l = ['Пришло', 'лето'] # обозначение кортежа
# l[1], l[0] = l[0], l[1]
# print(*l)

# def swap(a, b):  #возвращение кортежа
#     b, a = a, b
#     return a, b
# print(*swap(1, 2))
#
# #заменить кортеж на список
#
# def swap(a):
#     x = a ** 2
#     y = 2 * a
#     z = a / a
#     return x, y, z
#
# temp = swap(2)
# print(temp)

# a = 1, 1
# b = 1, 1

# print(a <= b)

# x, y, z = 1, 2, 3
# z, y = x, y

# print(x, y, z)

# a = list() # список
# b = tuple() # кортеж
# #c = set() # множество
#
# c = {'a', 'b', 'c'}

# print(c)

# a = {1, 2, 3, 4}
# b = {2, 3, 5, 7, 11}

# print(a.union(b)) #объединение
# print(a.intersection(b)) #пересечение
# print(a.difference(b)) #разность
# print(a.symmetric_difference(b)) #симметричная разность

# v = 'телевидение'
# d = set(v)
#
# print(*d, sep='')

# lst = [2, 3, 5, 7, 11]
#
# for index, value in enumerate(lst):
#     print('Индекс:', index, 'Значение:', value)

# словарь

# d = dict() #пустой словарь
# d = {
#     'Дмитриев': ['Плотник', 'Скульптор'],
#     'Иванов': 'Программист',
#     'Петров': 'Художник',
#     'Сидоров': 'Стоматолог'
# } #словарь

# d['Никитин'] = 'Официант'
# print(d['Никитин'])

#
# if 'Иванов' in d.keys():
#     print('Он есть')

# for item in d.keys():
#     print(item)

# if 'в' in 'Собака':
#     print('Есть такая буква')

# l = ['a', 'b', 'c']
#
# print('Вот алфавит:')
#
# for i, v in enumerate(l):
#     print(i + 1, v)

# symvol = 'a'
# code = 176
# print(35, '\u2710' + 'C')

# string = '     Python Language                         '
# num = '35'
# print(string.capitalize()) #
# print(string.title()) #
# print(string.upper())
# print(string.lower())
# print(num.isdigit())
# string = string.strip()
# lst = string.split(' ') #разделить строку...
# lst[0] = ''
# new_string = ' '.join(lst) #
# print(new_string)

# b_list = ['Аптека', 'Улица', 'Фонарь']
# b_string = ',  '.join(b_list).capitalize()
# print(b_string)
#
# d = 'аргентина манит негра'
# new_d = ''.join(d.split())
# print(new_d)
