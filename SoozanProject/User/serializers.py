from User.models import User
from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth.hashers import make_password

from Artist.models import Artist

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'number', 'is_artist']

    def create(self, validated_data):
        user =  User(password = make_password(validated_data['password']),
        				number = validated_data['number'],
        				is_artist = validated_data['is_artist'],
        				date_joined = timezone.now())

        return user
