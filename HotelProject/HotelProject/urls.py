
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from Hotel import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Hotel.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='hotel/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
