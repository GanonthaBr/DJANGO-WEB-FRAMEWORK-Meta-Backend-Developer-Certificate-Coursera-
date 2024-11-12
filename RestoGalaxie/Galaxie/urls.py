from django.urls import path
from .  import views

urlpatterns = [
    path('',views.home,name='home'),
    path('menu-items/',views.menu,name='menu'),
    path('menu-items/<int:pk>/',views.menu_details,name='menu_details'),
    path('booking/',views.book,name='book'),
    path('about/',views.about,name='about'),
    path('categories/',views.category,name='categories'),
]