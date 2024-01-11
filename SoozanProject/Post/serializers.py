from rest_framework import serializers
from Post.models import Post, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class UploadPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'