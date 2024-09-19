from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.views import View #class based view
from django.urls import reverse
from django.core.exceptions import *

from .forms import ApplicationForm
from .forms import FormLogger

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


#Path parameter
def pathview(request, name, id):
    return HttpResponse('<h1>Hi, {}! Your id is {}</h1>'.format(name, id))


#Query parameter
def qryview(request):
    name = request.GET['name'] #request.GET.get('name','default_value')
    id = request.GET['id']
    params = request.GET.dict() #Get a map of all query params as key-value pairs
    return HttpResponse('<h1>Hi, {}! Your id is {} and {}</h1>'.format(name, id,params))


#Body parameter
def showform(request): 
    return render(request,'form.html')

def getform(request): 
    if request.method == "POST": 
        id=request.POST['id'] 
        name=request.POST['name'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

#params
def get_product(request, name):
    try:
        products = {'huile':{'price':2000,'qty':2,'ingredients':'chebe, huile et more'},'pomade':{'price':4000,'qty':12,'ingredients':'pom, graisse et more'}, }
        product = products[name]['ingredients']
    except FileNotFoundError:
        raise Http404('Product not found')
    except Exception:
        raise Http404('Product not found, key misspelled')
    return HttpResponse(f'<h1>Product: {name} </h1> Ingredients are: {product}')

#class based view
class MyView(View):
    name = 'MyCosmetic Natural'
    def get(self, request):
        return HttpResponse(f'About {self.name}')
    
#regular expression
def article(request, year, month):
    url = reverse('article',args=[year,month])
    return HttpResponse(f'<h1>Article from {year} and {month}. The URL entered is: {url}')

def list_p(request,nom,id):
    url = reverse('list',args=[nom, id])
    return HttpResponse(f'Ceci est le produit {nom} qui a pour ID {id} and with URL {url}')

#form class
def apply_form(request):
    form  = ApplicationForm()
    return render(request, 'application_form.html', {'form':form})

def apply_data_process(request):
    # return HttpResponse('Submitted Successfully')
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        #check if form is valid
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            address = form.cleaned_data['address']
            position = form.cleaned_data['position']
            return HttpResponse(f'Name: {name}, Age: {age}, Address: {address}, Position: {position}')

def logger(request):
    logger_form = FormLogger()
    if request.method == 'POST':
        logger_form = FormLogger(request.POST)
        if logger_form.is_valid():
            logger_form.save()
    context = {"logger_form":logger_form}
    return render(request,'logger.html',context)


#about page

def about(request):
    about_context = {'about':'About Our website'}
    return render(request, 'about.html', about_context)


#menu page
def main(request):
    menu_context = {'menu':'Our Menu'}
    return render(request, 'menu.html', menu_context)

#booking page
def booking(request):
    booking_context = {'booking':'Booking Page'}
    return render(request, 'booking.html', booking_context)