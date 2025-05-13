# n = int(input('Введите целое число: '))
#
#     print('Число', n, 'чётное')
# else:
#   print('Число', n, 'нечётное')
#
#  for n in range(101):
#       if n % 10 == 7:
#          print(n)
#
# print("""Налево пойдешь - женишься,
#  направо - коня потеряешь,
#  прямо пойдешь - смерть свою найдешь.
#  Прямо - f, налево - l, направо - r.""")
# choice = input('\n Куда пойдем?')
#
# while True:
#     choice = input('\n Куда пойдем?')
#     if choice == 'r':
#         print('Коня нет')
#         break
#     elif choice == 'l':
#         print('Будешь счастлив!')
#         break
#     elif choice == 'f':
#         print('Смерчь')
#         break
#     else:
#         print('Выберите направление')

# password = input('Введите пароль: ')
#
#       if password == '1254':
#         print('Пароль верен')
#         break
#     else:
#         print('Пароль неверен')
#
# def divider(a, b):
#     if b != 0:
#      return a / b
#     return 'Ошибка делиться на ноль'

# def factorial1(n):
#     x = 1
#     for i in range(1, n + 1):
#         x *= i
#     return x
#
# def factorial_r(n):
#     if n == 0:
#         return 1
#     return n * factorial_r(n - 1)
#
# print(factorial1(5))
#
# print(factorial_r(5))

# from datetime import datetime
#
# get_time = datetime.time(datetime.now())
# cur_time = get_time.strftime("%H:%M:%S")
# hour = int(get_time.strftime("%H"))
# #print(cur_time)
#
# def greeting(hour):
#       if 8 <= hour < 12:
#           print('Доброе утро!')
#       elif 12 <= hour < 18:
#           print('Доброе день!')
#       elif 18 <= hour < 22:
#           print('Доброе вечер!')
#       else:
#           print('Доброй ночи!')
#
#   # for h in range(24):
#   #     print('На часах', h, end=': ')
#
# greeting(hour)

# steps_yest = 32500
# steps_today = 5500
# str_out = 'Вы прошли'
# steps_sum = steps_yest + steps_today
#
# if steps_sum >= 10000:
#     gyges = steps_sum // 10000
#     str_out += str(steps_sum) + 'шагов. Поздравляю!'
#     str_out += '\n Вам стало доступно' + str(gyges) + 'Гб'
#     str_out += '\n До следующего Гб Вам осталось пройти'
#     str_out += str(10000 * gyges - (steps_sum - 10000))
# else:
#     str_out += ' пока что только '
#     str_out += str(steps_sum)
#     str_out += 'шаговю Есть к чему стремиться '
#     str_out += '\n Для получения 1 Гб Вам нужно пройти ещё'
#     str_out += str(10000 - steps_sum) + 'шагов'
#
# print(str_out)

# color = input('Цвет шарика: ')
# if color == 'зеленый' or color == 'синий':
#     print('Эти шары подходят')
# else:
#     print('Не годится')

# import turtle as t
#
# colors = ['#E6BBC1', '#D8DEBA', '#CBBAC5', '#C1CACA', '#D8B1BF', '#98C793']
# angle = 59
#
# t.speed(0)
# t.bgcolor('#28071A')
# for x in range(201):
#   t.pencolor(colors[x % 6])
#   t.width(x // 50 + 1)
#   t.forward(x)
#   t.left(angle)
#
# t.mainloop()
# print(colors[2:6])

# string = input('Введите строку: ')
#
# if string == string[::-1]:
#  print(string, '- палидром')
# else:
#  print(string, '- не палиндром')

# number = input('Введите целое число:')
# a = 0
# for i in number:
#     a += int(i)
#
#     print('Сумма разрядов', number, '=', a)
