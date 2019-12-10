from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('profile/',views.profile,name='profile'),
    path('update_profile/',views.update_profile,name='update_profile'),

]