from db.run_sql import run_sql

from models.gym_class import GymClass

def new_type(type):
    sql = "INSERT INTO class_types (class_type) VALUES (%s)"
    values = [type]
    results = run_sql(sql, values)

def save(gym_class):
    sql = "INSERT INTO gym_classes (type, date, time, capacity, duration) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [gym_class.type, gym_class.date, gym_class.time, gym_class.capacity, gym_class.duration]
    results = run_sql(sql, values)
    id = results[0]["id"]
    gym_class.id = id
    return gym_class

def delete_all():
    sql = "DELETE FROM gym_classes"
    run_sql(sql)