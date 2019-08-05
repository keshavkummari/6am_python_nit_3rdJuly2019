"""
Python MySQL Database Access:
*****************************
The Python standard for database interfaces is the Python DB-API.
Most Python database interfaces adhere to this standard.

You can choose the right database for your application.
Python Database API supports a wide range of database servers such as :

1. GadFly
2. mSQL
3. MySQL
4. PostgreSQL
5. Microsoft SQL Server 2000
6. Informix
7. Interbase
8. Oracle
9. Sybase
10. mariadb

Windows|LInux|Unix : DB 
"""


"""
Python Database Interfaces and APIs .
You must download a separate DB API module for each database you need to access.
For example, if you need to access an Oracle database as well as a MySQL database,
you must download both the Oracle and the MySQL database modules.

The DB API provides a minimal standard for working with databases using
Python structures and syntax wherever possible.

This API includes the following:

1. Importing the API module.
2. Acquiring a connection with the database.
3. Issuing SQL statements and stored procedures.
4. Closing the connection
"""

"""
-----------------------------------------------------------
What is MySQLdb?
****************
MySQLdb is an interface for connecting to a MySQL database server from Python.
It implements the Python Database API v2.0 and is built on top of the MySQL C API.

-----------------------------------------------------------
How do I Install MySQLdb?
*************************
Before proceeding, you make sure you have MySQLdb installed on your machine.
Just type the following in your Python script and execute it:

#!/usr/bin/python
import MySQLdb

Note: If it produces the following result,
then it means MySQLdb module is not installed:

To install MySQLdb module, download it from MySQLdb website:

Go to browser and serach for this package and download and move it to linux server:

MySQL-python-1.2.2.tar.gz

$ tar -xvf MySQL-python-1.2.2.tar

$ cd MySQL-python-1.2.2

$ python setup.py build

$ python setup.py install

Note: Make sure you have root privilege to install above module.

#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","pythonawsdevops","pythonawsdevops")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Database version : %s " % data)

# disconnect from server
db.close()

"""

#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","redhat","HADOOP" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS emp")

# Create table as per requirement
sql = """CREATE TABLE emp (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         Gender CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

# disconnect from server
db.close()
