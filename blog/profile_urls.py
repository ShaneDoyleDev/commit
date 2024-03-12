from django.urls import path
from . import views

urlpatterns = [
    path('edit/<int:pk>/', views.ProfileUpdateView.as_view(), name='update-profile'),
    path('<int:pk>', views.ProfileDetailView.as_view(), name='profile'),
]
