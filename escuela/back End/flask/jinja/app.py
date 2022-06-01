from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def html():
    return render_template('hello.html')
