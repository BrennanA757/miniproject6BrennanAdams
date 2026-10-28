# INF601 - Advanced Programming in Python
# Brennan Adams
# Mini Project 6

from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
        ]


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
