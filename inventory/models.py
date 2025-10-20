from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Video(models.Model):
    GENRES = [
        ('COMEDY', 'Comedy'),
        ('ROMANCE', 'Romance'),
        ('ACTION', 'Action'),
        ('DRAMA', 'Drama'),
        ('SCIFI', 'Sci-Fi'),
        ('HORROR', 'Horror'),
        ('OTHER', 'Other'),
    ]

    movie_id = models.CharField(max_length=20, unique=True, verbose_name="MovieID")
    movie_title = models.CharField(max_length=200, verbose_name="MovieTitle")
    actor1_name = models.CharField(max_length=100, verbose_name="Actor1Name")
    actor2_name = models.CharField(max_length=100, blank=True, verbose_name="Actor2Name")
    director_name = models.CharField(max_length=100, verbose_name="DirectorName")
    movie_genre = models.CharField(max_length=20, choices=GENRES, verbose_name="MovieGenre")
    release_year = models.PositiveIntegerField(
        validators=[MinValueValidator(1888), MaxValueValidator(2100)],
        verbose_name="ReleaseYear"
    )

    def __str__(self):
        return f"{self.movie_title} ({self.release_year})"
