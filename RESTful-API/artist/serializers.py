from artist.models import Artist
from rest_framework import serializers


class ArtistDashBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['user', 'full_name', 'art_name', 'location', 'soozan_score']