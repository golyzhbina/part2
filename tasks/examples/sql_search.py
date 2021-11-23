import sqlite3

connection = sqlite3.connect("../task_19_20_22_23/films_1.sqlite")
cursor = connection.cursor()
# result = cursor.execute("""select * from films
# where title like '%?'""").fetchmany(10)

# result1 = cursor.execute(""""INSERT INTO films(id, title, year, genre, duration)
# VALUES (18003, 'Консультация по физике 3', 2021, 1, 45)""")

# connection.commit()

id_field = input("Введите id: ")
result1 = cursor.execute(f"""INSERT INTO films(id, title, year, genre, duration) 
VALUES ({id_field}, 'Консультация по физике 3', 2021, 1, 45)""")

connection.commit()
