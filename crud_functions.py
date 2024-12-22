import sqlite3


def initiate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            price INTEGER NOT NULL
        )
    ''')


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL DEFAULT 1000
        )
    ''')

    conn.commit()
    conn.close()


def add_user(username, email, age):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)
    ''', (username, email, age, 1000))
    conn.commit()
    conn.close()


def is_included(username):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Users WHERE username = ?', (username,))
    exists = cursor.fetchone()[0] > 0
    conn.close()
    return exists


def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()
    conn.close()
    return products

    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()

    conn.close()
    return products
