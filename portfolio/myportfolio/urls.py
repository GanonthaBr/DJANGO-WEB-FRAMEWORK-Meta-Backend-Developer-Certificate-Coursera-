from django.urls import path

from . import views
from .views import ProjectCreate, ProjectRetrieve,ProjectDetails, ProjectUpdate, ProjectDelete

urlpatterns = [
    path('',views.index, name="home"),
    path('about/',views.about, name="about"),
    path('projects/',ProjectRetrieve.as_view(), name="projects"),
    path('project/<int:pk>',ProjectDetails.as_view(), name="project"),
    path('<int:pk>/update',ProjectUpdate.as_view(), name="update"),
    path('<int:pk>/delete',ProjectDelete.as_view(), name="delete"),
    path('add_project/',ProjectCreate.as_view(), name="add_project"),
]