from rest_framework.permissions import BasePermission


class JustPostForUnidentified(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'post':
            return True
        else:
            return request.user.is_staff
