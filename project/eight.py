# англо-русский словарь, которые сам себя обучает
# import pickle
#
# with open('dictinary.bin', 'rb') as f:
#     d = pickle.load(f)
# while True:
#     word = input('Введите слово для перевода:')
#     if word == 'QQ':  ##для выхода из словаря
#         break
#     if word in d:
#         print(f'Слово {word} переводится  как {d[word]}')
#     else:
#         print('Я не знаю этого слова, но можете мне подсказать')
#         new_word = input(f'Как переводится {word}: ')
#         d[word] = new_word
#
# with open('dictinary.bin', 'wb') as f:
#     pickle.dump(d, f)

###
# d = {
#     'стол': 'table',
#     'стул': 'chair'
# }
# keys = tuple(d.keys())
# values = tuple(d.values())
#
# with open('dictinary.txt', 'wt', encoding='utf-8') as f:
#     print(*keys, file=f)
#     print(*values, file=f)

#
# d = dict()
# with open('dictinary.txt', 'rt', encoding='utf-8') as f:
#     keys = f.readline().strip('\n')
#     values = f.readline().strip('\n')
# print(keys)
# key_list = keys.split()
# value_list = values.split()
# length = len(key_list)
#
# for i in range(length):
#     d[key_list[i]] = value_list[i]
#
# print(values)
# print(d)

## Исключение
# name = input('ВВ')
# try: #
#     print(nname)
# except NameError:
#     name = input('Ваше имя:')
#     print('Вас зовут', name)

# там нет ошибки!
# try:
#     f = open('text.txt')
#     f.close()
#     print('Все в порядке')
# except FileNotFoundError:
#     f = open('text.txt', 'w')
#
#     f.close()
#     print('Файл был удален')
#     print('И он был удален')

# считаем остаток от деления
# print('Остаток от деления')
# value = int(input('С чего считаем остаток от деления: '))
# res = 10 / value
# #print(f'Остаток от деления {value} на 10 будет {res}')
# try:
#     value = int(input('остаток от деления: '))
#     res = 10 / value
#     #print(f'Остаток от деления {value} на 10 будет {res}.')
# except ZeroDivisionError:
#     print('а ноль делить нельзя')
# except ValueError:
#     print('Вас попросили ввести целое число, а вы!')
# else:
#     print(f'остаток от деления {value} на 10 будет {res}.' )

###
# try:
#      f = open('informer.txt') #пробудем открыть, если открывается, то читаем
#      print(f.read())
#      is_opened = True #устанавливаем "флаг" открытия
# except FileNotFoundError:
#      print('Файл не существует')
#      is_opened = False #файл не открывался
# finally:
#     if is_opened: #если файл был открыт на чтение успешно
#      print('Файл прочитан и закрыт.')
#      f.close()
#     else:
#         print('файл не открывался')

# while True:
#     try:
#         num = int(input('Введите целое число: '))
#         print(f'Вы ввели {num} и это верно!')
#         break
#     except ValueError:
#         print('Некорретный ввод')


# Исключение в диапозоне
# Thorow exception - выбрасывать исключения
# Raise exception - поднять исключение
# min_val = 1
# max_val = 10
# s_num = input(f'Введите число от {min_val} до {max_val}')
# try: # число перевсти в строку
#     num = int(s_num)
#     if not min_val <= num <= max_val:
#         raise ValueError('Введенное число вне заданного диапазона')
# except ValueError as exp:
#     print(f'Вас просили ввести целое число от 1 до 10, а вы ввели {s_num}')
#     print('Будьте внимательны', exp)
# else:
#     if flag:
#         print(f'Вас просили ввести целое число, а вы ввели "{s_num}"')
#     print(f'Число {num} в заданном диапазоне.')

# Assert - это утверждение. верно ли пришли к данному значению... В основном для откладки своего кода

# try:
#     text = input('Введите текст')
#     assert len(text) > 3 #утвержение
# except AssertionError:
#     print('Длина текста меньше 3-х символов')

# while True:
#     a = input('Введите число')
#     b = input('Введите число')
#     if a.isdigit() and b.isdigit(): # возвращение флага?
#         if int(b) == 0:
#             print('Нельзя делить на ноль')
#         else:
#             print(int(a) / int(b))
#             break
#     else:
#         print('Необходимо ввести число')
#

# !!!
# while True:
#     a = input('Введите число')
#     b = input('Введите число')
# try:
#     print(int(a) / int(b))
#     break
# except ZeroDivisionError:
#     print('Нельзя делить на ноль')
# except ValueError:
#     print('Необходимо ввести число')
#

# Syntax sugar (Синтаксический сахар) -
# def multy(*args):
#     print(f'Мне передали {len(args)} аргуметов.')
#
# multy(1, 2, 3, 4, 5)

# def average(*args):
#     print(f'Среднее значение суммы {sum(args) / len(args)}') #в {} можно делать всё что угодно!
#
# average(1, 2, 3, 4, 5)

##
# num_list = [1, 2, 3, 4, 5]
# #print(''.join(map(str, num_list)))
# # def doubled(x):
# #     return x * 2
# #lambda <аргумент(ы)>:<выражение с этими аргументами>
# #doubled = lambda x: x*2
# double_list = list(map(lambda x: math.pow(x, 3), num_list))
# print(double_list)


##
# string = ['Арбуз', 'Виноград', 'Банан']
# s_list = sorted(string)
# print(s_list)

# Regular expressions

# import re
# pattern = '20'
# test_string = '10 плюс на 20 будет 30'
# result = re.search(pattern, test_string)
# print(result.span())
