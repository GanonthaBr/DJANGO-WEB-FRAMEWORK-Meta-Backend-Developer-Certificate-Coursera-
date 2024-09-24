from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Projects
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.

def index(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

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

#Details
class ProjectDetails(DetailView):
    model = Projects
    template_name = 'project.html'
    context_object_name = 'project'

#Update
class ProjectUpdate(UpdateView):
    model = Projects
    fields = ['title','description','image']
    success_url = reverse_lazy('projects')
    

#Delete
class ProjectDelete(DeleteView):
    model = Projects
    success_url = reverse_lazy('projects')
    template_name = 'projects_confirm_delete.html'
    




# def add_project(request):
#     form = ProjectForm()
#     if request.method == 'POST':
#         form = ProjectForm(request.POST)
#         if form.is_valid():
#             form.save()
#             message = {'success':'Added with success'}
#             return render(request,'projects.html',message)
#     return render(request,'add_project.html',{'form':form})
