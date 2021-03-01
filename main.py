from flask import Flask
from libextra import strip_nu
app = Flask(__name__)

@app.route("/")
def hello():
    #strip_nu("D3A5V33E")
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)
