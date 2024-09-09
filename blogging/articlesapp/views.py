from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

# Create your views here.

def home(request): #home page
    try:
        content = "<h1>Welcome to our Blogging website</h1>"
    except HttpResponseNotFound:
        raise HttpResponseNotFound
    return HttpResponse(content)

all_articles = {'1':{
    'title':'Django is cool',
    'content':'Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.',
    'author':'John Doe',
    'date':'2023-05-12',
    'year':2023
},
2:{
    'title':'Python is cool',
    'content':'Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace.',
    'author':'Jane Doe',
    'date':'2021-05-12',
    'year':2021
},
3:{
    'title':'JavaScript is cool',
    'content':'JavaScript is a programming language that conforms to the ECMAScript specification. JavaScript is high-level, often just-in-time compiled, and multi-paradigm. It has curly-bracket syntax, dynamic typing, prototype-based object-orientation, and first-class functions.',
    'author':'John Doe',
    'date':'2020-05-12',
    'year':2020
},
4:{
    'title':'CSS is cool',
    'content':'Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML. CSS is a cornerstone technology of the World Wide Web, alongside HTML and JavaScript.',
    'author':'Jane Doe',
    'date':'2000-05-12',
    'year':2000
},
}

def all_articles(request,all): #get all articles
    content = "hi"
    try:
        content = "<h1>{all_articles['1']}</h1>"
    except HttpResponseNotFound:
        raise HttpResponseNotFound
    return HttpResponse(content)


def show_article(request, year, id): #get single article
    content= ""
    try:
        article = all_articles[int(id)]
        if article['year'] == int(year):
            content = "<h1>{0}</h1><p>{1}</p><p>By {2} on {3}</p>".format(article['title'], article['content'], article['author'], article['date'])
        else:
            content = "<h3>Not Found!</h3>"
    except HttpResponseNotFound:
        raise HttpResponseNotFound
    return HttpResponse(content)

def post_article(request, title, id): #post article
    content = ""
    try:
        content= f"<p>You are adding a new article with the title {title} and an id of {id}"
    except HttpResponseNotFound:
        raise HttpResponseNotFound
    return HttpResponse(content)