from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
app.count = 0


@app.route('/')
def index():
    session['count'] += 1
    return render_template('home.html')

@app.route('/increment', methods=['POST'])
def increment_by_two():
    session['count'] += 1
    #only increment by 1 since reloading the page also increments by 1
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)