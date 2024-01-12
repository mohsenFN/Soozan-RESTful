from rest_framework.decorators import (
	api_view, authentication_classes, permission_classes
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.authentication import TokenAuthentication

from User.permissions import IsArtistPermission

from Post.models import Tag
from Post.serializers import TagSerializer, UploadPostSerializer


@api_view(['GET'])
def get_tags_list(request : Request):
    queryset = Tag.objects.all()
    serializer = TagSerializer(queryset, many = True)
    return Response(serializer.data)



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsArtistPermission])
def new_post_from_artist(request : Request):

    serializer = UploadPostSerializer(data = request.data)

    if serializer.is_valid():
        post = serializer.create(user = request.user,
                                           validated_data=serializer.validated_data)
        
        post.save()
        return Response({'detail' : 'New post saved', 'post id' : post.id},
                        status=status.HTTP_201_CREATED)
    
    if serializer.data.get('image') in [None, '']:
        return Response({'detail' : 'No image file is specified'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    if serializer.data.get('caption') in [None, '']:
        return Response({'detail' : 'No caption is in form-data'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    if serializer.data.get('tags') in [None, '']:
        return Response({'detail' : 'No tags is in form-data'},
                        status=status.HTTP_400_BAD_REQUEST)

    return Response({'detail' : 'Invalid data.'})