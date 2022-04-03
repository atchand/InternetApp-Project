from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Movie(models.Model):
    movieid = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500, null=True)
    duration = models.IntegerField(blank=True, null=True)
    votes = models.IntegerField(blank=True, null=True)
    gross_earning_in_mil = models.FloatField(blank=True, null=True, default=None)
    director = models.ForeignKey('Director', related_name='directed_movies', on_delete=models.CASCADE, null=True, blank=True)
    actor = models.ForeignKey('Actor', related_name='acted_movies', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])

    def __str__(self) -> str:
        return self.title

class Director(models.Model):
    name = models.CharField(max_length=100)
    person_link = models.URLField(max_length=500, null=True, default=None)

    def __str__(self) -> str:
        return self.name
   
class Actor(models.Model):
    name = models.CharField(max_length=100)
    person_link = models.URLField(max_length=500, null=True, default=None)

    def __str__(self) -> str:
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)
    movie = models.ManyToManyField(Movie, related_name='genre_movies')

    def __str__(self) -> str:
        return self.name


