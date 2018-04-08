from flask import Flask, render_template, request, session, redirect
import random, datetime

app = Flask(__name__)
app.secret_key = "ENDANGERED GANGSTER SLOTHS"


@app.route('/')
def index():
    if not 'gold' in session:
        session['gold'] = 0
    if not 'activity' in session:
        session['activity'] = ""
    return render_template('index.html')
#all four forms will POST to this route
@app.route('/process_money', methods=['POST'])
def process_money():
    place = request.form['place']
    income = 0
    if place == 'farm':
        income += random.randint(10, 21)
    elif place == 'cave':
        income += random.randint(5, 11)
    elif place == 'house':
        income += random.randint(2, 6)
    else:
        income += random.randint(-50, 51)

    if income >= 0:
        session['activity'] += '<p class="win">Earn {} golds from {}! ({})</p>'.format(income, place, datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p"))
    else:
        session['activity'] += '<p class="lost">Entered a casino and lost {} golds... gotta know when to fold. ({})</p>'.format(income, datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p"))
    session['gold'] += income
    print income
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')
    
app.run(debug = True)
