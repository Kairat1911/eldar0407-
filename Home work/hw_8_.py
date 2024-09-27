import sqlite3

conn = sqlite3.connect('hw.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
)
''')

countries = [
    ("Кыргызстан",),
    ("Германия",),
    ("Китай",)
]
cursor.executemany('INSERT INTO countries (title) VALUES (?)', countries)

cursor.execute('''
CREATE TABLE IF NOT EXISTS cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    area REAL DEFAULT 0,
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES countries (id)
)
''')

cities = [
    ("Бишкек", 300.0, 1),
    ("Ош", 250.0, 1),
    ("Берлин", 891.8, 2),
    ("Мюнхен", 310.7, 2),
    ("Шанхай", 6340.5, 3),
    ("Пекин", 16410.5, 3),
    ("Гуанчжоу", 7434.4, 3)
]
cursor.executemany('INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)', cities)

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    city_id INTEGER,
    FOREIGN KEY (city_id) REFERENCES cities (id)
)
''')

students = [
    ("Алексей", "Иванов", 1),
    ("Мария", "Петрова", 1),
    ("Сергей", "Сидоров", 2),
    ("Анна", "Кузнецова", 2),
    ("Людмила", "Смирнова", 3),
    ("Олег", "Попов", 3),
    ("Елена", "Федорова", 4),
    ("Дмитрий", "Соловьев", 4),
    ("Татьяна", "Михайлова", 5),
    ("Роман", "Зайцев", 5),
    ("Ирина", "Коваленко", 6),
    ("Артем", "Семенов", 6),
    ("Виктория", "Алексеева", 7),
    ("Константин", "Павлов", 7),
    ("Наталья", "Григорьева", 1)
]
cursor.executemany('INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)', students)

conn.commit()


def display_cities():
    cursor.execute('SELECT id, title FROM cities')
    return cursor.fetchall()

print(
    "Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

cities_list = display_cities()
for city in cities_list:
    print(f"{city[0]}: {city[1]}")

city_id = int(input("Введите id города: "))

if city_id != 0:

    cursor.execute('''
        SELECT s.first_name, s.last_name, c.title AS country_title, ci.title AS city_title, ci.area 
        FROM students s
        JOIN cities ci ON s.city_id = ci.id
        JOIN countries c ON ci.country_id = c.id
        WHERE ci.id = ?
    ''', (city_id,))

    students_in_city = cursor.fetchall()

    if students_in_city:
        print("\nУченики в выбранном городе:")
        for student in students_in_city:
            print(
                f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь: {student[4]}")
    else:
        print("Нет учеников в этом городе.")
else:
    print("Выход из программы.")

conn.close()
