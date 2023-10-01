import sqlite3


class DatabaseHandler:
    def __init__(self, database_name):
        self.database_name = database_name
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.database_name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print("SQLite error:", e)

    def disconnect(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()

    def get_data(self, table_name):
        try:
            query = f"SELECT * FROM {table_name}"
            self.cursor.execute(query)
            self.conn.commit()
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print("SQLite error:", e)

    def insert_data(self, table_name, data):
        try:
            placeholders = ", ".join(["?"] * len(data))
            query = f"INSERT INTO {table_name} VALUES ({placeholders})"
            self.cursor.execute(query, data)
            self.conn.commit()
        except sqlite3.Error as e:
            print("SQLite error:", e)