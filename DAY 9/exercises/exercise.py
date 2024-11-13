import sqlite3

connection = sqlite3.connect("mydatabase.db")

cursor_obj = connection.cursor()
cursor_obj.execute(
    "CREATE TABLE IF NOT EXISTS employees(id integer PRIMARY KEY, name text, salary real, department text, position text)"
)
# connection.commit()
# entities = [
#     [6, "Alex", 700, "R&D", "Developer"],
#     [4, "Alex", 700, "R&D", "Developer"],
#     [5, "Alex", 700, "R&D", "Developer"],
# ]

# cursor_obj.executemany(
#     "INSERT INTO employees(id, name, salary, department, position) VALUES(?, ?, ?, ?, ?)",
#     entities,
# )

# cursor_obj.execute("UPDATE employees SET name = 'Tom' where id = 5")
# connection.commit()

# cursor_obj.execute("SELECT salary, name FROM employees")
# print(cursor_obj.fetchall())
