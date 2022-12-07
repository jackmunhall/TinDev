from django.forms import ModelForm
from django.forms import ModelForm, TextInput, EmailInput
from .models import *

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'type', 'city', 'state', 'skills', 'description', 'expiration', 'status']
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                })
        }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class RecruiterForm(ModelForm):
    class Meta():
        model = Recruiter
        fields = ['company', 'zip']
