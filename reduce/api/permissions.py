from rest_framework import permissions

class IsCustomer(permissions.BasePermission):
    """
        OWNER에게만 쓰기, 읽기 허용
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.customer is not None:
            return True

class IsReviewWriter(permissions.BasePermission):
    """
        읽기는 모두 가능
        수정/삭제는 댓글 작성자만 허용
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.customer == request.user.customer:
            return True


class IsOrderer(permissions.BasePermission):
    """
        주문자만 정보 확인 가능
    """
    def has_object_permission(self, request, view, obj):
        if obj.customer == request.user.customer:
            return True
