import sqlite3
# crud

conn=sqlite3.connect('company.sqlite3')
cursor =conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employee(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        dep TEXT NOT NULL,
        salary INTEGER NOT NULL
    )
""")
conn.commit()



def insert_students(name,email,dep,salary):
    cursor.execute("""
    INSERT INTO employee (name,email,dep,salary)
    VALUES (?,?,?,?)
""",(name,email,dep,salary))
    conn.commit()
    print("data inserted successfully")

name=input("enter name: ")
email=input("enter email: ")
dep=input("enter department: ")
salary=input("enter salary: ")
insert_students(name,email,dep,salary)

# def show_employee():
#     cursor.execute("""
#     SELECT * FROM employee
# """)
#     employee=cursor.fetchall()
#     print(employee)

# show_employee()

# def delete(id):
#     cursor.execute("""
#     DELETE FROM employee where id=?

# """,(id,))
#     conn.commit()
#     print("deleted successfully")

# delete(1)

def update(name,dep,salary,id):
    cursor.execute("""
    UPDATE employee SET name=?, dep=?, salary=? WHERE id=?
""",(name,dep,salary,id))
    conn.commit()
    print("Updated successfully")

update('rajesh','R&D',50000,2)