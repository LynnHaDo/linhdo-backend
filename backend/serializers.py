from rest_framework import serializers
from backend.models import *

class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = ('id', 'projectList','title', 'description', 'imageUrl', 'githubUrl', 'languages', 'frameworks', 'dateCreated', 'dateFinished')

class ProjectModelListSerializer(serializers.ModelSerializer):
    projects = ProjectModelSerializer(many=True)

    def create(self, validated_data):
        projects_data = validated_data.pop("projects")
        projects = ProjectModelList.objects.create(**validated_data)
        for project in projects_data:
            ProjectModel.objects.create(projectList=projects, **project)
        return projects

    class Meta:
        model = ProjectModelList
        fields = ('id','name', 'projects')