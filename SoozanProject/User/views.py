from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from User.serializers import UserSerializer
from Artist.serializers import ArtistSerializer
from User.models import User
from Applicant.models import Applicant
from Artist.models import Artist
from django.db.utils import  IntegrityError

from User.validators import UserValidator

from rest_framework.parsers import JSONParser

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
	
	return Response(f'{user.id}, {user.number}')


@api_view(['GET'])
def Signin(request : Request):
	number = request.data['number']
	password = request.data['password']

	return Response('LOGIN view')






