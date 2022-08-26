import datetime
from xml.dom import ValidationErr

from database import TextDatabaseDriver


def help():
    print(
        """
        set - Отметить настроение
        get - Посмотреть историю отметок
        exit - Выход
        """
    )

def set(mood):
    date = datetime.datetime.now().date()
    day = date.strftime('%d.%m.%Y')
    db = TextDatabaseDriver()
    mood_list = db.db_read()
    if day in mood_list:
        raise AssertionError('exists error')
    mood_list[day] = mood
    db.db_write(mood_list)

def get():
    db = TextDatabaseDriver()
    mood_list = db.db_read()
    for day in mood_list:
        day_print_format = 'Day: %s, Mood: %s'
        return (day_print_format % (day, mood_list[day]))    

dispatcher = {
    'help': help,
    'set': set,
    'get' : get
}

