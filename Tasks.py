def insert_elements():
    # Запрос существующего списка
    existing_list = list(map(int, input("Введите элементы существующего списка через пробел: ").split()))

    # Запрос числа элементов для вставки
    n = int(input("Введите количество элементов для вставки: "))

    # Вставка элементов
    for _ in range(n):
        index = int(input("Введите индекс для вставки: "))
        value = int(input("Введите значение для вставки: "))
        # Вставляем элемент в указанный индекс
        existing_list.insert(index, value)

    # Выводим результат
    print("Результат после вставки элементов:", existing_list)

# Вызов функции
insert_elements()
