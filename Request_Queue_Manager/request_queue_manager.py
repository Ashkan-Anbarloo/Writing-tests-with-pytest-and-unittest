import queue

class RequestQueue:
    def __init__(self):
        self.queue = []

    def add_request(self, request):
        if not isinstance(request , str) or not request.strip():
            raise ValueError('Request must be a non-empty string')
        self.queue.append(request.strip())

    def process_next(self):
        if self.is_empty():
            raise IndexError('No requests to process')
        return self.queue.pop(0)

    def peek_next(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def get_all_requests(self):
        return self.queue.copy()


    def is_empty(self):
        return len(self.queue) == 0

    def count(self):
        return len(self.queue)

