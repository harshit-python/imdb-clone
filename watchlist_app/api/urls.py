from django.urls import path
from watchlist_app.api.views import (
    WatchListAV,
    WatchDetailAV,
    StreamPlatformAV,
    StreamPlatformDetailAV,
    ReviewCreate,
    ReviewList,
    ReviewDetail
)


urlpatterns = [
    path("watchlist/", WatchListAV.as_view(), name='list-create-watchlist'),
    path("watchlist/<int:pk>/", WatchDetailAV.as_view(), name='retrieve-update-destroy-watchdetail'),
    path("stream/", StreamPlatformAV.as_view(), name='list-create-streamplatform'),
    path("stream/<int:pk>/", StreamPlatformDetailAV.as_view(), name='retrieve-update-destroy-streamplatform'),
    path("watchlist/<int:pk>/review-create/", ReviewCreate.as_view(), name='create-review'),
    path("watchlist/<int:pk>/review/", ReviewList.as_view(), name='list-review'),
    path("watchlist/review/<int:pk>/", ReviewDetail.as_view(), name='retrieve-review'),
]
