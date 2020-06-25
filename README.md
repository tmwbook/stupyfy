# PyFy
> Pronounced Pi-Fi like Hi-Fi

A Python wrapper for the [Spotify Web API](https://developer.spotify.com/documentation/web-api/).

* Calls all return a [Requests](https://requests.readthedocs.io/en/master/) object (though most of the data you want can just be accessed by a call to `.json()`)
* `TokenManager` will handle coordinating tokens in a single or multi-user environment and will even refresh expired tokens.