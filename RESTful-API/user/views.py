# Standard Library
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

# Django
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password

# Third-Party Packages
from rest_framework import status
from rest_framework.decorators import (
    api_view, authentication_classes, permission_classes
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import TokenError

# Local Imports
from user.jwt_utils import get_tokens, blacklist_token
from user.models import User
from user.serializers import UserSerializer
from artist.models import Artist
from artist.serializers import ArtistDashBoardSerializer
from applicant.models import Applicant
from utils.user_respones import RESPONSE_MESSAGES as MSG

@api_view(['POST'])
def user_register(request : Request):
    # Passing user data to serializer
    serializer = UserSerializer(data = request.data, many = False)


    if not serializer.is_valid():
        if serializer.data.get("number") == None:
            return Response({'detail' : MSG['NO_PHONE_NUMBER']}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(number = serializer.data['number']):
            return Response({'detail' : MSG['DUPLICATE_NUMBER']},
                        status=status.HTTP_409_CONFLICT)
        
        return Response({'detail': 'Invalid data', 'errors': serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)
    

    try:
        validate_password(serializer.validated_data['password'])
    except ValidationError as e:
        return Response({'detail' : e.messages},
                        status=status.HTTP_400_BAD_REQUEST)
    

    # Creating user profile based on user data
    if serializer.validated_data.get('is_artist'):
        user = serializer.save()
        Artist.objects.create(user=user)
    
    else:
        #user = serializer.save()
        #Applicant.objects.create(user = user)
        return Response({'detail' : "Can't register Applicant users for a while."},
                        status=status.HTTP_400_BAD_REQUEST)
    
    # Return more logical responses
    return Response({'detail' : MSG['REGISTER_OK'],
                    'user_id' : user.id},
                    status=status.HTTP_200_OK)


@api_view(['POST'])
def get_token(request: Request):
    number = request.data.get('number')
    password = request.data.get('password')

    # Checking user login data
    user = authenticate(request, username=number, password=password)

    if user:
        access_token, refresh_token = get_tokens(number, password)
        
        return Response({'access_token': access_token, 'refresh_token': refresh_token},
                        status=status.HTTP_200_OK)

    return Response({'detail' : MSG['AUTH_FAIL']}, status=status.HTTP_401_UNAUTHORIZED)

  
@api_view(['POST'])
def refresh_token(request : Request):
    refresh_token = request.data.get('refresh_token')

    if not refresh_token:
        return Response({'detail' : MSG['REFRESH_TOKEN_REQ']}, status=status.HTTP_400_BAD_REQUEST)

    try:
        refresh_token_obj = RefreshToken(refresh_token)
    except TokenError:
        return Response({'detail' : MSG['INVALID_REFRESH_TOKEN']}, status=status.HTTP_401_UNAUTHORIZED)

    user_id = refresh_token_obj.payload.get('user_id') # Used to get new refresh token based on user
    
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'detail' : MSG['INVALID_REFRESH_TOKEN']}, status=status.HTTP_401_UNAUTHORIZED)

    access_token = str(refresh_token_obj.access_token)
    refresh_token = str(RefreshToken.for_user(user))

    return Response({'access_token': access_token, 'refresh_token': refresh_token},
                    status=status.HTTP_200_OK)
    

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_user(request : Request):

    user = request.user
    user.delete()
    return Response({'detail' : MSG['DELETE_USER_OK']},
                status=status.HTTP_204_NO_CONTENT)



@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def user_logout(request : Request):    
    user_token = request.headers['Authorization'].split()[1]
    blacklist_token(user_token)
    return Response({'detail' : MSG['DELETE_USER_OK']}, status=status.HTTP_200_OK)

