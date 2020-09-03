class PagingObject:
    def __init__(self, href, items, limit, next, offset, previous, total):
        self.href = href
        self.items = items
        self.limit = limit
        self.next = next
        self.offset = offset
        self.previous = previous
        self.total = total
