#to instal flask (pip install flask)

from flask import Flask,render_template

app=Flask(__name__)  #creating and app

@app.route('/')   #Path of the function
def home():
    return "Welcome"

@app.route('/home')
def welcome():         #function does not need a request parameter
    return "Welcome to our home"  #return doesn't need a httpresponce

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/sec')
def sec():
    return render_template('sec.html')

app.run() #run server