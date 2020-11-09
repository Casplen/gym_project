from db.run_sql import run_sql

from models.member import Member

def save(member):
    sql = "INSERT INTO members (first_name, last_name, type, start_date, active_status) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [member.first_name, member.last_name, member.type, member.start_date, member.active_status]
    results = run_sql(sql, values)
    id = results[0]["id"]
    member.id = id
    return member
