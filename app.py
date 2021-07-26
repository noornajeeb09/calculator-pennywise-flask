# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
# from model import getImageUrlFrom
import os

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())

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

