import sqlite3

conn = sqlite3.connect("api/db/test.db")

cursor = conn.cursor()

cursor.execute(
    """ CREATE TABLE products 
               (
               user_id INTEGER PRIMARY KEY AUTOINCREMENT,
               first_name text,
               last_name text,
               email text,
               password text
               )

    """
)
