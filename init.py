import spotipy
from spotipy.oauth2 import SpotifyOAuth
import tweepy
import json


def load():
    with open("assets/user.json", "r") as f:
        dic = json.load(f)

    return dic


def get_spotify():
    dic = load()
    clientid = dic['spotify_client_id']
    clientsecret = dic['spotify_client_secret']
    uri = 'http://localhost:8888/callback'
    scope = 'user-read-currently-playing'

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientid,
                                                   client_secret=clientsecret,
                                                   redirect_uri=uri,
                                                   scope=scope))

    return sp


def get_twitter():
    dic = load()
    apikey = dic['twitter_consumer_key']
    apisecret = dic['twitter_consumer_secret']
    accesstoken = dic['twitter_access_token']
    accesssecret = dic['twitter_access_token_secret']

    client = tweepy.Client(consumer_key=apikey,
                           consumer_secret=apisecret,
                           access_token=accesstoken,
                           access_token_secret=accesssecret)

    return client
