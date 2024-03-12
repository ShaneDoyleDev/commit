from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Profile
from .forms import ProfileForm


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin class for managing the Post model in the admin interface.
    """

    list_display = ['title', 'author', 'slug', 'category', 'created_on']
    list_filter = ['created_on', 'category']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ['title']}
    date_hierarchy = 'created_on'
    ordering = ['created_on']
    summernote_fields = ['content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin class for managing Comment model in the Django admin interface.
    """

    list_display = ['author', 'content', 'post', 'created_at', 'updated_at']
    list_filter = ['created_at', 'author']
    search_fields = ['content', 'author__username', 'post__title']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Admin class for managing Profile model in the Django admin interface.
    """
    form = ProfileForm
    search_fields = ['user__username']
