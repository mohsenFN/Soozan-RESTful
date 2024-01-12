from rest_framework.decorators import (
	api_view, authentication_classes, permission_classes
)

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
        return Response({'detail' : 'data saved'})
    
    # TODO: validate more defined and send explained error msgs
    return Response({'detail' : 'Invalid data.'})
    
    
    