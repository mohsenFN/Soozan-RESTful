from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer 

from .models import BlacklistedToken

class BlacklistTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        authorization_header = request.META.get('HTTP_AUTHORIZATION', '')
        
        if authorization_header.startswith('Bearer '):
            # Extract token from the authorization header
            token = authorization_header.split(' ')[1]

            if BlacklistedToken.objects.filter(token=token).exists():
                # Token is blacklisted, handle accordingly (e.g., return 401 Unauthorized)

                resp = Response("Token is blacklisted", status=status.HTTP_200_OK)
                resp.accepted_renderer = JSONRenderer()
                resp.accepted_media_type = 'application/json'
                resp.renderer_context = {}
                resp.render()
                return resp


        response = self.get_response(request)
        return response
