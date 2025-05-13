# counter = 0
# while True:
#     counter += 1
#     if counter > 100:
#         break  # прирвет цикл и удейт
#     if counter % 10 == 5:
#         continue
#     # if counter == 5:
#     #     continue
#     # print(counter)
# # print('Цикл прерван')
#
# ##файл
# import os, sys

# print(os.getcwd())
# root = os.getcwd()  # начало скрипта
# #print('Мы здесь:', root)
# if not os.path.isdir('images'):# вернет правду, если имаджесть создан
#     os.mkdir('images')#создание директории (папки)
# files = os.listdir(root)
#
# images = []# пустой список файлов для изображения
# for file in files:
#     if os.path.isfile(file) and (file.endswith('.jpeg') or file.endswith('.jpg') or file.endswith('.png')):
#         images.append(file)
# #print(images)
# #os.chdir('images')#поменять каталог, от корня прыгнуть глубже
# #print('А теперь мы здесь:', os.getcwd())
# #print(type(path))
# os.chdir(root) # возвращение в корень
# #os.chdir('..') #root вверх на один уровень
# #print('Мы снова здесь', root)
# for image in images:
#     os.replace(image, 'images/' + image) #перемещение файла
# os.remove() #удаление директории, файла
# os.rename()#переименовать файл

# чтение файла
# root = os.getcwd()
#
# f = open('info.txt', 'r', encoding='utf-8')# r по умолчанию (режим открытия файла)
# print('Name file', f.name)
# print('Режим:', f.mode)
# print('Кодировка', f.encoding)
# #res = f.write(root)
# #f.read()
# res = f.read(2)
# temp = f.read(5)
# f.close()
# #print(root)
# print(res)
# print(temp)

# #
# fname = 'info.txt'
# root = os.getcwd()
# #f = open(fname, 'wr', encoding='utf-8')
# if os.path.isfile(fname):
#     file = open(fname, 'wt', encoding='utf-8')
#     print('Имя файла:', file.name, file=file)
#     print('Режим:', file.mode, file=file)
#     print('Кодировка:', file.encoding, file=file)

#     string = file.read()
#     lst = list(string)
#     summ = 0
#     for i in lst:
#         if i.isdigit():
#             summ +=int(i)
#     print(summ)
#
#     file.read(3)
#     user = file.read(4)
#     file.read(2)
#     student = file.read(7)
#
#     file.close()
#
#     print(f'A {user}-то {student}!')
#     #print(b)
# else:
#     print('НЕ существует')

# fname = 'info.txt'
# #string = ''
# list_1 = [1, 3, 5, 8, 12, 24, 37, 55, 89]
# list_2 = [2, 4, 5, 8, 14, 24, 39, 58, 89]
# set1 = set(list_1)
# set2 = set(list_2)
# temp = list(set1.intersection(set2))
#
# if os.path.isfile(fname):
#     with open(fname, 'wt', encoding='utf-8') as file:
#         print(*temp, sep=', ', file=file)

# if os.path.isfile(fname):
#    #file = open(fname, 'rt', encoding='utf-8') as file: #гарантировано будет закрыт файл
#     file = open(fname, 'rt', encoding='utf-8')
#     s = file.read()
#     # while s != '' :
#     #     string += s
#     #     s = file.readline()
#     file.close()
#     res = s.splitlines() #преобразование? строк
#     print(res)
#
#    with open (fname, 'rt', encoding='utf-8') as file:
#        s = file.read()

# import pickle
# d = {
#     'стол': 'table',
#     'стул': 'chair'
# }
# fname = 'dictinary.bin'

# with open(fname, 'wb') as file:
#     pickle.dump(d, file)

# with open(fname, 'rb') as file:
#     d = pickle.load(file)
# print(d)
