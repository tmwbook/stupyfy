class AlbumObjectFull:
    def __init__(self, album_type, artists, available_markets, copyrights, external_ids, external_urls, genres, href,spotify_id, images, label, name, popularity, release_date, release_date_precision, restrictions, tracks, api_type, uri):
        self.album_type = album_type
        self.artists = artists
        self.available_markets = available_markets
        self.copyrights = copyrights
        self.external_ids = external_ids
        self.external_urls = external_urls
        self.genres = genres
        self.href = href
        self.id = spotify_id
        self.images = images
        self.label = label
        self.name = name
        self.popularity = popularity
        self.release_date = release_date
        self.release_date_precision = release_date_precision
        self.restrictions = restrictions
        self.tracks = tracks
        self.type = api_type
        self.uri = uri
