from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Artist
from Artist.serializers import ArtistSerializer


@login_required
@api_view(['PATCH'])
def UpdateArtist(request : Request):
    return Response('hey')
