from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# Create your models here.
class Recruiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    company = models.CharField(max_length=255)
    zip = models.CharField(max_length=10)

class Post(models.Model):
    recruiter = models.ForeignKey(Recruiter, on_delete=models.RESTRICT)
    title = models.CharField(max_length=255)

    # false = part time
    type = models.BooleanField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    skills = models.TextField()
    description = models.TextField()
    expiration = models.DateField()

    # true = active
    status = models.BooleanField()

class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=500, blank=True, null=True)
    zip = models.CharField(max_length=10)
    skills = models.TextField()
    github = models.CharField(max_length=100)
    years_experience = models.IntegerField()
    education = models.CharField(max_length=100, blank=True, null=True)

    interested_posts = models.ManyToManyField(Post, related_name='interested')
    not_interested_posts = models.ManyToManyField(Post, related_name='not_interested')

class Offer(models.Model):
    post = models.ForeignKey(Post, on_delete=models.RESTRICT, related_name='offers')
    candidate = models.ForeignKey(Candidate, on_delete=models.RESTRICT, related_name='offers')
    due_date = models.DateField()
    salary = models.IntegerField()
    accepted = models.BooleanField(blank=True, null=True)
