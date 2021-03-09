class TrackObjectFull:
    def __init__(self, album, artists, available_markets, disc_number, duration_ms, explicit, external_ids, external_urls, href,spotify_id, is_playable, linked_from, restrictions, name, popularity, preview_url, track_number, api_type, uri, is_local):
        self.album = album
        self.artists = artists
        self.available_markets = available_markets
        self.disc_number = disc_number
        self.duration_ms = duration_ms
        self.explicit = explicit
        self.external_ids = external_ids
        self.external_urls = external_urls
        self.href = href
        self.id = spotify_id
        self.is_playable = is_playable
        self.linked_from = linked_from
        self.restrictions = restrictions
        self.name = name
        self.popularity = popularity
        self.preview_url = preview_url
        self.track_number = track_number
        self.type = api_type
        self.uri = uri
        self.is_local = is_local
