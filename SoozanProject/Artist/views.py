from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from User.models import User


@api_view(['GET'])
def artist_profile(request : Request, user_id : int):

    # check if user exists 

    try:
        user = User.objects.get(id = user_id)

    except User.DoesNotExist:
        return Response({'detail' : 'Artist does not exist'},
                        status=status.HTTP_404_NOT_FOUND)
    
    # check if user is artist


    if not user.is_artist:
        return Response({'detail' : 'Artist does not exist'},
                        status=status.HTTP_404_NOT_FOUND)

    return Response(user_id)

    


