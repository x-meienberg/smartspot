import json
import requests

CLIENT_ID = '0261a814cd694fcb9b29961468816353'

CLIENT_Secret = 'e35b42e4777149149e7f290462c585b3'

AUTH_URL = 'https://accounts.spotify.com/api/token'


auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_Secret,
})


auth_response_data = auth_response.json()

access_token = auth_response_data['access_token']



headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}


BASE_URL = 'https:api.spotify.com/v1/'

track_id = '6y0igZArWVi6Iz0rj35c1Y'

r = requests.get(BASE_URL + 'audio-features/' + track_id, headers = headers)

r = r.json()
r
