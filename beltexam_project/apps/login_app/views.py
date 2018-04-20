from django.shortcuts import render, redirect
from time import strftime, gmtime

# Create your views here.
def index(request):
    print "Index route working"
    return render(request, 'login_app/index.html')

def login(request):
    pass 