from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    content = '<h1>Hello World, title</h1> \
                <p>I am Bruno</p> \
                <h2>Title 2</h2> \
'
    return HttpResponse(content)

def home(request):
    return HttpResponse('Welcome to our Shop, Cosmetic Natural!')