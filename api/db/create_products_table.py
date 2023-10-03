import sqlite3

conn = sqlite3.connect("api/db/test.db")

cursor = conn.cursor()

cursor.execute(
    """ CREATE TABLE products 
               (
               product_id INTEGER PRIMARY KEY AUTOINCREMENT,
               price real,
               description text,
               image text
               )

    """
)
