from django.contrib import admin
from .models import Movie, Genre, Actor

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'get_genres')
    search_fields = ('title', 'description')
    list_filter = ('release_year', 'genres')
    filter_horizontal = ('genres', 'actors') 

    def get_genres(self, obj):
        return ", ".join([g.name for g in obj.genres.all()])
    get_genres.short_description = 'Жанри'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_date')