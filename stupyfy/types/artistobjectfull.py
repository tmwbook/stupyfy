class ArtistObjectFull:
    def __init__(self, external_urls, followers, genres, href,spotify_id, images, name, popularity, api_type, uri):
        self.external_urls = external_urls
        self.followers = followers
        self.genres = genres
        self.href = href
        self.id = spotify_id
        self.images = images
        self.name = name
        self.popularity = popularity
        self.type = api_type
        self.uri = uri
