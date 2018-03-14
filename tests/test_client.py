import seer
import unittest


class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = seer.Client("127.0.0.1:8080")

    def test_get_stream(self):
        name = "myStream"
        period = 3600
        stream = self.client.create_stream(name, period)
        self.assertEqual(stream.name, name)
        self.assertEqual(stream.period, period)
