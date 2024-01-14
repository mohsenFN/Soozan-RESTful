from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.utils import  IntegrityError
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from rest_framework import status
from rest_framework.decorators import (
	api_view, authentication_classes, permission_classes
)
                                       
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from User.models import User
from User.serializers import UserSerializer

from Artist.models import Artist
from Artist.serializers import ArtistDashBoardSerializer

# TODO: remove non-standard responses and use clean responses


@api_view(['POST'])
def user_register(request : Request):
	# Passing user data to serializer
	serializer = UserSerializer(data = request.data, many = False)


	if not serializer.is_valid():
		breakpoint()
		if User.objects.filter(number = serializer.data['number']):
			return Response({'detail' : 'Phone numbers dedicated to an account already.'},
				   		status=status.HTTP_409_CONFLICT)
		
		return Response({'detail': 'Invalid data', 'errors': serializer.errors},
				  		status=status.HTTP_400_BAD_REQUEST)
	

	try:
		validate_password(serializer.data['password'])
	except ValidationError as e:
		return Response({'detail' : e.message},
				   		status=status.HTTP_400_BAD_REQUEST)

	
	# creating a user if data is valid
	user = serializer.create(serializer.validated_data)
	user.save()


	# creating user profile based on user data
	if serializer.validated_data['is_artist']:
		profile = Artist(user = user)
	
	else:
		return Response({'detail' : "Can't register Applicant users for a while."},
				  	status=status.HTTP_400_BAD_REQUEST)

	# saving derived profile model
	profile.save()
	
	# return more logical responses
	return Response({'detail' : f'Registered successfuly as {user.id} id.'},
				 	status=status.HTTP_200_OK)


@api_view(['POST'])
def user_login(request : Request):
	number = request.data.get('number')
	password = request.data.get('password')
	
	# checking user login data
	user = authenticate(request,username = number,
						password = password)
	

	if user:
		# serving users auth token
		token, created = Token.objects.get_or_create(user=user)

		return Response({'detail' : 'Login was successfull',
				   	'token': token.key},
					status=status.HTTP_200_OK)

	else:
		return Response({'detail' : 'Login Failed (Invalid password or username)'},
				  	status=status.HTTP_401_UNAUTHORIZED)



@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_user(request : Request):

	User.objects.get(number = request.user).delete()
	return Response('User Deleted',
					status=status.HTTP_200_OK)