from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name="home"),
    path('about/',views.about, name="about"),
    path('projects/',views.projects, name="projects"),
    path('add_project/',views.add_project, name="add_project"),
]