from django.urls import path
from watchlist_app.api.views import (
    WatchListCreate,
    WatchDetail,
    StreamPlatformListCreate,
    StreamPlatformDetail,
    ReviewCreate,
    ReviewList,
    ReviewDetail
)


urlpatterns = [
    path("watchlist/", WatchListCreate.as_view(), name='list-create-watchlist'),
    path("watchlist/<int:pk>/", WatchDetail.as_view(), name='retrieve-update-destroy-watchdetail'),
    path("stream/", StreamPlatformListCreate.as_view(), name='list-create-streamplatform'),
    path("stream/<int:pk>/", StreamPlatformDetail.as_view(), name='retrieve-update-destroy-streamplatform'),
    path("watchlist/<int:pk>/review-create/", ReviewCreate.as_view(), name='create-review'),
    path("watchlist/<int:pk>/review/", ReviewList.as_view(), name='list-review'),
    path("watchlist/review/<int:pk>/", ReviewDetail.as_view(), name='retrieve-review'),
]
