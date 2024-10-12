from django.urls import path
from . import views

urlpatterns = [
    # path('books/',views.books),
    path('books/<int:pk>',views.Book.as_view()),
    path('books/',views.books),
    path('menu/',views.menu_items),
    # post menu
    path('post_menu/',views.post_menu),
    # get menu

]