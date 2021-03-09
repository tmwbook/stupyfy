from typing import Sequence

from ..api_utils import API_BASE, _get, api_call
from ..errors import SpotifyAPIParamError


@api_call([404])
def get_show(show_id: str, market: str = None):
    params = {
        "market": market,
    }
    return _get(f'{API_BASE}/shows/{show_id}', params=params)


@api_call([])
def get_shows(show_ids: Sequence[str], market: str = None):
    params = {
        "ids": show_ids,
        "market": market,
    }
    if len(show_ids) > 50:
        raise SpotifyAPIParamError('maximum number of show ids is 50.')
    return _get(f'{API_BASE}/shows', params=params)


@api_call([404])
def get_episodes(show_id: str, limit: int = None,
                 offset: int = None, market: str = None):
    params = {
        "limit": limit,
        "offset": offset,
        "market": market,
    }
    if limit > 50:
        raise SpotifyAPIParamError('limit must be less than 51.')
    if limit < 1:
        raise SpotifyAPIParamError('limit must be greater than 0.')
    return _get(f'{API_BASE}/shows/{show_id}/episodes', params=params)
