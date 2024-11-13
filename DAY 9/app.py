from flask import Flask, render_template, request
import sqlite3

# con = sqlite3.connect("users_database.db")
# cursor_obj = con.cursor()
# cursor_obj.execute(
#     "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)"
# )
# con.commit()

app = Flask(__name__)

users_data = []


@app.route("/")
def home():
    return render_template("homepage.html")


@app.route("/signup/", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Create database connection
        con = sqlite3.connect("mydatabase.db")
        cursor_obj = con.cursor()

        # Get values from form fields
        username = request.form.get("username")
        password = request.form.get("password")

        # Append user to database
        users_data.append({"username": username, "password": password})
        cursor_obj.execute(
            "INSERT INTO users (username, password) VALUES(?,?)", [username, password]
        )
        con.commit()

        # Get all users from database
        cursor_obj.execute("SELECT * FROM users")
        users = cursor_obj.fetchall()

        return render_template("users.html", users=users)

    return render_template(
        "signup.html",
    )


if __name__ == "__main__":
    app.run(debug=True)
