# Stupyfy
> Pronounced Stew-pi-fi

A Python wrapper for the [Spotify Web API](https://developer.spotify.com/documentation/web-api/).

* Calls all return a [Requests](https://requests.readthedocs.io/en/master/) object (though most of the data you want can just be accessed by a call to `.json()`)
* `TokenManager` will handle coordinating tokens in a single or multi-user environment and will even refresh expired tokens.

Bugs and suggestions welcome. Please file a GitHub Issue.

## Quickstart

### Installing
This is a beta library, insofar that I haven't published it to PyPi yet.
Because I haven't tested it fully, I also have not set any tags.
This means you should leave it as editable so you can easily update it.
If you would like to use it (please do!), here are some methods of getting it.

pip
```
pip install -e git+https://github.com/tmwbook/stupyfy@v1.0.0-beta#egg=pyfy
```
Pipfile (pipenv)
```toml
[packages]
stupyfy = { git = "https://github.com/tmwbook/stupyfy", editable = true, ref = "v1.0.0-beta" }
```

### Code
Ensure that your app and its callback URLs are registered in the Spotify Developer Dashboard!

```python
"""
current_user and db are imaginary variables to stand in
for getting the current user from and interacting with a
data store. Please provide your own method of doing this
in whatever callback functions you choose to use.
"""
from stupyfy.api_utils import TokenManager
from stupyfy.wrappers import player

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

# Must also have valid, authenticated tokens.
# See Authentication section for more information.
...

# Play "Welcome To The Jungle" by Guns N' Roses
# Will play for the user whose token is returned by `query_active_token()`
player.start_playback(track_uris=["spotify:track:0G21yYKMZoHa30cYVi1iA8"])
```
### Authentication

An example of a code flow that could be used with `Flask` for initial authorization:
```python
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('/profile'))

    context = {
        "spotify_auth_url": TokenManager.get_instance().gen_auth_url(
            # callback url, must match what is in your developer dashboard
            "http://localhost:3000/login/result", 
            # List[str] of spotify scopes
            SCOPES 
        ),
    }
    return render_template('index.html', **context)

@app.route('/login/result')
def auth_result():
    try:
        # Attempt to get tokens and finish out the authentication
        spotify_resp = TokenManager.get_instance().handle_auth_response(request.url)
    except SpotifyOAuthGenerationError:
        return redirect(url_for('/'))

    # Get some information about the user
    r = get(
        API_BASE+'/me',
        headers={
            "Authorization": "Bearer "+spotify_resp["access_token"]
        }
    ).json()
    
    # See if the user is already in the database
    local_user = User.query.filter_by(spotify_id=r['id']).first()
    # Parse the tokens out
    if local_user:
        local_user.access_token = spotify_resp['access_token']
        local_user.refresh_token = spotify_resp['refresh_token']
    else:
        local_user = User(
            spotify_id = r['id'],
            access_token = spotify_resp['access_token'],
            refresh_token = spotify_resp['refresh_token'],
        )
        db.session.add(local_user)
    db.session.commit()
    
    # Accept that the IdP has validated the login
    # and log in to our service
    login_user(local_user)
    return redirect(url_for('profile'))
```

## TokenManager
The central fixture of stupyfy is the `TokenManager`. The `TokenManager` deals with coordinating active tokens,
helping with initial authorization, and hands control back to your app on an API call if something goes horribly wrong.

TokenManager is a singleton class.
There should only be one per Python proccess.
It is recommended to use once `TokenManager.initalize()` and subsequently `TokenManager.get_instance()` to get instances of `TokenManager`.
Calls directly to the `__init__()` function will only work the first time.

Here is a description of the arguments `TokenManager` takes:
```
client_id: A string of your application's client_id from Spotify

client_secret: A string of your application's client_secret from Spotify

token_query_source: A function that will return what the current
    user's token is.

    This would be useful in a web application where there could be
    multiple active user sessions. For example:

    def token_query_source():
        return db.query(current_user).token

refresh_token_query_source: A function that will return what the
    current user's refresh token is.

    This would be the same as `token_query_source` but for refresh
    tokens.

store_refreshed_token: A function that takes 1 argument (string)
    that will store a token for the current user if the old one
    expires. For example:
    
    def store_refreshed_token(new_tkn):
        user = db.query(current_user)
        user.token = newtkn
        db.commit()

api_fail_callback: A function that you would like to be called after
    two Access Denied (or similar 400) responses. Its value will be
    returned instead of the result of the API call.
```

## Calling to the API
All of the endpoints as defined by the [Spotify Web API](https://developer.spotify.com/documentation/web-api/reference/) are available in stupyfy.
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
An api_call that violates this check will raise `pyfy.errors.SpotifyAPIParamError`.
Each wrapper method's arguments are type annotated if your editor supports that type of introspection.

**It is highly recommended that you use keyword args when calling these functions**

Every documented error status code documented by the api is expected by stupyfy.
If it is returned by a an api_all, a `pyfy.errors.SpotifyAPIResponseError`

```python
# Get information on a playlist
from stupyfy.wrappers import playlists

# requests Response object, data accessible through .json()
playlists.get_playlist("spotify:playlist:4OjGTUFArsa9iECAC7PYTS")

# Play a song
from stupyfy.wrappers import player

player.start_playback(
    track_uris=[
        "spotify:track:2QyuXBcV1LJ2rq01KhreMF",
        "spotify:track:5DttNeiizFqWUON9hZBqTY",
    ]
)
```

## Contributors
* [Tom White](https://github.com/tmwbook) - Author

---
Name pending, stupyfy is an existing projected on PyPi
