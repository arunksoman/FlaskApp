from flask import Flask, render_template, request
import mysql.connector
import json

from flask_wtf import Form
from wtforms import TextField

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="db_flaskTest"
)

cursor = db.cursor()

app = Flask(__name__)


@app.route('/')
def hello_world(title="Flask Server"):
	a = 3
	title = "Flask"
	drop_down = {'Home': '/', 'Login': '/login', 'Admin Panel': '/admin'}
	with open('social.json') as json_file:
		data = json.load(json_file)
	return render_template('default.html', title=title,a = a, drop_down=drop_down, data=data)


@app.route('/login', methods = ['GET', 'POST'])
def login():

	return render_template('login-page.html')


if __name__ == '__main__':
   app.run(debug = True)