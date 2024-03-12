from django.urls import path
from . import views

urlpatterns = [
    path('update/<int:pk>/',
         views.CommentUpdateView.as_view(), name='update-comment'),
    path('delete/<int:pk>/',
         views.CommentDeleteView.as_view(), name='delete-comment'),
]
