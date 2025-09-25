import sqlite3
conn=sqlite3.connect('student_database.db')
cursor=conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS STUDENTS
                        (studentid INTEGER PRIMARY KEY AUTOINCREMENT,
                         name TEXT,
                         subject1 INTEGER,
                         subject2 INTEGER,
                         subject3 INTEGER,
                         subject4 INTEGER,
                         subject5 INTEGER,
                         totalmarks INTEGER,
                         percentage REAL,
                         grade TEXT )''')
name=input("Enter student's Name:")
subject1=int(input("Enter mark for subject1:"))
subject2=int(input("Enter mark for subject2:"))
subject3=int(input("Enter mark for subject3:"))
subject4=int(input("Enter mark for subject4:"))
subject5=int(input("Enter mark for subject5:"))

totalmarks=subject1+subject2+subject3+subject4+subject5
percentage=totalmarks/5

if percentage>=80:
    grade='A'
elif percentage>=70:
    grade='B'
elif percentage>=60:
    grade='C'
elif percentage>=40:
    grade='D'
else :
    grade='E'
    
#insert data into database
cursor.execute('''INSERT INTO students
               (name,subject1,subject2,subject3,subject4,subject5,totalmarks,percentage,grade)
               VALUES(?,?,?,?,?,?,?,?,?)''',
               (name,subject1,subject2,subject3,subject4,subject5,totalmarks,percentage,grade))
#commit changes to the database
conn.commit()

#display the entered data
cursor=conn.execute("select*from students")

for row in cursor:
    print(row)
    
#close the database connection
conn.close()
