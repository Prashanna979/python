import sqlite3

# crud

conn = sqlite3.connect('college.sqlite3')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        address TEXT NOT NULL
    )
""")
conn.commit()


# def insert_students():
#     cursor.execute("""
#     INSERT INTO STUDENTS (name,email,address)
#     VALUES ('ram','ram2@gmail.com','ktm')

# """)
#     conn.commit()
#     print("data inserted successfully")
# insert_students()


def insert_students(name, email, address):
    cursor.execute("""
    INSERT INTO students (name,email,address)
    VALUES (?,?,?)
""", (name, email, address))
    conn.commit()
    print("data inserted successfully")


# name=input("enter name: ")
# email=input("enter email: ")
# address=input("enter address: ")
# insert_students(name,email,address)

def show_students():
    cursor.execute("""
    SELECT * FROM students
""")
    students = cursor.fetchall()
    print(students)


show_students
