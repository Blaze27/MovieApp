from django.db import models
from django.core.validators import RegexValidator
from django.utils.text import slugify
# Create your models here.



class Movie(models.Model):
    movie_title = models.CharField(max_length=200)
    prefix = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=2000)
    slug = models.SlugField(max_length=250)
    director = models.ManyToManyField('Director')
    studio = models.ForeignKey('Studio', on_delete=models.SET_NULL, null=True)
    released_date = models.DateField()
    cover_image = models.ImageField(upload_to="cover_image")
    review = models.CharField(max_length=200)
    genre = models.ManyToManyField('Genre')
    asin = models.CharField(max_length=10, validators=[RegexValidator(regex='^.{10}$', message='Length has to be 10', code='nomatch')])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.movie_title)

        return super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.movie_title
    


class Studio(models.Model):
    studio_title = models.CharField(max_length=200)
    prefix = models.CharField(max_length=200)
    website = models.URLField(max_length=200)
    slug = models.SlugField(max_length=250)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.studio_title)

        return super(Studio, self).save(*args, **kwargs)


    def __str__(self):
        return self.studio_title
    


class Genre(models.Model):
    genre_title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.genre_title)

        return super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.genre_title
    


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.DecimalField(max_digits=10, decimal_places=0)
    birth_date = models.DateField()
    website = models.URLField(max_length=200)

    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

