import sqlite3

class Database:
    def __init__(self, path):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS reviews (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,   
                    name TEXT,
                    phone_number TEXT,
                    rate INTEGER,
                    extra_comments TEXT
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS store (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name_product TEXT,
                    size TEXT,
                    price TEXT,
                    photo TEXT,
                    product TEXT
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products_details (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    productid INTEGER,
                    category TEXT,
                    infoproduct TEXT
                )
            """)
            conn.commit()

    def add_review(self, data: dict):
        print(data)
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO reviews (name, phone_number, rate, extra_comments) VALUES (?, ?, ?, ?)
            """,
            (data['name'], data['phone_number'], data['rate'], data['extra_comments'])
            )
            conn.commit()



