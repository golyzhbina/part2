import sqlite3

name = input("Введите имя базы данных: ")

connection = sqlite3.connect(name)
cursor = connection.cursor()

res = cursor.execute("""SELECT title FROM films
WHERE duration <= 85""").fetchall()

res = [res[i][0] for i in range(len(res))]
print(*res, sep="\n")