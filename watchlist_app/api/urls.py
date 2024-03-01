from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import (
    WatchListCreate,
    WatchDetail,
    StreamPlatformVS,
    ReviewCreate,
    ReviewList,
    ReviewDetail,
    ListAllReviews,
    UserReview,
)
# using routers
router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')


urlpatterns = [
    path("watchlist/", WatchListCreate.as_view(), name='list-create-watchlist'),
    path("watchlist/<int:pk>/", WatchDetail.as_view(), name='retrieve-update-destroy-watchdetail'),
    path('', include(router.urls)),
    path("watchlist/<int:pk>/review-create/", ReviewCreate.as_view(), name='create-review'),
    path("watchlist/<int:pk>/review/", ReviewList.as_view(), name='list-review'),
    path("watchlist/list-all-reviews/", ListAllReviews.as_view(), name='list-all-reviews'),
    path("watchlist/review/<int:pk>/", ReviewDetail.as_view(), name='retrieve-review'),
    path("review/", UserReview.as_view(), name='user-review'),
]
