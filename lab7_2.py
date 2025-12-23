import sqlite3

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

cursor.execute('UPDATE students SET group_name = ? WHERE id = ?', ('ИС-103', 2))
conn.commit()

cursor.execute('SELECT * FROM students WHERE id = 2')
updated_student = cursor.fetchone()
print(f"Обновлённая запись: {updated_student}")

conn.close()