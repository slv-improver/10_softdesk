from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):

    def has_permission(self, request, view):
        r_user = request.user
        return 
