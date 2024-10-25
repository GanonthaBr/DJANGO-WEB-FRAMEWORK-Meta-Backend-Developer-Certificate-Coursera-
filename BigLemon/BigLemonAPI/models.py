from django.db import models

# Create your models here.

class Categories(models.Model):
    title = models.CharField(max_length=255, default='little_lemon_home_made')

    def __str__(self):
        return self.title
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    category = models.ForeignKey(Categories, on_delete=models.PROTECT)
class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5,decimal_places=2)


