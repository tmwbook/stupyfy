from typing import Sequence

from ..api_utils import API_BASE, _get, api_call


@api_call([404])
def get_artist(artist_id: str):
    return _get(f"{API_BASE}/artists/{artist_id}")


@api_call([404])
def get_artist_albums(artist_id: str, include_groups: Sequence[str] = None,
                       country: str = None, limit: int = None, offest: int = None):
    params = {
        "include_groups": include_groups,
        "country": country,
        "limit": limit,
        "offset": offest,
    }
    return _get(f"{API_BASE}/artists/{artist_id}/albums", params=params)


@api_call([404])
def get_artist_top_tracks(artist_id: str, country: str = None):
    params = {
        "country": country,
    }
    return _get(f"{API_BASE}/artists/{artist_id}/top-tracks", params=params)


@api_call([404])
def get_related_artists(artist_id: str):
    return _get(f"{API_BASE}/artists/{artist_id}/related-artists")


@api_call([404])
def get_artists(artist_ids: Sequence[str]):
    params = {
        "ids": artist_ids,
    }
    return _get(f"{API_BASE}/artists", params=params)
