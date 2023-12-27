from Artist.models import Artist
from rest_framework import serializers


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'
    
    
    def create(self, user):
        #      (User Model Instance)
        artist = Artist(user = user,
                           full_name = validated_data['fullname'],
                           art_name = validated_data['art_name'],
                           validity = validated_data['validity'],
                           location = validated_data['location'],
                           )

        return artist




class ArtistDashBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['user', 'full_name', 'art_name', 'location', 'soozan_score']


class ArtistPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['fullname', 'art_name', 'location']

    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(ArtistPatchSerializer, self).__init__(*args, **kwargs)
