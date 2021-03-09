import re
from typing import Dict, Sequence, TypeVar

from ..api_utils import API_BASE, _get, api_call
from ..errors import SpotifyAPIParamError

TUNABLE_DICT = Dict[str, TypeVar('T', int, float)]

@api_call([404])
def get_category(category_id: str, country: str = None, locale: str = None):
    params = {
        "country": country,
        "locale": locale,
    }
    return _get(f"{API_BASE}/browse/categories/{category_id}", params=params)


@api_call([404])
def get_category_playlists(category_id: str, country: str = None,
                            limit: int = None, offset: int = None):
    params = {
        "country": country,
        "limit": limit,
        "offset": offset,
    }
    return _get(f"{API_BASE}/browse/categories/{category_id}/playlists", params=params)


@api_call([404])
def get_categories(country: str = None, locale: str = None,
                    limit: int = None, offset: int = None):
    params = {
        "country": country,
        "locale": locale,
        "limit": limit,
        "offset": offset,
    }
    return _get(f"{API_BASE}/browse/categories", params=params)


@api_call([404])
def get_featured_playlists(country: str = None, locale: str = None,
                           limit: int = None, offset: int = None,
                           timestamp: str = None):
    if (timestamp is not None and
            re.search(r"\d{4}(-\d{2}){2}T(\d{2}:){2}\d{2}", timestamp)
            is None):
        raise SpotifyAPIParamError("Timestamps need to be in ISO 8601 format,"
                                   " yyyy-MM-ddTHH:mm:ss")

    params = {
        "country": country,
        "locale": locale,
        "limit": limit,
        "offset": offset,
        "timestamp": timestamp,
    }
    return _get(f"{API_BASE}/browse/featured-playlists", params=params)


@api_call([404])
def get_new_releases(country: str = None, limit: int = None,
                     offset: int = None):
    params = {
        "country": country,
        "limit": limit,
        "offset": offset,
    }
    return _get(f"{API_BASE}/browse/new-releases", params=params)


def _merge_tunables(target, max_tune, min_tune, params):
    for opts, prefix in zip((target, max_tune, min_tune),
                            ('target', 'max', 'min')):
        if opts is not None:
            for k in opts.keys():
                opts[f"{prefix}_{k}"] = opts.pop(k)
            params.update(opts)


def _process_seeds(artists, genres, tracks, params):
    seeds = 0
    for seed, key in zip((artists, genres, tracks),
                         ("seed_artists", "seed_genre", "seed_tracks")):
        if seed is not None:
            params[key] = seed
            seeds += len(seed)
        if seeds > 5:
            raise SpotifyAPIParamError("Too many seeds provided."
                                       " A maximum of 5 seeds combined can be passed.")



@api_call([404])
def get_recommendations(seed_artists: Sequence[str] = None,
                        seed_genres: Sequence[str] = None,
                        seed_tracks: Sequence[str] = None,
                        limit: int = None, market: str = None,
                        target_tunables: TUNABLE_DICT = None,
                        max_tunables: TUNABLE_DICT = None,
                        min_tunables: TUNABLE_DICT = None):

    params = {
        "limit": limit,
        "market": market,
    }
    _merge_tunables(target_tunables, max_tunables, min_tunables, params)
    _process_seeds(seed_artists, seed_genres, seed_tracks, params)

    return _get(f"{API_BASE}/recommendations", params=params)
