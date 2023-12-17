from rest_framework import viewsets
from User.serializers import UserSerializer
from User.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer