from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
@api_view(['GET'])
# @api_view
def books(request):
    return Response('The book list',status=status.HTTP_200_OK)

class BookViews(APIView):
    def get(self, request, pk):
        return Response({"message":"single book with id " + str(pk)}, status.HTTP_200_OK)
    
    def put(self, request, pk):
        return Response({"title":request.data.get('title')}, status.HTTP_200_OK)
