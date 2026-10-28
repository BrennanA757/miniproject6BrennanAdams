from django.views import generic
from django.utils import timezone
from django.contrib.auth import logout
from django.shortcuts import redirect

from .models import Comment


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_comments_list"

    def get_queryset(self):
        return Comment.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")


class LoginView(generic.DetailView):
    model = Comment
    template_name = "blog/auth/login.html"


class BaseView(generic.DetailView):
    template_name = "blog/base.html"


class RegisterView(generic.DetailView):
    template_name = "blog/auth/register.html"


def logout_view(request):
    logout(request)
    return redirect('login')
