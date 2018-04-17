from django.shortcuts import render, redirect
from time import strftime
import random

def index(req):
    if 'gold' not in req.session:
        req.session['gold'] = 0
    if 'activity_log' not in req.session:
        req.session['activity_log'] = []
    context = {
        'gold': req.session['gold'],
        'activity_log': req.session['activity_log'],
    }
    return render(req, 'gold_app/index.html', context)

def process_money(req):
    print "This route is firing"
    print req.POST["place"]
    place = req.POST["place"]
    if place == "farm":
        number = random.randrange(10, 21)
    elif place == "cave":
        number = random.randrange(5, 11)
    elif place == "house":
        number = random.randrange(2, 6)
    elif place == "casino":
        number = random.randrange(-50, 51)
    
    req.session['time'] = strftime("%Y-%m-%d %H:%M %p")
    req.session['gold'] += number
    req.session['amount'] = number
    req.session['color'] = 'gold'
    req.session['word'] = 'earned'
    req.session['building'] = place
    if number < 0:
        print "you hit negative numbers"
        req.session['color'] = 'red'
        req.session['word'] = 'lost'
        req.session['building'] = 'casino'
    else:
        req.session['color'] = 'gold'
        req.session['word'] = 'earned'
        req.session['building'] = 'casino'
       
    dic = {
        'time': req.session['time'],
        'amount': req.session['amount'],
        'color': req.session['color'],
        'word': req.session['word'],
        'building': req.session['building'],
    }
    req.session['activity_log'].append(dic)

    return redirect('/')

def reset(req):
    req.session.pop('gold')
    req.session.pop('activity_log')
    return redirect('/')