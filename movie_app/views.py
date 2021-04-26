from django.shortcuts import render
from .models import Movie, Studio, Genre, Director, Review
from django.conf import settings
from django.templatetags.static import static
import os
# Create your views here.

def index(request):
    return render(request, 'index.html')



def all_movies(request):
    all_movie = Movie.objects.all()
    context = {
        'all_movie' : all_movie,
    }

    return render(request, 'movie_app/all_movies.html', context=context)














