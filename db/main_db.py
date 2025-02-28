# main_db.py
import sqlite3
from db import queries

db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()


async def create_tables():
    if db:
        print('База данных подключена!')

    cursor.execute(queries.CREATE_TABLE_store)
    cursor.execute(queries.CREATE_TABLE_store_details)
    cursor.execute(queries.CREATE_TABLE_collection_products)


async def sql_insert_store(name_product, price, size, product_id, photo):
    cursor.execute(queries.INSERT_store_query,
                   (name_product, price, size, product_id, photo))
    db.commit()


async def sql_insert_store_details(category, product_id):
    cursor.execute(queries.INSERT_store_details_query,
                   (category, product_id))
    db.commit()


async def sql_insert_collection_products(collection, product_id):
    cursor.execute(queries.INSERT_collection_products_query,
                   (collection, product_id))
    db.commit()


def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
    select * from store s
    INNER JOIN store_details sd on s.product_id = sd.product_id
    INNER JOIN collection_products cp ON s.product_id = cp.product_id
    """).fetchall()
    conn.close()
    return products

# def fetch_all_products():
#     try:
#         conn = get_db_connection()
#         query = """
#             SELECT s.product_id, s.name_product, sd.category
#             FROM store s
#             INNER JOIN store_details sd ON s.product_id = sd.product_id
#             INNER JOIN collection_products cp ON s.product_id = cp.product_id
#         """
#         products = conn.execute(query).fetchall()
#     except Exception as e:
#         print(f"Error: {e}")
#         products = []
#     finally:
#         conn.close()
#
#     return products

def update_product_field(product_id, field_name, new_value):
    conn = get_db_connection()

    store_table = ['name_product', 'price', 'size', 'product_id', 'photo']
    store_details_table = ['category', 'product_id']


    try:
        if field_name in store_table:
            query = f'UPDATE store SET {field_name} = ? WHERE product_id = ?'
        elif field_name in store_details_table:
            query = f'UPDATE store_details SET {field_name} = ? WHERE product_id = ?'

        else:
            raise ValueError(f'Нет такого поля как {field_name}')

        conn.execute(query, (new_value, product_id))
        conn.commit()

    except sqlite3.OperationalError as error:
        print(f'Ошибка - {error}')

    finally:
        conn.close()

