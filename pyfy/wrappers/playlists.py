from typing import Sequence

from requests import put

from ..api_utils import (API_BASE, TokenManager, _delete, _get, _post, _put,
                         api_call)
from ..errors import SpotifyAPIParamError


@api_call([403, 404])
def add_to_playlist(playlist_id: str, track_uris: Sequence[str],
                    position: int = None):
    """Users may run into an issue if the length of their tracks goes
    over the allowed length for a URI"""
    data = {
        "uris": track_uris,
        "position": position
    }
    if len(track_uris) > 100:
        raise SpotifyAPIParamError("cannot add more than 100 tracks at a time.")

    return _post(
        f'{API_BASE}/playlists/{playlist_id}/tracks',
        data=data
    )


@api_call([403])
def change_playlist_details(playlist_id: str, name: str = None,
                            public: bool = None, collaborative: bool = None,
                            description: str = None):
    data = {
        "name": name,
        "public": public,
        "collaborative": collaborative,
        "description": description,
    }
    return _put(
        f'{API_BASE}/playlists/{playlist_id}',
        data=data
    )


@api_call([403])
def create_playlist(user_id: str, name: str, public: bool = None,
                    collaborative: bool = None, description: str = None):
    data = {
        "name": name,
        "public": public,
        "collaborative": collaborative,
        "description": description,
    }
    return _post(
        f'{API_BASE}/users/{user_id}/playlists',
        data=data
    )


@api_call([])
def get_playlists(limit: int = None, offset: int = None):
    """Get the current user's playslist"""
    params = {
        "limit": limit,
        "offset": offset,
    }
    if limit is not None:
        if limit > 50:
            raise SpotifyAPIParamError("limit must be less than 51.")
        if limit < 0:
            raise SpotifyAPIParamError("limit must be more than 0.")
    if offset is not None:
        if offset > 100000:
            raise SpotifyAPIParamError('offset must be less than 100,001.')
    return _get(f'{API_BASE}/me/playlists', params=params)


@api_call([])
def get_user_playlists(user_id: str, limit: int = None, offset: int = None):
    params = {
        "limit": limit,
        "offset": offset,
    }
    if limit is not None:
        if limit > 50:
            raise SpotifyAPIParamError("limit must be less than 51.")
        if limit < 0:
            raise SpotifyAPIParamError("limit must be more than 0.")
    if offset is not None:
        if offset > 100000:
            raise SpotifyAPIParamError('offset must be less than 100,001.')
    return _get(f'{API_BASE}/users/{user_id}/playlists', params=params)


@api_call([])
def get_playlist_cover(playlist_id: str):
    return _get(f'{API_BASE}/playlists/{playlist_id}/images')


@api_call([403])
def get_playlist(playlist_id: str, fields: str = None,
                 market: str = None,
                 additional_types: Sequence[str] = None):
    params = {
        "fields": fields,
        "market": market,
        "additional_types": additional_types,
    }
    return _get(f'{API_BASE}/playlists/{playlist_id}', params=params)


@api_call([])
def get_playlist_tracks(playlist_id: str, fields: str = None,
                        market: str = None,
                        additional_types: Sequence[str] = None):
    params = {
        "fields": fields,
        "market": market,
        "additional_types": additional_types,
    }
    return _get(f'{API_BASE}/playlists/{playlist_id}/tracks', params=params)


@api_call([400, 403])
def remove_playlist_item(playlist_id: str, tracks: Sequence[dict],
                         snapshot_id: str = None):
    """
    Tracks example:
    {
        "tracks": [
            {"uri": spotify_uri, "positions": [0, 2]}
        ]
    }
    The positions param is optional if you only want a single occurance
    of an item deleted
    """
    data = {
        "tracks": tracks,
        "snapshot_id": snapshot_id,
    }
    if len(tracks) > 100:
        raise SpotifyAPIParamError('tracks must be less than 101.')
    for track in tracks:
        if not track.get('uri'):
            raise SpotifyAPIParamError(f'{track} did not have manditory uri argument.')
    return _delete(f"{API_BASE}/playlists/{playlist_id}/tracks", data=data)


@api_call([])
def reorder_tracks(playlist_id: str, range_start: int,
                   range_length: int, insert_before: int,
                   snapshot_id: str = None):
    data = {
        "range_start": range_start,
        "range_length": range_length,
        "insert_before": insert_before,
        "snapshot_id": snapshot_id,
    }
    return _put(f'{API_BASE}/playlists/{playlist_id}/tracks', data=data)


@api_call([403])
def replace_items(playlist_id: str, uris: Sequence[str]):
    data = {
        "uris": uris,
    }
    if uris > 100:
        raise SpotifyAPIParamError('must contain less than 101 uris.')
    return _put(f'{API_BASE}/playlists/{playlist_id}/tracks', data=data)


@api_call([])
def set_playlist_image(playlist_id: str, b64_jpg: str):
    data = {
        "image": b64_jpg,
    }
    return put(
        f"{API_BASE}/playlists/{playlist_id}/images",
        headers={
            "Authorization": "Bearer " + TokenManager.get_instance().get_current_token(),
            "Content-Type": "image/jpeg",
        },
        data=data
    )
