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

# Local Imports
from user.jwt_utils import get_tokens
from user.models import User
from user.serializers import UserSerializer
from artist.models import Artist
from artist.serializers import ArtistDashBoardSerializer


@api_view(['POST'])
def user_register(request : Request):
	# Passing user data to serializer
	serializer = UserSerializer(data = request.data, many = False)


	if not serializer.is_valid():
		if User.objects.filter(number = serializer.data['number']):
			return Response({'detail' : 'Phone numbers dedicated to an account already.'},
				   		status=status.HTTP_409_CONFLICT)
		
		return Response({'detail': 'Invalid data', 'errors': serializer.errors},
				  		status=status.HTTP_400_BAD_REQUEST)
	

	try:
		validate_password(serializer.validated_data['password'])
	except ValidationError as e:
		return Response({'detail' : e.messages},
				   		status=status.HTTP_400_BAD_REQUEST)
	

	# Creating user profile based on user data
	if serializer.validated_data.get('is_artist', False):
		user = serializer.save()
		Artist.objects.create(user=user)
	
	else:
		return Response({'detail' : "Can't register Applicant users for a while."},
				  		status=status.HTTP_400_BAD_REQUEST)
	
	# Return more logical responses
	return Response({'detail' : f'Registered successfuly as {user.id} id.'},
				 	status=status.HTTP_200_OK)


@api_view(['POST'])
def user_login(request: Request):
    number = request.data.get('number')
    password = request.data.get('password')

    # Checking user login data
    user = authenticate(request, username=number, password=password)

    if user:
	    access_token, refresh_token = get_tokens(number, password)
	    
	    return Response({'access_token': access_token, 'refresh_token': refresh_token},
	                    status=status.HTTP_200_OK)

    return Response({'detail' : 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)

  
@api_view(['POST'])
def new_token(request : Request):
	refresh_token = request.data.get('refresh_token')

	if not refresh_token:
		return Response({'detail' : 'Refresh token is required.'}, status=status.HTTP_400_BAD_REQUEST)

	try:
		refresh_token_obj = RefreshToken(refresh_token)
	except Exception as e:
		return Response({'detail' : 'Invalid refresh token.'}, status=status.HTTP_401_UNAUTHORIZED)

	user_id = refresh_token_obj.payload.get('user_id') # Used to get new refresh token based on user

	# NOTE: I'm not sure this error handling in below lines is a good practice or no !n
	try:
		user = User.objects.get(id=user_id)
	except User.DoesNotExist:
		return Response({'detail' : 'Invalid refresh token.'}, status=status.HTTP_401_UNAUTHORIZED)

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
	return Response({'detail' : 'User deleted successfully.'},
				status=status.HTTP_204_NO_CONTENT)