from rest_framework.response import Response
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from watchlist_app.models import Movie
from .serializers import MovieSerializer


# # function based views
# @api_view(['GET', 'POST'])
# def list_movies(request):
#
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def retrieve_movie(request, pk):
#
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Exception as e:
#             return Response({"error": "movie not found"}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#
#     if request.method == 'PUT':
#         try:
#             old_movie = Movie.objects.get(pk=pk)
#         except Exception as e:
#             return Response({"error": "movie not found"}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(data=request.data, instance=old_movie)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == "DELETE":
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Exception as e:
#             return Response({"error": "movie not found"}, status=status.HTTP_404_NOT_FOUND)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class based views
class MovieListAV(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailAV(APIView):

    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Exception as e:
            return Response({"error": "movie not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Exception as e:
            return Response({"error": "movie not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(data=request.data, instance=movie)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Exception as e:
            return Response({"error": "movie not found"}, status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
