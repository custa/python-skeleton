from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config.from_pyfile("./settings.conf")

greetings = "Hello, world."


@auth.verify_password
def verify_password(username, password):
    if username == app.config["USER"] and \
            check_password_hash(app.config["PASSWORD"], password):
        return username


@app.route('/', methods=["GET"])
def index():
    return greetings


@auth.login_required
@app.route('/', methods=["POST"])
def post():
    global greetings
    greetings = request.form["greetings"]
    return greetings
