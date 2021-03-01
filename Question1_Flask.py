from flask import Flask
from libextra import strip_nu
app = Flask(__name__)

@app.route("/")
def default():
    return "Welcome to my CSCB20 Website!"

@app.route("/<x>")
def hello(x):
    y = strip_nu(x)
    return "Welcome, {z}, to my CSCB20 Website!".format(z=y)
