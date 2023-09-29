import sqlite3


# DATABASE stuff ...

path = 'api/db/test.db'
conn = sqlite3.connect(path)


# Creating a cursor object using the cursor() method
cursor = conn.cursor()