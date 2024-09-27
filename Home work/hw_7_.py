import sqlite3

conn = sqlite3.connect('hw.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title TEXT NOT NULL CHECK(length(product_title) <= 200),
    price REAL NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
''')


def add_products():
    products = [
        ("Жидкое мыло с запахом ванили", 50.0, 10),
        ("Мыло детское", 30.0, 15),
        ("Шампунь", 100.0, 5),
        ("Гель для душа", 80.0, 8),
        ("Крем для рук", 60.0, 12),
        ("Зубная паста", 40.0, 20),
        ("Дезодорант", 70.0, 7),
        ("Лосьон для тела", 90.0, 6),
        ("Мыло хозяйственное", 20.0, 25),
        ("Соль для ванн", 45.0, 4),
        ("Шампунь для детей", 55.0, 9),
        ("Гель для бритья", 75.0, 11),
        ("Крем для лица", 95.0, 3),
        ("Парфюм", 150.0, 2),
        ("Масло для волос", 65.0, 14),
        ("Скраб для тела", 85.0, 1)
    ]

    cursor.executemany('''
    INSERT INTO products (product_title, price, quantity)
    VALUES (?, ?, ?)
    ''', products)
    conn.commit()


def update_quantity(product_id, new_quantity):
    cursor.execute('''
    UPDATE products
    SET quantity = ?
    WHERE id = ?
    ''', (new_quantity, product_id))
    conn.commit()


def update_price(product_id, new_price):
    cursor.execute('''
    UPDATE products
    SET price = ?
    WHERE id = ?
    ''', (new_price, product_id))
    conn.commit()

def delete_product(product_id):
    cursor.execute('''
    DELETE FROM products
    WHERE id = ?
    ''', (product_id,))
    conn.commit()


def print_all_products():
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def print_cheap_products(price_limit=100, quantity_limit=5):
    cursor.execute('''
    SELECT * FROM products
    WHERE price < ? AND quantity > ?
    ''', (price_limit, quantity_limit))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

def search_products_by_title(search_term):
    cursor.execute('''
    SELECT * FROM products
    WHERE product_title LIKE ?
    ''', ('%' + search_term + '%',))

    rows = cursor.fetchall()
    for row in rows:
        print(row)



add_products()
print("Все товары:")
print_all_products()

print("\nТовары дешевле 100 сом и количество больше 5:")
print_cheap_products()

print("\nПоиск товаров по названию 'мыло':")
search_products_by_title("мыло")

update_quantity(1, 20)
update_price(1, 55.0)

print("\nПосле обновления товара с id=1:")
print_all_products()

# Удаление товара с id = 1
delete_product(1)
print("\nПосле удаления товара с id=1:")
print_all_products()

conn.close()
