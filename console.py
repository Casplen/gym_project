from models.booking import Booking
from models.gym_class import GymClass
from models.member import Member

import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository

import datetime

gym_class_repository.delete_all()
member_repository.delete_all()

start_date1 = datetime.date(2020, 1, 1)
start_date2 = datetime.date(2020, 2, 1)
start_date3 = datetime.date(2020, 3, 1)
start_date4 = datetime.date(2020, 4, 1)

member_repository.new_type("Standard")
member_repository.new_type("Premium")

member1 = Member("John", "Smith", "Standard", start_date1)
member2 = Member("Jane", "Doe", "Standard", start_date2)
member3 = Member("Richard", "Richards", "Standard", start_date3)
member4 = Member("Max", "Power", "Premium", start_date4)

member_repository.save(member1)
member_repository.save(member2)
member_repository.save(member3)
member_repository.save(member4)

gym_class_repository.new_type("Yoga")


