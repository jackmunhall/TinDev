from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# Create your models here.
class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=500, blank=True, null=True)
    zip = models.CharField(max_length=10)
    skills = models.TextField()
    github = models.CharField(max_length=100)
    years_experience = models.IntegerField()
    education = models.CharField(max_length=100, blank=True, null=True)

class Recruiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    company = models.CharField(max_length=255)
    zip = models.CharField(max_length=10)
