import sqlite3

name = input("Введите имя базы данных: ")

connection = sqlite3.connect(name)
cursor = connection.cursor()

res = cursor.execute("""SELECT title FROM genres
WHERE id IN (SELECT genre FROM films WHERE year IN (2010, 2011))""").fetchall()

res = [res[i][0] for i in range(len(res))]
print(*res, sep="\n")