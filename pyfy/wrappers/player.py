from typing import Sequence, TypeVar

from ..api_utils import API_BASE, _get, _post, _put, api_call
from ..errors import SpotifyAPIParamError


@api_call([403, 404])
def queue_song(spotify_uri: str, device_id: str = None):
    params = {
        "uri": spotify_uri,
        "device_id": device_id,
    }
    return _post(f"{API_BASE}/me/player/queue", params=params)


@api_call([404])
def get_devices():
    return _get(f"{API_BASE}/me/player/devices")


@api_call([404])
def get_playback_state(market: str = None, additional_types: str = None):
    params = {
        "market": market,
        "additional_types": additional_types,
    }
    if additional_types not in ['track', 'episode']:
        raise SpotifyAPIParamError("additional_types need to be "
                                   "('track', 'episode').")
    return _get(f"{API_BASE}/me/player", params=params)


@api_call([404])
def get_recently_played(limit: int = None, after: int = None, before: int = None):
    params = {
        "limit": limit,
        "after": after,
        "before": before,
    }
    return _get(f"{API_BASE}/me/player/recently-played", params=params)


@api_call([404])
def get_currently_playing(market: str = None, additional_types: str = None):
    params = {
        "market": market,
        "additional_types": additional_types,
    }
    if additional_types not in ['track', 'episode']:
        raise SpotifyAPIParamError("additional_types need to be "
                                   "('track', 'episode').")
    return _get(f"{API_BASE}/me/player/currently-playing", params=params)


@api_call([403, 404])
def pause(device_id: str = None):
    params = {
        "device_id": device_id,
    }
    return _put(f"{API_BASE}/me/player/pause", params=params)


@api_call([403, 404])
def seek(position_ms: int, device_id: str = None):
    params = {
        "position_ms": position_ms,
        "device_id": device_id,
    }
    return _put(f"{API_BASE}/me/player/seek", params=params)


@api_call([403, 404])
def set_repeat(state: str, device_id: str = None):
    params = {
        "state": state,
        "device_id": device_id,
    }
    if state not in ['track', 'context', 'off']:
        raise SpotifyAPIParamError("state must be ('track', 'context', 'off')")
    return _put(f"{API_BASE}/me/player/repeat", params=params)


@api_call([403, 404])
def set_volume(percent: int, device_id: str = None):
    params = {
        "volume_percent": percent,
        "device_id": device_id,
    }
    if percent not in range(0, 101):
        raise SpotifyAPIParamError('percent must be between 0-100.')
    return _put(f"{API_BASE}/me/player/volume", params=params)


@api_call([403, 404])
def skip(device_id: str = None):
    params = {
        "device_id": device_id,
    }
    return _post(f"{API_BASE}/me/player/next", params=params)


@api_call([403, 404])
def skip_to_previous(device_id: str = None):
    params = {
        "device_id": device_id,
    }
    return _post(f"{API_BASE}/me/player/previous", params=params)


@api_call([400, 403, 404])
def start_playback(device_id: str = None, context_uri: str = None,
                   track_uris: Sequence[str] = None,
                   offset: TypeVar('T', int, str) = None,
                   position_ms: int = None):
    """
    Spotify API limitaiton: URIs for Tracks can only be pass through\
        `track_uris`
    """
    params = {
        "device_id": device_id,
    }
    data = {
        "context_uri": context_uri,
        "uris": track_uris,
        "offset": offset,
        "position_ms": position_ms,
    }
    if context_uri and track_uris:
        raise SpotifyAPIParamError('context_uri and uris are mutally exclusive.')
    if offset:
        if isinstance(offset, int):
            data['offset'] = {'position': offset}
        else:
            data['offset'] = {'uri': offset}
    return _put(
        f'{API_BASE}/me/player/play',
        params=params,
        data=data
    )


@api_call([403, 404])
def set_shuffle(state: bool, device_id: str = None):
    params = {
        "state": state,
        "device_id": device_id,
    }
    return _put(f"{API_BASE}/me/player/shuffle", params=params)


@api_call([403, 404])
def transfer_playback(device_ids: Sequence[str], force_play: bool = None):
    params = {
        "device_ids": device_ids,
        "play": force_play,
    }
    if len(device_ids) > 1:
        raise SpotifyAPIParamError('device_ids can only contain 1 device. '
                                   '(yes this is strange, check the Spotify API docs)')
    return _put(f"{API_BASE}/me/player", params=params)
