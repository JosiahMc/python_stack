from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'password'

# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"

   session['name'] = request.form['name']
   session['student_id'] = request.form['student_id']
   session['email'] = request.form['email']
   #This will then route us to the /show page to show session data
   return redirect('/show')
@app.route('/show')
def show_user():
  return render_template('user.html')


app.run(debug=True) 
