from django import forms

class ApplicationForm(forms.Form):
    posts = (
        ('Manager', 'Manager'),
        ('Developer', 'Developer'),
        ('Designer', 'Designer'),
        ('Tester', 'Tester'),
    )
    name = forms.CharField(label='Applicant name:', max_length=50)
    age = forms.IntegerField(label='Your age:')
    address = forms.CharField(label='Enter your address:', max_length=20)
    position = forms.ChoiceField(label='What is your Position:', choices=posts)
