from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('',views.MovieListView.as_view(),name='list'),
    path('<int:pk>/',views.MovieDetailView.as_view(),name='detail'),
]