class AlbumObjectSimplified:
    def __init__(self, album_group, album_type, artists, available_markets, external_urls, href,spotify_id, images, name, release_date, release_date_precision, restrictions, api_type, uri):
        self.album_group = album_group
        self.album_type = album_type
        self.artists = artists
        self.available_markets = available_markets
        self.external_urls = external_urls
        self.href = href
        self.id = spotify_id
        self.images = images
        self.name = name
        self.release_date = release_date
        self.release_date_precision = release_date_precision
        self.restrictions = restrictions
        self.type = api_type
        self.uri = uri
