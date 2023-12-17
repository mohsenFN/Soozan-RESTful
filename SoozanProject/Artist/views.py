from rest_framework import viewsets
from Artist.serializers import ArtistSerializer
from .models import DerivedArtist

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = DerivedArtist.objects.all()
    serializer_class = ArtistSerializer