def test_function():
    def inner_function():
        print("Я в области видимости функции")

    inner_function # Нет возврата
inner_function # Ошибка
test_function() # Правильный вызов функици