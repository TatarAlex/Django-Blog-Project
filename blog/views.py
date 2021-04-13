from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.models import User


def home(request):
    # Display posts
    context ={
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


# A class to list our posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/ <model>_<viewtype>.html
    context_object_name = 'posts'
    # Change the order of posts
    ordering = ['-date_posted']
    # Pagination functionality (How many posts per page)
    paginate_by = 5

# A class to list the user posts
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # <app>/ <model>_<viewtype>.html
    context_object_name = 'posts'
    # Pagination functionality (How many posts per page)
    paginate_by = 5

    # Checks if user exists if not get 404
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')




# Looking at a single post view
class PostDetailView(DetailView):
    model = Post


# Create posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        # Set the author as the current logged in user
        form.instance.author = self.request.user
        # Running form_valid function on the parent class
        return super().form_valid(form)


# Update posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        # Set the author as the current logged in user
        form.instance.author = self.request.user
        # Running form_valid function on the parent class
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        # Checking if the current user is the author of the post
        if self.request.user == post.author:
            return True
        return False


# Delete a view
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        # Checking if the current user is the author of the post
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


