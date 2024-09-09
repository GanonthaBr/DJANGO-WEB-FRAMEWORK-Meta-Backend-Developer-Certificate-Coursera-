from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('articles/<all>',views.all_articles,name='articles'), #all articles
    re_path(r'^articles/(?P<year>\d{4})/(?P<id>\d{1})',views.show_article, name='show_article'), #single article
    path('article/<str:title>/<int:id>',views.post_article, name="post")
]