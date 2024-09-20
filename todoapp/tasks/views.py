from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def tasks(request):
    pass

def addTask(request):
    return render(request,'add_task.html')

def process_task(request):
    return HttpResponse("Task has been added successfully")
