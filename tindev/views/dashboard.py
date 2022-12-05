from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from ..models import *
from ..forms import *

# Create your views here.
def index(request):
    return render(request, 'tindev/index.html')


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

