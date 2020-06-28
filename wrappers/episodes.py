from typing import Sequence

from ..api_utils import API_BASE, _get, api_call


@api_call([404])
def get_episode(episode_id: str, market: str = None):
    params = {
        "market": market,
    }
    return _get(f"{API_BASE}/episodes/{episode_id}", params=params)


@api_call([404])
def get_episodes(episode_ids: Sequence[str], market: str = None):
    params = {
        "ids": episode_ids,
        "market": market,
    }
    return _get(f"{API_BASE}/episodes", params=params)
