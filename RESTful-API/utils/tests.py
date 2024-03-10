from django.core.files.uploadedfile import SimpleUploadedFile

# these data will be used in test functions only
number = '09148387871'
password = 'VeryG00dPassword'
test_image_adr = '../11228.jpg'

def register_and_get_token(client, register_url, login_url):
    client.post(register_url, {'number': number,
                                        'password': password,
                                        'is_artist': True})
    # Get access token
    resp = client.post(login_url, {'number': number, 'password': password})
    return resp.data['access_token']

def test_image():
    with open(test_image_adr, 'rb') as f:
            bimage = f.read()
    return SimpleUploadedFile("test_image.jpg", bimage, content_type="image/jpeg")