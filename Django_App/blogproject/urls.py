# INF601 - Advanced Programming in Python
# Brennan Adams
# Mini Project 6

from django.contrib.auth import views as auth_views

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
]
