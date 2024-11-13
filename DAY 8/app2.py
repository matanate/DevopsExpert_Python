from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, !"


@app.route("/matan/")
def hello_matan():
    return "Hello, Matan!"


if __name__ == "__main__":
    app.run(port=5001)
