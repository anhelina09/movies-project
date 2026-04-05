from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва жанру")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанри"


class Actor(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Ім'я та прізвище")
    bio = models.TextField(blank=True, verbose_name="Біографія")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата народження")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Актор"
        verbose_name_plural = "Актори"


class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name="Назва фільму")
    description = models.TextField(verbose_name="Опис")
    release_year = models.PositiveIntegerField(verbose_name="Рік випуску")
    
    # Зв'язки ManyToMany
    genres = models.ManyToManyField(Genre, related_name="movies", verbose_name="Жанри")
    actors = models.ManyToManyField(Actor, related_name="movies", verbose_name="Актори")
    
    poster = models.ImageField(upload_to='posters/', null=True, blank=True, verbose_name="Постер")

    def __str__(self):
        return f"{self.title} ({self.release_year})"

    class Meta:
        verbose_name = "Фільм"
        verbose_name_plural = "Фільми"