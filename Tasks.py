# Запрос строки у пользователя
user_input = input("Введите строку: ")

# 1. Выводим строку на экран 5 раз, не используя циклы
print(user_input)
print(user_input)
print(user_input)
print(user_input)
print(user_input)

# 2. Выводим длину строки и каждый символ строки с указанием его индекса
print(f"Длина строки: {len(user_input)}")
for i, char in enumerate(user_input):
    print(f"Индекс {i}: {char}")

# 3. Выводим каждый второй символ строки на экран с указанием его позиции
for i in range(1, len(user_input), 2):  # начиная с индекса 1 (второй символ)
    print(f"Позиция {i+1}: {user_input[i]}")

# Запрос строки и двух чисел
user_input = input("Введите строку: ")
start_pos = int(input("Введите начальную позицию: ")) - 1  # корректируем на 0-based индекс
end_pos = int(input("Введите конечную позицию: "))  # в Python срезы включают конец

# Выводим все символы в указанном диапазоне
print(f"Символы в диапазоне: {user_input[start_pos:end_pos]}")

# Запрос строки
user_input = input("Введите строку: ")

# Изменяем первый и последний символ на '#'
if len(user_input) > 1:
    user_input = "#" + user_input[1:-1] + "#"
elif len(user_input) == 1:
    user_input = "#"

# Выводим измененную строку
print(f"Измененная строка: {user_input}")

# Запрос строки
user_input = input("Введите строку: ")

# Проверяем, состоит ли строка только из цифр, букв или и того, и другого
if user_input.isdigit():
    print("Строка состоит только из цифр.")
elif user_input.isalpha():
    if user_input.islower():
        print("Строка состоит только из строчных букв.")
    elif user_input.isupper():
        print("Строка состоит только из прописных букв.")
    else:
        print("Строка состоит только из букв.")
elif user_input.isalnum():
    print("Строка состоит только из цифр и букв.")
else:
    print("Строка содержит символы, не относящиеся ни к цифрам, ни к буквам.")


# Запрос строки
user_input = input("Введите строку: ")

# Разделяем строку на подстроки по пробелу
words = user_input.split()

# Объединяем слова через запятую
result = ', '.join(words)

# Выводим результат
print(f"Результат: {result}")

# Запрос двух строк
first_string = input("Введите первую строку: ")
second_string = input("Введите вторую строку: ")

# Находим количество вхождений первой строки во второй
count = 0
positions = []

pos = second_string.find(first_string)
while pos != -1:
    positions.append(pos + 1)  # учитываем, что индексы с 1
    count += 1
    pos = second_string.find(first_string, pos + 1)

# Выводим количество и позиции
print(f"Первая строка встречается {count} раз(а). Позиции: {', '.join(map(str, positions))}")

# Запрос слова у пользователя
word = input("Введите слово: ").lower()

# Проверка на палиндром
if word == word[::-1]:
    print("Это палиндром.")
else:
    print("Это не палиндром.")


# Запрос строки
user_input = input("Введите строку: ")

# Заменяем все двойные пробелы на одинарные
user_input = ' '.join(user_input.split())

# Выводим результат
print(f"Результат: {user_input}")


# Запрос вопроса и ответа
correct_answer = "Питон"  # Задайте правильный ответ
user_answer = input("Ответьте на вопрос: ").strip().lower()

# Проверка на правильность ответа
if user_answer == correct_answer.lower():
    print("Правильный ответ.")
else:
    print("Неправильный ответ.")
