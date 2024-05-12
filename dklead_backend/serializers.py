from rest_framework import serializers
from .models import News

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
