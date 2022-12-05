from django.forms import ModelForm
from .models import *

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'type', 'city', 'state', 'skills', 'description', 'expiration', 'status']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class RecruiterForm(ModelForm):
    class Meta():
        model = Recruiter
        fields = ['company', 'zip']
