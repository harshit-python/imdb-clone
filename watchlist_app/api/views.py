from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from watchlist_app.models import WatchList, StreamPlatform
from .serializers import WatchListSerializer, StreamPlatformSerializer


class StreamPlatformAV(APIView):

    def get(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamPlatformDetailAV(APIView):

    def get(self, request, pk):
        try:
            streamplatform_object = StreamPlatform.objects.get(pk=pk)
        except Exception as e:
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(streamplatform_object)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            streamplatform_object = StreamPlatform.objects.get(pk=pk)
        except Exception as e:
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(data=request.data, instance=streamplatform_object)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            streamplatform_object = StreamPlatform.objects.get(pk=pk)
        except Exception as e:
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        streamplatform_object.is_active = False
        streamplatform_object.is_deleted = True
        streamplatform_object.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class based views
class WatchListAV(APIView):

    def get(self, request):
        queryset = WatchList.objects.all()
        serializer = WatchListSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchDetailAV(APIView):

    def get(self, request, pk):
        try:
            watchlist_object = WatchList.objects.get(pk=pk)
        except Exception as e:
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(watchlist_object)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            watchlist_object = WatchList.objects.get(pk=pk)
        except Exception as e:
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(data=request.data, instance=watchlist_object)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            watchlist_object = WatchList.objects.get(pk=pk)
        except Exception as e:
            return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
        watchlist_object.is_active = False
        watchlist_object.is_deleted = True
        watchlist_object.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
