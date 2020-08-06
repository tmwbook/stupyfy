# PyFy
> Pronounced Pi-Fi like Hi-Fi

A Python wrapper for the [Spotify Web API](https://developer.spotify.com/documentation/web-api/).

* Calls all return a [Requests](https://requests.readthedocs.io/en/master/) object (though most of the data you want can just be accessed by a call to `.json()`)
* `TokenManager` will handle coordinating tokens in a single or multi-user environment and will even refresh expired tokens.


## Creating a TokenManager
**You will need some workflow defined by your app to get initial authentication with the Spotify Identity Provider (IdP).**

The reason PyFy doesn't do this, is because we do not want to be starting a webserver independently of the project that is currently using the library.
The same goes for expired refresh tokens, this is essentially the Spotify IdP 'logging out' the authed user due to a stale token.
You will have to have the user go through the initial auth process again.
It is recommended that new tokens obtained directly from the Spotify IdP service override existing tokens in the database.
```python
from pyfy import TokenManager

def query_active_token():
    return current_user.access_token

def query_refresh_token():
    return current_user.refresh_token

def store_refreshed_token(new_tkn):
    current_user.access_token = new_tkn
    db.session.commit()

def failed_api_call():
    logout_user()
    return redirect('/')

TokenManager.initialize(
    CLIENT_ID,
    CLIENT_SECRET,
    query_active_token,
    query_refresh_token,
    store_refreshed_token,
    failed_api_call
)
```
TokenManager is a singleton class.
There should only be one per Python proccess.
Calls directly to the `__init__()` function will only work the first time.
Otherwise the current instance will be returned.

An example of a code flow that could be used for initial authorization:
```python
@app.route('/login/result')
def auth_result():
    if request.args.get('code', None):
        # POST the login code from the IdP 
        # to spotify to continue the authentication process
        tokens = get_tokens(request.args.get('code'))
        # Get the tokens
        r = get(API_BASE+'/me', headers={"Authorization": "Bearer "+tokens["access_token"]}).json()
        # See if the user is already in the database
        local_user = User.query.filter_by(spotify_id=r['id']).first()
        # Parse the tokens out
        if local_user:
            local_user.access_token = tokens['access_token']
            local_user.refresh_token = tokens['refresh_token']
        else:
            local_user = User(
                spotify_id = r['id'],
                access_token = tokens['access_token'],
                refresh_token = tokens['refresh_token'],
            )
            db.session.add(local_user)
        db.session.commit()
        # Accept that the IdP has validated the login
        # and log in with our service
        login_user(local_user)
        # Continue the normal post auth flow for your app
        return redirect(url_for('hello'))
    else:
        return redirect(url_for('index'))
```

## Calling to the API
All of the endpoints as defined by the [Spotify Web API](https://developer.spotify.com/documentation/web-api/reference/) are available in PyFy.
They are separated by type as defined by the Web API:
* Albums
* Artists
* Browse
* Episodes
* Follow
* Library
* Personalization
* Player
* Playlists
* Profile
* Search
* Shows
* Tracks

Most (almost all) of the api calls that have pluralities (such as offset, limit) check to ensure that calls do not exceed documented limits.
An api_call that violates this check will raise `pyfy.errors.SpotifyAPIParamError`

Every documented error status code documented by the api is expected by PyFy.
If it is returned by a an api_all, a `pyfy.errors.SpotifyAPIResponseError`

```python
# Get information on a playlist
from pyfy import playlists

# requests Response object, data accessible through .json()
playlists.get_playlist("spotify:playlist:4OjGTUFArsa9iECAC7PYTS")

# Play a song
from pyfy import player

player.start_playback(
    track_uris=[
        "spotify:track:2QyuXBcV1LJ2rq01KhreMF",
        "spotify:track:5DttNeiizFqWUON9hZBqTY",
    ]
)
```