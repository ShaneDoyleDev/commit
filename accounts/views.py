# Third party imports
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# Local application imports
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    """
    Custom view for user sign up and registration.
    """

    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        messages.success(
            self.request, 'Account created successfully! You are now logged in.')
        return valid


class CustomLoginView(LoginView):
    """
    Custom view for logging in a user.
    """

    template_name = 'accounts/login.html'

