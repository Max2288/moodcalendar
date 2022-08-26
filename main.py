import sys
from database import TextDatabaseDriver
from services import dispatcher
from PySide6 import QtQml, QtGui



if __name__ == '__main__':
    """while True:
        print('Введите команду (введите help если нужна подсказка)')
        if (x := input()) == 'exit':
            break
        if x in dispatcher:
            dispatcher[x]()
            continue
        print('Такой командный нет')
    """
    
