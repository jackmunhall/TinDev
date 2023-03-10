from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.functional import wraps
from ..models import *
from ..forms import *
import datetime

@login_required(login_url='/login')
def offer_create_view(request, id):
    if not request.user.is_staff:
        return redirect(f"/posts/{id}")

    if request.method != "POST":
        return redirect(f"/posts/")

    post = Post.objects.get(pk=id)

    form = request.POST

    if 'offer_list' not in form:
        return redirect(f"/posts/{id}")

    post = Post.objects.get(pk=id)
    due_date = form['due_date']
    salary = form['salary']

    candidates = form.getlist('offer_list')
    for c in candidates:
        c = Candidate.objects.get(pk=int(c))
        Offer.objects.create(post=post, candidate=c, due_date=due_date, salary=salary, accepted=None)

    return redirect(f"/posts/{id}")

@login_required(login_url='/login')
def offer_view(request, id):
    if request.user.is_staff:
        return redirect(f"/recruiter_dashboard")

    offer = Offer.objects.get(pk=id)
    now = datetime.datetime.now()
    now = datetime.date(now.year, now.month, now.day)

    context = {
        'offer': offer,
        'now': now,
    }

    return render(request, 'tindev/offers/view.html', context)

@login_required(login_url='/login')
def offer_respond_view(request, id):
    if request.user.is_staff:
        return redirect(f"/recruiter_dashboard")

    if request.method != "POST":
        return redirect(f"/offers/{id}")

    response = True if 'response' in request.POST else False
    print("RESPONSE", response)

    offer = Offer.objects.get(pk=id)

    offer.accepted = response
    offer.save()

    print("CURR", offer.accepted)

    return redirect("/")
