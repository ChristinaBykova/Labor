from lib import Okno

if __name__ == '__main__':
    app = Okno()
#
# # s = Special()
# # print(s + 1)
# # print(1 + s)
# # s += 1
# # print(s)
#
# # t = Time(45, 28)
# # print(t.info())
#
# # t1 = Time(10, 70)
# # t2 = Time(10, 30)
# # t3 = [t1, t2]
# # #t3 = t1 + t2
# # print(t3.__repr__())
#
# r1 = Rectangle(90, 20)
# r2 = Rectangle(10, 70)
#
# print(r1 >= r2)

# from tkinter import *  # GUI
# from PIL import Image, ImageTk
#
# status = False
#
# class Okno:
#     def __init__(self):
#         self.window = Tk()  # Инициализация GUI
#         self.window.title('Добро пожалуйста в Tkinter')
#         self.window.geometry('800x600')
#         self.window.resizable(False, True)
#         self.lbl = Label(self.window, text='Ярык')
#         self.lbl.pack()
#         self.canvas = Canvas(self.window, height=100, width=133)
#         self.image = ImageTk.PhotoImage(Image.open('images\chvetok.jpg'))
#         self.canvas.create_image(0, 0, anchor='nw', image=self.image)
#         self.canvas.pack()
#         self.btn = Button(self.window, text='Нажми на кнопку - получишь результат!', command=self.click)
#         self.btn.pack()
#
#         self.window.mainloop()
#
#     def click(self):
#         #self.canvas = Canvas(self.window, height=100, width=133)
#         self.image = ImageTk.PhotoImage(Image.open('images\yand.jpg'))
#         self.canvas.create_image(0, 0, anchor='nw', image=self.image)
#         self.canvas.pack()


# global status
# if not status:
#     lbl['text'] = 'Результат!'
#     lbl['background'] = '#B00000'
#     btn['text'] = 'Результат!'
#     btn['background'] = '#FF4D00'
# else:
#     lbl['text'] = 'Результат!'
#     lbl['background'] = window.cget('bg')
#     btn['text'] = 'Результат!'
#     btn['background'] = window.cget('bg')
# status = not status  # инверсия

#
# window = Tk()  # Инициализация GUI
# window.title('Добро пожалуйста в Tkinter')
# window.geometry('800x600')
# window.resizable(False, True)
# lbl = Label(window, text='Ярык')
# lbl.pack()
# # canvas = Canvas(window, height=100, width=133)
# # image = ImageTk.PhotoImage(Image.open('images\chvetok.jpg.jpg'))
# # canvas.create_image(0, 0, anchor='nw', image=image)
# # canvas.pack()
# btn = Button(window, text='Нажми на кнопку - получишь результат!', command=click)
# btn.pack()
#
# window.mainloop()
