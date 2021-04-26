from django.urls import path
from . import views

app_name = 'movie_app'


urlpatterns = [
    path('', views.index, name="index"),
    path('all-movies/', views.all_movies, name="all-movies"),
] 


