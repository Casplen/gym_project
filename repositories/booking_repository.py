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

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row["member_id"])
        gym_class = gym_class_repository.select(row["gym_class_id"])
        booking = Booking(member, gym_class, row["id"])

        bookings.append(booking)
    return bookings

def select(id):
    booking = None

    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = member_repository.select(result["member_id"])
        gym_class = gym_class_repository.select(result["gym_class_id"])
        booking = Booking(member, gym_class, result["id"])
    return booking

def update(booking):
    sql = "UPDATE bookings SET (member_id, gym_class_id) VALUES (%s, %s) WHERE id = %s"
    values = [booking.member.id, booking.gym_class.id, booking.id]
    run_sql(sql, values)

def members(gym_class_id):
    members = []
    sql = "SELECT members.* FROM members INNER JOIN bookings ON members.id = bookings.member_id WHERE bookings.gym_class_id = %s"
    values = [gym_class_id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row["first_name"], row["last_name"], row["type"], row["start_date"], row["active_status"], row["id"])
        members.append(member)
    return members

def gym_classes(member_id):
    gym_classes = []
    sql = "SELECT gym_classes.* FROM gym_classes INNER JOIN bookings ON gym_classes.id = bookings.gym_class_id WHERE bookings.member_id = %s"
    values = [member_id]
    results = run_sql(sql, values)

    for row in results:
        gym_class = GymClass(row['type'], row['date'], row['time'], row['capacity'], row['duration'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes