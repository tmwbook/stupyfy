from typing import Sequence

from ..api_utils import API_BASE, _delete, _get, _put, api_call
from ..errors import SpotifyAPIParamError


@api_call([404])
def get_top_artists_and_tracks(category: str, limit: int = None,
                               offset: int = None, time_range: str = None):
    params = {
        "limit": limit,
        "offset": offset,
        "time_range": time_range,
    }
    if category not in ['artist', 'user']:
        raise SpotifyAPIParamError("Category needs to be 'artist' or 'user'.")
    if time_range not in ['long_term', 'medium_term', 'short_term']:
        raise SpotifyAPIParamError("time_range must be "
                                   "('short_term', 'medium_term',"
                                   "'long_term).")

    return _get(f"{API_BASE}/me/top/{category}", params=params)
