from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
        OWNER에게만 쓰기, 읽기 허용
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.owner is not None:
            return True
