try:
    dict = {"first": "key",
            "second": "key"}
    dict.items(3)
except:
    print("Ошибка. Данной пары в словаре не существует")