# import re

# pattern = '[^абвгд]'
# test_string = 'АБВГДейка - детская передача!'
# result = re.findall(pattern, test_string, re.I)
# #print('Цифры есть') if result else print('цифр нет')
# # print(result)
# # if result:
# #     print(result[0], result.span())
# # else:
# #     print('Нету')
# print(*result, sep='')

# выводит на печать значение в скобках
# pattern = r'\((.+?)\)'
# test_string = 'Поиск по образцу (Hello)!'
# result = re.findall(pattern, test_string, re.I)
# print(*result, sep='')

##
# pattern = 'Go{2,4}gle'
# test_string = 'Google, Gooogle, Gooooooogle'
# result = re.findall(pattern, test_string, re.I)
# print(result)

##
# pattern = '<img.*>'
# test_string = 'PIc <img src="bg.jpg"> text</p>'
# result = re.findall(pattern, test_string, re.I)
# print(result)

# Чтение делает человека знающим, беседа - находчивым, а привычка записывать - точным.
# лямда с двумя параметрами
# import math
# lst = [1, 2, 3, 4, 5]
# power = lambda x, y: math.pow(x,y)
# res = list(map(lambda x:power(x,2), lst))
# print(*res)

###zip, выводит картеж...
# rus = ['стул','стол','яблоко']
# eng = ['chair','table','apple']
# d = dict(zip(rus,eng))
# print(d)

##Декораторы функций
# def decorator_function(func):
#     def wrapper():
#         print(f'Оборачиваемая функция: {func}')
#         print('Выполняем функцию')
#         func()
#         print('Выход')
#     return wrapper()
# @decorator_function
# def say_hello():
#     print('Hello')
# say_hello
# # def say_hello():
#     print('Hello')

# def wrapper():
#     def say_hello():
#         print('Hello')
#     say_hello()
#
# #wrapper()
#
# def higher_order(func):
#     func()
#
# higher_order(say_hello)

# def benchmark(func):
#      import time
#      def wrapper():
#          start = time.time()
#          func()
#          end = time.time()
#          print(f'затраченное время:{end - start}сек.')
#      return wrapper
# @benchmark
# def long_list_creator():
#      a = [i for i in range(100000)]
#
# long_list_creator()
# class Fruit:
#     pass
# a = Fruit()
# b = Fruit()
#
# print(type(a))
