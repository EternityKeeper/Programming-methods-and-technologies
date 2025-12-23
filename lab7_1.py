import sqlite3

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    group_name TEXT
)
''')


students_data = [
    (1, 'Иван Иванов', 20, 'ИС-101'),
    (2, 'Мария Петрова', 21, 'ИС-102'),
    (3, 'Алексей Сидоров', 22, 'ИС-101')
]

cursor.executemany('INSERT INTO students VALUES (?, ?, ?, ?)', students_data)


conn.commit()


cursor.execute('SELECT * FROM students')
print("Студенты после вставки:")
for row in cursor.fetchall():
    print(row)

conn.close()