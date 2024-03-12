from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('posts/', include('blog.post_urls')),
    path('profile/', include('blog.profile_urls')),
    path('comment/', include('blog.comment_urls')),
    path('about/', views.AboutView.as_view(), name='about'),
]
