from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProjectForm
from .models import Projects

# Create your views here.

def index(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def projects(request):
    project = Projects.objects.all()
    context = {'projects':project}
    return render(request,'projects.html',context)

def add_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Project added successfully')
    return render(request,'add_project.html',{'form':form})
