from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies_list, name='movies_list'),
    path('movie/', views.movie_detail, name='movie_detail'),
    path('add/', views.add_movie, name='add_movie'),
    path('edit/', views.edit_movie, name='edit_movie'),
    path('delete/', views.delete_movie, name='delete_movie'),
]