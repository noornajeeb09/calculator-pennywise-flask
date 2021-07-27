# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template, request, redirect, session, url_for
from datetime import datetime
# from model import getImageUrlFrom
import os
from flask_pymongo import PyMongo

# -- Initialization section --
app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

#name of database
app.config['MONGO_DBNAME']= 'pennywise-database'
#URI of database
app.config['MONGO_URI']='mongodb+srv://new-admin:DYuiP04unSez1wQb@cluster0.btlah.mongodb.net/pennywise-database?retryWrites=true&w=majority'
mongo= PyMongo(app)

# # -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    #connect to appropriate "collection" in database
#     users = mongo.db.users
#     users.insert_one({"name":"Snigdha", "password":"blah"})
        return render_template("index.html", time = datetime.now())
# print("im in index")


@app.route('/calculate', methods = ['POST', 'GET'])
def calculate():
    current_savings = int(request.form['diffname1'])
    monthly_income = int(request.form['2'])
    monthly_expenses = int(request.form['3'])
    goal_to_save = int(request.form['gifchoice'])

    monthly_amount_left = int(monthly_income - monthly_expenses) 
    annual_amount_left = (monthly_amount_left * 12)
    monthly_amount_to_save = (goal_to_save - (current_savings + annual_amount_left))/12
    
    return (str(round(monthly_amount_to_save)))



@app.route('/signup', methods = ['GET', 'POST'])
def show_signup():
    print("Im in sign up")
    if request.method =='GET':
       return render_template('signup.html')
    else:
        print("posted")
        users = mongo.db.users
        existing_user = users.find_one({'username' : request.form['username']})
 
        if existing_user is None:
           users.insert_one({'username' : request.form['username'], 'password' : request.form['password']})
           session['username'] = request.form['username']
           print("")
           return redirect(url_for('index'))
        else:
           print(existing_user)
           return redirect(url_for('login'))
           

@app.route('/')
@app.route('/login', methods = ['GET', 'POST'])
def show_login():
   if request.method =='POST':
       return render_template('login.html')
   else:
       users = mongo.db.users
       login_user = users.find_one({'username' : request.form['username']})
      
       if login_user:
           if request.form['password'] == login_user['password']:
               session['username'] = request.form['username']
               return redirect(url_for('index'))
           else:
               return redirect(url_for('signup'))
    


# @app.route('/signup', methods = ['POST', 'GET'])
# def signup():
#     name = request.form['name']
#     age = request.form['age']
#     email = request.form['email']
#     username = request.form['username']
#     password = request.form['password']
 
#     collection = mongo.db.users
#     collection.insert({'name': name, 'age': age, 'email': email, 'username': username, 'password': password })
#     return redirect('/index')

    

