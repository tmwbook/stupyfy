from typing import Sequence

from ..api_utils import API_BASE, _get, api_call


@api_call([404])
def get_album(album_id: str, market: str = None):
    params = {
        "market": market,
    }
    return _get(f"{API_BASE}/albums/{album_id}", params=params)

@api_call([404])
def get_album_tracks(album_id: str, limit: int = None, offset: int = None, market: str = None):
    params = {
        "limit": limit,
        "offset": offset,
        "market": market,
    }
    return _get(f"{API_BASE}/albums/{album_id}/tracks", params=params)

@api_call([404])
def get_albums(album_ids: Sequence[str], market: str = None):
    params = {
        "ids": album_ids,
        "market": market,
    }
    return _get(f"{API_BASE}/albums", params=params)
