# INF601 - Advanced Programming in Python
# Brennan Adams
# Mini Project 6

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import RegisterForm, ContactForm, PostForm
from .models import Post


def register_view(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('home')

    else:
        form = RegisterForm()

    return render(
        request,
        "blog/register.html",
        {"form": form}
    )
