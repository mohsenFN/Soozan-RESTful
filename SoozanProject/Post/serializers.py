from rest_framework import serializers
from Post.models import Post, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'



class UploadPostSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(child=serializers.IntegerField())

    class Meta:
        model = Post
        fields = ['caption', 'tags', 'image']

    def create(self, user, validated_data):
        tag_ids = validated_data.pop('tags', [])
        tags = Tag.objects.filter(id__in=tag_ids)
        post = Post.objects.create(artist = user, **validated_data)
        post.tags.set(tags)
        return post