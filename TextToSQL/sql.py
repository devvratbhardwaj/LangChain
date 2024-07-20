import sqlite3

## Connect to database
connection = sqlite3.connect("student.db")

## Cursor to perform CRUD operations
cursor = connection.cursor()

## Create table

table_info = """
create table STUDENT(
NAME VARCHAR(50), 
STREAM VARCHAR(30),
MARKS INT,
SUBJECT VARCHAR(20)
);
"""
cursor.execute(table_info)

## Create records
cursor.execute("insert into STUDENT values('Alpha', 'Civil Engineering', 89, 'MATHS')")
cursor.execute("insert into STUDENT values('Beta', 'Computer Engineering', 85, 'MATHS')")
cursor.execute("insert into STUDENT values('Gamma', 'Mechanical Engineering', 98, 'MATHS')")
cursor.execute("insert into STUDENT values('Delta', 'Computer Engineering', 93, 'MATHS')")
cursor.execute("insert into STUDENT values('Echo', 'Civil Engineering', 90, 'MATHS')")

## Disply the table
## Reading
data = cursor.execute('''select * from STUDENT''')
for row in data:
    print(row)

## Close the db connection
connection.commit()
connection.close()