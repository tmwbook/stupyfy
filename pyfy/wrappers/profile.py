from ..api_utils import API_BASE, _get, api_call


@api_call([])
def get_current_user_profile():
    return _get(f'{API_BASE}/me')


@api_call([404])
def get_user_profile(user_id: str):
    return _get(f'{API_BASE}/users/{user_id}')
