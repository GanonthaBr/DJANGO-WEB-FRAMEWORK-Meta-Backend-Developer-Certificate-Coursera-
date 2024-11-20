# bookings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('room/<int:room_id>/', views.room_details, name='room_details'),
    path('book/', views.book_room, name='book_room'),
]
