from django.contrib import admin
from .models import Drinks
from .models import Menu
from .models import MenuCategories
from .models import Logger

# Register your models here.
admin.site.register(Drinks)
admin.site.register(Menu)
admin.site.register(MenuCategories)
admin.site.register(Logger)