from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from user.models import User

from utils.user_respones import ARTIST_RESPONES

@api_view(['GET'])
def artist_profile(request: Request, user_id: int):

    # Check if user exists
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'detail': ARTIST_RESPONES['USER_DOESNOTEXIST']}, status=status.HTTP_404_NOT_FOUND)

    # If user is not artist send an error message
    if not user.is_artist:
        return Response({'detail': ARTIST_RESPONES['USER_DOESNOTEXIST']}, status=status.HTTP_404_NOT_FOUND)

    # Return artist's profile (or other relevant data)
    return Response({'user_id': user_id})