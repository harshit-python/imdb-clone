from django.urls import path
# from .views import list_movies, retrieve_movie
from watchlist_app.api.views import MovieListAV, MovieDetailAV

# urlpatterns = [
#     path("", list_movies, name='list-movies'),
#     path("<int:pk>", retrieve_movie, name='retrieve-movie')
# ]

urlpatterns = [
    path("", MovieListAV.as_view(), name='list-movies'),
    path("<int:pk>", MovieDetailAV.as_view(), name='retrieve-movie')
]
