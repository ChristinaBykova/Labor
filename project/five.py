# from random import randint
# num = randint(1, 10)
# choice = int(input('Введите число'))
#
# while choice != num:
#     if choice < num:
#         print('Ваше число меньше загаданного')
#     else:
#         print('Ваше число больше загаданного')
#     choice = int(input('Введите число:'))
# print('Ура, вы угадали ', num)

#шифрование
# abc = 'АБВГДЕЁЖ...Я'
# text = input('')
# key = int(input(''))
#
# text = text.upper()
# encrypted = []
#
# for letter in text:
#     if letter in abc:
#         abc[(index + 3) % 33]
#

# source = 'город рим'
# lst = source.split()
# #print(lst[1][::-1] + lst[0])
# print(lst[0][::-1],  lst[0], lst[1][::-1] + lst[0])

# d = dict()
# source = ''.join(source.split()) #убрать пробелы в данном случае
# for b in source:
#     if b in d:
#         d[b] += 1
#     else:
#         d[b] = 1
#
# for k, v in d.items():
#     print(k, v, sep='-')
# t = 20
# print('тепло') if t < 20 else print('прохладно')

#строки, начиная с нуля
# string = 'Видеть, смотреть, вертеть'
# # find(что, старт, стоп)
# index = string.find('еть', 15,25) #3 начиная с нуля
# print(index)

# phone = '+7-952-364-57-88'
# print('Исходная строка:', phone)
#
# spaced_phone = phone.replace('-', ' ')
# print('Телефон через пробел:', spaced_phone)
#
# temp = phone.replace('-', ' (', 1)
# print(temp)
#
# bracked_code = temp.replace('-', ')', 1)
# print(bracked_code)

# %d - число
# %s - строка
# %f - float

# name = 'Виктор'
# age = 9
# height = 114.5
#
# f_string = '%9s,\n возраст: %2d лет, \n рост: %6.1f см.'%(name, age, height)
# print(f_string)
# d_str = f"Имя:{name}, возраст: {age}, рост: {height}"
# print(d_str)


# min_val = 5
# max_val = 50
#
# str = ' %d,  %d'%(min_val, max_val)
# print(str)

# спискиa
# a = []
# for i in range(1,11):
#     a.append(i)
# print(a)
#Списочные выражения
# a = [i for i in range(101) if i % 10 == 5]
# print(a)
# #
# ip = '198.162.100.101'
# b = [int(i) for i in ip.split('.')]
# print(sum(b))

#
# n = '8 8 7 7'
# a = sum([int(x) for x in n.split()])
# print(a)

#МОДУЛИ
from lib import *
#import lib # импортирование к библиотекам

#lib.say_hello('Sasha')
#lib.div(4,9)

#

# from PIL import Image
# from PIL import ImageDraw
#
# l = (229,43,80)
# b = (0,0,0)
# new_image =Image.new("RGB", (100,100), l)
# new_image.save('image.png', 'PNG')
#
# canvas = Image.new("RGB", (100,100), b)
# draw = ImageDraw.Draw(canvas)
#
# draw.line((0,0,100,100), fill=l, width=1)
# draw.line((100,0,0,100), fill=l, width=1)
# canvas.save('image.png', 'PNG')