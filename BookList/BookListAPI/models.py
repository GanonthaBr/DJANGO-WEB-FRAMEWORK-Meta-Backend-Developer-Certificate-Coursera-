from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    def __str__(self):
        return self.title
