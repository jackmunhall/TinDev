from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request, 'tindev/index.html')

def register(request):
    if request.method == "GET":
        return render(request, 'tindev/register.html')

    form = request.POST

    if form["is_recruiter"] == "1":
        username = form["username"]
        password = form["password"]

        try:
            user = User.objects.create_user(username=username, password=password, is_staff=True)
        except:
            return HttpResponse("Failed to create account")

        company = form["company"]
        zip = form["zip"]
        Recruiter.objects.create(zip=zip, company=company, user=user)

        user = login(request, user)
        return HttpResponse("created recruiter")
    else:
        username = form["username"]
        password = form["password"]

        try:
            user = User.objects.create_user(username=username, password=password, is_staff=True)
        except:
            return HttpResponse("Failed to create account")

        bio = form["bio"]
        zip = form["zip"]
        skills = form["skills"]
        github = form["github"]
        years_experience = form["years_exp"]
        education = form["education"]

        Candidate.objects.create(bio=bio, zip=zip, skills=skills, github=github, years_experience=years_experience, education=education)

        user = login(request, user)

        return HttpResponse("created candidate")

def login_view(request):
    if request.method == "GET":
        return render(request, 'tindev/login.html')

    form = request.POST

    username = form["username"]
    password = form["password"]

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("login success")
    else:
        return HttpResponse("login failed")

def logout_view(request):
    logout(request)
    return HttpResponse("logged out")

