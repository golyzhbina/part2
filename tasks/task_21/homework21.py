import sqlite3

name = input("Введите название жанра: ")

connection = sqlite3.connect("music_db_1.sqlite")
cursor = connection.cursor()

res = cursor.execute(f"""SELECT Album.ArtistId, Album.title FROM Album
    WHERE AlbumId IN (SELECT Track.AlbumId FROM Track
        WHERE GenreId=(SELECT GenreId FROM Genre WHERE Name='{name}' ))""").fetchall()
res = list(map(lambda x: x[-1], sorted(res)))

print(*res, sep="\n")