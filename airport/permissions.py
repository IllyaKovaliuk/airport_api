from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIsAuthenticatedReadOnly(BasePermission):

    def has_permission(self, request, view):
        return (bool(request.method in SAFE_METHODS and request.user and request.user.is_authenticated)
                or
                (request.user and request.user.is_staff))

class IsAdminOrReadOnly(BasePermission):
        def has_permission(self, request, view):
            return bool(
                request.method in SAFE_METHODS or
                request.user and
                request.user.is_staff
            )