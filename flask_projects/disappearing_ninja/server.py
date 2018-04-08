from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def display_all():
    filePath = "../static/images/home.png"
    return render_template('ninja.html', img_source = filePath)

@app.route('/ninja/<color>')
def display_color(color):
    colors_list = ["purple", "blue", "orange", "red"]
    if color not in colors_list:
        color = "notapril"

    filePath = "../static/images/" + color +".jpg"

    return render_template('ninja.html', img_source = filePath)

app.run(debug=True)