from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from watchlist_app.models import WatchList, StreamPlatform, Review
from .serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import AdminOrReadOnly, ReviewUserOrReadOnly


# generic class based views
class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        watchlist_pk = self.kwargs['pk']
        watchlist_object = WatchList.objects.get(pk=watchlist_pk)

        if watchlist_object.number_of_ratings == 0:
            # case when there are no ratings for current watchlist object
            watchlist_object.avg_rating = serializer.validated_data['rating']
        else:
            # case when there are already ratings present for current watchlist object
            watchlist_object.avg_rating = (watchlist_object.avg_rating + serializer.validated_data['rating'])/2
        # increasing number of ratings for current watchlist object by 1
        watchlist_object.number_of_ratings = watchlist_object.number_of_ratings + 1
        watchlist_object.save()
        serializer.save(
            watchlist=watchlist_object,
            reviewer=self.request.user
        )


# generic class based views
class ReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    # overriding queryset
    def get_queryset(self):
        watchlist_pk = self.kwargs['pk']
        queryset = Review.objects.filter(
            watchlist=watchlist_pk,
            reviewer=self.request.user
        )
        return queryset


# generic class based views
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        # adding a check that only the correct reviewer can update their review.
        if instance.reviewer != self.request.user:
            raise PermissionDenied("You don't have permission to update this review.")
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            # updating watchlist avg review and total review count
            update_watchlist_review(
                watchlist_pk=instance.watchlist.pk,
                rating=request.data['rating'],
                review_old_rating=instance.rating
            )
            serializer.save()
            return Response(serializer.validated_data)

    # adding object level permission
    permission_classes = [ReviewUserOrReadOnly]


class ListAllReviews(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# using ModelViewSet
class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer


# generic class based views
class WatchListCreate(generics.ListCreateAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer


# generic class based views
class WatchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer


def update_watchlist_review(
    watchlist_pk: int,
    rating: int,
    review_old_rating: int,
):
    """
    Method to update watchlist avg ratings
    :param watchlist_pk:
    :param rating:
    :param review_old_rating:
    :return:
    """
    if rating != review_old_rating:
        watchlist_object = WatchList.objects.get(pk=watchlist_pk)
        review_difference = rating - review_old_rating
        avg_rating = (watchlist_object.number_of_ratings * watchlist_object.avg_rating + review_difference) / 2
        watchlist_object.avg_rating = avg_rating
        watchlist_object.save()


# # using viewsets
# # calling this viewset using router in urls
# class StreamPlatformVS(viewsets.ViewSet):
#
#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         streamplatform_object = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(streamplatform_object)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#     def put(self, request, pk):
#         try:
#             stream_object = StreamPlatform.objects.get(pk=pk)
#         except Exception as e:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = StreamPlatformSerializer(data=request.data, instance=stream_object)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#     def destroy(self, request, pk):
#         try:
#             stream_object = StreamPlatform.objects.get(pk=pk)
#             stream_object.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Exception as e:
#             return Response(status=status.HTTP_404_NOT_FOUND)
