# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import UpdateView

# Local application imports
from .forms import PostForm, CommentForm, ProfileForm
from .models import Post, Comment, Profile


# ------- Site Views --------

def homepage(request):
    """
    View function for the homepage of the site.
    Returns the 4 most recent published posts.
    """

    recent_posts = Post.objects.order_by('-created_on')[:4]
    return render(request, 'blog/homepage.html', {'recent_posts': recent_posts})
