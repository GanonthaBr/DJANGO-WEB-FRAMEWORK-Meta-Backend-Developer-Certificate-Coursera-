from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


# Create your views here.

@api_view(['GET','POST','PUT','PATCH'])
def booksView(request):
    items = Book.objects.all()
    serialized_items = BookSerializer(items, many=True, context={'request':request})
    return Response(serialized_items.data)
    

class SingleBookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(['GET','POST','PUT','PATCH'])
def single_book(request, pk):
    # item = get_object_or_404(Book,pk=pk)
    item = Author.objects.get(pk=pk)
    serialized_item = BookSerializer(item)
    return Response(serialized_item.data)

class Authors(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def author_detail(request, pk):
    item = get_object_or_404(Author,pk=pk)
    serialized_item = AuthorSerializer(item)
    return Response(serialized_item.data)
