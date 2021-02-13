class EpisodeObjectFull:
    def __init__(self, audio_preview_url, description, duration_ms, explicit, external_urls, href,spotify_id, images, is_externally_hosted, is_playable, language, languages, name, release_date, release_date_precision, resume_point, show, api_type, uri):
        self.audio_preview_url = audio_preview_url
        self.description = description
        self.duration_ms = duration_ms
        self.explicit = explicit
        self.external_urls = external_urls
        self.href = href
        self.id = spotify_id
        self.images = images
        self.is_externally_hosted = is_externally_hosted
        self.is_playable = is_playable
        self.language = language
        self.languages = languages
        self.name = name
        self.release_date = release_date
        self.release_date_precision = release_date_precision
        self.resume_point = resume_point
        self.show = show
        self.type = api_type
        self.uri = uri
