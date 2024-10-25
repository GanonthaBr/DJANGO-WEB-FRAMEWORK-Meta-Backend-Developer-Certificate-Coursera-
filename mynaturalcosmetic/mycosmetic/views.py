from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

# Create your views here.

@api_view(['GET','POST'])
def category_list(request):
    if request.method == 'GET':
        items = Category.objects.all()
        
        serialized_item = CategorySerializer(items, many=True)
        return Response(serialized_item.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serialized_item = CategorySerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data,status=status.HTTP_201_CREATED)

@api_view(['GET','DELETE','PUT'])
def category_details(request,id):
    if request.method == 'GET':
        item = Category.objects.get(pk=id)
        serialized_item = CategorySerializer(item)
        return Response(serialized_item.data, status=status.HTTP_200_OK)
   
    if request.method == 'DELETE':
        item = Category.objects.get(pk=id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'PUT':
        item = Category.objects.get(pk=id)
        serialized_item = CategorySerializer(item,data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data,status=status.HTTP_200_OK)
    
    if request.method == 'PATCH':
        item = Category.objects.get(pk=id)
        serialized_item = CategorySerializer(item, data=request.data,partial=True)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data,status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        items = Product.objects.all()
        name = request.query_params.get('name') #filtering
        ordering = request.query_params.get('ordering') #ordering
        search = request.query_params.get('search')
        if name:
            items = items.filter(category__name__istartswith=name)
        if ordering:
            ordering_fields = ordering.split(",")
            items = items.order_by(*ordering_fields)
        if search:
            items = items.filter(name__icontains=search)  
        serialized_item = ProductSerializer(items, many=True)
        return Response(serialized_item.data, status=status.HTTP_200_OK)
    if request.method =='POST':
        serialized_item = ProductSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status=status.HTTP_201_CREATED)

@api_view(['GET','DELETE','PUT'])
def product_details(request,id):
    if request.method =='GET':
        item = Product.objects.get(pk=id)
        serialized_item = ProductSerializer(item)
        return Response(serialized_item.data, status=status.HTTP_200_OK)
    
    if request.method =='DELETE':
        item = Product.objects.get(pk=id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method =='PUT':
        item = Product.objects.get(pk=id)
        serialized_item = ProductSerializer(item, data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status=status.HTTP_200_OK)
    if request.method =='PATCH':
        item = Product.objects.get(pk=id)
        serialized_item = ProductSerializer(item, data=request.data, partial=True) #partial update
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status=status.HTTP_200_OK)