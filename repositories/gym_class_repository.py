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

def delete(id):
    sql = "DELETE FROM gym_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    gym_classes = []
    sql = "SELECT * FROM gym_classes"
    results = run_sql(sql)

    for row in results:
        gym_class = GymClass(row['type'], row['date'], row['time'], row['capacity'], row['duration'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes

def select(id):
    gym_class = None
    sql = "SELECT * FROM gym_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        gym_class = GymClass(result["type"], result["date"], result["time"], result["capacity"], row["duration"], row["id"])
    return gym_class

def update(gym_class):
    sql = "UPDATE gym_classes SET (type, date, time, capacity, duration) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = values = [gym_class.type, gym_class.date, gym_class.time, gym_class.capacity, gym_class.duration, gym_class.id]
    run_sql(sql, values)