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

    def test_process_request(self):
        self.queue.add_request('First')
        self.queue.add_request('Secend')
        processed = self.queue.process_next()
        self.assertEqual(processed , 'First')
        self.assertEqual(self.queue.peek_next() , 'Secend')


    def test_process_empty_queue(self):
        with self.assertRaises(IndexError):
            self.queue.process_next()

    def test_peek_next_empty(self):
        self.assertIsNone(self.queue.peek_next())

    def test_get_all_request(self):
        self.queue.add_request("A")
        self.queue.add_request("B")
        self.assertEqual(self.queue.get_all_requests() , ['A','B'])

    def test_is_empty_and_count(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.add_request("somethings")
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.count() , 1)
