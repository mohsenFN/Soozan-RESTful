from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from Artist.serializers import *
from Artist.models import Artist

from User.models import User

from Request.models import Request
from Request.serializers import ArtistRequestsSerializer


'''
this modules has some major problems
'''
@login_required
@api_view(['PATCH'])
def UpdateArtist(request : Request):
    queryset = User.objects.get(number = request.user)
    print(request.user)
    serializer = ArtistPatchSerializer(data = queryset)
    
    if serializer.is_valid():
        serializer.update()
    else:
        return Response('Invalid')

    return Response('hey')


@login_required
@api_view(['GET'])
def GetRequests(request : Request):
    if 
    
    if not request.user.is_artist:
        return Response('inke artist nist xarkosee')
    

    queryset = Request.objects.filter(pk = request.user.id)

    serializer = ArtistRequestsSerializer(queryset)
    
    return Response(serializer)



