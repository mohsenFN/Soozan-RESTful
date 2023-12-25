from rest_framework import viewsets
from Artist.serializers import ArtistSerializer
from .models import Artist

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer