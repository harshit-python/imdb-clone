from django.urls import path
from .views import list_movies, retrieve_movie

urlpatterns = [
    path("", list_movies, name='list-movies'),
    path("<int:pk>", retrieve_movie, name='retrieve-movie')
]
