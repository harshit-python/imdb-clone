from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAdminUser):
    # this class allows only the GET request or the Admin user

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)


class ReviewUserOrReadOnly(permissions.BasePermission):
    # this class allows only GET request or case when logged-in user is the reviewer

    # using object level permission
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.reviewer == request.user or request.user.is_staff
