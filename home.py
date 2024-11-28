#to instal flask (pip install flask)

from flask import Flask,render_template,request
import sqlite3
con=sqlite3.connect('D:/Sajan/flask/data.db')
try:
    con.execute("create table details(name text,age int)")
except:
    pass

app=Flask(__name__)  #creating and app

@app.route('/')   #Path of the function
def home():
    return "Welcome"

@app.route('/home')
def welcome():         #function does not need a request parameter
    return "Welcome to our home"  #return doesn't need a httpresponce

@app.route('/index',methods=['GET','POST'])
def index():
    con=sqlite3.connect('D:/Sajan/flask/data.db')
    if request.method=='POST':
        name=request.form.get('name')
        age=request.form.get('age')
        # print(name,age)
        con.execute("insert into details(name,age)values(?,?)",(name,age))
        con.commit()
    return render_template('index.html')

@app.route('/sec')
def sec():
    return render_template('sec.html')

app.run() #run server