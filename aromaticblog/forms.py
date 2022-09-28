""" A django module to manipulate models """
from django import forms
from .models import Comment, Post, ContactUser
from .widgets import CustomClearableFileInput


class PostForm(forms.ModelForm):
    """ A form for managing rendering post """
    class Meta:
        """ A class for displaying body and name of a post """
        model = Post
        fields = ('title', 'content', 'related_img', 'status', )        
        image = forms.ImageField(label='image', required=False,
                             widget=CustomClearableFileInput)


class CommentForm(forms.ModelForm):
    """ a model for the comment form """
    class Meta:
        """ A class for displaying body and name of a comment"""
        model = Comment
        fields = ('body', 'name', )


class ContactUserForm(forms.ModelForm):
    """ a model for the comment form """

    name = forms.CharField(label='name',widget=forms.TextInput(attrs={'placeholder':'Name'}))
    email_users = forms.CharField(label='email address',widget=forms.TextInput(attrs={'placeholder':'Your Email address'}))
    message = forms.Textarea()
    class Meta:
        """ A class for displaying body and name of a comment"""
        model = ContactUser
        fields = ('email_users', 'name', 'message', )
    
