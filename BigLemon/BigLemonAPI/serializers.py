from rest_framework import serializers
from .models import Menu

class MenuSerilizer(serializers.ModelField):
    class Meta:
        model = Menu
        fields = ['title','price']