from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.utils import  IntegrityError


# TODO : don't forget to use permission classes instead of login_required
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from User.models import User
from User.serializers import UserSerializer

from Artist.models import Artist
from Artist.serializers import ArtistSerializer, ArtistDashBoardSerializer

from Applicant.models import Applicant
from Applicant.serializers import ApplicantDashBoardSerializer



# TODO: remove non-standard responses and use clean responses
# E.G: use HTTP response codes

@api_view(['GET'])
def SingleUserView(request: Request, user_id : int):
    try:
        queryset = User.objects.get(id = user_id)
    except User.DoesNotExist:
        return Response('user peyda nashod')

    serializer = UserSerializer(queryset)
    return Response(serializer.data)


@api_view(['POST'])
def Register(request : Request):
	# Passing user data to serializer
	user_serializer = UserSerializer(data = request.data, many = False)

	# TODO: check entered number is unique before validating

	if not user_serializer.is_valid():
		return Response("Invalid Data")
	
	# creating a user if data is valid
	user = user_serializer.create(user_serializer.validated_data)
	user.save()


	# creating user profile based on user data
	if user_serializer.validated_data['is_artist']:
		'''Artist'''
		profile = Artist(user = user)
	
	else:
		'''Applicant'''
		profile = Applicant(user = user)

	# saving derived profile model
	profile.save()
	
	# return more logical responses
	return Response(f'{user.id}, {user.number}')


@api_view(['POST'])
def Login(request : Request):
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


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def DashBoard(request : Request):

	user = User.objects.get(number = request.user.number)
	

	# TODD: try using views from each profile model not loading them here
	if request.user.is_artist:
		queryset = Artist.objects.get(user = user)
		serializer = ArtistDashBoardSerializer(queryset)
		return Response(serializer.data)

	else:
		queryset = Applicant.objects.get(user = user)
		serializer = ApplicantDashBoardSerializer(queryset)
		return Response(serializer.data)



@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def DeleteUser(request : Request):

	User.objects.get(number = request.user).delete()
	return Response('User Deleted',
					status=status.HTTP_200_OK)

	