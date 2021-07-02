# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import madlibs


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results', methods = ['GET', 'POST'])
def results():
    if request.method=='POST':
        print(request.form)
        noun = request.form['noun']
        verb = request.form['verb']
        adjective = request.form['adjective']
        adverb = request.form['adverb']
        flasklibs = madlibs(noun, verb, adjective, adverb)
        return render_template("result.html", noun = noun, verb = verb, adjective = adjective, adverb = adverb, flasklibs = flasklibs)
    else:
        return "<h2>dique '404 error'...</h2>"