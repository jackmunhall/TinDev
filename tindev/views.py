from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'tindev/index.html')

def register(request):
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
            user = User.objects.create_user(username=username, password=password, is_staff=True)
        except:
            return HttpResponse("Failed to create account")

        bio = form["bio"]
        zip = form["zip"]
        skills = form["skills"]
        github = form["github"]
        years_experience = form["years_exp"]
        education = form["education"]

        Candidate.objects.create(bio=bio, zip=zip, skills=skills, github=github, years_experience=years_experience, education=education, user=user)

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
        if user.is_staff:
            return redirect('/recruiter_dashboard')
        else:
            return HttpResponse("login success")
    else:
        return HttpResponse("login failed")

def logout_view(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='/login')
def recruiter_dashboard_view(request):
    if not request.user.is_staff:
        return redirect('/')

    posts = request.user.recruiter.post_set.all()

    context = {
        'posts': posts
    }

    return render(request, 'tindev/recruiter_dashboard.html', context)

@login_required(login_url='/login')
def posts_create_view(request):
    if not request.user.is_staff:
        return redirect('/')

    if request.method == "GET":
        context = {
            'form': PostForm()
        }

        return render(request, 'tindev/posts/create.html', context)

    form = PostForm(request.POST)

    if not form.is_valid():
        return redirect('/posts/create')

    data = form.cleaned_data

    post = Post.objects.create(
    recruiter=request.user.recruiter,
    title=data['title'],
    type=data['type'],
    city=data['city'],
    state=data['state'],
    skills=data['skills'],
    description=data['description'],
    expiration=data['expiration'],
    status=data['status']
    )

    return redirect('/recruiter_dashboard')

@login_required(login_url='/login')
def posts_update_view(request, id):
    post = Post.objects.get(pk=id)

    if request.method == "GET":
        if not request.user.is_staff:
            return redirect(f"/posts/{post.id}")

        form = PostForm(instance=post)

        context = {
            'form': form,
            'post': post,
        }

        return render(request, f"tindev/posts/update.html", context)

    form = PostForm(request.POST)
    if not form.is_valid():
        return redirect(f"/posts/update/{id}")

    data = form.cleaned_data

    post.title = data['title']
    post.type = data['type']
    post.city = data['city']
    post.state = data['state']
    post.skills = data['skills']
    post.description = data['description']
    post.expiration = data['expiration']
    post.status = data['status']

    post.save()

    return redirect(f"/posts/update/{id}")
