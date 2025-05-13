# from PIL import ImageDraw
# from PIL import ImageFont

# l = (229,43,80)
# b = (0,0,0)
# W, H = 200, 200
# RH = 50
# RW = 50

# new_image =Image.new("RGB", (W,H), l)
# new_image.save('image.png', 'PNG')

# canvas = Image.new("RGB", (W,H), b)
# draw = ImageDraw.Draw(canvas)

# draw.line((0,0,100,100), fill=l, width=1)
# draw.line((100,0,0,100), fill=l, width=1)
# canvas.save('image.png', 'PNG')

# Квадрат

# red = (191,29,52)
# green = (71,167,106)
# blue = (0,71,171)
# white = (255,255,255)
#
# draw.rectangle((0,0,50,50), fill=red)
# draw.rectangle((75,75,125,125), fill=green)
# draw.rectangle((W-RW, H-RH, W, H), fill=blue)

# Дуга
# canvas = Image.new("RGB", (W,H), b)
# draw = ImageDraw.Draw(canvas)
# draw.arc(xy=(25,50,175,200), start=30, end=270,
#          fill=blue, width=10)

# Полигон
# draw.polygon((W // 2, 0, 0, H, W, H), fill=white, outline=green)

# Эллипс
# draw.ellipse((150,0,200,50), fill=red)
# draw.ellipse((75,75,125,125), fill=green)
# draw.ellipse((0, 150, 50, H), fill=blue)

# Текст
# text = 'Python'
# canvas = Image.new("RGB", (W, H), red)
# draw = ImageDraw.Draw(canvas)
# font = ImageFont.truetype('arial.ttf', size=20)
# draw.text((10, 10), text, font=font)

# Шахматная доска
# Cells = 8 #число клеток шахматная доска
# #заполняем поле белыми квадратами
# W, H = Cells * RW, Cells * RW
# for x in range(Cells):
#     for y in range((x + 1) % 2, Cells, 2):
#         draw.rectangle((x * RW, y * RW, (x + 1) * RW - 1, (y + 1)* RW - 1), fill=white)
# canvas.save('image.png', 'PNG')

# Открыть файл
# original = Image.open('python.jpg')
# print('Формат:', original.format)
# print('Цветовая схема:', original.mode)
# W, H = original.size
# print('Размер:', original.size)
# required_height = 100# обязательно хранить с высотой 100px
# ratio = W / H
# resized = original.resize((int(required_height * ratio), required_height)) #уменьшение изображение
# resized.save('resized.jpeg')

# замена каналов
# pixels = original.load()
# for x in range(W):
#     for y in range(H):
#         r, g, b = pixels[x,y]
#         #pixels[x,y] = g, b, r
#         averaged = (r + g + b) // 3 #черно-белый
#         pixels[x,y] = averaged, averaged, averaged
#
# original.save('grayscale.jpeg')
# original.save('inverted.jpeg')

# temp = Image.open('resized.jpeg')
# print(temp.format)

# cropped_image = original.crop((300, 0, 600, 200))
# cropped_image.save('cropped.jpeg')

##
# pixels = original.load()
# for x in range(W // 2):
#     for y in range(H):
#         r, g, b = pixels[x,y]
#         #pixels[x,y] = g, b, r
#         averaged = (r + g + b) // 3 #черно-белый
#         pixels[x,y], pixels[W-x-1,y] = pixels[W-x-1,y], pixels[x,y]
# original.save('h_flipped.jpeg')
# #original.save('grayscale.jpeg')

# замента цветового типа
#
# original = Image.open('python.jpg')
# W, H = original.size
# ratio = W / H
# original = original.convert('RGB')
# # mode = original.mode
# print(mode)
# фильтры
# blur = original.filter(ImageFilter.BLUR)
# blur.save('python_blur.png')
#
# blurbox = original.filter(ImageFilter.BoxBlur(100))
# blurbox.save('python_boxblur.png')
#
# blurgauss = original.filter(ImageFilter.GaussianBlur(20))
# blurgauss.save('python_boxgauss.png')
#
# contour = original.filter(ImageFilter.CONTOUR)
# contour.save('cont.png')
#
# sharped = ImageEnhance.Sharpness(original)
# sharped_image = sharped.enhance(10.0)
# sharped_image.save('sharped.jpg')

# C:\Users\student\AppData\Local\Programs\Python\Python39\Scripts\pip.exe

# from pymorphy2 import MorphAnalyzer
# form = MorphAnalyzer().parse('вода')[0]
# for bottle in reversed(range(9)):
#     print(f'В холодильнике {bottle + 1} {form.make_agree_with_number(bottle + 1).word}')
#     print('Возьмем одну и выпьем')
#
#     if bottle % 10 == 1 and bottle != 11:
#         remain = 'Осталось'
#     else:
#         remain = 'Осталось'
#     print(f'{remain} {bottle} {form.make_agree_with_number(bottle).word}')

# Word документ
# from docx import Document
# document = Document()
# document.add_heading('Привет',4)
# document.add_paragraph('Паспорт')
# p = document.add_paragraph('Паспорт ')
# p.add_run('не забыть').bold = True
#
# document.add_paragraph('', style='List Number')
# document.add_paragraph('Знание - сила!', style='Intense Quote')
#
# table = document.add_table(rows=1, cols=2)
# header_cells = table.rows[0].cells
# header_cells[0].text = 'rtftgh'
# header_cells[1].text = 'rtftgh'
# document.save('text.docx')
