from django.urls import path
from . import views

urlpatterns = [
    # path('books/',views.books),
    path('books/<int:pk>',views.Book.as_view()),
    path('books/',views.BookViews.as_view()),

]