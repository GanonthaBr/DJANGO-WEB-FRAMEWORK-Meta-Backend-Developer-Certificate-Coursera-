from rest_framework import serializers
from .models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name']

class BookSerializer(serializers.ModelSerializer):
    pricing = serializers.DecimalField(max_digits=5,decimal_places=3,source='price')
    author = AuthorSerializer() #relationship serializer
    class Meta:
        model = Book
        fields = ['id','title', 'author', 'pricing']
    
