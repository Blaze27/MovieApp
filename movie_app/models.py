from django.db import models
from django.core.validators import RegexValidator
from django.utils.text import slugify
from django.core.files.storage import FileSystemStorage
from django.conf import settings
# Create your models here.

image_storage = FileSystemStorage(
    location=u'{0}/cover_image/'.format(settings.MEDIA_ROOT),
    base_url=u'{0}cover_image/'.format(settings.MEDIA_URL),
)


def image_directory_path(instance, filename):
    return u'{0}'.format(filename)

class Movie(models.Model):
    movie_title = models.CharField(max_length=200)
    prefix = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=2000)
    slug = models.SlugField(max_length=250)
    director = models.ManyToManyField('Director')
    studio = models.ForeignKey('Studio', on_delete=models.SET_NULL, null=True)
    released_date = models.DateField()
    cover_image = models.ImageField(upload_to=image_directory_path, storage=image_storage)
    genre = models.ManyToManyField('Genre')
    asin = models.CharField(max_length=10, validators=[RegexValidator(regex='^.{10}$', message='Length has to be 10', code='nomatch')])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.movie_title)

        return super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.movie_title

    def amazon_url(self):
        return "https://www.amazon.com/dp/" + self.asin
    


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
    middle_name = models.CharField(max_length=100, blank=True)
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


class Review(models.Model):
    review = models.CharField(max_length=500)
    movie_name = models.ForeignKey('Movie', on_delete=models.CASCADE)

