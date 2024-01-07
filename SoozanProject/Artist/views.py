from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from Artist.serializers import *
from Artist.models import Artist

from User.models import User


