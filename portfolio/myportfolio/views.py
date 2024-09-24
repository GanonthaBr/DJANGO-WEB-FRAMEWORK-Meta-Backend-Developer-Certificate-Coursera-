from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Projects
from django.views.generic.edit import CreateView

# Create your views here.
class ProjectCreate(CreateView):
    model = Projects
    fields = ['title','description','image']
    success_url = reverse_lazy('projects')




def index(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def projects(request):
    project = Projects.objects.all()
    context = {'projects':project}
    return render(request,'projects.html',context)

# def add_project(request):
#     form = ProjectForm()
#     if request.method == 'POST':
#         form = ProjectForm(request.POST)
#         if form.is_valid():
#             form.save()
#             message = {'success':'Added with success'}
#             return render(request,'projects.html',message)
#     return render(request,'add_project.html',{'form':form})
