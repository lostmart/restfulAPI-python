import sqlite3


class DatabaseHandler:
    def __init__(self, database_name):
        self.database_name = database_name
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            # Establish DB connection
            # The option PARSE_DECLTYPES is telling SQLite to use the registered adapters and converters. If you don't include that option, it will not use what you have registered and will default to the standard data types.
            self.conn = sqlite3.connect(
                self.database_name,
                check_same_thread=False,
                detect_types=sqlite3.PARSE_DECLTYPES,
            )
            # Creating a cursor object using the cursor() method
            self.cursor = self.conn.cursor()
            # Catch any connection errors
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
            error_msg = str(e)
            return {
                "msg": "SQLite error: " + error_msg,
            }, 400

    def insert_data(self, table_name, data):
        try:
            self.cursor.execute(
                f"INSERT INTO {table_name} VALUES ( :product_id, :price, :description, :imgUrl )",
                data,
            )
            self.conn.commit()
            return "success!"
        except sqlite3.Error as e:
            return "SQLite insert error:", e

    def get_one_product(self, table_name, product_id):
        try:
            query = f"SELECT * FROM {table_name} WHERE product_id = {product_id}"
            self.cursor.execute(query)
            self.conn.commit()
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print("SQLite error:", e)
            error_msg = str(e)
            return {
                "msg": "SQLite error: " + error_msg,
            }, 400

    def get_last_product(self, table_name):
        try:
            query = f"SELECT * FROM {table_name} ORDER BY product_id DESC LIMIT 1"
            self.cursor.execute(query)
            self.conn.commit()
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print("SQLite error:", e)
            error_msg = str(e)
            return {
                "msg": "SQLite error: " + error_msg,
            }, 400
