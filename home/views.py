#from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<html><body bgcolor='#FFC300'><h1>Welcome to Django World</h1></body></html>")

    