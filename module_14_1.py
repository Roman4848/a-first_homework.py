import sqlite3
import random

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')


cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

#for i in range(1, 11):
#    username = f"User {i}"
#    email = f"example{i}@gmail.com"
#    age = i * 10
#    balance = 1000
#    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",(username, email, age, balance))

cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 = 1")


cursor.execute("DELETE FROM Users WHERE id % 3 = 1")


cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")


users = cursor.fetchall()
for user in users:
    print(user)

connection.commit()
connection.close()


