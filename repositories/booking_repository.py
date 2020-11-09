from db.run_sql import run_sql

from models.booking import Booking
from models.gym_class import GymClass
from models.member import Member

import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository 

def save(booking):
    sql = "INSERT INTO bookings (member_id, gym_class_id) VALUES (%s, %s) RETURNING *"
    values = [booking.member.id, booking.gym_class.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking