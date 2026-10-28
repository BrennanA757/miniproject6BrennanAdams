# INF601 - Advanced Programming in Python
# Brennan Adams
# Mini Project 6

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import RegisterForm, ContactForm, PostForm
from .models import Post


def home(request):
    return render(
        request,
        "blog/home.html",
    )


def posts(request):
    all_posts = Post.objects.all()

    return render(
        request,
        "blog/posts.html",
        {"posts": all_posts}
    )


def post_detail(request, id):
    post = get_object_or_404(
        Post,
        id=id
    )

    return render(
        request,
        "blog/post_detail.html",
        {"post": post}
    )


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if (form.is_valid()):
            post = form.save(
                commit=False
            )

            post.author = request.user

            post.save()

            return redirect(
                "posts"
            )

    else:
        form = PostForm()

    return render(
        request,
        "blog/create_post.html",
        {"form": form}
    )


def contact(request):
    form = ContactForm()

    return render(
        request,
        "blog/contact.html",
        {"form": form}
    )


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(
            request.POST
        )

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(
                "home"
            )
    else:
        form = RegisterForm()
    return render(
        request,
        "blog/register.html",
        {"form": form}
    )
