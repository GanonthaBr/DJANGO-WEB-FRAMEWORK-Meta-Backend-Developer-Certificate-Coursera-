from django import forms
from .models import Todotask

class TaskForm(forms.ModelForm):
    class Meta:
        model = Todotask
        fields = "__all__"