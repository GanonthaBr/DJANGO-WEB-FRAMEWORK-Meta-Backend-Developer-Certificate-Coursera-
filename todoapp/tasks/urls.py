from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('tasks/',views.tasks,name='tasks'),
    path('addtask/',views.process_task,name='process_task'),
    path('task/<int:pk>/',views.task_details,name='task_details'),
    path('task/<int:pk>/',views.delete,name='delete'),
]

