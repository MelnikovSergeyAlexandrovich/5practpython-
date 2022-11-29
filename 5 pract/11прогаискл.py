try:
    file = open('C:\\Users\\UsER\\Desktop\\python.txt', 'r')
    file.write('hi world')
except:
    print("Ошибка. Данной директории не существует. Функция write невыполнима")
