from django.forms import ModelForm
from django.forms import ModelForm, TextInput, EmailInput, CheckboxInput
from .models import *

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'type', 'city', 'state', 'skills', 'description', 'expiration', 'status']
        labels = {
            'skills':'Skills (comma-separated):',
            'expiration':'Expiration (MM/DD/YYYY):'
        }
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; ',
                }),
            'type': CheckboxInput(attrs={
                'class': "", 
                'style': 'max-width: 300px; ',
                }),
            'city': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }), 
            'state': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }), 
            'skills': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }), 
            'expiration': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }), 
        }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class RecruiterForm(ModelForm):
    class Meta():
        model = Recruiter
        fields = ['company', 'zip']
