from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt
from django import forms

def index(request):
	return render(request, 'quotes_app/index.html')

def register(request):
    context = User.objects.basic_validator(request.POST)
    print context
    if context['status']:
        request.session['id']= context['newUser'].id
        return redirect('/success')
    else:
        for tag, error in context['errors'].items():
            messages.warning(request, error)
        return redirect('/')
    return redirect('/')

def login(request):
    context = User.objects.login_validator(request.POST)
    print context
    if context['status']:
        request.session['id'] = context['user'].id
    else:
        for tag, error in context['errors'].items():
            messages.warning(request, error)
        return redirect('/')
    return redirect('/success')

def success(request):
    me = request.session['id']
    user = User.objects.filter(id = me)
    poster = user[0]
    print(poster.first_name)
    faved = Quote.objects.filter(faved_by = me)
    not_faved = Quote.objects.exclude(faved_by = me)
    context = {
        "quotes": not_faved,
        "fave_quotes": faved,
        "name": poster.first_name
    }
    return render(request, 'quotes_app/success.html', context)

def uShow(request, id):
    if 'id' not in request.session:
        return redirect('/')
    else:
        quotes = Quote.objects.filter(posted_by = id)
        print(quotes)
        count = quotes.count()
        print(count)
        context = {
            'user': User.objects.get(id = id),
            'count': count,
            'quotes': quotes
        }

        return render(request, 'quotes_app/user.html', context)

def rev_create(request):
    if 'id' not in request.session:
        return redirect('/')
    else:
        user = User.objects.get(id = request.session['id'])
        id = user.id
        quote = Quote.objects.quote_validator(id, request.POST)
        if quote['status'] == False:
            for tag, error in quote['errors'].items():
                messages.warning(request, error)
        return redirect('/success')
def fav_btn(request):
    id = request.session['id']
    set = Quote.objects.faveQuote(id, request.POST)
    print(set)
    return redirect('/success')
def unfav_btn(request):
    id = request.session['id']
    unset = Quote.objects.unfaveQuote(id, request.POST)
    return redirect('/success')

def logout(request):
    request.session['id'] = None
    return redirect('/')


# def login(request):
# 	errors = Users.objects.login_validator(request.POST)
#     #this will end up keeping the user home showing errors 
#     if len(errors):
#         for tag, error in errors.iteritems():
#             messages.error(request, error, extra_tags=tag)
#         print 'we hit this due to invalid email'
#         return redirect( '/')
# 		#if no validation issues store username in session
# 	request.session.modified = True
#     request.session['email'] = request.POST['email']
#     print '############# we hit success'
#     return render(request,'login_app/success.html')



# def home(request):
# 	print "########################hit home route homie"
# 	me = Users.objects.get(email=request.session['email'])
# 	context= {
# 		'my_trips': Trips.objects.filter(adventures=me),
# 		'not_my_trips': Trips.objects.exclude(adventures=me)