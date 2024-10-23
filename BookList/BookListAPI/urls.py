from django.urls import path
from . import views

urlpatterns = [
    path('books/',views.booksView),
    # path('books/<int:pk>/',views.SingleBookView.as_view()),
    path('books/<int:pk>/',views.single_book),
    path('authors/',views.author_list, name='authros'),
    path('authors/<int:pk>',views.author_detail, name='author-detail'),
]
