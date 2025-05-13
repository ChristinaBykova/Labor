import os
from tkinter import CENTER, LEFT, Button, NW, N  # подключаем элементы
from tkinter import filedialog, Tk, PhotoImage, Label, Canvas, X, Entry  # для выбора файла(картинки)
from PIL import Image, ImageTk, ImageFilter, ImageEnhance  # для обработки изображения
from datetime import datetime


class App:
    def __init__(self):
        self.image = None
        self.orig = None
        self.time_to_show = None
        self.h = None
        self.w = None
        self.name = 'Санкт-Петербург'
        self.window = Tk()  # создание окна
        self.window.title('Карта мира')
        self.window.geometry('800x600')
        self.window.resizable(False, False)
        # self.window.iconphoto(False, PhotoImage(file='love.png'))
        self.apikey = '40d1649f-0493-4b70-98ba-98533de7710b'
        self.geocoder_request = f'http://geocode-maps.yandex.ru/1.x/?apikey={self.apikey}&geocode={self.name}&kind=metro&format=json'
        self.place = Entry(font=('Verdana', 16))
        self.place.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)
        self.label = Label(text='Карта мира', background='#DDADAF', foreground='#BC987E',
                           font=('Verdana', 32))
        self.label.pack(fill=X, pady=5)
        self.canvas = Canvas(bg='white', width=600, height=400)
        self.canvas.pack(anchor=CENTER, pady=20)
        self.load = Button(text='Найти', command=self.open)
        self.load.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)
        # self.blur = Button(text='Размыть', command=self.blur)
        # self.blur.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)
        # self.sharp = Button(text='Резкость', command=self.sharp)
        # self.sharp.pack(anchor=N, side=LEFT, padx=5, fill=X, expand=True)
        self.dtime = Label(background='#BDECB6', foreground='#FF2400', font=('Verdana', 26))
        self.dtime.place(x=310, y=530)
        self.cwd = os.getcwd()
        # self.image = None  # заглушка
        # self.orig = Image.new('RGB', (600, 400), (255, 255, 255))
        self.show_time()
        self.window.mainloop()

    def open(self):
        try:
            fullpath = filedialog.askopenfilename(title='Выбор картинки',
                                                  initialdir=self.cwd,
                                                  filetypes=(
                                                      ('GIF', '*.gif'),
                                                      ('PNG', '*.png'),
                                                      ('JPG', '*.jpg'),
                                                  )
                                                  )
            self.orig = Image.open(fullpath)
            self.w, self.h = self.orig.size
            mode = self.orig.mode
            if mode == 'P':
                self.orig = self.orig.convert('RGB')
            if self.w > 600:
                ratio = self.w / 600
                self.orig = self.orig.resize((600, int(self.h / ratio)))
            self.image = ImageTk.PhotoImage(self.orig)
            self.canvas.create_image(0, 0, anchor=NW, image=self.image)
        except AttributeError:
            self.image = ImageTk.PhotoImage(self.orig)
            self.canvas.create_image(0, 0, anchor=NW, image=self.image)

    # def blur(self):
    #     blur_image = self.orig.filter(ImageFilter.BLUR)
    #     self.image = ImageTk.PhotoImage(blur_image)
    #     self.canvas.create_image(0, 0, anchor=NW, image=self.image)

    # def sharp(self):
    #     sharper = ImageEnhance.Sharpness(self.orig)
    #     sharp_img = sharper.enhance(5.0)
    #     self.image = ImageTk.PhotoImage(sharp_img)
    #     self.canvas.create_image(0, 0, anchor=NW, image=self.image)

    def show_time(self):
        self.time_to_show = datetime.time(datetime.now()).strftime("%H:%M:%S")
        self.dtime['text'] = self.time_to_show
        self.dtime.after(1000, self.show_time)  # after - будет оформление информации через какое количество секунд


if __name__ == '__main__':
    app = App()  # пустое окно
