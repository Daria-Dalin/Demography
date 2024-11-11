#class для работы с БД

import sqlite3

class DbRead:
    def __init__(self, db_name):
        if db_name == '':
            print('Введите имя базы')
            return
        try:
            #подключаемся
            self.db_name = db_name
            self.connection = sqlite3.connect(db_name)
            #создаем курсор
            self.cursor = self.connection.cursor()
            print('соединились с БД', db_name)
        except sqlite3.Error as e:

    def read_all(self, query):
        """
        :param query: запрос
        : return: результат
        """
        return self.cursor.execute(query).fetchall()

    def __del__(self):
        #закрываем соединение
        print(f'Соединение с {self.db_name} закрыто')
        self.connection.close()

db = DbRead('db_films.')
sql = """
insert into genres(id, title)
values (?, ?)
"""
result = db.read_all(sql, (25, 'Новый жанр'))

#for item in result:
  #  print(item)

class Dbwrite(DbRead):
    def __init__(self, db_name):
        if db_name == '':
            print('Введите имя базы')
            return
        super().__init__(db_name)

    def data_insert(self, insert_query, insert_data):
        try:
            self.cursor.execute(insert_query, insert_data)
            self.connection.commit()
            print('Добавлено усмпешно')
        except sqlite3.Error as e:
            print(f'Error: {e}')


    def data_delete(self, delete_query, delete_data):
        self.cursor.execute(delete_query, delete_data)
        choice = input('Действительно удалить? (Y/N):')
        if choice == 'Y':
            self.connection.commit()
            print('Y')

    def data_update(self, update_query, update_data):
        self.cursor.execute(update_data, update_query)
        self.connection.commit()
        print('обновлено')

db = Dbwrite('films_db.sqlite')
sql = """
insert into genres(id, title)
values (?, ?)"""
db.data_insert(sql, (25, 'Новый жанр'))

#delete from genres
#where id = 23
#db.data_delete(sql)

sql = """
update genres 
set title = 'western'
wehre id = ?
"""

db.data_update(sql, ('Western', 19))
