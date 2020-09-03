class Cursor-BasedPagingObject:
    def __init__(self, href, items, limit, next, cursors, total):
        self.href = href
        self.items = items
        self.limit = limit
        self.next = next
        self.cursors = cursors
        self.total = total
