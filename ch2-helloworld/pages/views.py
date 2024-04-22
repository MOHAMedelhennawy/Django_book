from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homePageView(request):
    '''
    This home page and it's url is: http://127.0.0.1:8000/pages/
    '''
    return HttpResponse("Hello, world! Welcome to Home pages")

def about(request):
    '''
    This is about page and it's url is http://127.0.0.1:8000/pages/about
    '''
    return HttpResponse("Welcome in about page")