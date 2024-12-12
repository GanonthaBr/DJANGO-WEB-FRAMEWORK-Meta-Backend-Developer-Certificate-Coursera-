from django.shortcuts import render
from .models import *
from .form import *
from django.contrib.auth.decorators import permission_required

# Create your views here.
def home(request):
    return render(request,'index.html')

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu":menu_data}
    return render(request,'menu.html',main_data)

def menu_details(request,pk):
    if pk:
        item = Menu.objects.get(pk=pk)
        return render(request, 'menu_details.html',{"menu_item":item})
    else:
        item = []
    return render(request,'menu_details.html',{"menu_item":item})

def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
        context = {"form":form}
        return render(request,'booking.html',context)
    else:
        form = BookingForm
        booking_list = Booking.objects.all()
        data = {"booking":booking_list}
        return render(request,'booking.html',data)
    
        
def about(request):
    return render(request, 'about.html')

def category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            print('SAVED BUDDY!')
        context = {'form':form}
        return render(request,'category.html',context)
    else:
        form = CategoryForm()
        category_list = Category.objects.all()
        data = {"category":category_list}
        return render(request,'category.html',data)