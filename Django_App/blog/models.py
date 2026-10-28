from django.db import models
from django.utils import timezone
from django.contrib import admin


class Comment(models.Model):
    comment_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.comment_text
