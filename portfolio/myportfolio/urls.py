from django.urls import path

from . import views
from .views import ProjectCreate, ProjectRetrieve

urlpatterns = [
    path('',views.index, name="home"),
    path('about/',views.about, name="about"),
    path('projects/',ProjectRetrieve.as_view(), name="projects"),
    path('add_project/',ProjectCreate.as_view(), name="add_project"),
]