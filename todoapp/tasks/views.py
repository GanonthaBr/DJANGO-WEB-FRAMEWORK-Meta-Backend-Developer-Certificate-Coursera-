from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.urls import reverse
from .forms import TaskForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def tasks(request):
    pass

def addTask(request):
    app_name = 'todo'
    form = TaskForm()
    return render(request,'add_task.html',{'form':form})

def process_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            priority = form.cleaned_data['priority']
            completed = form.cleaned_data['completed']
            #save the data to db
            task = TaskForm(title=title, description=description, priority=priority, completed=completed)
            task.save()
    # return HttpResponse("Task has been added successfully")
    return HttpResponsePermanentRedirect(reverse('todo:view'))
