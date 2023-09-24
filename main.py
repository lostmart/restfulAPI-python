from flask import Flask

app = Flask(__name__)


# home endpoint ('/')
@app.route("/")
def index():
    return "Hello world"


@app.route("/<name>")
def print_name(name):
    return f"hi,  {name} !"


if __name__ == "__main__":
    app.run(debug=True)
