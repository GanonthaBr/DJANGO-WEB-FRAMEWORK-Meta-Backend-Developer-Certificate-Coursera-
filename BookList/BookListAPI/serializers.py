from rest_framework import serializers
from .models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name']

class BookSerializer(serializers.ModelSerializer):
    pricing = serializers.DecimalField(max_digits=5,decimal_places=3,source='price')
    author = AuthorSerializer(read_only=True) #relationship serializer
    # author = serializers.HyperlinkedRelatedField(queryset = Author.objects.all(),
                                                #  view_name='author-detail')
    class Meta:
        model = Book
        fields = ['id','title', 'author', 'pricing']
        extra_kwarg = {
            'pricing': {'min_value': 2},
        }
        # The `depth = 1` in the `BookSerializer` class is used in Django REST framework to control
        # the depth of relationships that are traversed and displayed in the serialized data.
        # depth = 1 #display relationship
    
