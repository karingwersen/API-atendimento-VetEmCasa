from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/adeus")
def adeus_mundo():
    return "adeus, mundo"