import os
try:
    os.remove('C:\workspace\python\data.txt')
except:
    print("Ошибка. Файла по заданной директории не существует")


