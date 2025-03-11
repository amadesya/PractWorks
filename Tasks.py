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

def admit_students():
    # Примерные данные (баллы за экзамены и имена абитуриентов)
    math_scores = [75, 85, 95, 70, 88, 76, 67, 90, 60, 77]  # баллы по математике
    russian_scores = [80, 82, 78, 85, 91, 70, 80, 88, 65, 73]  # баллы по русскому языку
    informatics_scores = [85, 87, 90, 76, 80, 65, 95, 70, 88, 90]  # баллы по информатике
    names = ["Иван", "Петр", "Мария", "Анна", "Елена", "Дмитрий", "Алексей", "Светлана", "Юлия", "Олег"]  # имена абитуриентов

    # Порог для зачисления (например, суммарный балл ≥ 270)
    passing_score = 270
    admitted_students = []

    # Перебираем всех абитуриентов и их баллы
    for i in range(len(names)):
        total_score = math_scores[i] + russian_scores[i] + informatics_scores[i]
        if total_score >= passing_score:
            admitted_students.append(f"{i + 1}: {names[i]}")  # индекс и имя абитуриента

    # Выводим список зачисленных
    print("Зачисленные студенты:")
    for student in admitted_students:
        print(student)

# Вызов функции
admit_students()

def work_with_dict():
    # Пример словаря
    student_scores = {
        "Иван": 90,
        "Мария": 85,
        "Петр": 88,
        "Елена": 92,
        "Алексей": 76
    }

    # Вывод списка ключей и значений
    print("Ключи словаря:", list(student_scores.keys()))
    print("Значения словаря:", list(student_scores.values()))

    # Запрос ключа у пользователя
    key = input("Введите имя абитуриента: ")
    if key in student_scores:
        print(f"Оценка {key}: {student_scores[key]}")
    else:
        print("Абитуриент не найден.")

# Вызов функции
work_with_dict()

def find_region_for_city():
    # Словарь областей и городов
    regions = {
        "Архангельская область": ["Архангельск", "Новодвинск", "Северодвинск", "Шенкурск", "Котлас"],
        "Ленинградская область": ["Санкт-Петербург", "Пушкин", "Павловск"]
    }

    # Запрос города
    city = input("Введите название города: ")

    # Поиск области
    found = False
    for region, cities in regions.items():
        if city in cities:
            print(f"{city} относится к области: {region}")
            found = True
            break

    if not found:
        print("Город не найден в списках областей.")

# Вызов функции
find_region_for_city()
