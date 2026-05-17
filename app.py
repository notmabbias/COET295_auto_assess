from flask import Flask, render_template, request
#from database import database

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('hello.html')