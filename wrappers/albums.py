from typing import Sequence

from ..api_utils import API_BASE, _get, api_call


@api_call([404])
def get_album(album_id: str):
    return _get(f"{API_BASE}/albums/{album_id}")

@api_call([404])
def get_album_tracks(album_id: str):
    return _get(f"{API_BASE}/albums/{album_id}/tracks")

@api_call([404])
def get_albums(album_ids: Sequence[str]):
    # TODO(Tom): Does not yet support pagination
    return _get(f"{API_BASE}/albums", params={"ids": album_ids})
