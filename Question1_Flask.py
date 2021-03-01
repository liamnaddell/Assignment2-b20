from flask import Flask
app = Flask(__name__)

@app.route("/")
def default():
    return "Welcome to my CSCB20 Website!"

@app.route("/<x>")
def hello(x):
    y = generateResponse(x)
    return "Welcome, {z}, to my CSCB20 Website!".format(z=y)

if __name__ == "__Question1_Flask__":
    app.run(debug=True)

