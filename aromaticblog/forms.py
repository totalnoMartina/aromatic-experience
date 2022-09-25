""" A django module to manipulate models """
from django import forms
from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        """ A class for displaying body and name of a comment"""
        model = Post
        fields = ('title', 'content', 'related_img', 'slug', 'excerpt')


class CommentForm(forms.ModelForm):
    """ a model for the comment form """
    class Meta:
        """ A class for displaying body and name of a comment"""
        model = Comment
        fields = ('body', 'name', )
