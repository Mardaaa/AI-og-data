import sqlite3
from sqlite3 import Error

# Opret connection
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

# Create database file
connection = create_connection("school.db")

# Function to execute queries
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

create_students_table = """
CREATE TABLE IF NOT EXISTS Students (
student_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
major TEXT NOT NULL

);
"""

create_courses_table = """
CREATE TABLE IF NOT EXISTS Courses (
course_id INTEGER PRIMARY KEY AUTOINCREMENT,
course_name TEXT NOT NULL,
instructor TEXT NOT NULL

);
"""

execute_query(connection, create_students_table)
execute_query(connection, create_courses_table)

# Create records in Students table
create_students = """
INSERT INTO
    Students (student_id, name, major)
VALUES
    (01, 'Martin', 'AI'),
    (02, 'Victor', 'AI'),
    (03, 'Bob', 'Computer science'),
    (04, 'Hans', 'Medicin'),
    (05, 'Joe', 'Matematik');
"""
# execute_query(connection, create_students)

# Create records in Courses table
create_courses = """
INSERT INTO
    Courses (course_id, course_name, instructor)
VALUES
    (1, 'AI og data', 'Jesper Jensen'),
    (2, 'AI udvikling', 'Andreas Møgelmose'),
    (3, 'Matematik','Morten Rasmussen'),
    (4, 'Introduktion til AI','Lasse Østergaard'),
    (5, 'PBL','Søren');

"""
# execute_query(connection, create_courses)

# Create enrollments table
create_enrollments_table = """
CREATE TABLE IF NOT EXISTS Enrollments (
enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
student_id INTEGER NOT NULL,
course_id INTEGER NOT NULL,
FOREIGN KEY (student_id) REFERENCES Students (student_id)
FOREIGN KEY (course_id) REFERENCES Courses (course_id)

);
"""
execute_query(connection, create_enrollments_table)

# Create records in enrollements table
create_enrollment = """
INSERT INTO
    Enrollments (enrollment_id, student_id, course_id)
VALUES
    (1, 1, 3),
    (2, 2, 2),
    (3, 3, 5),
    (4, 4, 1),
    (5, 5, 4),
    (6, 1, 2),
    (7, 2, 2),
    (8, 3, 1),
    (9, 1, 1),
    (10, 2, 1);
"""
# execute_query(connection, create_enrollment)


# Forespørgsler
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

#1 Vælger alle kurser som en specific studerende er tilmeldt
select_course = """
SELECT Students.name, Courses.course_name
FROM Enrollments
INNER JOIN Students ON Enrollments.student_id = Students.student_id
INNER JOIN Courses ON Enrollments.course_id = Courses.course_id
WHERE Enrollments.student_id = 1
"""

students = execute_read_query(connection, select_course)

if students is not None:
    for student in students:
        print(student)
else:
    print("No courses found for the given student")

#2 Vælger alle studerende der er tilmeldt et specifikt kursus.
select_students = """
SELECT Courses.course_name, Students.name
FROM Enrollments
INNER JOIN Courses ON Enrollments.course_id = Courses.course_id
INNER JOIN Students ON Enrollments.student_id = Students.student_id
WHERE Enrollments.course_id = 1
"""

courses = execute_read_query(connection, select_students)

if courses is not None:
    for course in courses:
        print(course)
else:
    print("No students found for the given course")
