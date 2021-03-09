from typing import Sequence

from ..api_utils import API_BASE, _delete, _get, _put, api_call
from ..errors import SpotifyAPIParamError


@api_call([404])
def check_following(category: str, spotify_ids: Sequence[str]):
    if category not in ['artist', 'user']:
        raise SpotifyAPIParamError("Category needs to be 'artist' or 'user'.")
    params = {
        "type": category,
        "ids": spotify_ids,
    }
    return _get(f'{API_BASE}/me/following/contains', params=params)


@api_call([404])
def check_playlist_followers(playlist_id: str, spotify_ids: Sequence[str]):
    params = {
        "ids": spotify_ids,
    }
    return _get(f'{API_BASE}/playlists/{playlist_id}/followers/contains', params=params)


@api_call([404])
def follow_artist_or_user(category: str, spotify_ids: str):
    if category not in ['artist', 'user']:
        raise SpotifyAPIParamError("Category needs to be 'artist' or 'user'.")
    params = {
        "type": category,
        "ids": spotify_ids,
    }
    return _put(f"{API_BASE}/me/following", params=params)


@api_call([404])
def follow_playlist(playlist_id: str, display_public: bool):
    data = {
        "public": display_public,
    }
    return _put(f'{API_BASE}/playlists/{playlist_id}/followers/contains', data=data)


@api_call([404])
def get_followed_artists(limit: int = None, after: str = None):
    params = {
        "type": "artist",
        "limit": limit,
        "after": after,
    }
    return _get(f"{API_BASE}/me/following", params=params)


@api_call([404])
def unfollow_artist_or_user(category: str, spotify_ids: Sequence[str]):
    if category not in ['artist', 'user']:
        raise SpotifyAPIParamError("Category needs to be 'artist'or 'user'.")
    params = {
        "type": category,
        "ids": spotify_ids,
    }
    return _delete(f"{API_BASE}/me/following", params=params)


@api_call([404])
def unfollow_playlist(playlist_id: str):
    return _delete(f"{API_BASE}/playlists/{playlist_id}/followers")
