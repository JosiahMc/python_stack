from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission

@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"

   name = request.form['name']
   student_id = request.form['student_id']
   email = request.form['email']

   print request.form
   # redirects back to the '/' route
   return redirect('/')
app.run(debug=True) # run our server
