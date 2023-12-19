from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from User.serializers import UserSerializer
from User.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def SingleUserView(request: Request, user_id : int):
    try:
        queryset = User.objects.get(id = user_id)
    except User.DoesNotExist:
        return Response('user peyda nashod')
    data = UserSerializer(queryset).data
    
    return Response(data)


