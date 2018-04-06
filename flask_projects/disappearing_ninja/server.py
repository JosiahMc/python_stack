from flask import Flask, render_template, redirect, request
app = Flask(__name__)

colors_list = ["purple", "blue", "orange", "red"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def display_all():

    filePath = "../static/images/home.png"
    return render_template('ninja.html', img_source = filePath, colors = colors_list)

@app.route('/ninja/<color>')
def display_color(color):
    if color not in colors_list:
        color = "notapril"

    filePath = "../static/images/" + color +".jpg"
    return render_template('ninja.html', img_source = filePath, colors = colors_list)

app.run(debug=True)