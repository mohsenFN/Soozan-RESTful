from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.utils import  IntegrityError

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.parsers import JSONParser


from User.models import User
from User.serializers import UserSerializer

from Artist.models import Artist
from Artist.serializers import ArtistSerializer, ArtistDashBoardSerializer

from Applicant.models import Applicant
from Applicant.serializers import ApplicantDashBoardSerializer






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


	profile.save()
	
	# return more logical responses
	return Response(f'{user.id}, {user.number}')


@api_view(['GET'])
def Login(request : Request):
	number = request.data['number']
	password = request.data['password']
	
	user = authenticate(request,username = number,
						password = password)
	
	if user:
		login(request, user)
		print(request.user.is_authenticated)
		
		return Response('Welcome')

	else:
		print(request.user.is_authenticated)
		return Response('Invalid info')


@api_view(['GET'])
def Logout(request : Request):

	logout(request)
	return Response('Logged out.')



@login_required()
@api_view(['GET'])
def dashboard(request : Request):
	print(type(request.user), request.user)

	serializer = None
	queryset = None

	user = User.objects.get(number = request.user)

	if request.user.is_artist:
		queryset = Artist.objects.get(user = user)
		serializer = ArtistDashBoardSerializer(queryset)
		return Response(serializer.data)

	else:
		queryset = Applicant.objects.get(user = user)
		serializer = ApplicantDashBoardSerializer(queryset)
		return Response(serializer.data)

