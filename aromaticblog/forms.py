""" A django module to manipulate models """
from django import forms
from .models import Comment, Post
from .widgets import CustomClearableFileInput


class PostForm(forms.ModelForm):

    
    class Meta:
        """ A class for displaying body and name of a comment"""
        model = Post
        fields = '__all__'
        image = forms.ImageField(label='image', required=False,
                             widget=CustomClearableFileInput)
    def __init__(self, *args, **kwargs):
        """ A function that hides the item and user
        that is updating post so it canot be modified """
        super().__init__(*args, **kwargs)
        self.fields['author'].widget = forms.HiddenInput()
        self.fields['likes'].widget = forms.HiddenInput()

class CommentForm(forms.ModelForm):
    """ a model for the comment form """
    class Meta:
        """ A class for displaying body and name of a comment"""
        model = Comment
        fields = ('body', 'name', )
