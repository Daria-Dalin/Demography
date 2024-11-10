#CreateReadUpdateDdelete
#PEP 249 (connection, cursor)
import sqlite3
#подключение
connection = sqlite3.connect('films_db.sqlite')

#создаем курсов
cursor = connection.cursor()

#исполнение запрос
result = cursor.execute(
    """
    select
     title from films
    where year = ?
    and duration > ?
     """, (2010, 90)
).fetchall()



for item in result:
    print(item)

# закрытие соединения с базой
connection.close()



#select title from films where genre=(select id from genres where title=?), ('фантастика')