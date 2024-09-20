from django import forms

class TaskForm(forms.Form):
    urgencies = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    )
    title = forms.CharField(label='Task Title:' )
    description = forms.CharField(label='Task Description:')
    priority = forms.ChoiceField(label='Task Priority:', choices=urgencies)
    completed = forms.BooleanField(label='Task Completed:', required=False)