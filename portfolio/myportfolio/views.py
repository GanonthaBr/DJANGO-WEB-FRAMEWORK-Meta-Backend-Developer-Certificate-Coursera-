from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Projects
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

# Create your views here.

def index(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

# def projects(request):
#     project = Projects.objects.all()
#     context = {'projects':project}
#     return render(request,'projects.html',context)


#Create
class ProjectCreate(CreateView):
    model = Projects
    fields = ['title','description','image']
    success_url = reverse_lazy('projects')      #redirect after succces
    extra_context = {'projects':Projects.objects.all()}
    template_name = 'projects_form.html'

#Retrieve
class ProjectRetrieve(ListView):
    model = Projects
    template_name = 'projects.html'
    context_object_name = 'projects'





# def add_project(request):
#     form = ProjectForm()
#     if request.method == 'POST':
#         form = ProjectForm(request.POST)
#         if form.is_valid():
#             form.save()
#             message = {'success':'Added with success'}
#             return render(request,'projects.html',message)
#     return render(request,'add_project.html',{'form':form})
