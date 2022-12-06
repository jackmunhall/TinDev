from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from ..models import *
from ..forms import *

def register(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "GET":
        user_form = UserForm()
        recruiter_form = RecruiterForm()

        context = {
                'user_form': user_form,
                'recruiter_form': recruiter_form,
                }

        return render(request, 'tindev/register.html', context)

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
        return redirect('/recruiter_dashboard')
    else:
        username = form["username"]
        password = form["password"]

        try:
            user = User.objects.create_user(username=username, password=password, is_staff=False)
        except:
            return HttpResponse("Failed to create account")

        name = form["name"]
        bio = form["bio"]
        zip = form["zip"]
        skills = form["skills"]
        github = form["github"]
        years_experience = form["years_exp"]
        education = form["education"]

        Candidate.objects.create(name=name, bio=bio, zip=zip, skills=skills, github=github, years_experience=years_experience, education=education, user=user)

        user = login(request, user)

        return redirect("/candidate_dashboard")

def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "GET":
        return render(request, 'tindev/login.html')

    form = request.POST

    username = form["username"]
    password = form["password"]

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        if user.is_staff:
            return redirect('/recruiter_dashboard')
        else:
            return redirect('/candidate_dashboard')
    else:
        return HttpResponse("login failed")

def logout_view(request):
    logout(request)
    return redirect('/login')

