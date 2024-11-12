from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=3,decimal_places=2)

    def __str__(self):
        return self.name

class Booking(models.Model):
    number_of_seats = models.IntegerField()
    day = models.DateField()
    table_owner = models.CharField(max_length=255)

    def __str__(self):
        return self.table_owner
