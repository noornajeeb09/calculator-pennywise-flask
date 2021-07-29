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

# name of database
app.config['MONGO_DBNAME'] = 'pennywise-database'
# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://new-admin:DYuiP04unSez1wQb@cluster0.btlah.mongodb.net/pennywise-database?retryWrites=true&w=majority'
mongo = PyMongo(app)

# # -- Routes section --


@app.route('/')
@app.route('/index')
def index():
    # connect to appropriate "collection" in database
    #     users = mongo.db.users
    #     users.insert_one({"name":"Snigdha", "password":"blah"})
    return render_template("index.html", time=datetime.now())
# print("im in index")


@app.route('/calculate', methods=['POST', 'GET'])
def calculate():
    current_savings = int(request.form['diffname1'])
    monthly_income = int(request.form['2'])
    monthly_expenses = int(request.form['3'])
    goal_to_save = int(request.form['gifchoice'])

    monthly_amount_left = int(monthly_income - monthly_expenses)
    annual_amount_left = (monthly_amount_left * 12)
    monthly_amount_to_save = (
        goal_to_save - (current_savings + annual_amount_left))/12
    msg = "You need to save " + \
        str(round(monthly_amount_to_save)) + " dollars per month."
    print(msg)
    return render_template('calcresults.html', msg=msg)


@app.route('/signup', methods=['GET', 'POST'])
def show_signup():
    print("Im in sign up")
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        print("posted")
        users = mongo.db.users
        existing_user = users.find_one({'username': request.form['username']})

        if existing_user is None:
            users.insert_one(
                {'username': request.form['username'], 'password': request.form['password']})
            session['username'] = request.form['username']
            print("")
            return redirect(url_for('index'))
        else:
            print(existing_user)
            return redirect(url_for('login'))


@app.route('/Login', methods=['GET', 'POST'])
def Login():
    if request.method == 'GET':
        # return render_template('login.html')
        print("amin is here")
        return redirect(url_for('Login'))
    else:
        users = mongo.db.users
        login_user = users.find_one({'username': request.form['username']})

        if login_user:
            if request.form['password'] == login_user['password']:
                session['username'] = request.form['username']
                print(login_user['password'])
                return redirect(url_for('index'))
            else:
                return redirect(url_for('signup'))


@app.route('/transactions', methods = ['GET', 'POST'])
def transactions():
    collection = mongo.db.transactions
    trans = list(collection.find({}))
    print(trans)
    if request.method =='POST':
        print(request.form)
        t_name = request.form['t_name']
        t_date = request.form['t_date']
        t_amount = request.form['t_amount']
        t_type = request.form['t_type']
        collection.insert_one({'transaction_name': t_name, 'transaction_date':t_date, 'transaction_amount':t_amount, 'transaction_category': t_type})
        trans = collection.find({})
    return render_template("transactions.html", transactions=trans)
    
# @app.route('/transactions', methods=['GET', 'POST'])
# def transactions():
#     transactions = mongo.db.transactions
#     amin = transactions.find({})
#     print(list(amin))
#     # return redirect(url_for('transactions', transactions=amin))
#     return render_template("transactions.html", transactions=amin)


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
