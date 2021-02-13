class ExternalIdObject:
    def __init__(self, ean, isrc, upc):
        """
        ean - International Article Number
        isrc - International Standard Recording Code
        upc - Universal Product Code
        """
        self.ean = ean
        self.isrc = isrc
        self.upc = upc
