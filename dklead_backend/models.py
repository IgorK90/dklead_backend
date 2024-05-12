from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_data = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team_photos/')

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completion_date = models.DateField()
    team = models.ManyToManyField(TeamMember)
    thumbnail = models.ImageField(upload_to='project_thumbnails/')

class Contact(models.Model):
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=255)

class About(models.Model):
    content = models.TextField()
    mission = models.CharField(max_length=255)
    vision = models.CharField(max_length=255)

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    received_date = models.DateField(auto_now=True)