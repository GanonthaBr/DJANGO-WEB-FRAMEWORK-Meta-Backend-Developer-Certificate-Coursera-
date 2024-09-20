from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('tasks/',views.tasks,name='tasks'),
    path('newtask/',views.addTask,name='addtask'),
    path('/addtask/',views.process_task,name='process_task')
]

