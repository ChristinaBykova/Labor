import sqlite3

# #подкючаемся
connection = sqlite3.connect('films_db.sqlite')
# #создание курсора
# cursor = connection.cursor()
# #запрос по "доставке" информации
#
# result = cursor.execute("""SELECT * FROM films WHERE year = ?""", (2009,)).fetchall()
# #fetchall() - доставляет все полученные элементы
# #fetchone() - доставляет только первый элемент
# #fetchmamy(N) - доставляет только N элементов
# #print(f'Найдено {len(result)} результатов')
#
# #вывод на экране
# # for item in result:
# #     print(item)
#
# #отключение
# connection.close()
# connection = sqlite3.connect('Chinook_Sqlite.sqlite')
# cursor = connection.cursor()
# result = cursor.execute("""INSERT INTO genres (id, title) VALUES(43, 'Сказки')""") #добавление поля
# изменение записей
# UPDATE имя таблицы
# SET название поля = значение
# WHERE условие
# cursor = connection.cursor()
# # result = cursor.execute("""UPDATE films SET duration = '283' WHERE title = 'Аватар'""")
# # result = cursor.execute("""DELETE from  films where year < 1985""")
# # print(result)
#
# connection.commit()
# connection.close()

connection = sqlite3.connect('shop.sqlite')
# cursor.execute("""CREATE TABLE IF NOT EXISTS users(
# userid INT PRIMARY KEY,
# fname TEXT,
# lname TEXT,
# gender TEXT);
# """)
# cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
# orderid INT PRIMARY KEY,
# date TEXT,
# userid INT,
# total INT);
# """)
cursor = connection.cursor()

# cursor.execute("""INSERT INTO users(userid, fname, lname,gender)
# VALUES(1, 'Alex', 'Petrov', 'male');
# """)
# user = (2, 'Lois', 'Bession', 'female')
# cursor.execute("""INSERT INTO users VALUES(?, ?, ?,?)""", user)
# many_users = [
#     (3, 'Anna', 'Petrova', 'female'),
#     (4, 'Roman', 'Pavlov', 'male'),
#     (5, 'Maria', 'Ivanova', 'female'),
#              ]
#
# cursor.executemany("""INSERT INTO users VALUES(?, ?, ?, ?)""", many_users)
# добавление значений в поля
# many_orders = [
#     (1, '22.06.2022', 1, 5000),
#     (2, '04.01.2022', 3, 3500),
#     (3, '08.03.2022', 4, 10000),
#
# ]
#
# cursor.executemany("""INSERT INTO orders VALUES(?, ?, ?, ?)""", many_orders)


# connection.commit() #только при записи
# result = cursor.execute("""SELECT * FROM orders""").fetchall()
# print(result)
# result = cursor.execute("""SELECT * FROM orders WHERE userid = (
#  SELECT userid FROM users WHERE fname = 'Anna')""").fetchall()
# print(result)
# result = cursor.execute("""SELECT SUM(total) FROM orders WHERE userid = (
#  SELECT userid FROM users WHERE fname = 'Anna')""").fetchall()
# print(result[0][0])
# result = cursor.execute("""SELECT users.fname, users.lname FROM orders LEFT JOIN users ON users.userid = orders.userid""").fetchall()
#
#
# for item in result:
#     print(item)

# result = cursor.execute("""SELECT fname, lname FROM users WHERE userid = (SELECT userid from orders where total = 3500)""").fetchall()
# print(result)
# maxid = cursor.execute("""SELECT MAX(userid) FROM users""").fetchone()
# print(maxid[0])


# cursor.execute(f"""INSERT INTO users (userid, fname, lname, gender) VALUES({maxid[0] + 1}, 'Sasha', 'Sidorov', 'male' )""")

cursor.execute("""UPDATE users SET fname = 'Alex' WHERE userid = (
SELECT userid FROM orders WHERE total = 5000)""")

connection.commit()#для записи
# cursor.execute(f""""drop table goods""")# удалить таблицу
connection.close()
