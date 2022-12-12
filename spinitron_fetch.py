import dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)
verification_token = os.environ['SPINITRON_TOKEN']

import json
import os
import webbrowser

import requests


spinitron_key = os.environ.get('SPINITRON_TOKEN')
spins_url = 'https://spinitron.com/api/spins?access-token={}&count=1'.format(spinitron_key)
playlist_url = 'https://spinitron.com/api/playlist?access-token={}&count=1'.format(spinitron_key)
shows_url = 'https://spinitron.com/api/shows?access-token={}&count=1'.format(spinitron_key)

def get_current_artist_song(api_url):

    response = requests.get(api_url)
    json_response = json.loads(response.text)
    artist = json_response['items'][0]['artist']
    song = json_response['items'][0]['song']
    output = 'Currently playing {} by {}'.format(song, artist)
    return output


def get_current_show_url(api_url):
    response = requests.get(api_url)
    json_response = json.loads(response.text)
    pl_id = json_response['items'][0]['playlist_id']
    show_url = 'https://spinitron.com/WRBB/pl/{}'.format(pl_id)
    return show_url


def get_current_show_name(api_url):
    response = requests.get(api_url)
    json_response = json.loads(response.text)
    show_name = json_response['items'][0]['title']
    return show_name

def format_final_response():
    song = get_current_artist_song(spins_url)
    show_name = get_current_show_name(playlist_url)
    show_url = get_current_show_url(spins_url)
    final_response = '{} on the show {} \n {}'.format(song, show_name, show_url)
    return final_response

print(format_final_response())