import sqlite3

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# 1. Таблица студентов (уже есть)
# 2. Таблица курсов
cursor.execute('''
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    hours INTEGER
)
''')

# 3. Таблица связей (студент-курс)
cursor.execute('''
CREATE TABLE IF NOT EXISTS student_courses (
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
)
''')

courses_data = [
    (1, 'Базы данных', 72),
    (2, 'Python', 120),
    (3, 'Веб-разработка', 96)
]
cursor.executemany('INSERT INTO courses VALUES (?, ?, ?)', courses_data)

enrollments = [
    (1, 1),
    (1, 2),
    (2, 2),
    (3, 3)
]
cursor.executemany('INSERT INTO student_courses VALUES (?, ?)', enrollments)

conn.commit()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Таблицы в базе данных:")
for table in tables:
    print(table[0])

conn.close()