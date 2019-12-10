from django.contrib import admin
from movie.models import Movie
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    fields = ['movie_name', 'release_date',
              'box_office', 'duration', 'language', 'genre', 'casts',
              'rate', 'director', 'overview', ]

    search_fields = ['movie_name', 'language', 'director', 'genre', 'casts', ]

    list_filter = ['release_date', 'genre', 'rate', ]

    list_display = ['movie_name', 'release_date',
                    'rate', 'director', 'language', 'genre', ]


admin.site.register(Movie, MovieAdmin)
