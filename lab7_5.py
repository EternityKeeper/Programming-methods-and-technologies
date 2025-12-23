import psycopg2
from psycopg2 import sql

try:
    conn = psycopg2.connect(
        dbname="testdb",
        user="postgres",
        password="2005",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    print("Подключение к PostgreSQL успешно!")
except Exception as e:
    print(f"Ошибка подключения: {e}")
    exit()

# 2. Создаём таблицу books
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100),
    year INTEGER
)
''')
conn.commit()

# 3. Вставляем данные
books_data = [
    ('Война и мир', 'Лев Толстой', 1869),
    ('Мастер и Маргарита', 'Михаил Булгаков', 1966),
    ('1984', 'Джордж Оруэлл', 1949)
]

for book in books_data:
    cursor.execute(
        "INSERT INTO books (title, author, year) VALUES (%s, %s, %s)",
        book
    )
conn.commit()

# 4. Выбираем книги после 1900 года
cursor.execute("SELECT * FROM books WHERE year > 1900")
print("Книги после 1900 года:")
for row in cursor.fetchall():
    print(row)

# 5. Обновляем год у книги
cursor.execute("UPDATE books SET year = 1950 WHERE title = 'Мастер и Маргарита'")
conn.commit()

# 6. Удаляем книгу по id
cursor.execute("DELETE FROM books WHERE id = 3")
conn.commit()

# 7. Финальный вывод
cursor.execute("SELECT * FROM books")
print("Все книги в базе:")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()