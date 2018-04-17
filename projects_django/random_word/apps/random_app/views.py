from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
def index ( request ):
    word = {
        "randomWord": get_random_string( length = 14 )
    }
    print 'randomWord'

    return render( request, "random_word/landing.html", word )

    # request.session['Key']