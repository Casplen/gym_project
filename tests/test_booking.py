import unittest
import datetime
from models.booking import Booking
from models.gym_class import GymClass
from models.member import Member

class TestBooking(unittest.TestCase):
    def setUp(self):
        classdate = datetime.date(2020, 1, 1)
        classtime = datetime.time(13, 0, 0)
        self.gym_class1 = GymClass("Yoga", classdate, classtime, 10, 60)

        start_date = datetime.date(2020, 1, 1)
        self.member1 = Member("John", "Smith", "standard", start_date, True)

        self.booking1 = Booking(self.member1, self.gym_class1)

    def test_booking_has_member(self):
        self.assertEqual(self.member1, self.booking1.member)

    def test_booking_has_class(self):
        self.assertEqual(self.gym_class1, self.booking1.gym_class)
