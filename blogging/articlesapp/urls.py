from django.urls import path
from . import views

urlpatterns = [
   path('',views.index, name="home"), 
   path('articles/create/',views.create, name="create"),
   path('articles/<int:pk>/',views.detail, name="detail"),
   path('articles/',views.all_articles,name='all_articles'),
   path('article/<id>/',views.delete,name="delete"),
]