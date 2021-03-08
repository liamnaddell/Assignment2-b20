from flask import Flask
app = Flask(__name__)

from flask import render_template, url_for

@app.route('/')
def hello():
    return render_template('src/base.html')
@app.route('/<page>.html')
def normal(page=None):
    return render_template('src/'+page+'.html')
