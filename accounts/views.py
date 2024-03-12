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

    def form_valid(self, form):
        messages.success(self.request, 'You have successfully logged in.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('homepage')


class CustomLogoutView(LogoutView):
    """
    Custom view for logging out a user.
    """

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(
            request, messages.SUCCESS,
            'You have been logged out.'
        )
        return redirect('homepage')
