from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homePageView(request):
    '''
    This home page and it's url is: http://127.0.0.1:8000/pages/
    '''
    # return HttpResponse("Hello, world! Welcome to Home pages")
    context = {
        'name': 'mohammed',
        'var'
        'age': 22,
        'sentence': 'i need to cut The rest of the',
        'len': 'What is the length of this sentence?',
        'cuut': 'Cut All The Space Here!',
        'fileSize': 43243434234,
        }
    return render(request, 'pages/index.html', context)

def about(request):
    '''
    This is about page and it's url is http://127.0.0.1:8000/pages/about
    '''
    # return HttpResponse("Welcome in about page")
    return render(request, 'pages/about.html', context={'name': "mohammed"})