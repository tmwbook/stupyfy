from typing import Sequence

from ..api_utils import API_BASE, _get, api_call
from ..errors import SpotifyAPIParamError


@api_call([])
def search(search_string: str, types: Sequence[str],
           market: str = None, limit: int = None,
           offset: int = None,
           include_external_audio: bool = None):
    params = {
        "q": search_string,
        "type": types,
        "market": market,
        "limit": limit,
        "offset": offset,
        "include_external": "audio" if include_external_audio else None,
    }
    if limit > 50:
        raise SpotifyAPIParamError('limit must be below 51.')
    if limit < 1:
        raise SpotifyAPIParamError('limit must be above 0.')
    if offset > 2000:
        raise SpotifyAPIParamError('offset must be less than 2001.')
    return _get(f'{API_BASE}/search', params=params)
