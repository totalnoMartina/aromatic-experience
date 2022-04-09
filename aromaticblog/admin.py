from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


# Registering an app
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """ For admin to see specific informations on post model """
    list_display = ('title', 'slug', 'status', 'created')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """ For admin to see the specific informations on comments """
    list_display = ('name', 'body', 'post', 'created', 'approved')
    list_filter = ('approved', 'created')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """ A function for changing comments from 'draft' to approved """
        queryset.update(approved=True)
