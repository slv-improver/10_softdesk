from rest_framework import serializers

from . import models


class ProjectListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Project
        fields = ('id', 'title', 'description', 'type')


class ProjectDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Project
        fields = ('id', 'title', 'description', 'type')
