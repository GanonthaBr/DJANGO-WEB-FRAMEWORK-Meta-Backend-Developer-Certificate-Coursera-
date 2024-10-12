from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from .models import Books

# Create your views here.
@api_view(['GET','POST'])
# @api_view
def books(request):
    return Response('The book list',status=status.HTTP_200_OK)

# MENU
@api_view(['GET'])
def menu_items(request):
    return Response('The menu list',status=status.HTTP_200_OK)

@api_view(['POST'])
def post_menu(request):
    # add 
    return Response('The menu item added',status=status.HTTP_201_CREATED)
    

class BookViews(APIView):
    def get(self, request):
        author = request.GET.get('author')
        books = Books.objects.all()
        if(author):
            return Response({"message":"List of the books written by: " + author}, status.HTTP_200_OK)
        return Response(books.values(), status.HTTP_200_OK)
    def post(self, request, pk):
        return Response({"title":request.data.get('title')}, status.HTTP_200_OK)

class Book(APIView):
    def get(self, request,pk):
        return Response({"message":"single book with id:" + str(pk)}, status.HTTP_200_OK)
    
    def put(self, request,pk):
        return Response({"title":request.data.get('title')}, status.HTTP_200_OK)
