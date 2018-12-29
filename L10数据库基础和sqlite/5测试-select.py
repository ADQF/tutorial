import sqlite3
connect = sqlite3.connect("testsqlite.db")
cursor = connect.cursor()

cursor.execute("""
   SELECT * FROM employee;
""")
employee1 = cursor.fetchall()
print(employee1)

cursor.execute("""
   SELECT * FROM employee WHERE sex = '男';
""")

employee = cursor.fetchall()
print(employee)