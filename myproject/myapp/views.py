from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('Welcome to our Shop, Cosmetic Natural!')

def product_list(request):
    list_one = [1,2,3,]
    return HttpResponse('<h1>List of all products {} </h1>'.format(list_one))


def index(request): 
    path = request.path 
    method = request.method 
    content=''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method :{}</p></center> 
'''.format(path, method) 
    return HttpResponse(content) 

def pathview(request, name, id):
    return HttpResponse('<h1>Hi, {}! Your id is {}</h1>'.format(name, id))