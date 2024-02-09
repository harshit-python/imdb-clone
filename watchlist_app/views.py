from django.http import JsonResponse
from .models import Movie


# Create your views here.
def list_movies(request):
    movies = Movie.objects.all()
    data = {"results": list(movies.values())}
    return JsonResponse(data)


def retrieve_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        'name': movie.name,
        'description': movie.description,
        'is_active': movie.is_active
    }
    return JsonResponse(data)
