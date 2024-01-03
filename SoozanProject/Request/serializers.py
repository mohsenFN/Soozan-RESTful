from rest_framework import serializers
from Request.models import Request


class NewRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['artist', 'caption']
    
    def create(self, user, artist, validated_data):
        req = Request(user = user,
                        artist = artist,
                        caption = validated_data['caption'])
        return req




class ArtistRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['user', 'caption', 'status', 'pub_date']


class ApplicantRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['artist', 'caption', 'status', 'pub_date']