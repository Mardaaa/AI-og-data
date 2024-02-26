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



