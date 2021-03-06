from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import Emp, Dt, db, connect_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///employees_db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "abc123"

connect_db(app)

toolbar = DebugToolbarExtension(app)


@app.route('/')
def home():

    return render_template('home.html')
