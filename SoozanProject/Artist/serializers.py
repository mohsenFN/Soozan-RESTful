from Artist.models import DerivedArtist
from rest_framework import serializers


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = DerivedArtist
        fields = '__all__'