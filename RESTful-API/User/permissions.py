from rest_framework.permissions import BasePermission

class IsArtistPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_artist


class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True

        # Write permissions are only allowed to the owner of the object.
        return obj.artist == request.user
