import unittest
import datetime
from models.gym_class import GymClass 

class TestGymClass (unittest.TestCase):
    def setUp(self):
        date = datetime.date(2020, 1, 1)
        time = datetime.time(13, 0, 0)
        self.gym_class1 = GymClass("Yoga", date, time, 10, 60)

    def test_gym_class_has_type(self):
        self.assertEqual("Yoga", self.gym_class1.type)
    
    def test_gym_class_has_date(self):
        date = datetime.datetime.strftime(self.gym_class1.date, "%x")
        self.assertEqual("01/01/20", date)

    def test_gym_class_has_time(self):
        time = self.gym_class1.time
        self.assertEqual("13:00:00", time.strftime("%X"))

    def test_gym_class_has_capacity(self):
        self.assertEqual(10, self.gym_class1.capacity)

    def test_gym_class_has_duration(self):
        self.assertEqual(60, self.gym_class1.duration)