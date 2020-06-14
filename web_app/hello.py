# web_app/routes/home_routes.py
# hello.py
from flask import Blueprint

from flask import Flask
home_routes = Blueprint("home_routes", __name__)

app = Flask(__name__)

@app.route("/")
@home_routes.route("/")
def index():
    print("VISITING THE HOME PAGE")
    x = 2 + 2
    return f"Hello World! {x}"

@app.route("/about")
@home_routes.route("/about")
def about():
    print("VISITING THE ABOUT PAGE")
    return "About me"
