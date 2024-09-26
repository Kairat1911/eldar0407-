import sqlite3

conn = sqlite3.connect('store_products.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS categories (
    code VARCHAR(2) PRIMARY KEY,
    title VARCHAR(150) NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS store (
    store_id INTEGER PRIMARY KEY,
    title VARCHAR(100) NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    title VARCHAR(250) NOT NULL,
    category_code VARCHAR(2),
    unit_price FLOAT NOT NULL,
    stock_quantity INTEGER NOT NULL,
    store_id INTEGER,
    FOREIGN KEY (category_code) REFERENCES categories(code),
    FOREIGN KEY (store_id) REFERENCES store(store_id)
)
''')

cursor.execute("INSERT OR IGNORE INTO categories (code, title) VALUES ('FD', 'Food products')")
cursor.execute("INSERT OR IGNORE INTO store (store_id, title) VALUES (1, 'Asia')")
cursor.execute("INSERT OR IGNORE INTO store (store_id, title) VALUES (2, 'Globus')")
cursor.execute("INSERT OR IGNORE INTO store (store_id, title) VALUES (3, 'Spar')")

cursor.execute(
    "INSERT OR IGNORE INTO products (id, title, category_code, unit_price, stock_quantity, store_id) VALUES (1, 'Chocolate', 'FD', 10.5, 129, 1)")
cursor.execute(
    "INSERT OR IGNORE INTO products (id, title, category_code, unit_price, stock_quantity, store_id) VALUES (2, 'Bread', 'FD', 2.0, 50, 2)")
cursor.execute(
    "INSERT OR IGNORE INTO products (id, title, category_code, unit_price, stock_quantity, store_id) VALUES (3, 'Milk', 'FD', 1.5, 200, 1)")

conn.commit()

while True:
    print(
        "Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")

    cursor.execute("SELECT store_id, title FROM store")
    stores = cursor.fetchall()

    for store in stores:
        print(f"{store[0]}. {store[1]}")

    selected_store_id = input("Введите id магазина: ")

    if selected_store_id == '0':
        print("Выход из программы.")
        break

    cursor.execute(
        "SELECT p.title, c.title, p.unit_price, p.stock_quantity FROM products p JOIN categories c ON p.category_code = c.code WHERE p.store_id = ?",
        (selected_store_id,))
    products = cursor.fetchall()

    if products:
        for product in products:
            print(f"Название продукта: {product[0]}")
            print(f"Категория: {product[1]}")
            print(f"Цена: {product[2]}")
            print(f"Количество на складе: {product[3]}")
            print("-" * 20)
    else:
        print("Нет продуктов в выбранном магазине.")

conn.close()