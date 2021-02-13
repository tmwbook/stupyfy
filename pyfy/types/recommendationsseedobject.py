class RecommendationsSeedObject:
    def __init__(self, afterFilteringSize, afterRelinkingSize, href,spotify_id, initialPoolSize, type):
        self.afterFilteringSize = afterFilteringSize
        self.afterRelinkingSize = afterRelinkingSize
        self.href = href
        self.id = spotify_id
        self.initialPoolSize = initialPoolSize
        self.type = api_type
