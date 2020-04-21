import datetime
import unittest
from src.main import CheckTimeOfTheDay


class TestStringMethods(unittest.TestCase):
    def test_CheckTimeOfTheDay_expect_Morning(self):
        datetime.datetime(2012, 1, 1, 10, 10, 10)
        time = CheckTimeOfTheDay()
        self.assertEqual(time, "morning")

    def test_CheckTimeOfTheDay_expect_Afternoon(self):
        datetime.datetime(2012, 1, 1, 12, 10, 10)
        time = CheckTimeOfTheDay()
        self.assertEqual(time, "afternoon")

    def test_CheckTimeOfTheDay_expect_Night(self):
        datetime.datetime(2012, 1, 1, 21, 10, 10)
        time = CheckTimeOfTheDay()
        self.assertEqual(time, "afternoon")


