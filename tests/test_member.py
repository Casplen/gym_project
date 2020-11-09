import unittest
import datetime
from models.member import Member

class TestMember(unittest.TestCase):
    def setUp(self):
        start_date = datetime.date(2020, 1, 1)
        self.member1 = Member("John", "Smith", "standard", start_date, True)

    def test_member_has_first_name(self):
        self.assertEqual("John", self.member1.first_name)

    def test_member_has_last_name(self):
        self.assertEqual("Smith", self.member1.last_name)

    def test_member_has_membership_type(self):
        self.assertEqual("standard", self.member1.type)

    def test_member_has_start_date(self):
        date = datetime.datetime.strftime(self.member1.start_date, "%x")
        self.assertEqual("01/01/20", date)

    def test_member_has_active_status(self):
        self.assertTrue(self.member1.active_status)

    def test_member_deactivation(self):
        self.member1.deactivate()
        self.assertFalse(self.member1.active_status)

    def test_member_reactivation(self):
        self.member1.active_status = False
        self.member1.activate()
        self.assertTrue(self.member1.active_status)