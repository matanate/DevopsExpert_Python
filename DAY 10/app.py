from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=False, nullable=False)
    password = db.Column(db.String(20), unique=False, nullable=False)

    def __str__(self):
        return f"Username: {self.username}"


@app.route("/")
def home():
    return render_template("homepage.html")


@app.route("/signup/", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Get values from form fields
        username = request.form.get("username")
        password = request.form.get("password")

        # Append user to database
        profile = Profile(username=username, password=password)
        db.session.add(profile)
        db.session.commit()

        # Get all users from database
        users = Profile.query.all()

        return render_template("users.html", users=users)

    return render_template(
        "signup.html",
    )


if __name__ == "__main__":
    app.run(debug=True)
