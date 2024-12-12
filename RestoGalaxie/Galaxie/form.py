from django.forms import ModelForm
from .models import Booking, Category

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'