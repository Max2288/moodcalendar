import json
import sqlite3

def get_database_driver_name(driver):
    print(driver.name)

class DatabaseDriver:
    name = "BaseDriver" 
    def db_write(self, dict):
        raise NotImplementedError('Переопределите метод db_write')

    def db_read(self) -> dict:
        raise NotImplementedError('Переопределите метод db_read')

    def get_name(self):
        print(self.name)




class TextDatabaseDriver(DatabaseDriver):
    name = "TextDriver"

    def db_write(self, new_dict):
        with open('database.txt', 'w') as file:
            file.write(json.dumps(new_dict))

    def db_read(self) -> dict:
        try:
            with open('database.txt', 'r') as file:
                data = json.loads(file.read())
                return data
        except FileNotFoundError:
            return dict()
             


class SQLiteDatabaseDriver(DatabaseDriver):
    def db_read(self) -> dict:
        # connect = sqlite3.connect('db.sqlite3')
        # cursor = connect.cursor()
        # cursor.execute('SELECT * FROM mood_list')
        # data_list = cursor.fetchall()
        # data = dict()
        # for item in data_list:
        #     data[item[1]] = item[2]
        # cursor.close()
        # connect.close()
        # return data
        pass

    def db_write(self, dict):
        connect = sqlite3.connect('db.sqlite3')
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM mood_list')
        data_list=cursor.fetchall()
        for item in data_list:
            print(item)
        cursor.close()
        connect.close()
        pass


# dumps = словарь в строчку
# loads = из сторчки в словарь

# dumps {1: '1', 2: '2'} => "{1: '1', 2: '2'}"
# loads {1: '1', 2: '2'} <= "{1: '1', 2: '2'}"