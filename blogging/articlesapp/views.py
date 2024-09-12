from django.http import HttpResponse
from django.shortcuts import render
from .forms import ArticleForm
from .models import Article

def index(request):
    context = {}
    return render(request, 'home.html',context)

def create(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'create.html', context)

def detail(request, pk):
    article = Article.objects.get(id=pk)
    context = {"article":article}
    return render(request, 'detail.html', context)

def all_articles(request):
    articles = Article.objects.all()
    context = {"articles":articles}
    return render(request, 'all_articles.html', context)