# from datetime import datetime
import faker
from random import randint, choice
import sqlite3


NUMBER_GROUPS = 3
NUMBER_STUDENTS = 30
NUMBER_TEACHERS = 4
NUMBER_GRADES = 20

SUBJECTS = ["Mathematics", "English", "History", "Computer Science", "Geography"]

def generate_fake_data() -> tuple():
    fake_data = faker.Faker()

    fake_students = []
    for _ in range(NUMBER_STUDENTS):
        fake_students.append(fake_data.name())
    
    fake_teachers = []
    for _ in range(NUMBER_TEACHERS):
        fake_teachers.append(fake_data.name())

    fake_date = []
    for _ in range(NUMBER_STUDENTS*NUMBER_GRADES):
        fake_date.append(fake_data.date_of_birth().strftime('%m-%d'))

    return fake_students, fake_teachers, fake_date


def prepare_data(students, teachers, dates) -> tuple():
    for_students = [] #!!!
    for stud in students:
        for_students.append((stud, ))

    for_groups = [] #!!!
    for stud in range(1, NUMBER_STUDENTS + 1):
        for_groups.append((randint(1, NUMBER_GROUPS), stud))

    for_teachers = [] #!!!
    for teach in teachers:
        for_teachers.append((teach, ))

    for_subjects = [] #!!!
    for subject in SUBJECTS:
        for_subjects.append((subject, randint(1, NUMBER_TEACHERS)))

    for_grades = [] #!!!
    for stud in range(1, NUMBER_STUDENTS + 1):
        for _ in range(NUMBER_GRADES):
            for_grades.append((stud, randint(1, len(SUBJECTS)), randint(1, 10), choice(dates)))

    return for_students, for_groups, for_teachers, for_subjects, for_grades


def insert_data_to_db(students, groups, teachers, subjects, grades) -> None:
    with sqlite3.connect('university_data.db') as con:

        cur = con.cursor()


        sql_to_students = """INSERT INTO students(student_name)
                               VALUES (?)"""
        cur.executemany(sql_to_students, students)


        sql_to_groups = """INSERT INTO groups(id, student_id)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_groups, groups)


        sql_to_teachers = """INSERT INTO teachers(teacher_name)
                               VALUES (?)"""
        cur.executemany(sql_to_teachers, teachers)


        sql_to_subjects = """INSERT INTO subjects(subject_name, teacher_id)
                              VALUES (?, ?)"""
        cur.executemany(sql_to_subjects, subjects)


        sql_to_grades = """INSERT INTO grades(student_id, subject_id, grade, grade_date)
                              VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_grades, grades)


        con.commit()


if __name__ == "__main__":
    students, groups, teachers, subjects, grades = prepare_data(*generate_fake_data())
    insert_data_to_db(students, groups, teachers, subjects, grades)