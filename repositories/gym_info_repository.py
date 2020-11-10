from db.run_sql import run_sql

from models.gym_info import GymInfo

def save(gym_info):
    sql = "INSERT INTO gym_info (name, address, phone, email) VALUES (%s, %s, %s, %s)"
    values = [gym_info.name, gym_info.address, gym_info.phone, gym_info.email]
    run_sql(sql, values)

def update(gym_info):
    sql = "UPDATE gym_info SET (name, address, phone, email) = (%s, %s, %s, %s)"
    values = [gym_info.name, gym_info.address, gym_info.phone, gym_info.email]
    run_sql(sql, values)