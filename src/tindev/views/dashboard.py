from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Count
import datetime
from ..models import *
from ..forms import *

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'tindev/index.html')

    if request.user.is_staff:
        posts = request.user.recruiter.post_set.all()
        now = datetime.datetime.now()
        now = datetime.date(now.year, now.month, now.day)
        for post in posts:
            if post.expiration < now:
                post.status = False
                post.save()
        context = {
                'posts': posts
                }
        return render(request, 'tindev/recruiter_dashboard.html', context)
    
    posts = request.user.candidate.interested_posts.all()

    # update post expirations on page load
    now = datetime.datetime.now()
    now = datetime.date(now.year, now.month, now.day)
    for post in posts:
        if post.expiration < now:
            post.status = False
            post.save()

    offers = request.user.candidate.offers.all()
    context = {
            'posts': posts,
            'offers': offers
            }
    return render(request, "tindev/candidate_dashboard.html", context)



@login_required(login_url='/login')
def recruiter_dashboard_view(request):
    if request.method != "POST":
        return redirect("/")

    active_filter = request.POST["active_filter"]
    interested_filter = request.POST["interested_filter"]

    posts = request.user.recruiter.post_set.all()
    if active_filter == "active":
        posts = posts.filter(status=True)
    elif active_filter == "inactive":
        posts = posts.filter(status=False)

    if interested_filter == "true":
        posts = posts.annotate(num_interested=Count('interested')).filter(num_interested__gt=0)


    context = {
            'posts': posts,
            }

    return render(request, 'tindev/recruiter_dashboard.html', context)


@login_required(login_url='/login')
def candidate_dashboard_view(request):
    if request.user.is_staff:
        return redirect('/recruiter_dashboard')

    posts = request.user.candidate.interested_posts.all()
    offers = request.user.candidate.offers.all()

    context = {
            'posts': posts,
            'offers': offers
            }
    return render(request, "tindev/candidate_dashboard.html", context)

