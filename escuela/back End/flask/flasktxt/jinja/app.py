from random import randint, choice, sample
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)


@app.route('/hello')
def html():
    return render_template('hello.html')


@app.route("/lucky")
def random_number():
    """Example of simple dynamic template"""
    num = randint(1, 10)

    return render_template('lucky.html', lucky_num=num)


@app.route('/form')
def show_form():
    return render_template('form.html')


COMPLIMENTS = ['Cool', 'Amazing', 'Awesome', 'Great', 'Super',
               'Beatiful']  # from random import  choice and sample we are selecting the elements inside ;random is been use in /greet
#    sample is been use in /greet2


@app.route('/greet')
def greeter():
    # chooses a random complement from COMPLIMENTS
    nice_compliment = choice(COMPLIMENTS)
    username = request.args["username"]
    return render_template('greeter.html', username=username, complements=nice_compliment)


# loops

@app.route('/spell/<word>')
def spell_word(word):
    caps_word = word.upper()
    return render_template('spell.html', word=caps_word)


# greeter2
@app.route('/form2')
def greet_demo():
    return render_template('form2.html')


@app.route('/greet2')
def get_greet2():
   username = request.args['username']

   wants_compliments = request.args.get('wants_compliments')

   nice_things = sample(COMPLIMENTS, 3)  # select 3 out of COMPLIMENTS

   return render_template('greet2.html', username=username, wants_compliments=wants_compliments, complements=nice_things)

# base html template home


@app.route('/')
def home_page():
    return render_template('home.html')
