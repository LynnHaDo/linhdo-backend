from django.db import models
from datetime import datetime

# Create your models here.
"""
Represents a list of projects
"""
class ProjectModelList(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
    
"""
Represents a project
"""
class ProjectModel(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(default="Project Description Unavailable")
    imageUrl = models.TextField(default="../../../assets/logo.png")
    githubUrl = models.URLField(default="https://github.com/LynnHaDo")
    languages = models.TextField(default="HTML,CSS,TypeScript,JavaScript,Java,Python,R")
    frameworks = models.TextField(default="Angular,Spring Boot,PyTorch,Django,JavaFx,matplotlib,numpy,albumentations,Open CV")
    dateCreated = models.DateField(default=datetime.now())
    dateFinished = models.DateField(default=datetime.now())
    projectList = models.ForeignKey(ProjectModelList, on_delete = models.CASCADE, related_name="projects")

    def __str__(self):
        return self.title + " " + ": " + self.githubUrl