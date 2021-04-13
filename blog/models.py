from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # Posts inherit from User
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return how we want this to be printed out"""
        return self.title

    # Return to the post after creating one
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

