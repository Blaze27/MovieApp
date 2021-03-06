# Generated by Django 3.2 on 2021-04-26 05:46

import django.core.files.storage
from django.db import migrations, models
import movie_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_alter_director_middle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cover_image',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(base_url='/media/cover_image/', location='/home/hp/Documents/github/movie/media/cover_image/'), upload_to=movie_app.models.image_directory_path),
        ),
    ]
