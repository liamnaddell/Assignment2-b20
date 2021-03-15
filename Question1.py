from flask import Flask
app = Flask(__name__)

def strip_nu(s: str) -> str:
    newstr = ""
    #what about special characters??
    if s.islower() and s.isalpha():
        return s.upper()
    elif s.isupper() and s.isalpha():
        return s.lower()
    else:
        for c in s:
            if not c in ['0','1','2','3','4','5','6','7','8','9']:
                newstr+=c
        return newstr

@app.route("/")
def default():
    return "Welcome to my CSCB20 Website!"

@app.route("/<x>")
def generateResponse(x):
    y = strip_nu(x)
    return "Welcome, {z}, to my CSCB20 Website!".format(z=y)
