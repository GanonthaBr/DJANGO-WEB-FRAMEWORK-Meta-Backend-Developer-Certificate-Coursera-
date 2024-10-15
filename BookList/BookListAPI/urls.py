from django.urls import path

from . import views

urlpatterns = [
    path('books/',views.BooksView.as_view()),
    # path('books/<int:pk>/',views.SingleBookView.as_view()),
    path('books/<int:pk>/',views.single_book),
    path('authors/',views.Author.as_view()),
    
]
