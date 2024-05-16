from rest_framework import serializers
from .models import News, TeamMember, Project, Contact, About, Feedback


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
    # title = serializers.CharField(max_length=255)
    # content = serializers.TextField()
    # published_data = serializers.DateTimeField()
    # author = serializers.CharField(source = 'user.name', max_length=100)

class CreateNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'content', 'author']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'

class CreateTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['name','position','bio']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title','description','completion_date']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'