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
def new_post_from_artist(request):
    serializer = UploadPostSerializer(data=request.data, context={'request': request})

    if serializer.is_valid():
        post = serializer.save()
        return Response({'detail': 'New post saved', 'post_id': post.id}, status=status.HTTP_201_CREATED)

    return Response({'detail': 'Invalid data', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)