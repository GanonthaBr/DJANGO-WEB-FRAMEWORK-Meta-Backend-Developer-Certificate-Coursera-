from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.urls import reverse

from .models import Todotask
from .forms import TaskForm

# Create your views here.

def index(request):
    tasks = Todotask.objects.all()
    task_list = {'tasks':tasks}
    return render(request, 'index.html',task_list)

def tasks(request):
    pass


def process_task(request):
    task = TaskForm()
    if request.method == 'POST':
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save()
    context = {'task':task}
    # return HttpResponse("Task has been added successfully")
    return render(request,'add_task.html',context)


def task_details(request,pk=None):
    if pk:
        task = Todotask.objects.get(pk=pk)
    else:
        task = ''
    task = {'task':task}
    return render(request,'task_details.html',task)

def delete(request,pk):
    task = Todotask.objects.get(pk=pk)
    task.delete()
    return HttpResponse('Deleted')