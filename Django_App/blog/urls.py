# INF601 - Advanced Programming in Python
# Brennan Adams
# Mini Project 6

from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'posts/',
        views.posts,
        name='posts'
    ),

    path(
        'post/<int:id>/',
        views.post_detail,
        name='post_detail'
    ),

    path(
        'create/',
        views.create_post,
        name='create_post'
    ),

    path(
        'contact/',
        views.contact,
        name='contact'
    ),

    path(
        'register/',
        views.register_view,
        name='register',
    )
]
