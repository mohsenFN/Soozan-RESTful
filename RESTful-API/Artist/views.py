from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from User.models import User


@api_view(['GET'])
def artist_profile(request: Request, user_id: int):

    # Check if user exists
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'detail': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # If user is not artist send an error message
    if not user.is_artist:
        return Response({'detail': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # Return artist's profile (or other relevant data)
    return Response({'user_id': user_id})