from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from User.models import User
from .serializers import *

from Request.models import Request


'''
how to send req
artist --> artist pk
caption --> kossher
'''
@login_required
@api_view(['POST'])
def NewRequest(request : Request):
    user = request.user # user phonenumber

    if request.user.is_artist == True:
        return Response('artists can only recive reqs not send them !')
    

    serializer = NewRequestSerializer(data = request.data)

    if not serializer.is_valid():
        return Response('Invalid data')
    
    user = User.objects.get(number = request.user)

    artist = serializer.validated_data['artist']
    
    req = serializer.create(user = user, artist = artist, validated_data = serializer.validated_data)
    req.save()
    return Response('request saved')



@login_required
@api_view(['GET'])
def ListRequests(request : Request):
    if request.user.is_artist:
        queryset = Request.objects.filter(artist = request.user)
        serializer = ArtistRequestsSerializer(queryset, many = True)
        return Response(serializer.data)
    
    else:
        queryset = Request.objects.filter(user = request.user)
        serializer = ApplicantRequestsSerializer(queryset, many = True)
        return Response(serializer.data)



