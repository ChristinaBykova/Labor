import csv

# with open('sq.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f, delimiter=';', quotechar='"',
#                         quoting=csv.QUOTE_MINIMAL)
#     for i in range(10):
#         writer.writerow([i, i ** 2, f'Квадрат числа {i} = {i ** 2}'])


# with open('sq.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f, delimiter=';', quotechar='"')
#     for i in reader:
#         x, y, z = i
#         print(x, y, z)

# with open('t.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f, delimiter=';', quotechar='"',
#                         quoting=csv.QUOTE_MINIMAL)
#     goods = [('Ковер', 5000), ('Зубная щетка', 200), ('Пенал', 120)]
#     for i in goods:
#         writer.writerow(i)
#         #print(i)
#
# with open('t.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f, delimiter=';', quotechar='"')
#     for i in reader:
#         x, y = i
# print(x, y)

data = [{
    'lastname': 'Петров',
    'firstname': 'Иван',
    'class_number': 9,
    'class_letter': 'А'
}, {
    'lastname': 'Иванов',
    'firstname': 'Петр',
    'class_number': 9,
    'class_letter': 'Б'
}]

with open('form.csv', 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=list(data[0].keys()),
                            delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for item in data:
        writer.writerow(item)

with open('form.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    for item in reader:
        for k, v in item.items():
            print(k, v)



