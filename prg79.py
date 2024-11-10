import sqlite3
#подключение
connection = sqlite3.connect('films_db.sqlite')

#создаем курсов
cursor = connection.cursor()

#исполнение запрос
result = cursor.execute(
    """
    insert into genres(id, title)
    values(12, 'Жанр12')
    
     """
    #"""delete from genres
    #where id=12"""
    #update genres
    #set title = 'мелодрама'
    #where id =3
    #update films
    #set duration = 282
    #where title = 'Аватар'
)
# подтверждаем все изменения в БД
choice = input('Вы действительно хотите удалить (Y/N):')
if choice == 'Y':
    connection.commit()

for item in result:
    print(item)

# закрытие соединения с базой
connection.close()