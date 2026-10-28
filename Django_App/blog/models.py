from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User


class Comment(models.Model):
    comment_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.comment_text


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
