from rest_framework.throttling import UserRateThrottle


class ReviewCreateThrottle(UserRateThrottle):
    scope = 'create-review'   # this is the name of key in settings.py


class ReviewListThrottle(UserRateThrottle):
    scope = 'list-review'
