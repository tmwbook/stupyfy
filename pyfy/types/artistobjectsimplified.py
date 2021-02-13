class ArtistObjectSimplified:
    def __init__(self, external_urls, href,spotify_id, name, api_type, uri):
        self.external_urls = external_urls
        self.href = href
        self.id = spotify_id
        self.name = name
        self.type = api_type
        self.uri = uri
