try:
   list = []
   a = int(input("Введите число: "))
   b = int(input("Введите число: "))
   list.append(a)
   list.append(b)
   list.pop(1)
except :
    print("Ошибка. В листе не сущесвует второго значения. Функция pop не выполнима")
else:
    print("Awesome! Функция pop сработала! ")
finally:
    print("Конец работы программы.")