# def say_hello(name):
#     print('Hello', name)
#
# say_hello('Sasha')
#
# def div(a,b):
#     if b != 0:
#         print(f'{a/b:.1f}')
#     else:
#         print('Ошибка')
#
# print('__name__')
#
# if __name__ == '__main__':
#     print('no')
# def get_size(obj):
#     print(f'Размер: {obj.__sizeof__()} байт(a)')
#
#
# class Fruit:
#     def __init__(self, name, color, weight):
#         self.name = name
#         # self.__name= name
#         self.color = color
#         self.weight = weight
#
#     def set_color(self, new_color):  # setter
#         self.color = new_color
#
#     def get_color(self):
#         return self.color
#
#     def get_info(self):
#         print(f'{self.name},{self.color}, {self.weight}')
#
#
# class Greeter:  # внутри него есть функция, обязанны вызвать как класс, метод только обязан определиться внутри классаб у всех методов обязательно первый всегда будет self, в self передается тот объект, который вызывает
#     def say_hello(self):
#         print('Hello')
#
#     def hello_name(self, name):
#         print(f'Hello {name}')
#
#     def hello_and_talk(self, name, weather):
#         print(f'Hello, {name}')
#         print(f'{name}, {weather}')
#
# #
# class Car:
#     count = 0 #статический атрибут
#
#     def __init__(self):
#         self.engine_on = False
#         Car.count +=1 # увеличиваетм на 1 всегда
#         # print('Объект создан')
#
#     def start_engine(self):
#         self.engine_on = True
#
#     def drive(self, place):
#         if self.engine_on:
#             print(f'I go to {place}')
#         else:
#             print('Забыли завсети мотор')
#     @staticmethod
#     def get_count():
#         return Car.count


# class Book:
#     def __init__(self, name, author):
#         self.name = name
#         self.author = author
#
#     def get_name(self):
#         return self.name
#
#     def set_author(self, new_author):
#         self.author = new_author
#
#

# def print_figure_info(figure):
#     if isinstance(figure, Square):
#         print('Для Квадрата')
#     elif isinstance(figure, Rectangle):
#         print('Для Прямоугольника')
#     else:
#         print('Для Круга')
#
#     print(f'\tArea={figure.area()} \n\tPerimeter={figure.perimeter()}')
#     #print(type(figure).__name__)
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return pi * self.radius ** 2
#
#     def perimeter(self):
#         return 2 * pi * self.radius
#
#
# class Square:
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side ** 2
#
#     def perimeter(self):
#         return self.side * 4
#
#
# class Rectangle:
#     def __init__(self, side_1, side_2):
#         self.a = side_1
#         self.b = side_2
#
#     def area(self):
#         return self.a * self.b
#
#     def perimeter(self):
#         return (self.a + self.b) * 2
#
#  class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side,side)
#         self.side = side
#
#     def area(self):
#         return self.side ** 2
#
#     def perimeter(self):
#         return self.side * 4


# class Rectangle:
#     def __init__(self, side_1, side_2):
#         self.a = side_1
#         self.b = side_2
#
#     def area(self):
#         return self.a * self.b
#
#     def perimeter(self):
#         return (self.a + self.b) * 2
#
#     def __eq__(self, other):
#         if self.a == other.a and self.b == other.b:
#             return True
#         else:
#             return False
#
#     # def __ne__(self, other):
#     #     print('Меня вызвали')
#     #
#     # def __lt__(self, other):
#     #     print()
#
#     def __ge__(self, other):
#         if self.a >= other.a and self.b >= other.b:
#             return True
#         else:
#             return False


# def print_figure_info(figure):
#     print(f'Perimeter={figure.perimeter()}')
#
#
# class Triangle:
#     def __init__(self, side_1, side_2, side_3):
#         self.a = side_1
#         self.b = side_2
#         self.c = side_3
# #
# #     # def area(self):
# #     #     return self.a * self.b
# #
# #     def perimeter(self):
# #         return self.a + self.b + self.c
# #
# #
# # class EquilateralTriangle(Triangle):
# #     def __init__(self, side):
# #         super().__init__(side, side, side)
# #         self.side = side
#
# class List:
#     def __init__(self, n=0):
#         if n == 0:
#             self.a = []
#         else:
#             try:
#                 n = int(n)
#                 n = abs(n)
#                 self.a = [i for i in range(n)]
#             except ValueError:
#                 self.a = []
#
#     def add(self, value=''):
#         self.a.append(value)
#
#     def clear(self):
#         self.a.clear()
#
#     def remove(self, value):
#         try:
#             self.a.remove(value)
#         except:
#             print('Элемента нет в списке')
#
#     def show_list(self):
#         print(*self.a, sep=', ')
#
#
# class Special:
#     def __init__(self):
#         self.value = 10
#
#     def __add__(self, other):
#         return 'Выполнился __add__'
#
#     def __radd__(self, other):
#         return 'Выполнился __radd__'
#
#     def __iadd__(self, other):
#         self.value += other
#         print('Выполнился __iadd__')
#         return self
#
#     def __str__(self):
#         return f'Значение {self.value}'
#
#
# class Time:
#     def __init__(self, minutes, seconds):
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def info(self):
#         return f'{self.minutes}:{self.seconds}'
#
#     def __add__(self, other):
#         m = self.minutes + other.minutes
#         s = self.seconds + other.seconds
#
#         m += s // 60
#         s = s % 60
#         return Time(m, s)
#
#     def __repr__(self):
#         return f'{self.minutes}:{self.seconds}'

from tkinter import *  # GUI
from tkinter import filedialog

from PIL import Image, ImageTk

status = False


class Okno:
    def __init__(self):
        self.window = Tk()  # Инициализация GUI
        self.window.title('Добро пожалуйста в Tkinter')
        self.window.geometry('800x600')
        self.window.resizable(False, True)
        self.lbl = Label(self.window, text='Ярык')
        self.lbl.pack()
        self.canvas = Canvas(self.window, height=100, width=133)
        self.image = ImageTk.PhotoImage(Image.open('images\chvetok.jpg'))
        self.canvas.create_image(0, 0, anchor='nw', image=self.image)
        self.canvas.pack()
        self.btn = Button(self.window, text='Нажми на кнопку - получишь результат!', command=self.click)
        self.btn.pack()

        self.window.mainloop()

    def click(self):
        path = filedialog.askopenfilename()
        original = Image.open(path)
        w, h = original.size
        ratio = w / h
        if w > 133:
            original.resize(133, int(133 * ratio))
        # self.canvas = Canvas(self.window, height=100, width=133)
        self.image = ImageTk.PhotoImage(original)
        self.canvas.create_image(0, 0, anchor='nw', image=self.image)
        self.canvas.pack()
