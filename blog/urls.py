from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,UserPostListView
from . import views

urlpatterns = [
    # The path to my home page
    path('', PostListView.as_view(), name='blog-home'),
    # The path to user posts
    path('user/<username>', UserPostListView.as_view(), name='user-posts'),
    # The path of a single post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # The path for creating a post
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    # The path for updating a post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # The path for deleting a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # The path to about page
    path('about/', views.about, name='blog-about'),
]