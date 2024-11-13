import sqlite3

connection = sqlite3.connect("second_db.db")

cursor_obj = connection.cursor()

cursor_obj.execute(
    "CREATE TABLE IF NOT EXISTS articles(id integer PRIMARY KEY AUTOINCREMENT, author text, name text, date datetime)"
)
connection.commit()

articles = [
    ("John", "Free", "12/12/1993"),
    ("Jim", "Into the wild", "01/12/2005"),
    ("Maxim", "Bear", "01/11/2015"),
]

cursor_obj.executemany(
    "INSERT INTO articles(author, name, date) VALUES(?, ?, ?)",
    articles,
)
connection.commit()
