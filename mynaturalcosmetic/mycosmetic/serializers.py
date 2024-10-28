from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = Product
        fields = ['id','name', 'price','category','description']
        
        extra_kwargs = {
            'price': {'min_value': 2}
        }

def create(self, validated_data):
        return Product.objects.create(**validated_data)