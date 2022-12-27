from rest_framework import serializers

from . import models


class ContributorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Contributor
        fields = ('id', 'user', 'project')


class ProjectListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Project
        fields = ('id', 'title', 'description', 'type')


class ProjectDetailSerializer(serializers.ModelSerializer):

    contributors = serializers.SerializerMethodField()

    class Meta:
        model = models.Project
        fields = ('id', 'title', 'description', 'type', 'contributors')

    def get_contributors(self, instance):
        queryset = models.Contributor.objects.filter(project_id=instance.id)
        serializer = ContributorListSerializer(queryset, many=True)
        return serializer.data
