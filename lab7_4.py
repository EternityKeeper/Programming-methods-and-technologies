from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

# Таблица Student
class Student(Base):
    __tablename__ = 'students_orm'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    group_name = Column(String)

# Таблица Course
class Course(Base):
    __tablename__ = 'courses_orm'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    hours = Column(Integer)

# Создаём базу и таблицы
engine = create_engine('sqlite:///university_orm.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# CREATE
new_student1 = Student(name='Ольга Козлова', age=19, group_name='ИС-104')
new_student2 = Student(name='Дмитрий Волков', age=20, group_name='ИС-103')
session.add_all([new_student1, new_student2])
session.commit()

# READ
students = session.query(Student).all()
print("Все студенты:")
for s in students:
    print(f"{s.id}: {s.name}, {s.age} лет, группа {s.group_name}")

# UPDATE
student_to_update = session.query(Student).get(1)
if student_to_update:
    student_to_update.group_name = 'ИС-105'
    session.commit()

# DELETE
student_to_delete = session.query(Student).get(2)
if student_to_delete:
    session.delete(student_to_delete)
    session.commit()


remaining_students = session.query(Student).all()
print("Студенты после обновления и удаления:")
for s in remaining_students:
    print(f"{s.id}: {s.name}")

session.close()