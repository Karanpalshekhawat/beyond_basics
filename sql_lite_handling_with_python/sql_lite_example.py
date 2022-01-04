"""
Handling sqlite
"""

import sqlite3

from employee import employee

conn = sqlite3.connect('employee.db')
c = conn.cursor()

# c.execute("""CREATE TABLE employees(
#     first  text,
#     last text,
#     pay integer
#     )""")

# c.execute("INSERT INTO employees VALUES ('KARAN', 'SHEKHAWAT', 1000)")


emp1 = employee("Komal", "Rathore", 3000)
emp2 = employee("John", "dev", 5000)

"""Bad practice as it is vulnerable to SQL injection attack"""
c.execute("INSERT INTO employees VALUES ({}, {}, {})".format(emp1.name, emp1.last, emp1.pay))

c.execute("SELECT * FROM employees")
print(c.fetchall())

# c.execute("INSERT INTO employees VALUES ('KARAN', 'SHEKHAWAT', 1000)")
conn.commit()  # it will update the database whenever it is used
conn.close()
