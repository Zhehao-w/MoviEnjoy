from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from movie.models import Movie

# Create your models here.


class Review(models.Model):
    movie = models.ForeignKey(
        Movie, related_name='reviews', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("review_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    review = models.ForeignKey(
        Review, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    content = models.TextField()
    comment_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content
