# Generated by Django 3.2 on 2021-04-26 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_auto_20210424_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='middle_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]