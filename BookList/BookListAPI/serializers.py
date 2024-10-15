from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    pricing = serializers.DecimalField(max_digits=5,decimal_places=3,source='price')
    class Meta:
        model = Book
        fields = ['title', 'author', 'pricing']
    
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']