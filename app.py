# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
# from model import getImageUrlFrom
import os
from flask_pymongo import PyMongo

# -- Initialization section --
app = Flask(__name__)

#name of database
app.config['MONGO_DBNAME']= 'pennywise-database'
#URI of database
app.config['MONGO_URI']='mongodb+srv://new-admin:DYuiP04unSez1wQb@cluster0.btlah.mongodb.net/pennywise-database?retryWrites=true&w=majority'
mongo= PyMongo(app)

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    #connect to appropriate "collection" in database
    users = mongo.db.users
    users.insert_one({"name":"Snigdha", "password":"blah"})
    return render_template("index2.html", time = datetime.now())


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


