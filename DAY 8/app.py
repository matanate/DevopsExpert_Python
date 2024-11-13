from flask import Flask, request, render_template, redirect

app = Flask(__name__)

pokemones = ["pikachu", "miu", "fdgdf", "dsgdf"]


@app.route("/")
def hello_world():
    return render_template("homepage.html")


@app.route("/matan/")
def hello_matan():
    return "Hello, Matan!"


@app.route("/call/<name>")
def call_name(name):
    return f"My name is {name}"


@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        return render_template("logged_in.html", username=username, password=password)

    return render_template(
        "login.html",
    )


@app.route("/pokemones/")
def show_pokemones():
    return render_template("pokemones.html", pokemones=enumerate(pokemones))


if __name__ == "__main__":
    app.run(debug=True)
