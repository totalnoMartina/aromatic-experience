from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin



@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created', 'approved')
    list_filter = ('approved', 'created')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
