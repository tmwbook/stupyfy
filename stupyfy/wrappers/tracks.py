from typing import Sequence

from ..api_utils import API_BASE, _get, api_call


@api_call([])
def get_audio_analysis(track_id: str):
    return _get(f'{API_BASE}/audio-analysis/{track_id}')


@api_call([])
def get_audio_features(track_id: str):
    return _get(f'{API_BASE}/audio-features/{track_id}')


@api_call([])
def get_multiple_audio_features(track_ids: Sequence[str]):
    params = {
        'ids': track_ids,
    }
    return _get(f'{API_BASE}/audio-features', params=params)


@api_call([])
def get_tracks(track_ids: Sequence[str], market: str = None):
    params = {
        "ids": track_ids,
        'market': market,
    }
    return _get(f'{API_BASE}/tracks', params=params)


@api_call([])
def get_track(track_id: str):
    return _get(f'{API_BASE}/tracks/{track_id}')
