from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.response import  Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from . import serializers, models


class ProjectList(APIView):

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
        serializer = serializers.ProjectListSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.ProjectListSerializer(data=request.data)
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


class ProjectDetail(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, *args, **kwargs):
        User = get_user_model()
        project = get_object_or_404(
            models.Project,
            id=self.kwargs['project_id']
        )
        serializer = serializers.ProjectDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        project = get_object_or_404(
            models.Project,
            id=self.kwargs['project_id']
        )
        serializer = serializers.ProjectDetailSerializer(
            project,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        project = get_object_or_404(
            models.Project,
            id=self.kwargs['project_id']
        )
        project.delete()
        data = {'delete': 'ok'}
        return Response(data, status=status.HTTP_202_ACCEPTED)
