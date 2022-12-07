from rest_framework import serializers

from . import models


class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Project
        fields = ('title', 'description', 'type')
