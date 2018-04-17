from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    # print "double time working"
    return render(request, 'session_words/index.html')



def process(request):
    request.session['new_word'] = request.GET['new_word']
    print "process working"
    return redirect('/')


#
# def index(request):
#     # if 'counter' not in request.session:
#     request.session['counter'] = 0
#     request.session['counter'] += 1
#     request.session['random_word'] = get_random_string(length = 14)
#
#     return render(request, 'rando_app/index.html')
#
#
# def index(request):
#     if 'counter' not in request.session:
#         request.session['counter'] = 0
#     return render(request, 'surveys/index.html')
#
# # Processes form submission
#
#
# # Renders the submitted information
# def result(request):
#     return render(request, 'surveys/result.html')
#
# # Resets the session counter
# def reset(request):
#     request.session['counter'] = 0
#     return redirect('/')
