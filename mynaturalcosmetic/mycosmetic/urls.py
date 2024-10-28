from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('category',views.category_list,name='category_list'),
    path('category/<int:id>',views.category_details,name='category_details'),
    path('product',views.product_list,name='product_list'),
    path('product/<int:id>',views.product_details,name='product_details'),
    path('api-token-auth/',obtain_auth_token,name='api_token_auth'),
]