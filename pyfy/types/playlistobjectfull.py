class PlaylistObjectFull:
    def __init__(self, collaborative, description, external_urls, followers, href,spotify_id, images, name, owner, public, snapshot_id, tracks, api_type, uri):
        self.collaborative = collaborative
        self.description = description
        self.external_urls = external_urls
        self.followers = followers
        self.href = href
        self.id = spotify_id
        self.images = images
        self.name = name
        self.owner = owner
        self.public = public
        self.snapshot_id = snapshot_id
        self.tracks = tracks
        self.type = api_type
        self.uri = uri
