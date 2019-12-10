from django.urls import path, include
from review import views

app_name = 'review'

urlpatterns = [
    path('',views.ReviewListView.as_view(),name='list'),
    path('<int:pk>/',views.ReviewDetailView.as_view(),name='detail'),
    path('create_review/', views.create_review, name='create_review'),


]