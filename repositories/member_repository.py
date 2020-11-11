from db.run_sql import run_sql

from models.member import Member

def new_type(type):
    sql = "INSERT INTO membership_types VALUES (%s)"
    values = [type]
    run_sql(sql, values)

def select_types():
    membership_types = []
    sql= "SELECT * FROM membership_types"
    results = run_sql(sql)
    
    for row in results:
        membership_type = row["type"]
        membership_types.append(membership_type)
    
    return membership_types

def save(member):
    sql = "INSERT INTO members (first_name, last_name, type, start_date, active_status) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [member.first_name, member.last_name, member.type, member.start_date, member.active_status]
    results = run_sql(sql, values)
    member.id = results[0]["id"]
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    members = []
    
    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = Member(row["first_name"], row["last_name"], row["type"], row["start_date"], row["active_status"], row["id"])
        members.append(member)
    return members

def select(id):
    member = None

    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result["first_name"], result["last_name"], result["type"], result["start_date"], result["active_status"], result["id"])
    return member

def update(member):
    sql = "UPDATE members SET (first_name, last_name, type, start_date, active_status) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.type, member.start_date, member.active_status, member.id]
    run_sql(sql, values)

def member_count():
    members = select_all()
    return len(members)