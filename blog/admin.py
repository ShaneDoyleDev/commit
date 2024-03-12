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
