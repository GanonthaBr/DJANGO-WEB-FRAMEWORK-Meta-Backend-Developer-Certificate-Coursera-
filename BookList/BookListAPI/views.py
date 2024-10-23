from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


# Create your views here.

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def booksView(request):
    if request.method == 'GET':
        items = Book.objects.all()
        name = request.query_params.get('name')
        price = request.query_params.get('to_price')

        if name:
            items = items.filter(author__name=name)
        if price:
            items = items.filter(price__lte=price)
        if price and name:
            items = items.filter(author__name=name, price__lte=price)
        serialized_items = BookSerializer(items, many=True, context={'request':request})
        return Response(serialized_items.data)
    if request.method == 'POST':
        serialized_items = BookSerializer(data = request.data,context={'request':request})
        serialized_items.is_valid(raise_exception=True)
        serialized_items.save()
        return Response(serialized_items.data, status=status.HTTP_201_CREATED)
    
class SingleBookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(['GET','POST','PUT','PATCH'])
def single_book(request, pk):
    # item = get_object_or_404(Book,pk=pk)
    item = Author.objects.get(pk=pk)
    serialized_item = AuthorSerializer(item)
    return Response(serialized_item.data)

class Authors(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def author_detail(request, pk):
    if request.method == 'GET':
        item = get_object_or_404(Author,pk=pk)
        serialized_item = AuthorSerializer(item,context={'request':request} )
        return Response(serialized_item.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serialized_item = AuthorSerializer(data=request.data,context={'request':request})
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status=status.HTTP_201_CREATED)
   
