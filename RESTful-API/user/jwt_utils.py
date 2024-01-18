from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

def get_tokens(number, password):
    # Function to obtain tokens and handle token refresh logic
    credentials = {'number': number, 'password': password}
    serializer = TokenObtainPairSerializer(data=credentials)
    
    serializer.is_valid(raise_exception=True)
    
    tokens = serializer.validated_data
    access_token = tokens['access']
    refresh_token = tokens['refresh']

    # TODO: checking if the refresh token is about to expire and obtaining a new one

    return access_token, refresh_token
