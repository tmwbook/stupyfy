from typing import Sequence

from ..api_utils import API_BASE, _delete, _get, _put, api_call


@api_call([404])
def check_saved_albums(album_ids: Sequence[str]):
    params = {
        "ids": album_ids,
    }
    return _get(f"{API_BASE}/me/albums/contains", params=params)


@api_call([404])
def check_saved_shows(show_ids: Sequence[str]):
    params = {
        "ids": show_ids,
    }
    return _get(f"{API_BASE}/me/shows/contains", params=params)


@api_call([404])
def check_savaed_tracks(track_ids: Sequence[str]):
    params = {
        "ids": track_ids,
    }
    return _get(f"{API_BASE}/me/tracks/contains", params=params)


@api_call([404])
def get_saved_albums(limit: int = None, offset: int = None, market: str = None):
    params = {
        "limit": limit,
        "offset": offset,
        "market": market,
    }
    return _get(f"{API_BASE}/me/albums", params=params)


@api_call([404])
def get_saved_shows(limit: int = None, offset: int = None):
    params = {
        "limit": limit,
        "offset": offset,
    }
    return _get(f"{API_BASE}/me/shows", params=params)


@api_call([404])
def get_saved_tracks(limit: int = None, offset: int = None, market: str = None):
    params = {
        "limit": limit,
        "offset": offset,
        "market": market,
    }
    return _get(f"{API_BASE}/me/tracks", params=params)


@api_call([403, 404])
def remove_saved_albums(album_ids: Sequence[str]):
    params = {
        "ids": album_ids,
    }
    return _delete(f"{API_BASE}/me/albums", params=params)


@api_call([403, 404])
def remove_saved_shows(show_ids: Sequence[str]):
    params = {
        "ids": show_ids,
    }
    return _delete(f"{API_BASE}/me/shows", params=params)


@api_call([403, 404])
def remove_saved_tracks(track_ids: Sequence[str]):
    params = {
        "ids": track_ids,
    }
    return _delete(f"{API_BASE}/me/tracks", params=params)


@api_call([403, 404])
def add_saved_albums(album_ids: Sequence[str]):
    params = {
        "ids": album_ids,
    }
    return _put(f"{API_BASE}/me/albums", params=params)


@api_call([403, 404])
def add_saved_shows(show_ids: Sequence[str]):
    params = {
        "ids": show_ids,
    }
    return _put(f"{API_BASE}/me/shows", params=params)


@api_call([403, 404])
def add_saved_tracks(track_ids: Sequence[str]):
    params = {
        "ids": track_ids,
    }
    return _put(f"{API_BASE}/me/tracks", params=params)
