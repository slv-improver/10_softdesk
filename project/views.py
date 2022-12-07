from django.contrib.auth import get_user_model
from rest_framework.response import  Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from . import serializers, models


class ProjectAPIView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        User = get_user_model()
        projects = models.Project.objects.filter(
            contributor__in=models.Contributor.objects.filter(
                user=request.user
            )
        )
        serializer = serializers.ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.ProjectSerializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save()
            models.Contributor.objects.create(
                user=request.user,
                project=project,
                permission='UD',
                role='AU'
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
