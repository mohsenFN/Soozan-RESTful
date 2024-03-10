number = '09148387871'
password = 'VeryG00dPassword'

def register_and_get_token(client, register_url, login_url):
    client.post(register_url, {'number': number,
                                        'password': password,
                                        'is_artist': True})
    # Get access token
    resp = client.post(login_url, {'number': number, 'password': password})
    return resp.data['access_token']