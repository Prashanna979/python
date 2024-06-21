import sqlite3
# crud

conn=sqlite3.connect('college.sqlite3')
cursor =conn.cursor()

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


# def insert_students(name,email,address):
#     cursor.execute("""
#     INSERT INTO students (name,email,address)
#     VALUES (?,?,?)
# """,(name,email,address))
#     conn.commit()
#     print("data inserted successfully")

# name=input("enter name: ")
# email=input("enter email: ")
# address=input("enter address: ")
# insert_students(name,email,address)

# def show_students():
#     cursor.execute("""
#     SELECT * FROM students
# """)
#     # students=cursor.fetchall()
#     students=cursor.fetchone()
#     # students=cursor.fetchmany(2)
#     print(students)

# show_students()

# def delete(id):
#     cursor.execute("""
#     DELETE FROM students where id=?

# """,(id,))
#     conn.commit()
#     print("deleted successfully")

# delete(3)

def update(name,address,id):
    cursor.execute("""
    UPDATE students SET name=?, address=? WHERE id=?
""",(name,address,id))
    conn.commit()
    print("Updated successfully")

update('rajesh','ktm',2)