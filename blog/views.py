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


class AboutView(TemplateView):
    """
    View class for the about page of the site.
    """

    template_name = 'blog/about.html'


# ------- Post Views --------

class PostListView(ListView):
    """
    View class for listing all posts.
    """

    model = Post
    template_name = 'blog/post/post-list.html'
    paginate_by = 6

    def get_queryset(self):
        """
        Returns the queryset for the view.

        If a category filter is provided in the request parameters,
        the queryset will be filtered based on the category.
        """

        queryset = super().get_queryset()
        category = self.request.GET.get('filter', None)
        if category:
            queryset = queryset.filter(category=category)
        return queryset


class UserPostListView(LoginRequiredMixin, ListView):
    """
    View class for listing posts related to the signed-in user.
    """

    model = Post
    template_name = 'blog/post/user-posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """
        Override the get_queryset method to filter posts by the signed-in user.
        """

        return Post.objects.filter(author=self.request.user)


def post_detail_view(request, slug):
    """
    View function for displaying the details of a blog post.
    Renders and handles the comment form for an individual blog post
    """

    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(
                request, 'Your comment has been added successfully.'
            )
            return redirect('post-detail', slug=slug)
        else:
            messages.error(
                request, 'Form Invalid. Please check your input.'
            )
    else:
        comment_form = CommentForm()
    return render(request, 'blog/post/post-detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    View class for creating a new post.
    Requires user to be logged in.
    """

    model = Post
    form_class = PostForm
    template_name = 'blog/post/create-post.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        """
        Override the form_valid method to set the author of the form instance
        to the currently logged-in user.
        """

        form.instance.author = self.request.user
        response = super().form_valid(form)
        messages.success(
            self.request, 'Your post has been created successfully.')
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(
            self.request, 'Form Invalid. Please check your input.')
        return response


class PostUpdateView(LoginRequiredMixin, UpdateView):
    """
    View class for editing an existing post.
    Requires user to be logged in.
    """

    model = Post
    form_class = PostForm
    template_name = 'blog/post/create-post.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        messages.success(
            self.request, 'Your post has been updated successfully.')
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(
            self.request, 'Form Invalid. Please check your input.')
        return response


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View for deleting a post.

    Requires the user to be logged in and pass the test_func() method to access the view.
    Deletes the specified post and redirects to the 'all-posts' URL upon successful deletion.
    """

    model = Post
    template_name = 'blog/post/delete-post.html'
    success_url = reverse_lazy('all-posts')

