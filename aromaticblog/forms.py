""" A django module to manipulate models """
from django import forms
from .models import Comment, Post
from .widgets import CustomClearableFileInput


class PostForm(forms.ModelForm):
    """ A form for managing rendering post """
    class Meta:
        """ A class for displaying body and name of a post """
        model = Post
        fields = ('title', 'content', 'related_img', 'slug', )        
        image = forms.ImageField(label='image', required=False,
                             widget=CustomClearableFileInput)


class CommentForm(forms.ModelForm):
    """ a model for the comment form """
    class Meta:
        """ A class for displaying body and name of a comment"""
        model = Comment
        fields = ('body', 'name', )
