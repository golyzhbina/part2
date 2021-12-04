import sqlite3

connection = sqlite3.connect("sql_search.py")
cursor = connection.cursor()

query = cursor.execute("""INSERT INTO teacher(first_name, last_name, start_work, birthday) VALUES""")