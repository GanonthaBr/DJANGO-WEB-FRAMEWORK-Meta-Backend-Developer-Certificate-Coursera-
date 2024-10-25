from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from .models import Books, Menu
from .serializers import MenuSerializer

# Create your views here.
@api_view(['GET','POST'])
# @api_view
def books(request):
    return Response('The book list',status=status.HTTP_200_OK)

# MENU
@api_view(['GET','POST','DELETE'])
def menu_items(request):
    if request.method == 'GET':
        items = Menu.objects.all()
        serialized_items = MenuSerializer(items, many=True)
        return Response(serialized_items.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serialized_items = MenuSerializer(data=request.data)
        serialized_items.is_valid(raise_exception=True)
        serialized_items.save()
        return Response(serialized_items.data, status=status.HTTP_201_CREATED)



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
