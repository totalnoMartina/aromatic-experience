""" A django module to manipulate models """
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """ a model for the comment form """
    class Meta:
        """ A class for displaying body and name of a comment"""
        model = Comment
        fields = ('body', 'name', )

# class UpdateComment(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('body', )
