# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def do_add():
    """Add a and b parameters."""

    a = request.args.get("a")
    b = request.args.get("b")

    result = add(a,b)
    return result