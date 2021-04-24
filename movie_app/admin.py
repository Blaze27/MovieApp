from django.contrib import admin
from .models import Movie, Director, Genre, Studio

# Register your models here.

all_model = [
    Movie,
    Director,
    Genre,
    Studio,
]

for _ in all_model:
    admin.site.register(_)
