from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from Post.models import Tag
from Post.serializers import TagSerializer


@api_view(['GET'])
def get_tags_list(request : Request):
    queryset = Tag.objects.all()

    serializer = TagSerializer(queryset)

    return Response(serializer.data)