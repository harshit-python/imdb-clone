from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from watchlist_app.models import WatchList, StreamPlatform, Review
from .serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer


# generic class based views
class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        watchlist_pk = self.kwargs['pk']
        watchlist_object = WatchList.objects.get(pk=watchlist_pk)
        serializer.save(watchlist=watchlist_object)


# generic class based views
class ReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer

    # overriding queryset
    def get_queryset(self):
        watchlist_pk = self.kwargs['pk']
        queryset = Review.objects.filter(watchlist=watchlist_pk)
        return queryset


# generic class based views
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
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
