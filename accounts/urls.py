from django.urls import path
from .views import SignUpView, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
]
