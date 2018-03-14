"""Tests for the more idiomatic python client.

These are light, because exceptions, arg parsing happen serverside.
"""
import unittest

import seer


class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = seer.Client("127.0.0.1:8080")
        self.client.create_stream("test", 86400)

    def test_create_stream(self):
        name = "myStream"
        period = 3600
        stream = self.client.create_stream(name, period)
        self.assertEqual(stream.name, name)
        self.assertEqual(stream.period, period)

    def test_get_stream(self):
        stream = self.client.get_stream("test")
        self.assertEqual(stream.name, "test")
        self.assertEqual(stream.period, 86400)

    def test_list_streams(self):
        streams = self.client.list_streams(10, 1)
        self.assertEqual(len(streams), 1)
        self.assertEqual(streams[0].name, "test")

    def test_update_stream(self):
        times = []
        values = []
        stream = self.client.update_stream("test", times, values)
        self.assertEqual(stream.name, "test")
        self.assertEqual(stream.period, 86400)
        self.assertEqual(stream.last_event_time, "")

    def test_get_forecast(self):
        forecast = self.client.get_forecast("test", 100)
        self.assertEqual(len(forecast.times), 100)
        self.assertEqual(len(forecast.values), 100)
        self.assertEqual(len(forecast.intervals[0].lower_bound), 100)
