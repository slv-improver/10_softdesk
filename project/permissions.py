from rest_framework.permissions import BasePermission
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from . import models


class IsContributorOrAuthor(BasePermission):

    def has_permission(self, request, view):
        r_user = request.user.id
        project = view.kwargs['project_id']
        
        try:
            user_permission = models.Contributor.objects.get(
                Q(user=r_user) & Q(project=project)
            ).permission
            if request.method == 'GET':
                # is contributor
                return user_permission == 'R' or user_permission == 'UD'
            else:
                # is author
                return user_permission == 'UD'
        except ObjectDoesNotExist:
            return False
