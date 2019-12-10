from django.db import models


# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length=268)
    release_date = models.DateField()
    box_office = models.DecimalField(decimal_places=0, max_digits=11)
    duration = models.IntegerField()
    language = models.CharField(max_length=100)
    overview = models.TextField()
    genre = models.TextField()
    casts = models.TextField()
    rate = models.FloatField()
    director = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.movie_name
