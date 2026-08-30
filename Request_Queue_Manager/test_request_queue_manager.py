import unittest
from .request_queue_manager import RequestQueue

class TestRequestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = RequestQueue()

    def test_add_vali_request(self):
        self.queue.add_request('Download file')
        self.assertEqual(self.queue.count() , 1)
        self.assertEqual(self.queue.peek_next() , 'Download file')

    def test_add_invalid_request(self):
        with self.assertRaises(ValueError):
            self.queue.add_request('')
        with self.assertRaises(ValueError):
            self.queue.add_request('    ')
        with self.assertRaises(ValueError):
            self.queue.add_request(7423)