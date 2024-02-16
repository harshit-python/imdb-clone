from django.urls import path
from watchlist_app.api.views import (
    WatchListAV,
    WatchDetailAV,
    StreamPlatformAV,
    StreamPlatformDetailAV
)


urlpatterns = [
    path("watchlist/", WatchListAV.as_view(), name='list-create-watchlist'),
    path("watchlist/<int:pk>/", WatchDetailAV.as_view(), name='retrieve-update-destroy-watchdetail'),
    path("streamplatform/", StreamPlatformAV.as_view(), name='list-create-streamplatform'),
    path("streamplatform/<int:pk>/", StreamPlatformDetailAV.as_view(), name='retrieve-update-destroy-streamplatform'),
    path("streamplatform/<int:pk>/", StreamPlatformDetailAV.as_view(), name='retrieve-update-destroy-streamplatform'),
    path("streamplatform/<int:pk>/", StreamPlatformDetailAV.as_view(), name='retrieve-update-destroy-streamplatform'),
]
