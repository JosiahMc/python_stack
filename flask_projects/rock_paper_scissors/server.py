from flask import Flask, render_template, redirect, session
import random
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<choice>')
def game_logic(choice):
    if 'wins' not in session:
        session['wins'] = 0
        session['ties'] = 0
        session['losses'] = 0


    rand = random.randint(0,2)         #can do random.choice(choices)
    choices = ['rock','paper','scissors']
    print "the computer picked {}".format(choices[rand])
    dictionary = {
        'rock':['ties','losses','wins'],
        'paper':['wins','ties','losses'],
        'scissors':['losses','wins','ties']
    }

    session[dictionary[choice][rand]] +=1
    # if choice == computerchoice
    print 'no wins in session yet'
    print "we made it! you picked {}...".format(choice)
    print dictionary[choice][rand]
    return redirect('/')



app.run(debug=True)
