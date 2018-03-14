"""Tests for the more idiomatic python client.

These are light, because exceptions, arg parsing happen serverside.
"""
import datetime
import random
import string
import unittest

import seer


class TestClient(unittest.TestCase):

    def setUp(self):
        self.name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        self.client = seer.Client("127.0.0.1:8080")
        self.client.create_stream(self.name, 86400)

    def tearDown(self):
        self.client.delete_stream(self.name)

    def test_create_stream(self):
        name = self.name + "_new"
        period = 3600
        stream = self.client.create_stream(name, period)
        self.assertEqual(stream.name, name)
        self.assertEqual(stream.period, period)

    def test_get_stream(self):
        stream = self.client.get_stream(self.name)
        self.assertEqual(stream.name, self.name)
        self.assertEqual(stream.period, 86400)

    def test_list_streams(self):
        streams = self.client.list_streams(10, 1)
        self.assertTrue(len(streams) <= 10)
        names = [s.name for s in streams]
        self.assertTrue(self.name in names)

    def test_update_stream(self):
        times = [
            datetime.datetime(2016, 1, 1),
            datetime.datetime(2016, 1, 2),
            datetime.datetime(2016, 1, 3),
        ]
        values = [10, 9, 8]
        stream = self.client.update_stream(self.name, times, values)
        self.assertEqual(stream.name, self.name)
        self.assertEqual(stream.period, 86400)
        self.assertEqual(stream.last_event_time.ToDatetime(), datetime.datetime(2016, 1, 3))

    def test_get_forecast(self):
        forecast = self.client.get_forecast(self.name, 100)
        self.assertEqual(len(forecast.times), 100)
        self.assertEqual(len(forecast.values), 100)
        self.assertEqual(len(forecast.intervals[0].lower_bound), 100)
