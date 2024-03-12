from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='all-posts'),
    path('user-posts/', views.UserPostListView.as_view(),
         name='user-posts'),
    path('create/', views.PostCreateView.as_view(), name='create-post'),
    path('update/<int:pk>/',
         views.PostUpdateView.as_view(), name='update-post'),
    path('delete/<int:pk>',
         views.PostDeleteView.as_view(), name='delete-post'),
    path('<slug:slug>/', views.post_detail_view, name='post-detail'),
]
