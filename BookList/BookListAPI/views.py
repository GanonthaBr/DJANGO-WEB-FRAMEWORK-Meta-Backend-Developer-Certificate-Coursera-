from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view
from .models import Book
from .serializers import BookSerializer


# Create your views here.


class BooksView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class SingleBookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view()
def single_book(request, pk):
    item = get_object_or_404(Book,pk=pk)
    serialized_item = BookSerializer(item)
    return Response(serialized_item.data)