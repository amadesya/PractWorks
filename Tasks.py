try:
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))
    result = a / b
    print(f"Частное: {result}")
except ZeroDivisionError:
    print("Ошибка! Деление на 0 невозможно.")

while True:
    try:
        a = float(input("Введите число a: "))
        b = float(input("Введите число b: "))
        
        if b == 0:
            print("Число b не может быть равно 0. Пожалуйста, введите другое число b.")
            continue  # Запросить ввод числа b повторно

        result = a / b
        print(f"Частное: {result}")
        break  # Если деление прошло успешно, выйти из цикла
    except ZeroDivisionError:
        print("Ошибка! Деление на 0 невозможно.")
    finally:
        print("Операция завершена.")


import math

try:
    x = float(input("Введите число x: "))
    y = float(input("Введите число y: "))
    z = float(input("Введите число z: "))
    
    # Проверка, что знаменатель не равен нулю
    denominator = (x - y + z)**2
    if denominator == 0:
        raise ZeroDivisionError("Знаменатель не может быть равен нулю.")
    
    # Вычисление выражения
    result = math.sqrt(x + y + z) / denominator
    print(f"Результат выражения: {result}")

except ValueError:
    print("Ошибка! Введены некорректные данные.")
except ZeroDivisionError as e:
    print(f"Ошибка! {e}")


import math

try:
    x = float(input("Введите число x: "))
    y = float(input("Введите число y: "))
    z = float(input("Введите число z: "))
    
    # Проверка, что под корнем не будет отрицательного числа
    under_sqrt = x + y + z
    if under_sqrt < 0:
        raise ValueError("Под корнем отрицательное число!")
    
    # Проверка, что знаменатель не равен нулю
    denominator = (x - y + z)**2
    if denominator == 0:
        raise ZeroDivisionError("Знаменатель не может быть равен нулю.")
    
    # Вычисление выражения
    result = math.sqrt(under_sqrt) / denominator
    print(f"Результат выражения: {result}")

except ValueError as e:
    print(f"Ошибка: {e}")
except ZeroDivisionError as e:
    print(f"Ошибка: {e}")


books = {}

def add_book():
    title = input("Введите название книги: ")
    author = input("Введите имя автора: ")
    books[title] = author
    print("Книга добавлена!")

def remove_book():
    try:
        title = input("Введите название книги для удаления: ")
        del books[title]  # Попытка удалить книгу
        print(f"Книга '{title}' удалена!")
    except KeyError:
        print("Ошибка! Книга с таким названием не найдена.")

def view_books():
    if books:
        print("Список книг:")
        for title, author in books.items():
            print(f"{title} - {author}")
    else:
        print("Список книг пуст.")

while True:
    print("\nМеню:")
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Просмотр списка книг")
    print("4. Выход")
    
    choice = input("Выберите действие (1-4): ")
    
    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        view_books()
    elif choice == "4":
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор, попробуйте снова.")
