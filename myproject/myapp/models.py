from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()

class Huiles(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()

class Drinks(models.Model):
    drink_name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.drink_name}"

#categories
class MenuCategories(models.Model):
    menu_category_name = models.CharField(max_length=200)

#menus
class Menu(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    menu_category = models.ForeignKey(MenuCategories, on_delete=models.PROTECT, default=None,related_name='category_id' )

    def __str__(self):
        return f"Name: {self.name} Price: {self.price}"
    
#model form
class Logger(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name}"