import json
import requests
import config

CLIENT_ID = config.client_id

CLIENT_Secret = config.client_secret

AUTH_URL = 'https://accounts.spotify.com/api/token'


auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_Secret,
})

#convert the response to JSON
auth_response_data = auth_response.json()

#save access token
access_token = auth_response_data['access_token']



headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}


BASE_URL = 'https://api.spotify.com/v1/'

track_id = '6y0igZArWVi6Iz0rj35c1Y'

r = requests.get(BASE_URL + 'audio-features/' + track_id, headers = headers)

r = r.json()


print(r)
