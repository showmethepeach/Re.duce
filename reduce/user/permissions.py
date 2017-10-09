from rest_framework import permissions

class IsAuthenticatedOrWriteOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.method == 'POST' or
            request.user and
            request.user.is_authenticated
        )
